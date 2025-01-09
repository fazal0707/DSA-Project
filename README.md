# DSA-Project


# DSA Adventure Quest

DSA Adventure Quest is a fun and interactive game built with Python's `tkinter` library. The game helps players learn and practice Data Structures and Algorithms (DSA) concepts through engaging puzzles and challenges.

## Features

- **Level 1: Array Puzzle**  
  Rearrange a set of numbers to form the largest possible number.

- **Level 2: Sorting Visualization**  
  Predict the result of a Bubble Sort operation on a random array.

- **Level 3: Graph Connectivity Puzzle**  
  Analyze a graph to determine whether all nodes are connected.

- **Interactive GUI**  
  - Modern and clean interface with consistent theming.
  - Button hover effects for better interactivity.
  - Real-time feedback and scoring.

## Requirements

- Python 3.x
- `tkinter` library (pre-installed with Python)

## How to Run

1. Clone or download this repository.
2. Open a terminal or command prompt and navigate to the project folder.
3. Run the following command:
   ```bash
   python DSAAdventureQuest.py
   ```

4. The game window will open. Follow the instructions in each level to play.

## Gameplay Instructions

1. **Start the Game**: Click the **Start Game** button on the intro screen.
2. **Level 1**: Rearrange the given numbers in the input box to form the largest number.
3. **Level 2**: Predict the sorted order of the array displayed on the screen and input it.
4. **Level 3**: Determine if the graph displayed is fully connected and input "yes" or "no."
5. **Game Over**: View your final score and choose to play again or exit.

## Code Structure

- **Main Class**: `DSAAdventureQuest`  
  Handles the game logic and GUI setup.
- **Functions**:  
  - `setup_intro`: Sets up the intro screen.  
  - `level1_array_puzzle`: Displays Level 1.  
  - `level2_sorting_visualization`: Displays Level 2.  
  - `level3_connectivity_puzzle`: Displays Level 3.  
  - `game_over`: Displays the final score and play-again options.

## Customization

You can modify the game puzzles and logic to include more levels or challenges. Adjustments to GUI themes can be made by changing the color codes and font settings in the script.

## Future Improvements

- Add more levels with different DSA concepts (e.g., binary trees, dynamic programming).
- Include animations for sorting and graph traversal algorithms.
- Save high scores and player progress.


Enjoy learning DSA while playing! 🎮
