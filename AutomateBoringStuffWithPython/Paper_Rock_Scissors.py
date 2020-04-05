import random, sys

#Decalre and initialize varibales.
wins = 0
losses = 0
ties = 0

while True:
    print(f"{wins} Wins, {losses} Losses, {ties} Ties'")

    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        player_move = input(">")

        if player_move == 'p' or player_move == 'r' or player_move == 's':
            break
        elif player_move == 'q':
            sys.exit()
        else:
            print("Type one of valid inputs p or q or r or s")

    # Display what the player chose:
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')
    
    # Display what the computer chose:
    random_number = random.randint(1, 3)

    if random_number == 1:
        computer_move = 'p'
        print('PAPER')
    elif random_number == 2:
        computer_move = 'r'
        print('ROCK')
    else:
        computer_move = 's'
        print('SCISSORS')
    
    if player_move == computer_move:
        print("It's a tie!")
        ties = ties + 1
    elif (player_move == 'p' and computer_move == 'r') or (player_move == 'r' and computer_move == 's') or (player_move == 's' and computer_move == 'p'):
        print("You Win!")
        wins = wins + 1
    else:
        print("You lose!")
        losses = losses + 1
    


    
