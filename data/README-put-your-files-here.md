# data/ — your raw financial documents live here

Everything in this folder stays on your machine: it is excluded from git and must never be uploaded to a web/cloud session.

Before adding statements, black out account numbers and SSNs. Balances, holdings, and transactions stay — that's the analysis.

Suggested layout (optional):

```
data/
├── notes.md            # your annual household notes (template in DATA_CHECKLIST.md)
├── 2026/               # one folder per review year
│   ├── statements/
│   ├── transactions/
│   └── workpapers/     # saved by the review session for reproducibility
```
