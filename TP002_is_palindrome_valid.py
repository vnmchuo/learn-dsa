def is_palindrome_valid(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        # 1. Jika karakter kiri bukan huruf/angka, lewati (geser ke kanan)
        if not s[left].isalnum():
            left += 1
        # 2. Jika karakter kanan bukan huruf/angka, lewati (geser ke kiri)
        elif not s[right].isalnum():
            right -= 1
        # 3. Keduanya sudah berupa huruf/angka, bandingkan (abaikan huruf besar/kecil)
        else:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

    return True


# Uji Coba:
print(is_palindrome_valid("A man, a plan, a canal: Panama"))  # True
print(is_palindrome_valid("race a car"))  # False
print(is_palindrome_valid("Kasur ini, rusak!"))  # True