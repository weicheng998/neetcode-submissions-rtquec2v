class TrieNode:
    def __init__(self, is_end=False, children=None) -> None:
        self.is_end: bool = is_end
        self.children: dict = children if children is not None else {}


class PrefixTree:
    def __init__(self):
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                node = TrieNode()
                cur.children[char] = node
                cur = node
        cur.is_end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build the trie with all the words to find
        trie = PrefixTree()
        for word in words:
            trie.insert(word)

        ROWS, COLS = len(board), len(board[0])
        found = set()
        visited = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        def helper(node: TrieNode, row: int, col: int, word: str):
            if not 0 <= row < ROWS or not 0 <= col < COLS:
                return
            if visited[row][col] == 1:
                return
            if board[row][col] not in node.children.keys():
                return

            visited[row][col] = 1
            char = board[row][col]
            word += char

            if node.children[char].is_end:
                found.add(word)

            DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right
            for dx, dy in DIRECTIONS:
                helper(node.children[char], row + dx, col + dy, word)

            visited[row][col] = 0

        for row in range(ROWS):
            for col in range(COLS):
                helper(trie.root, row, col, "")

        return list(found)
