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

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return False
        if not cur.is_end:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return False
        return True
