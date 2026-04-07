# Claude AI Configuration

## Project Overview

**Class-AI-Agent** is a professional AI-powered development framework that standardizes how Claude AI assists with software engineering. It provides specialized agent roles, mandatory engineering rules, reusable command workflows, and advanced skills — all designed for teams building production-grade applications.

This repository is a **template/framework** — it contains configuration, documentation, and standards (no application source code yet). Projects built with this framework should follow the approved tech stack and layered architecture defined here.

## Core Instructions

- **Always** follow the rules defined in `.claude/rules/` — they are mandatory
- Use available commands from `.claude/commands/` for common tasks (deploy, fix-issue, review)
- Leverage skills from `.claude/skills/` for specialized operations (deployment automation, security audits)
- Delegate to the appropriate sub-agent in `.claude/agents/` based on the task domain
- When writing code, use **TypeScript always** — plain JavaScript is not permitted
- Follow **conventional commits** for all git messages (see `rules/git-workflow.md`)

---

## Repository Structure

```
Class-AI-Agent/
├── .claude/                        # AI Agent Configuration Hub
│   ├── CLAUDE.md                   # This file — master AI instructions
│   ├── settings.json               # Project-level AI settings
│   ├── agents/                     # 7 specialized AI role definitions
│   │   ├── frontend.md             # Next.js, React, TypeScript, UI
│   │   ├── backend.md              # Express, Node, PostgreSQL, APIs
│   │   ├── systems-architect.md    # System design, ADRs, scalability
│   │   ├── ui-ux-designer.md       # Design systems, wireframes, a11y
│   │   ├── project-manager.md      # User stories, sprints, status
│   │   ├── qa.md                   # Test plans, coverage, bug reports
│   │   └── copywriter-seo.md       # Content, microcopy, SEO, schema
│   ├── commands/                   # 3 reusable command workflows
│   │   ├── deploy.md               # Full deployment pipeline
│   │   ├── fix-issue.md            # Bug analysis & systematic fixing
│   │   └── review.md               # Code review checklist
│   ├── rules/                      # 13 mandatory engineering standards
│   │   ├── clean-code.md           # Clean Code JS principles
│   │   ├── code-style.md           # Formatting & naming conventions
│   │   ├── error-handling.md       # AppError class, global handler
│   │   ├── tech-stack.md           # Approved technologies & decisions
│   │   ├── system-design.md        # CAP, caching, scaling patterns
│   │   ├── project-structure.md    # Layered architecture & folders
│   │   ├── api-conventions.md      # REST standards & response format
│   │   ├── naming-conventions.md   # Cache keys, DB, queues, env vars
│   │   ├── database.md             # Prisma, transactions, migrations
│   │   ├── security.md             # CRITICAL security requirements
│   │   ├── monitoring.md           # Prometheus, Grafana, Pino logging
│   │   ├── testing.md              # Vitest, 80% coverage minimum
│   │   └── git-workflow.md         # Git Flow, conventional commits
│   └── skills/                     # 2 advanced capabilities
│       ├── deploy/SKILL.md         # Automated deployment pipeline
│       └── security-review/SKILL.md # Systematic security audit
├── .env.example                    # Environment variables template
├── .gitignore                      # Git ignore rules
└── README.md                       # Project documentation
```

### Expected Application Structure (when code is added)

```
src/
├── config/             # Configuration files
├── controllers/        # Route handlers (thin — delegates to services)
├── middleware/          # Express middleware (auth, validation, errors)
├── models/             # Database models/schemas (Prisma)
├── repositories/       # Data access layer (queries, DB operations)
├── routes/             # Route definitions (URL mapping only)
├── services/           # Business logic layer (core application logic)
├── utils/              # Utility functions (AppError, logger, cache)
└── index.js            # Application entry point

tests/
├── unit/               # Fast, isolated logic tests (80%+ of tests)
├── integration/        # Component interaction tests
└── e2e/                # End-to-end flow tests (Playwright)
```

