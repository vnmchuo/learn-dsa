# Longest Substring Without Repeating Characters
def length_of_longest_substring(s: str) -> int:
    left = 0
    max_len = 0
    seen = {}

    for right in range(len(s)):
        seen[s[right]] = seen.get(s[right], 0) + 1

        while seen[s[right]] > 1:
            seen[s[left]] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)

    return max_len


print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("bbbbb"))
print(length_of_longest_substring("pwwkew"))
