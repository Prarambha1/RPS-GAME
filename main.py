import random
from colorama import init, Style, Fore

init(autoreset=True)

def get_player_move():
    moves = ['rock', 'paper' , 'scissors']
    print(Fore.CYAN + "Choose your move from rock, paper, or scissors ")
    player_move = input("Enter your move: ").lower()
    while player_move not in moves:
        print(Fore.RED + "Invalid move. Try again!")
        player_move = input("Enter your move: ").lower()
    return player_move

def get_ai_move():
    moves = ['rock', 'paper' , 'scissors']
    ai_move = random.choice(moves)
    print(Fore.YELLOW + f"AI chose: {ai_move}")
    return ai_move

def determine_winner(player, ai):
    if player == ai:
        return "It's a tie!"
    elif (player == "rock" and ai == "scissors") or \
         (player == "scissors" and ai == "paper") or \
         (player == "paper" and ai == "rock"):
        return Fore.GREEN + "You win!"
    else:
        return Fore.RED + "AI wins!"
        
    
def play_game():
    print(Fore.LIGHTMAGENTA_EX + "Welcome to Rock, Paper, Scissors!")
    name = input(Fore.LIGHTYELLOW_EX + "What is your name: ")
    print(Fore.MAGENTA + f"Hello, {name}! Let's start the game.")
    rounds = int(input("How many rounds do you want to play? "))
    player_score, ai_score = 0, 0

    for i in range(rounds):
        print(Style.BRIGHT + Fore.BLUE + f"\nRound {i + 1}")
        player_move = get_player_move()
        ai_move = get_ai_move()
        result = determine_winner(player_move, ai_move)
        print(result)

        # Update scores
        if "You win" in result:
            player_score += 1
        elif "AI wins" in result:
            ai_score += 1

    # Final scores
    print(Style.BRIGHT + f"\nGame Over, {name}, Here are the final scores:")
    print(Fore.GREEN + f"{name}'s Score: {player_score}")
    print(Fore.RED + f"AI Score: {ai_score}")
    if player_score > ai_score:
        print(Fore.GREEN + f"🎉 Congratulations {name}! You won the game!")
    elif player_score < ai_score:
        print(Fore.RED + "😔 AI wins the game. Better luck next time!")
    else:
        print(Fore.YELLOW + "It's a draw!")

# Run the game
if __name__ == "__main__":
    play_game()