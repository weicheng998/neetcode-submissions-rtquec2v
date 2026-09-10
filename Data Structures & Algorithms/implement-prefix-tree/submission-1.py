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
        res, cur = self._traversalHelper(word)
        return res and cur.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._traversalHelper(prefix)[0]

    def _traversalHelper(self, word: str) -> tuple[bool, TrieNode]:
        cur = self.root
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return (False, cur)
        return (True, cur)