**Request flow**: `Routes -> Middleware -> Controllers -> Services -> Repositories -> Database`

---

## Approved Technology Stack

| Layer | Primary Choice | Notes |
|-------|---------------|-------|
| **Frontend (Public)** | Next.js 14+ (App Router) | SSR/SSG for SEO pages |
| **Frontend (Admin)** | React + Vite (SPA) | Internal tools, dashboards |
| **UI Components** | shadcn/ui + Radix UI | Lightweight, accessible |
| **Styling** | Tailwind CSS | With design tokens |
| **State Management** | Zustand | Minimal boilerplate |
| **Data Fetching** | TanStack Query | Server state management |
| **Backend** | Express.js + Node 20 | Layered architecture |
| **Language** | TypeScript 5+ | Always required |
| **Database** | PostgreSQL 16 | ACID, jsonb, FTS |
| **ORM** | Prisma | Type-safe, migrations |
| **Cache** | Redis (ioredis) | Sessions, rate limiting |
| **Queue** | BullMQ (default) | RabbitMQ for microservices, Kafka for streaming |
| **Auth** | JWT + bcrypt | 15min access + 7d refresh tokens |
| **Testing** | Vitest + Testing Library | 80% minimum coverage |
| **E2E Testing** | Playwright | Cross-browser |
| **Logging** | Pino | Structured JSON |
| **Monitoring** | Prometheus + Grafana | RED/USE methods |
| **CI/CD** | GitHub Actions | Automated pipelines |
| **API Docs** | OpenAPI 3.0 / Swagger | Mounted at `/api-docs` |

See `rules/tech-stack.md` for the full decision rationale and alternatives.

---

## Mandatory Rules

All rules in `.claude/rules/` are **mandatory** and must be followed at all times.

### Code Quality
| Rule | File | Key Points |
|------|------|------------|
| Clean Code | `clean-code.md` | Meaningful names, small functions, SOLID, no dead code |
| Code Style | `code-style.md` | 2-space indent, single quotes, semicolons, camelCase vars, PascalCase classes |
| Error Handling | `error-handling.md` | `AppError` class, `asyncHandler` wrapper, centralized error middleware |

### Architecture & Design
| Rule | File | Key Points |
|------|------|------------|
| Tech Stack | `tech-stack.md` | Use only approved technologies; evaluate new deps against criteria |
| System Design | `system-design.md` | CAP theorem awareness, circuit breakers, exponential backoff |
| Project Structure | `project-structure.md` | Layered architecture, kebab-case files, feature folders |
| API Conventions | `api-conventions.md` | REST, plural nouns, `{ success, data, error }` envelope, proper status codes |

### Data & Naming
| Rule | File | Key Points |
|------|------|------------|
| Naming | `naming-conventions.md` | Cache: `app:v1:entity:id`, DB: snake_case, env: UPPER_SNAKE |
| Database | `database.md` | Prisma ORM, connection pooling, transactions, no raw SQL in business logic |

### Operations
| Rule | File | Key Points |
|------|------|------------|
| Security | `security.md` | **CRITICAL** — no hardcoded secrets, validate all inputs, bcrypt 12+, Helmet.js |
| Monitoring | `monitoring.md` | Structured JSON logs, Prometheus metrics, RED/USE dashboards, alerting |
| Testing | `testing.md` | 80% unit coverage, all features tested, all bug fixes get regression tests |
| Git Workflow | `git-workflow.md` | Git Flow branches, conventional commits, PR reviews required |

---

## Available Commands

| Command | File | Purpose |
|---------|------|---------|
| `deploy` | `commands/deploy.md` | Pre-deploy checks, build, deploy, post-deploy verification, rollback plan |
| `fix-issue` | `commands/fix-issue.md` | Understand issue, find root cause, plan fix, implement, verify, commit |
| `review` | `commands/review.md` | Code review checklist: quality, security, errors, tests, DB, API standards |

---

## Available Agents

Specialized sub-agents in `.claude/agents/`. Invoke the right agent based on the task domain:

