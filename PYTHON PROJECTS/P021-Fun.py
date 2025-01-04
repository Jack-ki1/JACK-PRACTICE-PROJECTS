name = input("please enter your name? ").upper()
print(f"HI THERE [name] WELCOME THIS WONDERFUL EXPERIENCE")

board = [" " for _ in range(9)]

def print_board():
    for row in [board[ i*3:(i+1)*3] for i in range(3)]:
        print("|".join(row))
        
def make_move(player, position):
    if board[position] == " ":
        board[position] = player
        return True
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return  False

player = "x"
for _ in range(9):
    print_board()
    move = int(input(f"player {player}, choose your move (0-8): "))
    if make_move(player, move):
        if check_winner(player):
            print_board()
            print(f"player {player}  wins!")
            break
        player = "O"  if player == "x" else "x"
    else:
        print("it's a tie!")