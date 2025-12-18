# Software Specification Document

**Ancient Language Learning Web Application**

**Project Name: LearnAncient**

**Initial Language: Biblical Greek**


---

## 1. Executive Summary

### 1.1 Purpose

This application is a **visual-first, manuscript-centered web platform** for learning ancient languages through direct engagement with historical texts. Rather than abstract drills or isolated flashcards, users learn by reading *real manuscripts*, interacting with every word, and progressively internalizing grammar, vocabulary, and syntax in context.

The first supported language is **Biblical Greek**, with explicit architectural support for adding additional ancient languages (e.g., Hebrew, Latin, Syriac) through modular **Language Packs** without refactoring core application logic.

---

### 1.2 Target Audience

* **Beginner learners**

  * No prior exposure to ancient languages
  * Require guided reading, clear explanations, and visual grounding

* **Intermediate readers**

  * Familiar with grammar and morphology
  * Want fast, accurate manuscript reading with reference overlays

* **Instructors / study groups (future)**

  * Desire shared passages, assignments, and progress monitoring

* **Independent learners**

  * Mobile-first, offline-capable, self-paced learning

---

### 1.3 Key Differentiators

* Manuscript-first reading experience (images + aligned text)
* Token-level interactivity (every word is explorable)
* Offline-first Progressive Web App (PWA)
* Modular, versioned language pack system
* Designed for ancient languages (not retrofitted from modern-language tools)

---

## 2. Goals and Non-Goals

### 2.1 Goals

**MVP Goals**

* Enable users to read Biblical Greek manuscripts with:

  * Clickable tokens
  * Lemma, morphology, gloss, pronunciation
* Provide guided learning paths from alphabet → grammar → reading
* Support offline reading for downloaded passages
* Establish a robust Language Pack architecture

**Long-Term Goals**

* Add multiple ancient languages without core refactors
* Instructor/group learning tools
* Advanced search and cross-text analysis
* Customizable reading layers and views

---

### 2.2 Non-Goals (Explicit)

* No AI-generated translations in MVP
* No free-form user content creation (notes may come later)
* No social networking features
* No real-time collaboration in early phases
* No requirement for users to upload manuscripts

---

## 3. User Personas & Use Cases

### 3.1 Beginner Learner

**Needs**

* Clear progression
* Human-readable explanations
* Audio pronunciation support
* Minimal cognitive overload

**Core Flows**

* Start lesson → guided reading → light quiz → review

---

### 3.2 Intermediate Reader

**Needs**

* Fast lookup
* Minimal UI friction
* Control over overlays

**Core Flows**

* Open passage → toggle morphology → read fluidly → review vocab

---

### 3.3 Instructor / Group (Future)

**Needs**

* Assign passages
* Monitor progress
* Share annotations

**Status**

* Architecture-ready, not implemented in MVP

---

### 3.4 Guest vs Authenticated Users

| Feature              | Guest | Authenticated |
| -------------------- | ----- | ------------- |
| Read sample passages | ✅     | ✅             |
| Clickable tokens     | ✅     | ✅             |
| Progress tracking    | ❌     | ✅             |
| Offline downloads    | ❌     | ✅             |
| SRS review           | ❌     | ✅             |

---

## 4. UX & Navigation Principles

### 4.1 Core UX Rules

* **Mobile-first**: All primary flows must work on ≤375px width
* **3-click rule**: Any core action reachable within 3 interactions
* **Progressive disclosure**: Advanced info hidden by default
* **Visual hierarchy over text density**

---

### 4.2 Navigation Model

* **Bottom tab bar (mobile)** / **Left rail (desktop)**

  * Learn
  * Read
  * Review
  * Library
  * Profile

* Persistent **“Next Step” CTA**

  * Context-aware guidance (lesson, passage, review)

---

### 4.3 Accessibility (WCAG 2.1 AA)

* Full keyboard navigation
* Screen reader–friendly token metadata
* High-contrast mode
* Reduced motion support
* Minimum 44×44px tap targets

---

## 5. Functional Requirements

### 5.1 Authentication & Profiles

* Guest mode (no auth)
* JWT-based authentication (access + refresh)
* Profile preferences:

  * Default language pack
  * Transliteration on/off
  * Font size
  * Reading direction (language-dependent)
* Seamless guest → account upgrade

---

### 5.2 Language Pack System (Critical)

**Design Requirements**

* Fully modular
* Versioned
* Independently deployable
* Validated at runtime

**Language Pack Contents**

* Alphabet definitions
* Phonology rules
* Lemmas
* Morphology schemas
* Passages
* Manuscript metadata
* Lexicon entries
* Audio references (optional)

**Manifest File**

```json
{
  "language": "biblical-greek",
  "version": "1.0.0",
  "direction": "ltr",
  "script": "Greek",
  "features": ["morphology", "audio", "manuscripts"]
}
```