| Agent | File | When to Invoke |
|-------|------|---------------|
| Frontend Developer | `agents/frontend.md` | Components, pages, routing, state management, performance |
| Backend Developer | `agents/backend.md` | APIs, services, DB queries, background jobs, auth |
| Systems Architect | `agents/systems-architect.md` | Architecture decisions, ADRs, system design, scalability |
| UI/UX Designer | `agents/ui-ux-designer.md` | Design system, wireframes, UX patterns, accessibility |
| Project Manager | `agents/project-manager.md` | User stories, sprint planning, status reports, requirements |
| QA Engineer | `agents/qa.md` | Test plans, writing tests, bug reports, coverage analysis |
| Copywriter/SEO | `agents/copywriter-seo.md` | Page copy, microcopy, meta tags, SEO optimization |

---

## Available Skills

| Skill | File | Purpose |
|-------|------|---------|
| Deploy | `skills/deploy/SKILL.md` | Automated deployment: clean state check, tests, build, Docker, health checks, rollback |
| Security Review | `skills/security-review/SKILL.md` | Systematic audit: secrets, injection, auth, headers, CORS, error exposure |

---

## Development Workflows

### Starting a New Feature
1. Create branch: `feature/descriptive-name` from `develop`
2. Delegate to the appropriate agent(s) based on scope
3. Write code following all mandatory rules
4. Write tests (unit + integration) — 80% coverage minimum
5. Run `review` command before committing
6. Commit with conventional format: `feat(scope): description`
7. Open PR targeting `develop`

### Fixing a Bug
1. Create branch: `fix/descriptive-name` from `develop`
2. Run `fix-issue` command to analyze systematically
3. Write a regression test that reproduces the bug
4. Implement the fix
5. Verify the regression test passes
6. Commit: `fix(scope): description`

### Deploying
1. Run `review` command on all changes
2. Run `deploy` command or invoke the deploy skill
3. Verify health checks pass post-deploy
4. Monitor dashboards for anomalies

### Code Review Checklist
- Follows clean code and style rules
- No security violations (hardcoded secrets, unsanitized input, etc.)
- Proper error handling with `AppError`
- Tests included and passing
- Database queries are optimized (no N+1, proper indexes)
- API responses follow the standard envelope format

---

## Key Conventions Quick Reference

| Area | Convention |
|------|-----------|
| **File names** | `kebab-case.ts` (e.g., `user-service.ts`) |
| **Variables/functions** | `camelCase` |
| **Classes/interfaces** | `PascalCase` |
| **Constants** | `UPPER_SNAKE_CASE` |
| **DB tables** | `snake_case` plural (e.g., `user_profiles`) |
| **DB columns** | `snake_case` (e.g., `created_at`, `user_id`) |
| **API routes** | `/api/v1/resource-name` (kebab-case, plural) |
| **Cache keys** | `app:v1:entity:id:variant` |
| **Queue names** | `app.entity.action` (dot-separated) |
| **Domain events** | `entity.past_tense` (e.g., `order.placed`) |
| **Env vars** | `UPPER_SNAKE_CASE` |
| **Commits** | `type(scope): description` |
| **Branches** | `feature/*`, `fix/*`, `hotfix/*`, `release/*` |

---

## Environment Setup

Copy `.env.example` to `.env` and configure:
- `DATABASE_URL` — PostgreSQL connection string
- `REDIS_URL` — Redis connection string
- `JWT_SECRET` / `JWT_REFRESH_SECRET` — Auth secrets (never commit)
- `PORT`, `NODE_ENV`, `APP_URL` — Application settings

See `.env.example` for the full list of required variables.

---

## Agent Behavior

- Be proactive in identifying potential issues
- Always explain changes before making them
- Prefer incremental changes over large rewrites
- Test assumptions before acting
- Follow the testing pyramid: many unit tests, some integration, few E2E
- Never violate security rules — they are non-negotiable
- Use structured JSON logging (Pino) — never `console.log` in production
- Document architectural decisions with ADRs when making significant choices
