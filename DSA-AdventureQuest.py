import tkinter as tk
from tkinter import messagebox, simpledialog
import random


class DSAAdventureQuest:
    def __init__(self, root):
        self.root = root
        self.root.title("DSA Adventure Quest")
        self.root.geometry("800x600")
        self.root.config(bg="#1e1e2e")
        self.score = 0
        self.level = 1
        self.setup_intro()

    def reset_gui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def setup_intro(self):
        self.reset_gui()

        # Background Color
        self.root.config(bg="#1e1e2e")

        # Title Label
        title = tk.Label(
            self.root,
            text="DSA Adventure Quest",
            font=("Verdana", 36, "bold"),
            fg="#f39c12",
            bg="#1e1e2e",
        )
        title.pack(pady=50)

        # Subtitle
        intro_text = tk.Label(
            self.root,
            text="Solve puzzles, level up, and conquer DSA!",
            font=("Verdana", 18),
            fg="#ecf0f1",
            bg="#1e1e2e",
        )
        intro_text.pack(pady=20)

        # Start Game Button
        start_button = tk.Button(
            self.root,
            text="Start Game",
            font=("Verdana", 16, "bold"),
            bg="#2980b9",
            fg="#ecf0f1",
            relief="flat",
            command=self.start_game,
            width=15,
            height=2,
        )
        start_button.pack(pady=30)
        start_button.bind("<Enter>", lambda event, b=start_button: self.on_hover(b))
        start_button.bind("<Leave>", lambda event, b=start_button: self.on_leave(b))

    def on_hover(self, button):
        button.config(bg="#3498db")

    def on_leave(self, button):
        button.config(bg="#2980b9")

    def start_game(self):
        self.level1_array_puzzle()

    # Level 1: Array Puzzle
    def level1_array_puzzle(self):
        self.reset_gui()

        # Level Title
        title = tk.Label(
            self.root,
            text="--- Level 1: Array Puzzle ---",
            font=("Verdana", 28, "bold"),
            fg="#f39c12",
            bg="#1e1e2e",
        )
        title.pack(pady=20)

        # Puzzle Instructions
        puzzle_text = tk.Label(
            self.root,
            text="Rearrange the numbers to form the largest possible number.",
            font=("Verdana", 14),
            fg="#ecf0f1",
            bg="#1e1e2e",
        )
        puzzle_text.pack(pady=15)

        # Generate Random Numbers for Puzzle
        self.numbers = [random.randint(1, 99) for _ in range(5)]
        numbers_text = tk.Label(
            self.root,
            text=f"Numbers: {self.numbers}",
            font=("Verdana", 14),
            fg="#ecf0f1",
            bg="#1e1e2e",
        )
        numbers_text.pack(pady=15)

        # User Input Field
        self.array_input = tk.Entry(
            self.root,
            font=("Verdana", 16),
            width=20,
            justify="center",
            bd=5,
            relief="flat",
            bg="#ecf0f1",
            fg="#2c3e50",
        )
        self.array_input.pack(pady=20)

        # Submit Button
        submit_button = tk.Button(
            self.root,
            text="Submit",
            font=("Verdana", 16, "bold"),
            bg="#2980b9",
            fg="#ecf0f1",
            relief="flat",
            command=self.check_level1_solution,
            width=15,
            height=2,
        )
        submit_button.pack(pady=20)
        submit_button.bind("<Enter>", lambda event, b=submit_button: self.on_hover(b))
        submit_button.bind("<Leave>", lambda event, b=submit_button: self.on_leave(b))

    def check_level1_solution(self):
        try:
            # Get Player's Input
            player_solution = self.array_input.get().strip().split()
            player_solution = [int(num) for num in player_solution]

            if len(player_solution) != len(self.numbers):
                raise ValueError("Please enter the correct number of inputs.")

            # Sort the correct solution
            correct_solution = sorted(self.numbers, reverse=True)

            # Check if the player's solution matches the correct solution
            if player_solution == correct_solution:
                messagebox.showinfo("Success!", "Great job! You solved the puzzle.", icon="info")
                self.score += 10
                self.level2_sorting_visualization()  # Proceed to the next level
            else:
                messagebox.showerror("Incorrect!", f"Oops! The correct order was: {correct_solution}", icon="error")
        except ValueError as e:
            messagebox.showerror("Error", str(e), icon="error")

    # Level 2: Sorting Visualization
    def level2_sorting_visualization(self):
        self.reset_gui()

        title = tk.Label(
            self.root,
            text="--- Level 2: Sorting Visualization ---",
            font=("Verdana", 28, "bold"),
            fg="#f39c12",
            bg="#1e1e2e",
        )
        title.pack(pady=20)

        puzzle_text = tk.Label(
            self.root,
            text="Visualize the Bubble Sort algorithm and predict the sorted array.",
            font=("Verdana", 14),
            fg="#ecf0f1",
            bg="#1e1e2e",
        )
        puzzle_text.pack(pady=15)

        self.sort_array = [random.randint(1, 50) for _ in range(6)]
        array_display = tk.Label(
            self.root,
            text=f"Array: {self.sort_array}",
            font=("Verdana", 14),
            fg="#ecf0f1",
            bg="#1e1e2e",
        )
        array_display.pack(pady=15)

        user_instruction = tk.Label(
            self.root,
            text="Enter the sorted array:",
            font=("Verdana", 14),
            fg="#ecf0f1",
            bg="#1e1e2e",
        )
        user_instruction.pack(pady=15)

        self.sorting_input = tk.Entry(
            self.root,
            font=("Verdana", 16),
            width=20,
            justify="center",
            bd=5,
            relief="flat",
            bg="#ecf0f1",
            fg="#2c3e50",
        )
        self.sorting_input.pack(pady=20)

        submit_button = tk.Button(
            self.root,
            text="Submit",
            font=("Verdana", 16, "bold"),
            bg="#2980b9",
            fg="#ecf0f1",
            relief="flat",
            command=self.check_level2_solution,
            width=15,
            height=2,
        )
        submit_button.pack(pady=20)
        submit_button.bind("<Enter>", lambda event, b=submit_button: self.on_hover(b))
        submit_button.bind("<Leave>", lambda event, b=submit_button: self.on_leave(b))

    def check_level2_solution(self):
        try:
            user_solution = list(map(int, self.sorting_input.get().strip().split()))
            correct_solution = sorted(self.sort_array)

            if user_solution == correct_solution:
                messagebox.showinfo("Success!", "Correct! You predicted the sorted array.", icon="info")
                self.score += 20
                self.level3_connectivity_puzzle()
            else:
                messagebox.showerror("Incorrect!", f"The correct sorted array is: {correct_solution}", icon="error")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers separated by spaces.", icon="error")

    # Level 3: Graph Connectivity Puzzle
    def level3_connectivity_puzzle(self):
        self.reset_gui()

        title = tk.Label(
            self.root,
            text="--- Level 3: Graph Connectivity Puzzle ---",
            font=("Verdana", 28, "bold"),
            fg="#f39c12",
            bg="#1e1e2e",
        )
        title.pack(pady=20)

        puzzle_text = tk.Label(
            self.root,
            text="Determine if all nodes in the graph are connected.",
            font=("Verdana", 14),
            fg="#ecf0f1",
            bg="#1e1e2e",
        )
        puzzle_text.pack(pady=15)

        # Graph Representation
        self.graph = {
            "1": ["2", "3"],
            "2": ["1", "4"],
            "3": ["1"],
            "4": ["2"],
            "5": []  # Node 5 is disconnected
        }

        graph_display = tk.Label(
            self.root,
            text=f"Graph: {self.graph}",
            font=("Verdana", 14),
            fg="#ecf0f1",
            bg="#1e1e2e",
        )
        graph_display.pack(pady=20)

        question = tk.Label(
            self.root,
            text="Is the graph fully connected? (yes/no):",
            font=("Verdana", 14),
            fg="#ecf0f1",
            bg="#1e1e2e",
        )
        question.pack(pady=20)

        self.connectivity_input = tk.Entry(
            self.root,
            font=("Verdana", 16),
            width=20,
            justify="center",
            bd=5,
            relief="flat",
            bg="#ecf0f1",
            fg="#2c3e50",
        )
        self.connectivity_input.pack(pady=20)

        submit_button = tk.Button(
            self.root,
            text="Submit",
            font=("Verdana", 16, "bold"),
            bg="#2980b9",
            fg="#ecf0f1",
            relief="flat",
            command=self.check_level3_solution,
            width=15,
            height=2,
        )
        submit_button.pack(pady=20)
        submit_button.bind("<Enter>", lambda event, b=submit_button: self.on_hover(b))
        submit_button.bind("<Leave>", lambda event, b=submit_button: self.on_leave(b))

    def check_level3_solution(self):
        user_answer = self.connectivity_input.get().strip().lower()
        correct_answer = "no"  # Because node 5 is disconnected

        if user_answer == correct_answer:
            messagebox.showinfo("Success!", "Correct! The graph is not fully connected.", icon="info")
            self.score += 30
            self.game_over()
        else:
            messagebox.showerror("Incorrect!", "The graph is not fully connected. Node 5 is disconnected.", icon="error")

    # Game Over
    def game_over(self):
        self.reset_gui()
        title = tk.Label(
            self.root,
            text="Game Over!",
            font=("Verdana", 32, "bold"),
            fg="#f39c12",
            bg="#1e1e2e",
        )
        title.pack(pady=50)

        score = tk.Label(
            self.root,
            text=f"Your Score: {self.score}",
            font=("Verdana", 18),
            fg="#ecf0f1",
            bg="#1e1e2e",
        )
        score.pack(pady=20)

        play_again = tk.Button(
            self.root,
            text="Play Again",
            font=("Verdana", 16, "bold"),
            bg="#2980b9",
            fg="#ecf0f1",
            relief="flat",
            command=self.setup_intro,
            width=15,
            height=2,
        )
        play_again.pack(pady=30)
        play_again.bind("<Enter>", lambda event, b=play_again: self.on_hover(b))
        play_again.bind("<Leave>", lambda event, b=play_again: self.on_leave(b))

        exit_button = tk.Button(
            self.root,
            text="Exit",
            font=("Verdana", 16, "bold"),
            bg="#e74c3c",
            fg="#ecf0f1",
            relief="flat",
            command=self.root.quit,
            width=15,
            height=2,
        )
        exit_button.pack(pady=20)


# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = DSAAdventureQuest(root)
    root.mainloop()
