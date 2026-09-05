def remove_duplicates_ii(nums: list[int]) -> int:
    # Jika panjang array <= 2, semua angka pasti valid
    if len(nums) <= 2:
        return len(nums)

    # Indeks 0 dan 1 sudah pasti aman, mulai isi dari indeks 2
    slow = 2

    for fast in range(2, len(nums)):
        # Kapan angka di fast boleh ditulis ke slow?
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1

    return slow


nums1 = [1, 1, 1, 2, 2, 3]
nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(remove_duplicates_ii(nums1))
print(remove_duplicates_ii(nums2))
