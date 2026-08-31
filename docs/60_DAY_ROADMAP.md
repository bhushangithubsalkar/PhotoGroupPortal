# Photo Group Portal — 60-Day Master Roadmap

This document outlines the 60-day development plan for **Photo Group Portal**.

---

## Phase Breakdown Summary

### PHASE 1 — DAYS 1–5: FOUNDATION
- **Day 1**: Define architecture, repository structure, coding standards, environments, health endpoint. *(COMPLETED)*
- **Day 2**: Create Python backend & React frontend baseline; establish `/api/health` connection. *(COMPLETED)*
- **Day 3**: PostgreSQL connection, migrations foundation, declarative base models (`Base`, `SystemLog`). *(COMPLETED)*
- **Day 4**: Configuration, structured logging (`logs/app.log`), global error-handling foundation, health endpoint DB metrics. *(COMPLETED)*
- **Day 5**: Basic authentication foundation and smoke tests. *(NEXT)*
- **DELIVERABLE**: End-to-end local application baseline.

---

### PHASE 2 — DAYS 6–10: AUTH + ROLES
- **Day 6**: User model and authentication database structures.
- **Day 7**: Password hashing (bcrypt/argon2), login/register/logout.
- **Day 8**: Roles & Role-Based Access Control (RBAC: Photographer, User, Admin).
- **Day 9**: Protected React routes and role dashboards.
- **Day 10**: Authentication tests and security review.
- **DELIVERABLE**: Working authentication and role management.

---

### PHASE 3 — DAYS 11–15: ROOMS + QR
- **Day 11**: Room database model and migrations.
- **Day 12**: Photographer room CRUD APIs.
- **Day 13**: Photographer Room Dashboard UI.
- **Day 14**: Secure public room token generation & QR code creation.
- **Day 15**: QR display/download functionality and room tests.
- **DELIVERABLE**: Photographer can create event rooms and download room QR codes.

---

### PHASE 4 — DAYS 16–21: PHOTO UPLOAD
- **Day 16**: Photo database model and storage abstraction (originals/thumbnails).
- **Day 17**: Bulk photo upload API and file type/size validation.
- **Day 18**: Storage pipeline flow (temporary/file/object storage).
- **Day 19**: React bulk photo upload UI with upload progress.
- **Day 20**: Photo grid, photo details, and delete management UI.
- **Day 21**: Automatic thumbnail generation and upload tests.
- **DELIVERABLE**: Photographers can bulk upload and manage high volumes of event photos.

---

### PHASE 5 — DAYS 22–26: BACKGROUND PROCESSING
- **Day 22**: Processing-job model and job status tracking.
- **Day 23**: Queue & background worker architecture (Celery/Redis or Python async worker).
- **Day 24**: Async processing states (Pending, Processing, Completed, Failed).
- **Day 25**: Job retry and failure handling.
- **Day 26**: Processing monitoring UI + background job tests.
- **DELIVERABLE**: Asynchronous processing pipeline (uploads do not block web requests).

---

### PHASE 6 — DAYS 27–31: IMAGE QUALITY
- **Day 27**: Image validation pipeline.
- **Day 28**: Blur detection (Laplacian variance calculation).
- **Day 29**: Resolution, exposure (too dark/bright), corruption checks.
- **Day 30**: Quality scoring system and photographer review warning UI.
- **Day 31**: Quality check tuning and integration tests.
- **DELIVERABLE**: Flagging low-quality photos for photographer review without automatic deletion.

---

### PHASE 7 — DAYS 32–37: FACE DETECTION
- **Day 32**: Face-processing service interface abstraction.
- **Day 33**: Face detection model integration (OpenCV / MediaPipe / dlib / insightface).
- **Day 34**: Multi-face handling and bounding box extraction.
- **Day 35**: Face metadata persistence (`face_id`, `photo_id`, `room_id`, `bounding_box`).
- **Day 36**: Error & retry handling for face processing jobs.
- **Day 37**: Face detection test suite and photo face-tagging review UI.
- **DELIVERABLE**: Automatic face detection and tagging per room collection.

---

### PHASE 8 — DAYS 38–43: FACE EMBEDDINGS + GROUPING
- **Day 38**: Face vector embedding generation (512d / 128d representations).
- **Day 39**: Vector similarity calculation (Cosine similarity / Euclidean distance).
- **Day 40**: Face grouping and clustering algorithm.
- **Day 41**: Room-isolated face vector index (ensuring strict room boundary isolation).
- **Day 42**: Configurable matching confidence thresholds & search service.
- **Day 43**: Matching accuracy & performance testing.
- **DELIVERABLE**: Room-isolated face searching and grouping.

---

### PHASE 9 — DAYS 44–48: USER PHOTO SEARCH
- **Day 44**: User web search flow entry point.
- **Day 45**: User selfie upload and validation interface.
- **Day 46**: Selfie embedding & room-only face matching.
- **Day 47**: Expiring secure gallery URL generation.
- **Day 48**: User web gallery UI, photo selection/download, and edge-case tests.
- **DELIVERABLE**: Web-based selfie search returning personal photos in an expiring gallery.

---

### PHASE 10 — DAYS 49–52: WHATSAPP INTEGRATION
- **Day 49**: WhatsApp service provider interface & webhook endpoint.
- **Day 50**: QR code -> Room -> WhatsApp bot session mapping.
- **Day 51**: Receiving user selfie via WhatsApp, processing match, and returning gallery URL.
- **Day 52**: Webhook error handling, session expiration, and end-to-end WhatsApp tests.
- **DELIVERABLE**: Complete QR code -> WhatsApp selfie -> Personal gallery workflow.

---

### PHASE 11 — DAYS 53–56: ADMIN DASHBOARD
- **Day 53**: Secure Admin Dashboard entry point.
- **Day 54**: Photographer and Room management interface.
- **Day 55**: Storage, processing job, and system health monitoring UI.
- **Day 56**: Audit logging system and admin security verification.
- **DELIVERABLE**: Full administrative oversight over users, rooms, jobs, and system health.

---

### PHASE 12 — DAYS 57–60: HARDENING + DELIVERY
- **Day 57**: Security review (rate limiting, URL signing, privacy audit, biometric data safety).
- **Day 58**: Comprehensive unit, integration, and load testing.
- **Day 59**: Docker containerization (`docker-compose`), environment config, deployment guide.
- **Day 60**: Final demo verification, architecture documentation, project wrap-up.
- **DELIVERABLE**: Production-ready Photo Group Portal.
