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
	- src:
		- main.py
		- game_rules.py
		- model.py
	- graphs:
		- graphs.py
		- figures 
	- logs:
		- log_utils.py
		- log.txt
	- csv:
		- model_weights.csv
		- wins.csv
		- losses.csv
		- draws.csv

	- README.MD
    - 
---

## What's In What?
**- src** 
  - main.py, responsible for running the whole program and model training
  - game_rules.py responsible for handling all things board related 
  - model.py responsible for handling all functions required to create the learning model 
  

- **graphs**
  - graphs.py responsible for creating all graphs
  

**- logs**
  - log_utils.py responsible for handling loging information like errors or logging data into a csv

**- csv**
  - model_weights.csv responsible for holding all weights changes of the model 
  - wins.csv, losses.csv, draws.csv responsible for holding info on wins, losses, draws


**- README.MD** responsible for the readme 