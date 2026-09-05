def valid_palindrome_ii(s: str) -> bool:
    # Fungsi pembantu untuk cek apakah suatu rentang indeks adalah palindrom murni
    def is_palindrome_range(left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left = 0
    right = len(s) - 1

    while left < right:
        # Jika menemukan perbedaan karakter:
        if s[left] != s[right]:
            # Coba dua opsi:
            # 1. Hapus s[left]  -> cek sisa rentang (left + 1, right)
            # 2. Hapus s[right] -> cek sisa rentang (left, right - 1)
            return is_palindrome_range(left + 1, right) or is_palindrome_range(
                left, right - 1
            )

        left += 1
        right -= 1

    # Jika loop selesai tanpa pernah ada karakter berbeda
    return True


# Uji Coba:
print(valid_palindrome_ii("aba"))  # True
print(valid_palindrome_ii("abca"))  # True (hapus 'b' atau 'c')
print(valid_palindrome_ii("raceacar"))  # True (hapus 'e')
print(valid_palindrome_ii("abc"))  # False