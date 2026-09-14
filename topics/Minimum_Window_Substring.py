from collections import Counter

def min_window(s, t):
    if not t or not s:
        return ""

    need = Counter(t)
    missing = len(t)   # total characters still needed
    left = 0
    best_left, best_right = 0, float('inf')

    for right, char in enumerate(s, 1):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1

        while missing == 0:   # valid window found, try to shrink it
            if right - left < best_right - best_left:
                best_left, best_right = left, right

            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1   # removing this char breaks validity
            left += 1

    return s[best_left:best_right] if best_right != float('inf') else ""


print(min_window("ADOBECODEBANC", "ABC"))   # "BANC"
