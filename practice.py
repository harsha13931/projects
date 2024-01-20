import random

'''l=['farahan','gulpa','karthik']
s=['kabadi','cricket','volleyball']

k=1
while(k==1):
     s1= random.choice(l)
     s2=random.choice(s)
     print(f'name is :{s1}  game is {s2} ')
     print("if you want to continue enter '1' to quit enter '2' ")
     k1=int(input())
     if k1==2:
         break'''


'''def dice():
   s=random.randint(1,6)
   return s

matrikx=[]
num=0 
for i in  range(10,0,-1):
    m1 = []
    for j in range(10,0,-1):
        num+=1
        m1.append(num)
    if i%2==0:


        matrikx.append(m1)
        m1.reverse()
        print(m1)
    else:
        matrikx.append((m1[::-1]))

print(matrikx)
player=dice()
print(player)
for i in matrikx:
    pass'''


'''
import random

def dice():
    return random.randint(1, 6)

matrikx = []
num = 0
for i in range(10, 0, -1):
    m1 = []
    for j in range(10, 0, -1):
        num += 1
        m1.append(num)
    if i % 2 == 0:
        matrikx.append(m1)
        print(m1.reverse())'''
'''
    else:
        matrikx.append(m1[::-1])

print(matrikx)

player = dice()
print("Player rolled:", player)
'''

digits = [9, 9]
s = ''.join(map(str, digits))
k = int(s) + 1
l = [int(digit) for digit in str(k)]

print(l)



'''def play():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

player1_name = input("Enter name for player 1: ")
player2_name = input("Enter name for player 2: ")

player1_points = 0
player2_points = 0

print("Press 1 to play the game, or any other key to quit.")
play_game = input()

while play_game == '1':
    player1_choice = play()
    player2_choice = play()
    print(f"{player1_name} chose {player1_choice}")
    print(f"{player2_name} chose {player2_choice}")

    if player1_choice == player2_choice:
        print("It's a tie!")
    elif (player1_choice == 'rock' and player2_choice == 'scissors') or (
         player1_choice == 'scissors' and player2_choice == 'paper') or (
         player1_choice == 'paper' and player2_choice == 'rock'):
        player1_points += 1
        print(f"{player1_name} wins this round!")
    else:
        player2_points += 1
        print(f"{player2_name} wins this round!")

    print(f"{player1_name}: {player1_points} points")
    print(f"{player2_name}: {player2_points} points")

    print("Press 1 to play another round, or any other key to quit.")
    play_game = input()


'''




'''import random

def roll_die():
    return random.randint(1, 6)

def move_player(player, roll):
    player += roll
    if player in snakes_and_ladders:
        player = snakes_and_ladders[player]
    return player

def print_board(player1, player2):
    for row in range(9, 0, -1):
        for col in range(1, 11):
            cell_num = (row - 1) * 10 + col
            if cell_num in snakes_and_ladders:
                print(f'{snakes_and_ladders[cell_num]:02}', end=' ')
            elif player1 == cell_num:
                print('P1', end=' ')
            elif player2 == cell_num:
                print('P2', end=' ')
            else:
                print(f'{cell_num:02}', end=' ')
        print()

def play_ladder_game():
    player1, player2 = 1, 1

    while player1 < 100 and player2 < 100:
        input("Press Enter to roll the dice for Player 1.")
        roll = roll_die()
        print(f"Player 1 rolled a {roll}.")
        player1 = move_player(player1, roll)
        if player1 >= 100:
            print("Player 1 wins!")
            break

        input("Press Enter to roll the dice for Player 2.")
        roll = roll_die()
        print(f"Player 2 rolled a {roll}.")
        player2 = move_player(player2, roll)
        if player2 >= 100:
            print("Player 2 wins!")
            break

        print_board(player1, player2)

snakes_and_ladders = {
    2: 38, 7: 14, 8: 31, 15: 26, 16: 6,
    21: 42, 28: 84, 36: 44, 46: 25, 49: 11,
    51: 67, 62: 19, 64: 60, 71: 91, 74: 53,
    78: 98, 87: 94, 89: 68, 92: 88, 95: 75,
    99: 80
}

play_ladder_game()
'''

'''def print_board(player1, player2):
    board = [
        "  100  99  98  97  96  95  94  93  92  91",
        "    81  82  83  84  85  86  87  88  89  90",
        "  80  79  78  77  76  75  74  73  72  71",
        "    61  62  63  64  65  66  67  68  69  70",
        "  60  59  58  57  56  55  54  53  52  51",
        "    41  42  43  44  45  46  47  48  49  50",
        "  40  39  38  37  36  35  34  33  32  31",
        "    21  22  23  24  25  26  27  28  29  30",
        "  20  19  18  17  16  15  14  13  12  11",
        "  1   2   3   4   5   6   7   8   9   10"
    ]

    for row in board:
        print(row)

    print(f"Player 1 is at position {player1}")
    print(f"Player 2 is at position {player2}")

# Example usage:
player1_position = 1
player2_position = 1
print_board(player1_position, player2_position)
'''