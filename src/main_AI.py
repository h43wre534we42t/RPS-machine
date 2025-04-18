import AI
import trie

class Main_AI:
    def __init__(self):
        self.memory = trie.Trie()

        self.ai1 = AI.AI(1, self.memory)
        self.ai2 = AI.AI(2, self.memory)
        self.ai3 = AI.AI(3, self.memory)
        self.ai4 = AI.AI(4, self.memory)
        self.ai5 = AI.AI(5, self.memory)
        self.ais = [self.ai1, self.ai2, self.ai3, self.ai4, self.ai5]

        self.rounds_played = 0
        self.lead = 0

    def play(self, string, opponent_move):
        moves = []

        for ai in self.ais:
            moves.append(ai.decide_move(string))

        print(moves)

        self.rounds_played += 1
        if self.rounds_played == 5:
            self.update_lead()
            self.rounds_played = 0
        
        self.add_credits(moves, opponent_move)
        self.update_memory(string + opponent_move)

        if moves[self.lead] != None:
            return moves[self.lead]

        return self.ai1.random_move()
    
    def ai_moves(self, string):
        moves = []
        for ai in self.ais:
            moves.append(ai.decide_move(string))

        return moves

    def add_credits(self, moves, opponent_move):
        counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}

        for i in range(len(moves)):
            if moves[i] == None:
                continue
            if counter_moves[opponent_move] == moves[i]:
                self.ais[i].credit += 1
            elif counter_moves[moves[i]] == opponent_move:
                self.ais[i].credit -= 1

    def display_credits(self):
        credits = []

        for ai in self.ais:
            credits.append(ai.credit)
        return credits

            
    def update_lead(self):
        max_credit = -1000

        for i in range(len(self.ais)):
            if self.ais[i].credit > max_credit:
                max_credit = self.ais[i].credit
                self.lead = i

    def update_memory(self, string):
        self.memory.add_node(string)
