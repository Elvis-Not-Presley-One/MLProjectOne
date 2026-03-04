# CSC426 Machine Learning - Project 1: Tic Tac Toe Learning System
**Dr. Bloodgood**

Colin Friedlander, Tyler Elvis, Joey Crane, Mina Guglietta

---

## Objective

Implement a machine learning system for tic tac toe that learns an evaluation function through self-play. The learner trains against an opponent with a fixed hand-crafted evaluation function and improves its strategy over time using the LMS weight update rule.

---

## Getting Started

### Prerequisites

This project runs on the TCNJ ELSA HPC system with Python 3.10+. The only external dependency is `matplotlib` for generating plots.

### Running the Project
```bash
module load python/3.10.11
python -m pip install matplotlib

cd MLProjectOne
python3 -m src.main
```

### Generating Plots
```bash
cd MLProjectOne
python3 -m graphs.graphs
```

---

## Project Structure
```
ML_Project_One/
├── src/
│   ├── main.py            # Entry point, runs training loop
│   ├── game_rules.py      # Board state, move logic, win/draw detection
│   └── model.py           # Learned evaluation function and weight updates
├── graphs/
│   ├── graphs.py          # Plot generation for wins, losses, draws
│   └── figures/           # Output directory for generated plot PDFs
├── logs/
│   ├── log_utils.py       # Logging utilities and CSV data writing
│   └── log.txt            # Runtime log output
├── csv/
│   ├── model_weights.csv  # Weight history across training
│   ├── wins.csv           # Win counts per training interval
│   ├── losses.csv         # Loss counts per training interval
│   └── draws.csv          # Draw counts per training interval
└── README.md
```

---

## Module Descriptions

### src

- **main.py** - Entry point for the program. Runs the training loop where the learner plays repeated games against the fixed-strategy opponent and updates its weights after each game.
- **game_rules.py** - Handles board representation, legal move generation, and win/draw detection.
- **model.py** - Implements the learned evaluation function as a linear combination of board features, and performs weight updates using the LMS rule.

### graphs

- **graphs.py** - Reads training data from the csv directory and generates plots of win, loss, and draw percentages over training games. Outputs PDF files to the figures directory.

### logs

- **log_utils.py** - Utility functions for logging runtime information and writing training data to CSV files.

### csv

Stores all training output data. Each CSV file tracks its respective metric across training intervals.

---

## Commit Convention

We follow Conventional Commits for a clean git history.
```
<type>(<scope>): <subject>
```

| Type         | Purpose                                      |
| ------------ | -------------------------------------------- |
| **feat**     | New feature                                  |
| **fix**      | Bug fix                                      |
| **docs**     | Documentation only                           |
| **refactor** | Code change that does not alter behavior      |
| **chore**    | Maintenance (deps, formatting, repo hygiene) |
| **ci**       | CI/CD and workflow changes                   |

Keep subjects under 72 characters, imperative mood ("add", "fix", "remove").
