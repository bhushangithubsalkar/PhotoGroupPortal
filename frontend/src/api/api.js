/**
 * API Service Module for Photo Group Portal Frontend
 * Uses environment variable VITE_API_URL for configuration.
 */

const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

/**
 * Helper to perform HTTP requests with error handling and optional timeout.
 */
async function apiFetch(endpoint, options = {}) {
  const url = `${BASE_URL}${endpoint}`;
  
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 5000); // 5 second timeout

  try {
    const response = await fetch(url, {
      ...options,
      signal: controller.signal,
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      const errorText = await response.text().catch(() => '');
      throw new Error(`API Error (HTTP ${response.status}): ${errorText || response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    clearTimeout(timeoutId);

    if (error.name === 'AbortError') {
      throw new Error('API Request timed out. Backend server is unresponsive.');
    }

    if (error instanceof TypeError && error.message.includes('fetch')) {
      throw new Error('Network error: Unable to reach FastAPI backend server.');
    }

    throw error;
  }
}

/**
 * Get basic API health status (GET /api/health)
 */
export async function getHealthStatus() {
  return await apiFetch('/api/health');
}

/**
 * Get detailed system & database health status (GET /api/v1/health)
 */
export async function getDetailedHealth() {
  return await apiFetch('/api/v1/health');
}
