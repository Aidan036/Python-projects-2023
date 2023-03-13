import settings as settings
import random

def game_hangman():
    word = random.choice(settings.WORDS)
    so_far = "?"*len(word)
    used_letters = []

    print("Welcome to Hangman.  Good luck!")
    while settings.guesses < settings.max_guess and so_far != word:

        print("you have used the following Letters")
        print(used_letters)
        print()
        print()

        print(settings.HANGMAN[settings.guesses])

        print("\nSo far, the word is:\n", so_far)


        guess = input("\n\npick a letter: ")
        while guess in used_letters:
            guess = input("\n\npick a letter: ")
            if guess.isalpha():
                guess = guess.lower()
            else:
                continue
        used_letters.append(guess)

        if guess in word:
            print("\nYes!", guess, "is in the word!")
            new = ""
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]
            so_far = new

        else:
            print("\nSorry,", guess, "isn't in the word.")
            settings.guesses += 1



# tictac toe methods
def display_instructions():
    print(""" 
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.  
    This will be a showdown between your human brain and my silicon processor. 
    """)
    print("""
    You will make your move known by entering a number, 1 - 9.  The number 
    will correspond to the board position as illustrated:
    """)
    display_board([1,2,3,4,5,6,7,8,9])
    print(" Prepare yourself, human.  The ultimate battle is about to begin.")
    input("Press Enter to Continue")



def display_board(curboard):
    print(str.format("""
    \t {0} | {1} | {2}
    \t-----------
    \t {3} | {4} | {5}
    \t-----------
    \t {6} | {7} | {8} 
    """,curboard[0],curboard[1],curboard[2],curboard[3],curboard[4],curboard[5],curboard[6],curboard[7],curboard[8]))

def new_board():
    board=[]
    for i in range(settings.MAX_SPOTS):
        board.append(settings.E)

    return board

def rock_paper_scissors():
    while True:
        options = ["Rock","Paper","Scissors"]
        choice = settings.display_menu(options,"choose?")
        player = options[choice-1]
        comp = random.choice(options)
        print("You",player)
        print("comp",comp)
        if (comp == options[0] and player == options[2]) or (comp == options[1] and player == options[0]) or \
                (comp == options[2] and player == options[1]):
            print("player lost")
            return "lose"
        elif comp == player:
            print("tie")
            continue
        else:
            print("player wins")
            return "win"

def setPieces(human,comp):
    win = rock_paper_scissors()
    if win == "win":
        human = settings.X
        comp = settings.O
    else:
        human = settings.O
        comp = settings.X

    return human,comp

def human_turn(board,human):
    legal = legal_moves(board)
    choice = None
    while choice not in legal:
        choice = settings.getNumberInRange("What square would you like?",1,settings.MAX_SPOTS)-1
        if choice not in legal:
            print("\nThat square is already occupied, foolish human.  Choose another.\n")

    return choice

def legal_moves(board):
    moves = []
    for i in range(settings.MAX_SPOTS):
        if board[i] == settings.E:
            moves.append(i)
    return moves

def comp_Move(board):
    diff = "easy"
    if diff == "easy":
        # easy
        choice = 0
        legal = legal_moves(board)
        choice = random.choice(legal)
        return choice
    elif diff == "normal":
        pass
    elif diff =="hard":
        pass

def game_TicTacToe():
    human = ""
    comp = ""


    display_instructions()
    board = new_board()
    human, comp = setPieces(human,comp)
    while True:

        if human == settings.X:
            spot = human_turn(board,human)
            board[spot] = human
            display_board(board)
            input()
            spot = comp_Move(board)
            display_board(board)
            board[spot] = comp
            input()
        else:
            spot = comp_Move(board)
            board[spot] = comp
            display_board(board)
            input()
            spot = human_turn(board, human)
            board[spot] = human
            display_board(board)
            input()
