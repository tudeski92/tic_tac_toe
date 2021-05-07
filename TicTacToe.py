from random import shuffle
from random import randint
from tkinter import *
from tkinter import messagebox



#commit 1

class TicTac:

    def __init__(self, player_one="Player 1", player_two="Player 2"):
        self.signs = ["X", "O"]
        shuffle(self.signs)
        self.board = [
            ["' '","' '","' '"],
            ["' '","' '","' '"],
            ["' '","' '","' '"]
        ]
        self.player_one = [player_one, self.signs.pop()]
        self.player_two = [player_two, self.signs.pop()]
        self.current_player = self.player_one if randint(0,1) == 0 else self.player_two
        print(f"Player 1: {self.player_one[0]}, {self.player_one[1]}")
        print(f"Player 2: {self.player_two[0]}, {self.player_two[1]}")
        print(f"{self.current_player[0]} starts")
        self.busy_position = list()

    def print_board(self):
        for row in self.board:
            for column in row:
                print(column, end='\t')
            print('')

    def reinitialize_board(self):
        self.board = [
            ["' '","' '","' '"],
            ["' '","' '","' '"],
            ["' '","' '","' '"]
        ]

    def board_full(self):
        counter = 0
        for raw in self.board:
            for column in raw:
                if column in ["X", "O"]:
                    counter += 1
        return True if counter == 9 else False

    def switch_player(self):
        if self.current_player[0] == self.player_one[0]:
            self.current_player = self.player_two
        else:
            self.current_player = self.player_one

    def insert(self, *args):
        raw, column = args
        self.board[raw][column] = self.current_player[1]

    def is_busy(self, *args):
        if args not in self.busy_position:
            self.busy_position.append(args)
        else:
            print(f"Current player: {self.current_player[0]}, {self.current_player[1]}")
            raise Exception(f"{args} position is busy, try another one")

    def check_win(self):
        self.print_board()
        if self.board[0][0] == self.board[0][1] == self.board[0][2] == self.current_player[1]:
            print(f"Winner {self.current_player[0]}")
            return True
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == self.current_player[1]:
            print(f"Winner {self.current_player[0]}")
            return True
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == self.current_player[1]:
            print(f"Winner {self.current_player[0]}")
            return True
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == self.current_player[1]:
            print(f"Winner {self.current_player[0]}")
            return True
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == self.current_player[1]:
            print(f"Winner {self.current_player[0]}")
            return True
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == self.current_player[1]:
            print(f"Winner {self.current_player[0]}")
            return True
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player[1]:
            print(f"Winner {self.current_player[0]}")
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player[1]:
            print(f"Winner {self.current_player[0]}")
            return True
        elif self.board_full():
            self.current_player = ["Tie", ""]
            print("Tie, board is full")
            return True
        else:
            self.switch_player()
            print(f"Current player: {self.current_player[0]}, {self.current_player[1]}")
            return False


