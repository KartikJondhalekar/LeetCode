# Problem #211: Design Add and Search Words Data Structure
# Difficulty : Medium
# Language   : python3
# Runtime    : 859 ms
# Memory     : 68.4 MB
# URL        : https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        curr.endOfWord = True     

    def search(self, word: str) -> bool:

        def dfs(i, node):
            if i == len(word):
                return node.endOfWord

            c = word[i]

            if c == '.':
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True

                return False
            else:
                if c not in node.children:
                    return False

                return dfs(i + 1, node.children[c])

        return dfs(0, self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)