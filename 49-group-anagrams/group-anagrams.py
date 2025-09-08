class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to hold groups of anagrams
        res = defaultdict(list)

        for s in strs:
            # Frequency array of size 26 for each lowercase letter
            freq_list = [0] * 26

            # Count frequency of each character
            for char in s:
                freq_list[ord(char) - ord('a')] += 1
            
            # Use the frequency tuple as the key
            res[tuple(freq_list)].append(s)
        
        # Return all grouped anagrams
        return list(res.values())