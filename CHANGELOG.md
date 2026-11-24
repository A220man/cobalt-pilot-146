# Changelog

## 1.1.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

All notable changes to cobalt-pilot-146 will be documented in this file.

## 1.0.0 — 2026-11-24

- Fixed: FastAPI v1 router properly included in main app
- Added: /v1/status and /v1/health endpoints
- Updated: app/main.py now includes app.api.v1.routes router without redundant prefix
