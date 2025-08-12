class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        res = []

        for s in spells:
            l,r = 0,len(potions) - 1
            idx = len(potions) #furthest left so that we know how many elements are to right of it satisfying the condition

            while l <= r:
                m = (l + r) // 2
                if s * potions[m] >= success:
                    r = m - 1
                    idx = m
                else:
                    l = m + 1

            res.append(len(potions) - idx) #incase no success then it will be: len(potions) - len(potions) since idx wont be updated

        return res

        
