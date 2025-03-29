import AI
import trie

class Main_AI:
    def __init__(self):
        self.memory = trie.Trie()
        self.ai1 = AI.AI(2, self.memory)
        self.ai2 = AI.AI(3, self.memory)
        self.ai3 = AI.AI(4, self.memory)
        self.ai4 = AI.AI(5, self.memory)
        self.ai5 = AI.AI(6, self.memory)
        self.ais = [self.ai1, self.ai2, self.ai3, self.ai4, self.ai5]
        self.lead = 0

    def play(self, string, opponent_move):
        moves = []

        for ai in self.ais:
            moves.append(ai.decide(string))

        self.update_lead()
        self.update_memory(string + opponent_move)

        sorted_indices = sorted(range(len(self.ais)), key=lambda i: self.ais[i].credit, reverse=True)
        
        #credits for current move are added last so they don't influence the decision as the AI shouldn't know what move the opponent played
        self.add_credits(moves, opponent_move)

        # Try moves in order of highest credit AIs
        for index in sorted_indices:
            if moves[index] is not None: 
                return moves[index]

        return self.ai1.random_move()

    def add_credits(self, moves, opponent_move):
        counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}

        for i in range(len(moves)):
            if moves[i] == None:
                continue
            if counter_moves[opponent_move] == moves[i]:
                self.ais[i].credit += 1
            elif counter_moves[moves[i]] == opponent_move:
                self.ais[i].credit -= 1
    
    def update_lead(self):
        max_credit = -1000
        for i in range(len(self.ais)):
            if self.ais[i].credit > max_credit:
                max_credit = self.ais[i].credit
                self.lead = i

    def update_memory(self, string):
        self.memory.add_node(string)

    def display_credits(self):
        credits = []
        for ai in self.ais:
            credits.append(ai.credit)
        return credits
