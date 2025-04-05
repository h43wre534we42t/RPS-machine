import random

class AI:
    def __init__(self, lookback, memory):
        self.lookback = lookback
        self.memory = memory
        self.credit = 0

    def random_move(self):
        return random.choice(['R', 'P', 'S'])
    
    def decide_move(self, string):
        if len(string) < self.lookback:
            return None
        recent_moves = string[-self.lookback::]
        move = self.memory.next_move(recent_moves)

        counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}
        if not move:
            return None
        
        return counter_moves[move]

