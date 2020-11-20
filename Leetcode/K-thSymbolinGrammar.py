# question: https://leetcode.com/problems/k-th-symbol-in-grammar/submissions/
"""
element of nth row is identical as elements of (n-1)th row upto the mid and after that they are opposite
so if k<=mid print the kth element of (n-1)th row else its opposite value
"""

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N==1 and K==1:
            return 0
        mid = (2**(N-1))//2 
        if K <= mid:
            return int(self.kthGrammar(N-1, K))
        else:
            return int(not self.kthGrammar(N-1, K-mid))
