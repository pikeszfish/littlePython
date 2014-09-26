class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        a = A[0]
        b = A[0]
        c = A[0]
        result = A[0]
        for j in xrange(1, len(A)):
            i = A[j]
            a *= i
            b *= i
            c = i
            a, b = max(max(a, b), c), min(min(a, b), c)
            if result < a:
                result = a
            print str(a) + " " + str(b) + " " + str(c)
        return result
# hey = Solution()
# a = [-1,-2,-9,-6]
# print hey.maxProduct(a)