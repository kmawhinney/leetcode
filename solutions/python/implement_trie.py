class TrieNode:
    def __init__(self):
        self.children = {} # character:TrieNode
        self.word_end = False # indicates where a word ends


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children: # if character not in Trie, add it
                curr.children[c] = TrieNode()
            curr = curr.children[c] # move curr to the TrieNode at the next character
        curr.word_end = True # mark end of word

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children: # if character not in Trie, word not in Trie
                return False
            curr = curr.children[c]
        return curr.word_end # if word_end is True, we know that this word is already in Trie

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children: # if character not in Trie, prefix not in Trie
                return False
            curr = curr.children[c]
        return True # if we don't ever return False, we know the entire prefix is in Trie


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
