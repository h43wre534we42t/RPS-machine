#FOR TESTS
import trie
import AI

first_moves = ("R", "R", "P", "S", "S")
game_length = 0
string = ""
memory = trie.Trie()
ai1 = AI.AI(2, memory)

print("just testing for now")
user_input = "A"
while user_input != "Q":
    user_input = input("What is your move? (R, P, S)   (Q to quit)")

    if game_length < 5:
        print(first_moves[game_length])
    else:
        print(ai1.decide(string))

    string += user_input
    memory.add_node(string[-5:])

    game_length += 1