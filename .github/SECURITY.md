# Security Policy

## Supported Versions

BitGenesis is currently under active development.

Security updates are provided for the latest stable release and the current development branch.

| Version            | Supported |
| ------------------ | --------- |
| Latest release     | ✅ Yes     |
| Development branch | ✅ Yes     |
| Older versions     | ❌ No      |

As BitGenesis is an evolving research-oriented cognitive architecture, older versions may not receive security fixes after major architectural changes.

---

## Reporting a Vulnerability

If you discover a potential security vulnerability in BitGenesis, please do **not** open a public GitHub Issue.

Public disclosure of security issues before a fix is available may put users and contributors at risk.

Instead, please report vulnerabilities privately through:

* GitHub Security Advisories (preferred method)
* Private contact with the maintainers

When reporting a vulnerability, please include:

* A clear description of the issue
* Steps to reproduce the problem
* Affected component/module
* Possible impact
* Any relevant logs, screenshots, or proof-of-concept code

The more details provided, the faster the issue can be investigated.

---

## Security Response Process

After receiving a vulnerability report:

1. The maintainers will acknowledge the report.
2. The issue will be reviewed and classified.
3. A fix or mitigation strategy will be developed.
4. A security update will be released when appropriate.
5. Credit may be given to the reporter unless anonymity is requested.

Response times may vary depending on the severity and complexity of the issue.

---

## Scope

Security reports may include, but are not limited to:

* Unauthorized access or privilege escalation
* Data corruption or loss
* Memory persistence vulnerabilities
* Unsafe serialization/deserialization
* Event system abuse
* Runtime isolation issues
* Dependency vulnerabilities
* Information disclosure
* Integrity issues affecting cognitive state, identity, or memory systems

---

## Out of Scope

The following are generally not considered security vulnerabilities:

* Feature requests
* Documentation issues
* Normal bugs without security impact
* Performance improvements
* Code style issues
* Issues requiring physical access to the user's machine

---

## Responsible Disclosure

BitGenesis follows a responsible disclosure approach.

We ask security researchers and contributors to:

* Give maintainers reasonable time to investigate and fix issues
* Avoid accessing or modifying other users' data
* Avoid disrupting services or repositories
* Avoid public disclosure before a fix is available

We appreciate responsible researchers who help improve the security and reliability of BitGenesis.

---

## Security Philosophy

BitGenesis is designed as an open and modular cognitive architecture.

Security is considered a fundamental part of the project architecture, especially regarding:

* Data integrity
* Persistent memory systems
* Identity management
* Event-driven communication
* Extensibility and third-party modules

Contributors are encouraged to consider security implications when designing new components or modifying existing systems.
