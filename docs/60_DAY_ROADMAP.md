# Photo Group Portal — 60-Day Master Roadmap

This document defines the 60-day engineering execution strategy, deliverables, and technical quality gates for **Photo Group Portal**.

---

## Roadmap Overview by Phases

### PHASE 1 — DAYS 1–5: FOUNDATION & BASELINE
* **Day 1**: System architecture, project structure, environment configuration, base health route. *(COMPLETED)*
* **Day 2**: Backend (FastAPI) and Frontend (React/Vite) setup; cross-origin requests & status ping. *(COMPLETED)*
* **Day 3**: PostgreSQL database connectivity, Alembic migration engine, base models (`User`, `SystemLog`). *(COMPLETED)*
* **Day 4**: Structured logging (`logs/app.log`), Pydantic settings validation, exception standardizers. *(COMPLETED)*
* **Day 5**: Basic authentication baseline, user registration/login contracts, and foundation smoke tests. *(NEXT)*
* **Deliverable**: End-to-end runnable baseline with database persistence, structured logging, and test coverage.

---

### PHASE 2 — DAYS 6–10: AUTHENTICATION & ACCESS CONTROL (RBAC)
* **Day 6**: Extended User schema (roles, active states, audit fields) and schema migrations.
* **Day 7**: Secure password hashing (Argon2 / Passlib) and JWT issue/verify pipeline (`/api/v1/auth/token`).
* **Day 8**: Role-Based Access Control (RBAC) dependencies (`Photographer`, `User`, `Admin`).
* **Day 9**: Frontend state management (AuthContext) and protected route guards.
* **Day 10**: Security audits, token expiration tests, and authentication test coverage.
* **Deliverable**: Fully secured JWT authentication engine with RBAC enforced across API and UI.

---

### PHASE 3 — DAYS 11–15: ROOM MANAGEMENT & QR GENERATION
* **Day 11**: Room entity design (`Room`, `RoomToken`, `PhotographerID`) and migrations.
* **Day 12**: Photographer Room CRUD REST endpoints (`/api/v1/rooms`).
* **Day 13**: Photographer Room Dashboard UI (create, list, configure expiration).
* **Day 14**: Secure public token generation engine and QR code rendering service.
* **Day 15**: QR code download/export capabilities and integration tests.
* **Deliverable**: Photographers can spin up isolated event rooms and generate room-specific QR codes.

---

### PHASE 4 — DAYS 16–21: BULK PHOTO INGESTION & STORAGE PIPELINE
* **Day 16**: Storage abstraction layer (`LocalStorageProvider` interface) and Photo metadata schema.
* **Day 17**: High-throughput multi-part file upload endpoints (`/api/v1/rooms/{id}/photos`).
* **Day 18**: Server-side storage validation (mime-type, file signatures, size boundaries).
* **Day 19**: React drag-and-drop bulk upload dashboard with real-time file progress trackers.
* **Day 20**: Photo management gallery (grid view, photo deletion, manual tagging).
* **Day 21**: Automated asynchronous thumbnail generation worker (PIL/Pillow pipeline).
* **Deliverable**: Robust media upload pipeline capable of handling high-volume photo ingestion.

---

### PHASE 5 — DAYS 22–26: ASYNCHRONOUS JOB QUEUE & WORKERS
* **Day 22**: Job execution tracking model (`ProcessingJob`, state machine: `PENDING`, `PROCESSING`, `COMPLETED`, `FAILED`).
* **Day 23**: Task queue setup (Celery + Redis or FastAPI background execution worker).
* **Day 24**: Async job dispatch pipeline for media processing tasks.
* **Day 25**: Exponential backoff retry policies, dead-letter management, and error capture.
* **Day 26**: Worker health monitoring UI and background processing test suite.
* **Deliverable**: Asynchronous event processing pipeline keeping web workers decoupled from heavy jobs.

---

