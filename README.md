# MeetUp Platform

> A unified platform connecting email, meetings, scheduling, video conferencing, and transport logistics into one intuitive interface.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-in%20development-yellow)

---

## Overview

MeetUp eliminates the friction of coordinating meetings by combining everything in one place:
- Book meetings with Calendly-style scheduling
- Auto-create Microsoft Teams or Google Meet rooms
- Parse and send meeting emails automatically
- Book transport (taxi, public transit, organized) timed to your meeting

---

## Core Features

### 1. Email Integration
- Connect Gmail and Outlook via OAuth 2.0
- Automatically parse meeting invites (date, time, location, attendees)
- Send meeting confirmations, reminders, and updates from the platform
- Thread-based communication tied to each meeting event

### 2. Meeting Scheduling (Calendly-style)
- Show availability based on connected calendars (Google Calendar, Outlook)
- Share booking links with customizable time slots and buffer times
- Support for 1-on-1, group, and round-robin scheduling
- Automatic timezone detection and conversion

### 3. Video Conferencing Integration
- Auto-create and manage Microsoft Teams and Google Meet rooms on booking
- Edit rooms: rename, add/remove participants, change time
- Generate and distribute meeting links via email confirmation
- Support for recurring meetings and series management

### 4. Transport Integration
- **Taxi**: Uber, Bolt, and local taxi APIs — book a ride timed to meeting start
- **Public transport**: Entur, Ruter, Skyss (Norway) for real-time route suggestions
- **Organized transport**: Company shuttles and shared group transport booking
- Auto-calculate departure time based on user location and meeting venue
- Transport confirmation sent alongside meeting confirmation email

---

## Architecture

```
┌──────────────────────────────────────────────────────┐
│              Frontend (Web + Mobile)                 │
│      Single dashboard — meetings, mail, transport    │
└───────────────────┬──────────────────────────────────┘
                    │
┌───────────────────▼──────────────────────────────────┐
│                API Gateway / BFF                     │
└──┬──────────┬──────────┬──────────┬──────────────────┘
   │          │          │          │
┌──▼──┐  ┌───▼───┐  ┌───▼───┐  ┌──▼─────────┐
│Email│  │Sched- │  │Video  │  │ Transport  │
│Svc  │  │uling  │  │Conf.  │  │ Service    │
└──┬──┘  └───┬───┘  └───┬───┘  └──┬─────────┘
   │         │           │         │
┌──▼─────────▼───────────▼─────────▼──────────┐
│           External API Integrations          │
│  Gmail · Outlook · Google Cal · Teams · Meet │
│  Uber · Bolt · Entur · Ruter · Skyss         │
└──────────────────────────────────────────────┘
```

---

## Project Structure

```
meetup-platform/
├── frontend/              # Next.js app
│   ├── app/               # App router pages
│   ├── components/        # Reusable UI components
│   └── lib/               # API clients, utilities
├── backend/               # FastAPI or Node.js API
│   ├── api/               # Route handlers
│   ├── services/          # Business logic
│   │   ├── email/         # Gmail/Outlook integration
│   │   ├── scheduling/    # Calendar & booking logic
│   │   ├── conferencing/  # Teams/Meet integration
│   │   └── transport/     # Taxi & transit APIs
│   ├── models/            # Database models
│   └── utils/             # Shared utilities
├── docs/                  # Architecture & API docs
└── .github/               # CI/CD workflows, issue templates
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React / Next.js |
| Backend | Python (FastAPI) |
| Auth | OAuth 2.0 (Google, Microsoft) |
| Database | PostgreSQL + Redis (caching) |
| Notifications | WebSockets + Email (SendGrid) |
| Hosting | Vercel (frontend) + Railway (backend) |

---

## UX Principles

- **Single dashboard** — all upcoming meetings, transport, and emails in one view
- **One-click booking** — schedule meeting + book transport in a single flow
- **Smart suggestions** — AI-suggested meeting times based on all attendees' availability
- **Mobile-first** — full functionality on mobile with native app feel
- **Minimal friction** — no more than 3 steps from intent to confirmed meeting + transport

---

## Roadmap

| Phase | Milestone | Status |
|---|---|---|
| v0.1 | Email + Calendar integration, basic scheduling | 🔲 Planned |
| v0.2 | Teams/Meet room creation and management | 🔲 Planned |
| v0.3 | Transport integration (taxi + public transport) | 🔲 Planned |
| v0.4 | Unified dashboard UI | 🔲 Planned |
| v1.0 | Full release, mobile app, notifications | 🔲 Planned |

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/danieskild/meetup-platform.git
cd meetup-platform

# Frontend
cd frontend
npm install
npm run dev

# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## License

MIT © [Daniel Eskildsen](https://github.com/danieskild)
