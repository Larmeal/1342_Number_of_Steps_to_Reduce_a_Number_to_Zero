class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        
        while not num <= 0:
            if num % 2 == 0:
                count += 1
                num = num / 2
                
            elif num % 2 == 1:
                count += 1
                num = num - 1
                
        return count
            