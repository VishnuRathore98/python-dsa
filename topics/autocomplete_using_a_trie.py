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

    def autocomplete(self, prefix):
        node = self.root
        # step 1: walk down to the node representing the prefix
        for char in prefix:
            if char not in node.children:
                return []   # no words with this prefix
            node = node.children[char]

        # step 2: collect all complete words under this node
        results = []
        self._collect_words(node, prefix, results)
        return results

    def _collect_words(self, node, path, results):
        if node.is_end_of_word:
            results.append(path)
        for char, child in node.children.items():
            self._collect_words(child, path + char, results)


trie = Trie()
for word in ["cat", "car", "card", "care", "careful", "dog", "do"]:
    trie.insert(word)

print(trie.autocomplete("car"))    # ['car', 'card', 'care', 'careful']
print(trie.autocomplete("do"))     # ['do', 'dog']
print(trie.autocomplete("cat"))    # ['cat']
print(trie.autocomplete("xyz"))    # []
