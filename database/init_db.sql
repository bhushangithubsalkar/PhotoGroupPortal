-- Photo Group Portal - Initial PostgreSQL Setup Script
-- Day 1 Foundation Schema

CREATE DATABASE photo_group_portal;

\c photo_group_portal;

-- Extension for UUID generation
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Base operational log / metadata ping verification table (Foundation)
CREATE TABLE IF NOT EXISTS system_health_logs (
    id SERIAL PRIMARY KEY,
    status VARCHAR(50) NOT NULL,
    checked_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    details TEXT
);

INSERT INTO system_health_logs (status, details) 
VALUES ('INITIALIZED', 'Day 1 foundation database structure established successfully.');
