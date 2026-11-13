# DOM XSS via innerHTML
# CWE-79 | Severity: HIGH
# File: docs/theme/js/prettify-1.0.js line 25

**Risk:** Setting innerHTML with user data allows script injection in other users' browsers.

**Fix:** Use textContent. If HTML is needed, sanitize with DOMPurify.sanitize() first.
