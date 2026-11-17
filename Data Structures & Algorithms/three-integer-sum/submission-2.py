class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i,a in enumerate(nums):
            if a>0: #first number greater than 0 after sorting means no valid triplet
                break
            if i > 0 and a == nums[i-1]: 
                continue #increment if value same as last one
            l,r = i+1 , len(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r: #updating one pointer updates the other one too in while loop
                        l += 1
        return res