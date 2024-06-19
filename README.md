## 3D Tic-Tac-Toe Game

This project implements a 3D Tic-Tac-Toe game using Python and Tkinter. The game is played on a 3x3 grid, where two players (human vs. computer) take turns placing their respective markers (X and O) until one player wins or the game ends in a tie.

### Requirements

- Python 3.x
- Tkinter (typically included with Python installations)

### Features

- **Player vs. Computer**: You can play against the computer, which randomly selects its moves.
- **Winning Condition**: The game checks for winning combinations after each move and declares the winner (X or O) or indicates a tie if all squares are filled.
- **Responsive UI**: Built using Tkinter, the game provides a simple yet effective graphical interface for gameplay.

### Usage

1. Navigate to the directory containing the Python script.

2. Run the script with Python:

   ```bash
   python tic_tac_toe.py
   ```

3. The game window will open, displaying a 3x3 grid of buttons. Click on any button to place your marker (X), and the computer will make its move (O) automatically.

4. The game ends when one player wins by completing a line of three markers or when all squares are filled without a winner.

### Implementation Details

- **Global Variables**: `x_o` and `flag` are used to track whose turn it is (`x_o` for player X and `flag` for counting the number of moves).
  
- **Button Click Handling**: The `ButtonClick` function manages the player's move and triggers the computer's move if playing against the computer.

- **Computer Move**: The `computer_move` function randomly selects an available button for the computer's move.

- **Winning Condition**: The `checkforwin` function checks all possible winning combinations after each move and displays a message box when a player wins or when the game ends in a tie.

- **Resetting the Game**: The `reset_game` function resets the game board and variables to start a new game.

### Example

Here’s a brief example of how the game looks and behaves:

![image](https://github.com/SaiKrishnaIyer/SKPYI-143-TASK-PHASE-4-TASK-SKILLRAACE/assets/113880966/ccb6105d-aab3-4f7d-bad5-4e0f7e3b3413)

### Further Customization

Feel free to customize the game further based on your preferences. 

