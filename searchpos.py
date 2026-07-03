arr = input()
arr_2 = arr.replace('[', '').replace(']', '').split(',')
nums = list(map(int, arr_2))
target = int(input())

n = len(nums)

for i in range(n):
    if target == nums[i]:
        return i

if target not in nums:
    nums.append(target)
    nums.sort()

    for i in range(n + 1):
        if nums[i] == target:
            return i


