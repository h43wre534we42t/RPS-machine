class Node:
    def __init__(self, value=None):
        self.children = {}
        self.name = value
        self.count = 0

class Trie:
    def __init__(self):
        self.root = Node()

    #example. if value = "RPS" adds "R->P->S"  and "P->S" nodes to trie
    def add_node(self, value):
        for start in range(len(value)-1):
            current_node = self.root
            for char in value[start:]:
                if char in current_node.children:
                    current_node = current_node.children[char]
                else:
                    current_node.children[char] = Node(char)
                    current_node = current_node.children[char]
            current_node.count += 1

    def frequency(self, string):
        current_node = self.root
        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return 0
        return current_node.count
    
    def frequency_list(self, string):
        current_node = self.root
        for char in string:
            if char not in current_node.children:
                return []
            current_node = current_node.children[char]
            
        frequencies = []
        for char, node in current_node.children.items():
            frequencies.append((node.name, node.count))

        return frequencies

    def next_move(self, string):
        moves = self.frequency_list(string)
        if moves == []:
            return None
        highest = max(moves, key=lambda x: x[1])
        if highest[1] == 0:
           return None
        return highest[0]
