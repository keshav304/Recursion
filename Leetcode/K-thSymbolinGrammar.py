question: https://leetcode.com/problems/k-th-symbol-in-grammar/submissions/

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N==1 and K==1:
            return 0
        mid = (2**(N-1))//2 
        if K <= mid:
            return int(self.kthGrammar(N-1, K))
        else:
            return int(not self.kthGrammar(N-1, K-mid))
