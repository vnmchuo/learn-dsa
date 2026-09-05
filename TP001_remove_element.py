def remove_element(nums: list[int], val: int) -> int:
    # 1. Tentukan pointer slow mulai dari mana
    slow = 0
    # 2. Gunakan for-loop untuk fast menjelajahi nums
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]  # slow yang harus ditimpa fast
            slow += 1
    # 3. Kapan slow harus menulis/menyimpan nilai?
    # 4. Return apa di akhir?
    return slow


nums1 = [3, 2, 2, 3]
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val1 = 3
val2 = 2

print(remove_element(nums1, val1))
print(remove_element(nums2, val2))
