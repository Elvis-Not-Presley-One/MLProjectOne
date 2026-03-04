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

---

# Command Line 
```bash
#Adding matplotlib
module load python/3.10.11

python -m pip install matplotlib

# Running The Main 
cd to ML_Project_One

python3 -m src.main
```

---

# File Structure:
- ML_Project_One:
	- Src:
		- main.py
		- game_rules.py
		- model.py
	- Graphs:
		- graphs.py
		- Figures 
	- Logs:
		- log_utils.py
		- Log.txt
	- Csv:
		- model_weights.csv
		- Wins.csv
		- losses.csv
		- Draws.csv

	- README.MD



