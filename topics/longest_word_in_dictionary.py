class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True


def longest_word(words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    best = ""

    def dfs(node, path):
        nonlocal best
        # only continue exploring if this node marks a complete word
        if len(path) > len(best) or (len(path) == len(best) and path < best):
            best = path

        for char, child in node.children.items():
            if child.is_end_of_word:              # prefix must be buildable
                dfs(child, path + char)

    dfs(trie.root, "")
    return best


words = ["w", "wo", "wor", "worl", "world"]
print(longest_word(words))   # "world"

words2 = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print(longest_word(words2))   # "apple"
