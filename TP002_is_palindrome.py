def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        # 1. Bandingkan karakter di ujung kiri dan kanan
        # 2. Jika ada yang beda, langsung kembalikan apa?
        if s[left] != s[right]:
            return False

        # 3. Jika sama, geser kedua pointer ke mana?
        else:
            left += 1
            right -= 1

    # Jika loop selesai tanpa masalah, berarti palindrom!
    return True


print(is_palindrome("katak"))
print(is_palindrome("kopol"))
print(is_palindrome("kasurrusak"))
print(is_palindrome("mobil"))
