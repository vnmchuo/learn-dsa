def total_fruit(nums: list[int]) -> int:
    left = 0
    max_len = 0
    seen = {}

    for right in range(len(nums)):
        seen[nums[right]] = seen.get(nums[right], 0) + 1

        while len(seen) > 2:
            seen[nums[left]] -= 1
            if seen[nums[left]] == 0:
                del seen[nums[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


nums1 = [1, 2, 1, 2, 3]
nums2 = [0, 1, 2, 2, 2, 2]
nums3 = [1, 2, 3, 2, 2]

print(total_fruit(nums1))
print(total_fruit(nums2))
print(total_fruit(nums3))
