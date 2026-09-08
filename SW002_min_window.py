from collections import Counter


def min_window(s: str, t: str) -> str:
    if not s or not t or len(s) < len(t):
        return ""

    # 1. Catat target kebutuhan dari t
    target = Counter(t)
    required = len(target)  # Banyaknya karakter unik yang harus terpenuhi

    # 2. State untuk jendela aktif s
    window = {}
    formed = 0  # Berapa karakter unik yang syarat jumlahnya sudah beres

    # Menyimpan: (panjang_minimum, indeks_left, indeks_right)
    ans = (float("inf"), None, None)
    left = 0

    # 3. EXPAND: right maju menelan karakter
    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1

        # Jika karakter ini ada di target DAN jumlahnya pas memenuhi syarat
        if char in target and window[char] == target[char]:
            formed += 1

        # 4. SHRINK: Selama jendela VALID, ciutkan dari kiri untuk mencari yang terpendek
        while formed == required:
            # Perbarui rekor substring terpendek
            if (right - left + 1) < ans[0]:
                ans = (right - left + 1, left, right)

            # Buang karakter paling kiri
            char_left = s[left]
            window[char_left] -= 1

            # Jika karakter yang dibuang membuat syarat target jadi kurang
            if char_left in target and window[char_left] < target[char_left]:
                formed -= 1

            left += 1

    # Kembalikan substring jika ketemu, atau string kosong jika tidak ada
    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]