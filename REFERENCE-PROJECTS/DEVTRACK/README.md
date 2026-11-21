# DevTrack — AISDF Reference Project

Status: **REFERENCE SPECIFICATION / NOT IMPLEMENTED**. This project is a controlled validation exercise for AISDF. It is not evidence that AISDF has already delivered a working application.

## Objective
Build a small developer learning and skill tracker to test AISDF's end-to-end lifecycle. Initial release is intentionally narrow: create learning goals, record learning sessions, track skills and show progress.

## Suggested scope
- Create/edit/archive skill records.
- Create learning goals with target dates.
- Record learning sessions (date, duration, notes, linked skill).
- Show progress summaries and simple filters.
- Export user-owned data.

## Explicit non-goals for first validation
Social feeds, AI recommendations, payments, multi-tenant organizations, mobile native apps, complex gamification and integrations.

## Suggested implementation baseline
Use a stack selected only after requirements and compatibility review. A simple web app with a relational database is sufficient. Do not treat any stack in this document as an approved decision.

## Validation evidence to collect
PRD approval; UX flows; architecture decision records; task graph; commit/diff references; executed test logs; security review; accessibility checks; staging deployment evidence; smoke-test report; completion report; known limitations.

## Pass condition
An independent reviewer can reproduce the build/test process and trace each in-scope requirement to implementation and verification. Production deployment is not required for the first validation; staging is sufficient.
