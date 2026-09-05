def max_vowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # 1. Hitung jumlah vokal di jendela pertama (s[:k])
    window_sum = 0
    for i in range(k):
        print(f'Iter - {i}')
        if s[i] in vowels:
            window_sum += 1
    print(f'init_count: {window_sum}')
    max_sum = window_sum
    # 2. Geser jendela dari indeks k hingga len(s)
    for right in range(k, len(s)):
        #    - tambah 1 jika huruf baru ada di vowels
        if s[right] in vowels:
            window_sum += 1
        #    - kurang 1 jika huruf keluar ada di vowels
        if s[right - k] in vowels:
            window_sum -= 1
        #    - perbarui max_count
        print(f'Iter - {right}, Window Sum: {window_sum}')

        max_sum = max(max_sum, window_sum)

    # 3. Return max_count
    return max_sum


s = "abciidef"
k = 3
max_vow = max_vowels(s, k)
print(max_vow)
