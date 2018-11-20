#SOURCE: https://en.wikipedia.org/wiki/Minimax

class Node:

    def __init__(self):
        self.value = 0
        self.children = []

    def update_value(value):
        self.value = value


#---------------------------------------------------

def minimax(node, depth, maximizingPlayer):
    if (depth == 0) or (node.children == []):
        return node.value
    if (maximizingPlayer == True):
        node.update_value(0)
        for child in node.children:
            node.update_value(max(child.value, minimax(child, depth - 1, False)))
        return node.value
    else:
        node.update_value(0)
        for child in node.children:
            node.update_value(min(node.value, minimax(child, depth - 1, True)))
        return node.value

#---------------------------------------------------

# Initital call to minimax (put in computer move function)
minimax(origin, depth, True)
