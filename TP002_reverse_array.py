def reverse_array(nums: list[int]) -> None:
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr)
