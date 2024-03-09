# File: CS112_A2_T21
# Purpose:the game is a 2 player turn each one pick a number from 1 to 9 if the sum of 3 numbers equal 15 the player will win if no winner game will be a draw
# Author: Madonna Sameh Samir
# ID: 20230299
#faculty of computers and artificial intelligence cairo universty


# Function to check if the sum of any three numbers in the list equals 15
def check_sum(num):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            for k in range(j + 1, len(num)):
                if num[i] + num[j] + num[k] == 15:
                    return True

# Function to play the game
def the_game():
    # Get player names
    player1_name = input("Player 1, please enter your name: ")
    player2_name = input("Player 2, please enter your name: ")

    num_List = list(range(1, 10))
    player1 = []
    player2 = []

    # Loop for 9 turns
    for _ in range(9):
        # player 1 turn
        print(f"\n{player1_name}'s turn")
        print(f"Numbers left: {num_List}")
        while True:
            try:
                pick = int(input(f"{player1_name}, pick a number: "))
                if pick in num_List:
                    player1.append(pick)
                    num_List.remove(pick)
                    break
                else:
                    print("Invalid pick. The number is not available.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Check if player 1 has won
        if check_sum(player1):
            print(f"{player1_name} wins!")
            break

        # If there is no winner after 9 turns
        if not num_List:
            print("\nIt's a draw!")
            break

        # player 2 turn
        print(f"\n{player2_name}'s turn")
        print(f"Numbers left: {num_List}")
        while True:
            try:
                pick = int(input(f"{player2_name}, pick a number: "))
                if pick in num_List:
                    player2.append(pick)
                    num_List.remove(pick)
                    break
                else:
                    print("Invalid pick. The number is not available.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Check if player 2 has won
        if check_sum(player2):
            print(f"{player2_name} wins!")
            break

        # If there is no winner after 9 turns
        if not num_List:
            print("\nIt's a draw!")
            break

# Ask the user if they want to play again or not
def playing_again():
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes" :
            the_game()
        elif play_again == "no" :
            print("Goodbye. I hope you enjoyed playing.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no.'")

# Start the game
the_game()

# Ask if the user wants to play again
playing_again()