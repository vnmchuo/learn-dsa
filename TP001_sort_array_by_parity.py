def sort_array_by_parity(nums: list[int]) -> list[int]:
    slow = 0

    for fast in range(len(nums)):
        # Angka mana yang mau dikumpulkan di depan?
        # Trik: angka genap dicek dengan `nums[fast] % 2 == 0`
        if nums[fast] % 2 == 0:
            # Gunakan swap/tukar seperti di Move Zeroes
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

    return nums


nums = [3, 1, 2, 4]

print(sort_array_by_parity(nums))
