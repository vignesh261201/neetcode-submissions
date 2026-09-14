class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for string in strs:
            joined_string= "".join(sorted(string))

            if joined_string in seen:
                seen[joined_string].append(string)
            else:
                seen[joined_string] = [string]
        
        return list(seen.values())