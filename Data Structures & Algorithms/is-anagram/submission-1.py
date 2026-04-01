class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = dict()

        # Add each char in s to the frequency table
        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        
        # Remove each char in t from the frequency table
        for char in t:
            if char not in freq:
                return False
            else:
                freq[char] -= 1
        
        # Check if any of the values is not 0
        for f in freq.values():
            if f != 0:
                return False
                
        return True

