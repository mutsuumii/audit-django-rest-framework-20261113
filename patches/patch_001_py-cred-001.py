# Hardcoded credentials
# CWE-798 | Severity: HIGH
# File: tests/test_testing.py line 167

**Risk:** Credentials hardcoded in source. Anyone with repo access can extract them.

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
