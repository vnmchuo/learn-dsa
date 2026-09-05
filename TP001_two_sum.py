def two_sum(nums: list[int], target: int) -> list[int]:
    # Simpan nilai yang sudah dilihat beserta indeksnya
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


print(two_sum([1, 2, 3, 4, 5], 9))
