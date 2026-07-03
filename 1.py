arr = input() 
arr_2 = arr.replace('[', '').replace(']', '').split(',')
nums = list(map(int, arr_2))
target = int(input())


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return [j, i]

s1 = Solution()
res = s1.twoSum(nums, target)
print (res)


