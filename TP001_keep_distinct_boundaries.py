def keep_distinct_boundaries(nums: list[int]) -> int:
    if not nums:
        return 0

    slow = 0

    # Pikirkan loop for untuk fast:
    for fast in range(len(nums)):
        if fast == len(nums) - 1 or nums[fast] != nums[fast + 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow
    # Bagaimana cara membandingkan elemen fast dengan tetangga kanannya?
    # Jangan lupa elemen paling ujung!


nums = [1, 1, 2, 3, 3, 4]
print(keep_distinct_boundaries(nums))
