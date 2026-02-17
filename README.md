# This Rock-Paper-Scissors game is a lightweight, command-line interface (CLI) application developed in Python. It provides a digital version of the classic hand game, allowing a user to compete against a computer opponent.The program is built using foundational Python concepts, including conditional logic, infinite loops, and input handling. It leverages the Python random library to ensure that the computer's choices are unpredictable and unbiased for every round.

# Key Features
# Randomized Opponent: Uses the random.choice() method to select between Rock, Paper, and Scissors for the computer.

# Case-Insensitive Input: The script uses the .capitalize() method, allowing users to enter "rock," "ROCK," or "Rock" without causing errors.

# Input Validation: Checks user input against the valid list of choices and prompts for a correct entry if the input is invalid.

# Continuous Gameplay: Wrapped in a while True loop, the game allows for multiple rounds of play without needing to restart the script.

# Exit Functionality: Includes a dedicated "Exit" command to gracefully terminate the program.

# Game Logic and Rules
# The winner is determined by comparing the user's input against the computer's choice based on the following standard rules:

# User Choice	Computer Choice	Result
# Rock	Rock	Match Tie
# Rock	Paper	Computer Win
# Rock	Scissor	User Win
# Paper	Paper	Match Tie
# Paper	Rock	User Win
# Paper	Scissor	Computer Win
# Scissor	Scissor	Match Tie
# Scissor	Paper	User Win
# Scissor	Rock	Computer Win
