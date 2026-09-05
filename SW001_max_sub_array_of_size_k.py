def max_sub_array_of_size_k(nums: list[int], k: int) -> int:
    if len(nums) < k or k <= 0:
        return 0
    # 1. Hitung total jumlah untuk jendela pertama (indeks 0 hingga k - 1)
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # 2. Geser jendela dari indeks k sampai ujung array
    for right in range(k, len(nums)):
        # Masukkan elemen baru (nums[right]), buang elemen lama (nums[right - k])
        window_sum += nums[right] - nums[right - k]
        # Catat rekor nilai tertinggi sejauh ini
        max_sum = max(max_sum, window_sum)

    return max_sum


# Uji Coba:
data = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sub_array_of_size_k(data, k))  # Output: 9 (dari [5, 1, 3])