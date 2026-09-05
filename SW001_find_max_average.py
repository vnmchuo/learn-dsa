def find_max_average(nums: list[int], k: int) -> float:
    # 1. Hitung total sum jendela pertama
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # 2. Geser jendela dari indeks k hingga akhir:
    for right in range(k, len(nums)):
        #    - tambah elemen baru (nums[right])
        window_sum += nums[right] - nums[right - k]
        #    - kurangi elemen lama (nums[right - k])
        #    - perbarui max_sum
        max_sum = max(max_sum, window_sum)

    return max_sum / k


nums = [1, 12, -5, -6, 50, 3]
k = 4

print(find_max_average(nums, k))

