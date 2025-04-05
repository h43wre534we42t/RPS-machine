import main_AI


def validate_input(player_input):
    """Validate user input and return cleaned version or None if invalid"""
    player_input = player_input.upper().strip()
    if player_input in ('R', 'P', 'S', 'Q'):
        return player_input
    return None

def main():
    game = main_AI.Main_AI()
    counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}
    full_move_names = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    string = ""
    player_points = 0
    ai_points = 0

    print("Rock Paper Scissors Game \n")
    
    while True:
        print("Rock [R] Paper [P] Scissors [S]       Quit [Q]\n")
        
        player_input = validate_input(input("What is your move: "))

        if player_input is None:
            print("Invalid input! Try again!")
            continue

        if player_input == "Q":
            print("Your points: ", player_points, "    AI points: ", ai_points, "    Score: ", player_points - ai_points)
            print("All AI credits: ", game.display_credits())
            
            break
        
        ai_output = game.play(string, player_input)

        print("You play: ", full_move_names[player_input], "               AI plays: ", full_move_names[ai_output])

        if counter_moves[player_input] == ai_output:
            print("                   You lose!")
            ai_points += 1
        elif counter_moves[ai_output] == player_input:
            print("                   You win!")
            player_points += 1
        else:
            print("                  It's a tie!")

        print("Your points: ", player_points, "    AI points: ", ai_points, "    Score: ", player_points - ai_points)
        print("----------------------------------------------------------")

        string += player_input
