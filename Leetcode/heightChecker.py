class Solution:
    def heightChecker(self, heights):
        expected=sorted(heights)
        indicesNotMatched=0
        for i in range (len(heights)):
            if expected[i]!=heights[i]:
                indicesNotMatched+=1
        return indicesNotMatched
        
