# Code injection via eval/exec
# CWE-95 | Severity: CRITICAL
# File: tests/test_fields.py line 119

**Risk:** User input passed to eval() or exec(). Attacker executes arbitrary Python on the server.

**Fix:** Use ast.literal_eval() for parsing Python literals. Never eval user input.
