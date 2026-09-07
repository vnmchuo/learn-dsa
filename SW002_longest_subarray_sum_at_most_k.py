def longest_subarray_sum_at_most_k(nums: list[int], k: int) -> int:
    left = 0
    total = 0
    max_len = 0

    for right in range(len(nums)):
        # 1. Tambahkan angka baru ke total
        total += nums[right]

        # 2. Tertibkan jika total melanggar aturan (kapan while harus jalan?)
        while total > k:
            total -= nums[left]
            left += 1

        # 3. Jendela sudah aman! Perbarui max_len
        # Rumus panjang jendela: right - left + 1
        max_len = max(max_len, right - left + 1)

    return max_len


nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8
res = longest_subarray_sum_at_most_k(nums, k)

print(res)