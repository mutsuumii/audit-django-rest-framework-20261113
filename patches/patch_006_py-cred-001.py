# Hardcoded credentials
# CWE-798 | Severity: HIGH
# File: tests/browsable_api/test_browsable_api.py line 41

**Risk:** Credentials hardcoded in source. Anyone with repo access can extract them.

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
