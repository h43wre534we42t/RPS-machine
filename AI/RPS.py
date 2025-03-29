import main_AI

a = main_AI.Main_AI()
first_moves = ("R", "R", "P", "S", "S", "P")
game_length = 0
string = ""

print("just testing for now")
user_input = "A"
while user_input != "Q":
    user_input = input("What is your move? (R, P, S)   (Q to quit)  ")

    if game_length < 6:
        print(first_moves[game_length])
    else:
        print(a.play(string, user_input))
        print(a.display_credits())

    string += user_input


    game_length += 1