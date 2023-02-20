def subarray_sum(nums, k):
    count = 0
    sum = 0
    map = {}
    for num in nums:
        sum += num
        if sum == k: count += 1
        count += map.get(sum - k, 0)
        map[sum] = map.get(sum, 0) + 1
    return count

cases = [
    ([1,1,1], 2),
    ([1,2,3,4,-1,-2], 3)
]
for nums, k in cases:
    print(nums, subarray_sum(nums, k))
