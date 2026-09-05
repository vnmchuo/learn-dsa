def remove_negative_odds(nums: list[int]) -> int:
    slow = 0

    for fast in range(len(nums)):
        # Kriteria lolos: BUKAN (negatif dan ganjil)
        # Atau: lolos jika nilainya >= 0 ATAU nilainya genap
        if not (nums[fast] % 2 != 0 and nums[fast] < 0):
            nums[slow] = nums[fast]
            slow += 1

    return slow


nums = [2, -3, 4, -1, -2, 0, -5, 6]
print(remove_negative_odds(nums))
