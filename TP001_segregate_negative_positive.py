def segregate_negative_positive(nums: list[int]) -> list[int]:
    slow = 0

    for fast in range(len(nums)):

        if nums[fast] < 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

    return nums


# Test case
data = [4, -3, 2, -1, -5, 0]
print(segregate_negative_positive(data))