### PHASE 6 — DAYS 27–31: AUTOMATED IMAGE QUALITY ASSURANCE
* **Day 27**: Media validation pipeline for corrupt file detection and EXIF extraction.
* **Day 28**: OpenCV integration for blur analysis via Laplacian Variance calculation.
* **Day 29**: Exposure inspection (histogram bounds check) and low-resolution flagging.
* **Day 30**: Composite Quality Score calculation and Photographer Quality Flagging UI.
* **Day 31**: Threshold tuning tools and end-to-end quality assessment tests.
* **Deliverable**: Automated quality gate flagging sub-optimal photos without destructive deletion.

---

### PHASE 7 — DAYS 32–37: FACE DETECTION & BOUNDING BOX EXTRACTION
* **Day 32**: Abstract face-detection service interface design.
* **Day 33**: Face detection engine integration (InsightFace / OpenCV / MediaPipe).
* **Day 34**: Multi-face detection and bounding box coordinate normalization.
* **Day 35**: Face entity persistence (`Face`, `bounding_box`, `photo_id`, `room_id`).
* **Day 36**: Error handling for zero-face or congested multi-face images.
* **Day 37**: Face bounding box overlay UI for photographer inspection and testing.
* **Deliverable**: Automatic detection and spatial indexing of face coordinates within room collections.

---

### PHASE 8 — DAYS 38–43: VECTOR EMBEDDINGS & ROOM-ISOLATED MATCHING
* **Day 38**: Biometric vector embedding generation (512-dimensional facial representations).
* **Day 39**: PostgreSQL `pgvector` extension setup and vector similarity distance queries.
* **Day 40**: Facial similarity clustering for grouping recurring individuals across room media.
* **Day 41**: Strict room-boundary query filtering (preventing cross-event data exposure).
* **Day 42**: Adjustable confidence threshold algorithms for match verification.
* **Day 43**: Matching accuracy benchmarks, vector index tuning, and unit tests.
* **Deliverable**: High-speed, room-isolated facial vector matching pipeline.

---

### PHASE 9 — DAYS 44–48: ATTENDEE WEB SEARCH & SECURE GALLERIES
* **Day 44**: Public attendee Web Portal entry point (`/room/{token}`).
* **Day 45**: Attendee camera selfie upload interface with quality and face validation.
* **Day 46**: Real-time selfie embedding generation and room vector search execution.
* **Day 47**: Signed, time-expiring gallery token generation service.
* **Day 48**: Secure attendee photo gallery UI with bulk download capabilities.
* **Deliverable**: Web workflow allowing attendees to upload selfies and access personal photo galleries.

---

### PHASE 10 — DAYS 49–52: WHATSAPP WORKFLOW & BOT INTEGRATION
* **Day 49**: WhatsApp Business API Webhook integration (`/api/v1/webhooks/whatsapp`).
* **Day 50**: Session state engine linking WhatsApp users to specific room QR sessions.
* **Day 51**: Inbound WhatsApp selfie processing, matching, and dynamic response link delivery.
* **Day 52**: Webhook security, retry logic, rate limits, and end-to-end WhatsApp tests.
* **Deliverable**: Full WhatsApp selfie interaction delivering matched personal photo galleries.

---

### PHASE 11 — DAYS 53–56: ADMINISTRATIVE DASHBOARD & AUDITING
* **Day 53**: Unified System Admin Dashboard frontend base.
* **Day 54**: Photographer, Room, and Storage quota management screens.
* **Day 55**: Worker queue metrics, system resource utilization, and error log viewers.
* **Day 56**: Audit log system capturing key administrative and security events.
* **Deliverable**: Comprehensive administrative console for system ops and user oversight.

---

### PHASE 12 — DAYS 57–60: HARDENING, CONTAINERIZATION & RELEASE
* **Day 57**: Comprehensive security review (rate limiting, CORS verification, biometric data privacy).
* **Day 58**: End-to-end integration testing, API load testing, and database query optimization.
* **Day 59**: Complete Docker containerization setup (`docker-compose.yml`, multi-stage Dockerfiles).
* **Day 60**: Deployment guide finalization, architectural documentation signoff, and project delivery.
* **Deliverable**: Production-ready, fully containerized system ready for cloud deployment.