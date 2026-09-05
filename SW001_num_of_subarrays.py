def num_of_subarrays(arr: list[int], k: int, threshold: int) -> int:
    target_sum = threshold * k
    count = 0

    # 1. Hitung window_sum awal (arr[:k])
    window_sum = sum(arr[:k])
    #    Cek apakah jendela pertama memenuhi target_sum?
    if window_sum >= target_sum:
        count += 1

    # 2. Geser jendela dari indeks k hingga len(arr):
    for right in range(k, len(arr)):
        #    - Update window_sum (masuk arr[right], keluar arr[right - k])
        window_sum += arr[right] - arr[right - k]
        #    - Cek apakah memenuhi target_sum? Jika ya, count += 1
        if window_sum >= target_sum:
            count += 1

    return count


arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4

print(num_of_subarrays(arr, k, threshold))
