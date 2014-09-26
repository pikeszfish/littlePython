class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        i = 0
        n = len(s)
        while i < n-1:
            j = i + 1
            while j < n:
                if s[i:j] in dict:
                    