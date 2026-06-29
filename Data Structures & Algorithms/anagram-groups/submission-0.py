class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        if len(strs) == 0:
            return [[""]]
        elif len(strs) == 1:
            return [strs]
        
        for i in strs:
            sort_str = "".join(sorted(i))
            if sort_str not in dct:
                dct[sort_str] = [i]
            else:
                dct[sort_str].append(i)

        res = []
        for k,v in dct.items():
            res.append(v)
        return res