class Board():

    def __init__(self, master, player_1="Player 1", player_2="Player 2"):
        self.player_1 = player_1
        self.player_2 = player_2
        self.tictac=TicTac(self.player_1, self.player_2)
        self.top_frame = Frame(master, width=300, height=70)
        self.bottom_frame = Frame(master, width=300, height=300)
        self.top_frame.pack(side=TOP)
        self.bottom_frame.pack(side=BOTTOM)
        self.label_p1 = Label(self.top_frame, text=f"{self.tictac.player_one[0]}, {self.tictac.player_one[1]}")
        self.label_p2 = Label(self.top_frame, text=f"{self.tictac.player_two[0]}, {self.tictac.player_two[1]}")
        self.label_current = Label(self.top_frame, text=f"Current player: {self.tictac.current_player[0]}, {self.tictac.current_player[1]}")
        self.label_p1.place(x=0, y=0)
        self.label_p2.place(x=0, y=20)
        self.label_current.place(x=0, y=40)
        self.button00 = Button(self.bottom_frame, text="", width=10, height=5, command=self.disable_00)
        self.button01 = Button(self.bottom_frame, text="", width=10, height=5, command=self.disable_01)
        self.button02 = Button(self.bottom_frame, text="", width=10, height=5, command=self.disable_02)
        self.button10 = Button(self.bottom_frame, text="", width=10, height=5, command=self.disable_10)
        self.button11 = Button(self.bottom_frame, text="", width=10, height=5, command=self.disable_11)
        self.button12 = Button(self.bottom_frame, text="", width=10, height=5, command=self.disable_12)
        self.button20 = Button(self.bottom_frame, text="", width=10, height=5, command=self.disable_20)
        self.button21 = Button(self.bottom_frame, text="", width=10, height=5, command=self.disable_21)
        self.button22 = Button(self.bottom_frame, text="", width=10, height=5, command=self.disable_22)
        self.button00.place(x=0, y=0)
        self.button01.place(x=90, y=0)
        self.button02.place(x=180, y=0)
        self.button10.place(x=0, y=90)
        self.button11.place(x=90, y=90)
        self.button12.place(x=180, y=90)
        self.button20.place(x=0, y=180)
        self.button21.place(x=90, y=180)
        self.button22.place(x=180, y=180)

    def disable_00(self):
        self.button00["state"] = DISABLED
        self.button00["text"] = self.tictac.current_player[1]
        self.tictac.insert(0, 0)
        result = self.tictac.check_win()
        if result:
            messagebox.showinfo("Winner", f"{self.tictac.current_player[0]}")
            self.reinitialize()
        self.label_current["text"] = f"Current player: {self.tictac.current_player[0]}, {self.tictac.current_player[1]}"

    def disable_01(self):
        self.button01["state"] = DISABLED
        self.button01["text"] = self.tictac.current_player[1]
        self.tictac.insert(0, 1)
        result = self.tictac.check_win()
        if result:
            messagebox.showinfo("Winner", f"{self.tictac.current_player[0]}")
            self.reinitialize()
        self.label_current["text"] = f"Current player: {self.tictac.current_player[0]}, {self.tictac.current_player[1]}"

    def disable_02(self):
        self.button02["state"] = DISABLED
        self.button02["text"] = self.tictac.current_player[1]
        self.tictac.insert(0, 2)
        result = self.tictac.check_win()
        if result:
            messagebox.showinfo("Winner", f"{self.tictac.current_player[0]}")
            self.reinitialize()
        self.label_current["text"] = f"Current player: {self.tictac.current_player[0]}, {self.tictac.current_player[1]}"

    def disable_10(self):
        self.button10["state"] = DISABLED
        self.button10["text"] = self.tictac.current_player[1]
        self.tictac.insert(1, 0)
        result = self.tictac.check_win()
        if result:
            messagebox.showinfo("Winner", f"{self.tictac.current_player[0]}")
            self.reinitialize()
        self.label_current["text"] = f"Current player: {self.tictac.current_player[0]}, {self.tictac.current_player[1]}"

    def disable_11(self):
        self.button11["state"] = DISABLED
        self.button11["text"] = self.tictac.current_player[1]
        self.tictac.insert(1, 1)
        result = self.tictac.check_win()
        if result:
            messagebox.showinfo("Winner", f"{self.tictac.current_player[0]}")
            self.reinitialize()
        self.label_current["text"] = f"Current player: {self.tictac.current_player[0]}, {self.tictac.current_player[1]}"

    def disable_12(self):
        self.button12["state"] = DISABLED
        self.button12["text"] = self.tictac.current_player[1]
        self.tictac.insert(1, 2)
        result = self.tictac.check_win()
        if result:
            messagebox.showinfo("Winner", f"{self.tictac.current_player[0]}")
            self.reinitialize()
        self.label_current["text"] = f"Current player: {self.tictac.current_player[0]}, {self.tictac.current_player[1]}"

    def disable_20(self):
        self.button20["state"] = DISABLED
        self.button20["text"] = self.tictac.current_player[1]
        self.tictac.insert(2, 0)
        result = self.tictac.check_win()
        if result:
            messagebox.showinfo("Winner", f"{self.tictac.current_player[0]}")
            self.reinitialize()
        self.label_current["text"] = f"Current player: {self.tictac.current_player[0]}, {self.tictac.current_player[1]}"

    def disable_21(self):
        self.button21["state"] = DISABLED
        self.button21["text"] = self.tictac.current_player[1]
        self.tictac.insert(2, 1)
        result = self.tictac.check_win()
        if result:
            messagebox.showinfo("Winner", f"{self.tictac.current_player[0]}")
            self.reinitialize()
        self.label_current["text"] = f"Current player: {self.tictac.current_player[0]}, {self.tictac.current_player[1]}"

    def disable_22(self):
        self.button22["state"] = DISABLED
        self.button22["text"] = self.tictac.current_player[1]
        self.tictac.insert(2, 2)
        result = self.tictac.check_win()
        if result:
            messagebox.showinfo("Winner", f"{self.tictac.current_player[0]}")
            self.reinitialize()
        self.label_current["text"] = f"Current player: {self.tictac.current_player[0]}, {self.tictac.current_player[1]}"

    def reinitialize(self):
        self.tictac.reinitialize_board()
        self.tictac = TicTac(self.player_1, self.player_2)
        self.button00["state"] = NORMAL
        self.button00["text"] = ""
        self.button01["state"] = NORMAL
        self.button01["text"] = ""
        self.button02["state"] = NORMAL
        self.button02["text"] = ""
        self.button10["state"] = NORMAL
        self.button10["text"] = ""
        self.button11["state"] = NORMAL
        self.button11["text"] = ""
        self.button12["state"] = NORMAL
        self.button12["text"] = ""
        self.button20["state"] = NORMAL
        self.button20["text"] = ""
        self.button21["state"] = NORMAL
        self.button21["text"] = ""
        self.button22["state"] = NORMAL
        self.button22["text"] = ""

if __name__ == "__main__":
    root = Tk()
    root.resizable(False, False)
    root.geometry("260x335")
    root.title("Tic Tac Toe")
    board = Board(root, "Andrzej", "Kornelia")
    root.mainloop()

