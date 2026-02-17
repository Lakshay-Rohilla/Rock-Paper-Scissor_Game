**Rock Paper Scissor Game**

A professional command-line interface application developed in Python that brings the classic hand game to your terminal. This script allows a user to compete against a computer opponent with randomized decision-making and instant result processing.

**Core Features**

**Randomized Opponent**: Utilizes the Python random library to ensure the computer makes unpredictable and fair moves every round.

**Case-Insensitive Input**: Handles user input flexibly by allowing various capitalizations of the choices Rock, Paper, or Scissor.

**Infinite Gameplay Loop**: Allows users to play multiple rounds continuously without needing to restart the application.

**Graceful Exit**: Includes a dedicated exit command to terminate the game session smoothly at any time.

**Game Logic**

The application determines the winner based on these standard competitive rules:

**Rock Scenarios**: Rock vs Rock results in a Tie; Rock vs Paper results in a Computer Win; Rock vs Scissor results in a User Win.

**Paper Scenarios**: Paper vs Paper results in a Tie; Paper vs Rock results in a User Win; Paper vs Scissor results in a Computer Win.

**Scissor Scenarios**: Scissor vs Scissor results in a Tie; Scissor vs Paper results in a User Win; Scissor vs Rock results in a Computer Win.

**Installation and Usage**

**Prerequisites**: Ensure Python 3.x is installed on your local machine.

**Deployment**: Clone or download the game script file to your directory.

**Execution**: Run the script via the terminal using the command: python game.py

**Operation**: Enter Rock, Paper, or Scissor when prompted, or type Exit to close the game.

**Technical Details**

**Language**: Python

**Input Handling**: Standard CLI input with string capitalization and validation.

**Dependencies**: None (Uses Python Standard Library random module).