**Constraints**

* Core app must not hardcode any language-specific logic
* All UI labels and grammatical logic resolved via pack metadata

---

### 5.3 Learn Module

* Structured lesson paths:

  * Alphabet & pronunciation
  * Core grammar
  * Syntax patterns
* Embedded micro-quizzes
* Immediate feedback
* Lesson completion tracking

---

### 5.4 Read Module (Manuscript Viewer)

**Features**

* High-resolution manuscript image viewer

  * Pan / zoom
  * Touch gestures
* Text transcription aligned to image regions
* Token-level interaction:

  * Lemma
  * Morphology (human-readable)
  * Gloss
  * Audio (optional)
* Layer toggles:

  * Morphology
  * Gloss
  * Translation (optional)
* Offline-capable passages

**Performance Target**

* Initial render < 500ms on mid-range mobile

---

### 5.5 Review Module (Spaced Repetition)

* Vocabulary review
* Morphological forms
* Phrase recognition
* SM-2–derived scheduling algorithm
* Due counts, streaks, accuracy stats

---

### 5.6 Library / Reference Tools

* Lexicon browser
* Morphology charts
* Grammar reference pages
* Cross-linked from reader

---

### 5.7 Search

* Global fuzzy search:

  * Lemmas
  * Surface forms
  * Passages
* Transliteration-aware
* Accent-insensitive
* Language-pack scoped

---

### 5.8 Progress Tracking & Analytics

**User-visible**

* Lessons completed
* Reading streaks
* Vocabulary mastery

**Internal (Privacy-safe)**

* Feature usage
* Drop-off points
* Offline vs online usage

---

## 6. Backend Architecture (Django)

### 6.1 App Breakdown

* `accounts`
* `languages`
* `content`
* `reader`
* `srs`
* `search`
* `analytics`

---

### 6.2 Data Model Strategy

* Strong foreign-key relationships
* Language pack–scoped content
* Immutable content versions
* User data always references specific content versions

---

### 6.3 Content Ingestion Pipeline

* Validate language pack schema
* Normalize text/token alignment
* Generate search indexes
* Precompute morphology expansions

---

### 6.4 Search Implementation

* PostgreSQL full-text search
* Trigram similarity
* Optional Elastic/OpenSearch later

---

### 6.5 Caching

* Redis:

  * Token metadata
  * Lexicon entries
* CDN for images/audio

---

### 6.6 Security & Permissions

* Read-only content for users
* Admin-only content ingestion
* Signed URLs for S3 assets
* Rate limiting on auth endpoints

---

## 7. API Design

### 7.1 Auth

* `POST /auth/login`
* `POST /auth/refresh`
* `POST /auth/guest-upgrade`

---

### 7.2 Content

* `GET /languages`
* `GET /languages/{id}/packs`
* `GET /passages/{id}`

---

### 7.3 Reader

* `GET /reader/passage/{id}`
* `GET /reader/token/{id}`

---

### 7.4 Search

* `GET /search?q=`

---

### 7.5 SRS

* `GET /review/due`
* `POST /review/answer`

---

### 7.6 Versioning

* URL versioning: `/api/v1/`
* Content version pinned in responses

---

## 8. Data Models (High-Level)

* User
* UserProfile
* Language
* LanguagePack
* Passage
* Token
* Lemma
* Morphology
* Manuscript
* ReviewItem
* ProgressEvent

---

## 9. Offline & Performance Strategy

* Service Worker with:

  * Cache-first for static assets
  * Network-first for auth
* IndexedDB for:

  * Downloaded passages
  * User progress queue
* Background sync when online

---

## 10. Accessibility & Quality Standards

* WCAG 2.1 AA
* No color-only meaning
* Font scaling support
* Pronunciation audio captions

---

## 11. Testing Strategy

* Unit tests (logic, models)
* Integration tests (API flows)
* E2E tests (critical user journeys)
* Content validation tests per language pack

---

## 12. Deployment & Operations

### 12.1 Frontend

* Static hosting (Vercel / Netlify / S3 + CDN)

### 12.2 Backend

* Dockerized Django
* Gunicorn + Nginx
* PostgreSQL (managed)

### 12.3 CI/CD

* Lint → test → build → deploy
* Language pack validation in pipeline

---

## 13. Roadmap & Phases

### Phase 1 – MVP

* Biblical Greek
* Read + Learn + basic Review
* Offline reading
  **Acceptance**
* User reads manuscript offline with token interaction

---

### Phase 2

* Expanded SRS
* Advanced search
* More manuscripts

---

### Phase 3+

* Additional languages
* Instructor tools
* Cross-text analysis

---

## Final Notes

This system is designed as a **content-driven, language-agnostic platform** where *text fidelity, performance, and clarity* are prioritized over novelty. Every architectural choice supports longevity, scholarly accuracy, and learner trust.
