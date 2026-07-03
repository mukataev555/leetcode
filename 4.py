arr = input() 
arr_2 = arr.replace('[', '').replace(']', '').split(',')
nums = list(map(int, arr_2))
     
nums.sort()

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        for i in nums:
            if i > 0 and -i in nums:
                return i
        return -1


s4 = Solution()
result = s4.findMaxK(nums)




        






