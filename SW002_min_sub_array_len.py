def min_sub_array_len(target: int, nums: list[int]) -> int:
    left = 0
    window_sum = 0
    min_len = float('inf')  # Inisialisasi dengan tak hingga untuk mencari minimum

    for right in range(len(nums)):
        # 1. Expand: Masukkan elemen baru ke jendela
        window_sum += nums[right]

        # 2. Shrink: Selama target terpenuhi, perbarui rekor dan ciutkan dari kiri
        while window_sum >= target:
            min_len = min(min_len, right - left + 1)
            window_sum -= nums[left]
            left += 1

    # Jika min_len tidak pernah berubah, artinya tidak ada kombinasi yang valid
    return min_len if min_len != float('inf') else 0


# Uji Coba:
target = 7
nums = [2, 3, 1, 2, 4, 3]
print(min_sub_array_len(target, nums))  # Output: 2 (dari subarray [4, 3])