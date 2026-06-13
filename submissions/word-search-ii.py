# Problem #212: Word Search II
# Difficulty : Hard
# Language   : python3
# Runtime    : 503 ms
# Memory     : 20.9 MB
# URL        : https://leetcode.com/problems/word-search-ii/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie
        root = TrieNode()

        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word

        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, parent):
            char = board[r][c]

            if char not in parent.children:
                return

            node = parent.children[char]

            # Found a word
            if node.word:
                res.append(node.word)
                node.word = None  # avoid duplicates

            # Mark as visited
            board[r][c] = "#"

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and board[nr][nc] != "#"
                ):
                    dfs(nr, nc, node)

            # Restore cell
            board[r][c] = char

            # Trie pruning
            if not node.children and node.word is None:
                del parent.children[char]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return res