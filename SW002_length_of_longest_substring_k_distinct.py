def length_of_longest_substring_k_distinct(s: str, k: int) -> int:

    if k == 0 and not s:
        return 0

    left = 0
    max_len = 0
    seen = {}

    for right in range(len(s)):
        seen[s[right]] = seen.get(s[right], 0) + 1

        while len(seen) > k:
            seen[s[left]] -= 1
            if seen[s[left]] == 0:
                del seen[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)

    return max_len


print(length_of_longest_substring_k_distinct("eceba", 2))  # 3
print(length_of_longest_substring_k_distinct("aa", 1))  # 2
print(length_of_longest_substring_k_distinct("aabacbebebe", 3))  # 7
