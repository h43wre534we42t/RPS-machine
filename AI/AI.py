import random

class AI:
    def __init__(self, lookback, memory):
        self.lookback = lookback
        self.memory = memory
        self.credit = 0

    def random_move(self):
        return random.choice(['R', 'P', 'S'])
    
    def decide(self, string):
        recent_moves = string[-self.lookback::]
        move = self.memory.next_move(recent_moves)

        counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}
        if not move:
            return self.random_move()
        
        return counter_moves[move]

