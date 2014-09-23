class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if not dict:
            return False
        n = len(s)
        res = [False] * n
        for i in xrange(0, n):
            if s[:i+1] in dict:
                res[i] = True
        if not True in res:
            return False
        i = 0
        while i < n:
            if res[i]:
                i += 1
                continue
            for k in xrange(0, i+1):
                if res[i-k] and s[i-k+1:i+1] in dict:
                    res[i] = True
                    break
            i += 1
        return res[-1]