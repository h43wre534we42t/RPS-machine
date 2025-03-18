class Node:
    def __init__(self, value=None):
        self.children = {}
        self.value = 1

class Trie:
    def __init__(self):
        self.root = Node()

    def add_node(self, value):
        current_node = self.root
        for char in value[:-1]:
            current_node = current_node.children[char]
        last_char = value[-1]
        if last_char in current_node.children:
            current_node = current_node.children[last_char]
            current_node.value += 1
        else:
            current_node.children[last_char] = Node(last_char)

    def frequency(self, string):
        current_node = self.root
        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return 0
        return current_node.value
    
a = Trie()
a.add_node("R")
a.add_node("P")
a.add_node("P")
a.add_node("RP")
a.add_node("RPS")
print(a.frequency("R"))
print(a.frequency("P"))
print(a.frequency("RPS"))