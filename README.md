CSC426 Machine Learning - Project 1: Tic Tac Toe Learning System
Dr. Bloodgood
Colin Friedlander, Tyler Elvis, Joey Crane, Mina Guglietta

================================================================

OBJECTIVE
---------
Implement a machine learning system for tic tac toe that learns an
evaluation function through self-play. The learner trains against an
opponent with a fixed hand-crafted evaluation function and improves
its strategy over time using the LMS weight update rule.


GETTING STARTED
---------------
This project runs on the TCNJ ELSA HPC system with Python 3.10+.
The only external dependency is matplotlib for generating plots.


RUNNING THE PROJECT
-------------------
Step-by-step commands to run on the TCNJ ELSA HPC system:

    module load python/3.10.11
    python -m pip install matplotlib
    cd ML_Project_One
    python3 -m src.main

This will run the full training loop where the learner plays repeated
games against the fixed-strategy opponent and updates its weights
after each game. Training data is written to the csv directory.


GENERATING PLOTS
----------------
After training has completed, generate the plot PDFs with:

    cd ML_Project_One
    python3 -m graphs.graphs

Plot PDFs will be saved to the graphs/figures directory.


PROJECT STRUCTURE
-----------------
ML_Project_One/
    src/
        main.py            - Entry point, runs training loop
        game_rules.py      - Board state, move logic, win/draw detection
        model.py           - Learned evaluation function and weight updates
    graphs/
        graphs.py          - Plot generation for wins, losses, draws
        figures/           - Output directory for generated plot PDFs
    logs/
        log_utils.py       - Logging utilities and CSV data writing
        log.txt            - Runtime log output
    csv/
        model_weights.csv  - Weight history across training
        wins.csv           - Win counts per training interval
        losses.csv         - Loss counts per training interval
        draws.csv          - Draw counts per training interval
    README


MODULE DESCRIPTIONS
-------------------
src/main.py
    Entry point for the program. Runs the training loop where the
    learner plays repeated games against the fixed-strategy opponent
    and updates its weights after each game.

src/game_rules.py
    Handles board representation, legal move generation, and
    win/draw detection.

src/model.py
    Implements the learned evaluation function as a linear combination
    of board features, and performs weight updates using the LMS rule.

graphs/graphs.py
    Reads training data from the csv directory and generates plots of
    win, loss, and draw percentages over training games. Outputs PDF
    files to the graphs/figures directory.

logs/log_utils.py
    Utility functions for logging runtime information and writing
    training data to CSV files.

csv/
    Stores all training output data. Each CSV file tracks its
    respective metric across training intervals.
