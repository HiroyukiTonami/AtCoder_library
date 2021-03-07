class Solution:
    def maxProduct(self, words: List[str]) -> int:
        score = 0
        for i, A in enumerate(words):
            for B in words[i+1:]:
                shared = len(set(A).intersection(B))
                if shared == 0:
                    score = max(score, len(A) * len(B))

        return score
