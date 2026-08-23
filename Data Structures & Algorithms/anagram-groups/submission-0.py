class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for st in strs:
            temp_str = ''.join(sorted(st))
            if temp_str not in grouped:
                grouped[temp_str] = [st]
            else:
                grouped[temp_str].append(st)
        return list(grouped.values())
