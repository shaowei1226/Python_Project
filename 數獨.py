import tkinter as tk
import random
from tkinter import messagebox

class SudokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("數獨")
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.generate_board()
        
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_board()

    def generate_board(self):
        # Generate a complete Sudoku board
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        for row in range(9):
            for col in range(9):
                self.board[row][col] = numbers[(3 * (row % 3) + row // 3 + col) % 9]
    
    def create_board(self):
        for row in range(9):
            for col in range(9):
                value = self.board[row][col]
                if random.random() < 0.4:  # Adjust the probability to control the number of empty cells
                    value = 0
                if value == 0:
                    entry = tk.Entry(self.root, width=3, font=("Helvetica", 24))
                    entry.grid(row=row, column=col)
                    self.cells[row][col] = entry
                else:
                    label = tk.Label(self.root, text=str(value), font=("Helvetica", 24))
                    label.grid(row=row, column=col)
                    self.cells[row][col] = label
        
        check_button = tk.Button(self.root, text="Check", command=self.check_solution)
        check_button.grid(row=9, columnspan=9)
    
    def check_solution(self):
        for row in range(9):
            for col in range(9):
                entry = self.cells[row][col]
                if isinstance(entry, tk.Entry):
                    value = entry.get()
                    if not value:
                        messagebox.showerror("Error", "Please fill in all cells.")
                        return
                    try:
                        num = int(value)
                        if num < 1 or num > 9:
                            messagebox.showerror("Error", "Invalid input.")
                            return
                        if num != self.board[row][col]:
                            messagebox.showerror("Error", "Incorrect solution.")
                            return
                    except ValueError:
                        messagebox.showerror("Error", "Invalid input.")
                        return
        messagebox.showinfo("Success", "Congratulations! You solved the puzzle!")

def main():
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
