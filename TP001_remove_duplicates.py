def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1  # Geser slot unik ke kanan
            nums[slow] = nums[fast]  # Isi slot tersebut dengan nilai baru

    return slow + 1  # Banyaknya elemen unik (indeks terakhir + 1)


# Contoh dengan array terurut:
arr = [1, 1, 2, 2, 3, 4, 4]
k = remove_duplicates(arr)
print("Jumlah unik:", k)  # Output: 4
print("Isi array:", arr[:k])  # Output: [1, 2, 3, 4]
