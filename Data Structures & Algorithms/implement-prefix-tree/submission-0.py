class PrefixTree:

    def __init__(self):
        self.wordBank = {}
        
    def insert(self, word: str) -> None:
        if word not in self.wordBank:
            self.wordBank[word] = 1

    def search(self, word: str) -> bool:
        if word in self.wordBank:
            return True

        return False        

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)

        for word in self.wordBank:
            if word[:n] == prefix:
                return True

        return False
        