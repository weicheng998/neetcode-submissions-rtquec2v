from collections import deque

class TrieNode:
    def __init__(self, is_end=False, children=None) -> None:
        self.is_end: bool = is_end
        self.children: dict = children if children is not None else {}


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
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
        candidates = deque([self.root])
        for char in word:
            if char == '.':
                size = len(candidates)
                if size == 0:
                    return False
                for _ in range(size):
                    node = candidates.popleft()
                    for child in node.children.values():
                        candidates.append(child)
            else:  # char != '.'
                size = len(candidates)
                if size == 0:
                    return False
                found = False
                for _ in range(size):
                    node = candidates.popleft()
                    if char in node.children:
                        candidates.append(node.children[char])
                        found = True
                if not found:
                    return False
        for candidate in candidates:
            if candidate.is_end:
                return True
        return False

