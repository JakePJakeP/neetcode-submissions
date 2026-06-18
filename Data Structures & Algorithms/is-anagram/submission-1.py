class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = dict()
        tdict = dict()
        for schar in s:
            if schar not in sdict:
                sdict[schar] = 1
            else:
                sdict[schar] += 1
        for tchar in t:
            if tchar not in tdict:
                tdict[tchar] = 1
            else:
                tdict[tchar] += 1
        for key in sdict:
            if len(sdict) != len(tdict) or key not in tdict or sdict[key] != tdict[key]:
                return False
        return True