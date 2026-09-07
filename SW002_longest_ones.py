def longest_ones(nums: list[int], k: int) -> int:
    left = 0
    max_len = 0
    zero_count = 0

    for right in range(len(nums)):
        # 1. EXPAND: Jendela melebar ke kanan
        if nums[right] == 0:
            zero_count += 1

        # 2. SHRINK: Jika kuota angka 0 jebol (> k), ciutkan jendela dari kiri
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1  # Ambil kembali kuota karena 0 ini ditinggal
            left += 1  # Geser ekor jendela ke kanan

        # 3. RECORD: Di titik ini, jendela dijamin VALID (zero_count <= k)
        # Hitung panjang jendela: right - left + 1
        max_len = max(max_len, right - left + 1)

    return max_len
