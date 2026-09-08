def length_of_longest_substring_optimized(s: str) -> int:
    left = 0
    max_len = 0
    last_seen = {}  # Menyimpan: karakter -> indeks terakhirnya

    for right in range(len(s)):
        char = s[right]

        # Jika karakter sudah pernah muncul di dalam jendela aktif saat ini
        if char in last_seen:
            left = max(left, last_seen[char] + 1)

        # Perbarui posisi terakhir karakter ini
        last_seen[char] = right

        # Catat rekor panjang
        max_len = max(max_len, right - left + 1)

    return max_len
