class Solution:
    def get_fingerprint(self, s: str) -> tuple:
        fingerprint = [0] * 26
        for char in s:
            index = ord(char) - ord('a')
            fingerprint[index] += 1
        return tuple(fingerprint)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = dict()
        for s in strs:
            fingerprint = self.get_fingerprint(s)
            if fingerprint in results:
                results[fingerprint].append(s)
            else:
                results[fingerprint] = [s]
        return list(results.values())
