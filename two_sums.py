class Solution:
    def twoSum(self, nums, target) :
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            print(i,n)
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
    
nums = [2,3,4,5,6]
target = 7
sol = Solution()
print(sol.twoSum(nums,target))
        