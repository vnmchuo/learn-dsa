def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [nums[left], nums[right]]
        elif current_sum < target:
            # Jumlahnya kekecilan! Butuh angka lebih besar -> geser left ke kanan
            left += 1
        else:
            # Jumlahnya kegedean! Butuh angka lebih kecil -> geser right ke kiri
            right -= 1

    return []


print(two_sum_sorted([2, 7, 11, 15], 9))
print(two_sum_sorted([2, 7, 11, 15], 26))