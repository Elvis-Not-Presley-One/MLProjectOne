# CSC426 - Machine Learning :: Dr. Bloodgood 
    - Colin Friedlander, Tyler Elvis, Joey Crane, Mina Guglietta

---

# OBJECTIVE
Our objective is to create a machine, learning algorithm for tic-tac-toe that never loses That never loses and finds the most optimal move to win given the board state

-----

## Commit Convention

We use a Conventional Commits–style format so the git history is easy to scan.

```
<type>(<scope>): <subject>
```

| Type         | Purpose                                      |
| ------------ | -------------------------------------------- |
| **feat**     | New feature                                  |
| **fix**      | Bug fix                                      |
| **docs**     | Documentation only                       e   |
| **refactor** | Code change that doesn't alter behavior      |
| **chore**    | Maintenance (deps, formatting, repo hygiene) |
| **ci**       | CI/CD and workflow changes                   |

**Examples:**

- `feat(ui): add GlassIconButton`
- `fix(api): handle null patientId`
- `ci: install pnpm via npm`
- `docs(readme): add commit convention section`
- `chore: bump deps`
- `feat(api)!: rename /v1/messages to /v2/messages` ← breaking change

Keep subjects short (< 72 chars), imperative mood ("add", "fix", "remove").
