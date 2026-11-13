# Security audit: encode/django-rest-framework

Date: 2026-11-13 | Auditor: [mutsuumii](https://github.com/mutsuumii)

## Summary

Found 9 issue(s): 3 critical, 6 high.

## Findings

### 1. [HIGH] Hardcoded credentials

**CWE-798** | `tests/test_testing.py` line 167

Credentials hardcoded in source. Anyone with repo access can extract them.

```
self.client.login(username='example', password='password')
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 2. [HIGH] Hardcoded credentials

**CWE-798** | `tests/test_testing.py` line 177

Credentials hardcoded in source. Anyone with repo access can extract them.

```
client.login(username='example', password='password')
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 3. [CRITICAL] Insecure deserialization

**CWE-502** | `tests/test_relations.py` line 518

Deserializing untrusted data with pickle or yaml.load. Attacker executes arbitrary code.

```
upkled = pickle.loads(pickle.dumps(self.default_hyperlink))
```

**Fix:** Use json for data, yaml.safe_load() for YAML. Never unpickle untrusted input.
---

### 4. [HIGH] DOM XSS via innerHTML

**CWE-79** | `docs/theme/js/prettify-1.0.js` line 25

Setting innerHTML with user data allows script injection in other users' browsers.

```
hashComments:3,cStyleComments:!0,multilineStrings:!0,tripleQuotedStrings:!0,regexLiterals:!0}),["coffee"]);k(x([],[["str",/^[\S\s]+/]]),["regex"]);window.prettyPrintOne=function(a,m,e){var h=document.createElement("PRE");h.innerHTML=a;e&&D(h,e);E({g:m,i:e,h:h});return h.innerHTML};window.prettyPrint=function(a){function m(){for(var e=window.PR_SHOULD_USE_CONTINUATION?l.now()+250:Infinity;p<h.length&&l.now()<e;p++){var n=h[p],k=n.className;if(k.indexOf("prettyprint")>=0){var k=k.match(g),f,b;if(b=
```

**Fix:** Use textContent. If HTML is needed, sanitize with DOMPurify.sanitize() first.
---

### 5. [CRITICAL] Code injection via eval/exec

**CWE-95** | `tests/test_fields.py` line 119

User input passed to eval() or exec(). Attacker executes arbitrary Python on the server.

```
exec("def valid(param: str='value'):  pass", locals)
```

**Fix:** Use ast.literal_eval() for parsing Python literals. Never eval user input.
---

### 6. [HIGH] Hardcoded credentials

**CWE-798** | `tests/browsable_api/test_browsable_api.py` line 41

Credentials hardcoded in source. Anyone with repo access can extract them.

```
self.password = 'password'
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 7. [HIGH] Hardcoded credentials

**CWE-798** | `tests/browsable_api/test_browsable_api.py` line 82

Credentials hardcoded in source. Anyone with repo access can extract them.

```
self.password = 'password'
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 8. [HIGH] Hardcoded credentials

**CWE-798** | `tests/test_negotiation.py` line 163

Credentials hardcoded in source. Anyone with repo access can extract them.

```
token = 'application/json; indent=8'
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 9. [CRITICAL] Insecure deserialization

**CWE-502** | `tests/test_serializer.py` line 600

Deserializing untrusted data with pickle or yaml.load. Attacker executes arbitrary code.

```
data = pickle.loads(pickled)
```

**Fix:** Use json for data, yaml.safe_load() for YAML. Never unpickle untrusted input.
---
