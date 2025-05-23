# jogo-da-velhar


import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Jogo da Velha")

        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        for i in range(9):
            button = tk.Button(
                master,
                text="",
                font=("Arial", 40),
                width=3,
                height=1,
                command=lambda j=i: self.button_click(j),
            )
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def button_click(self, position):
        if self.board[position] == "":
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player)
            if self.check_win():
                messagebox.showinfo("Fim de Jogo", f"Jogador {self.current_player} venceu!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.reset_board()
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
            [0, 4, 8], [2, 4, 6]             # Diagonais
        ]
        for condition in win_conditions:
            if (self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ""):
                return True
        return False

    def check_draw(self):
        return all(cell != "" for cell in self.board)

    def reset_board(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    gui = TicTacToeGUI(root)
    root.mainloop()
