test = '1234'


def aux(s, r, curr):
    if len(s) == 0:
        r.append(curr)

    for i in range(len(s)):
        aux(s[:i] + s[i+1:], r, curr + [s[i]])


def permutations(s):
    if not s:
        return []

    ans = []
    aux(s, ans, [])
    return ans


print(permutations(test))
print(len(permutations(test)))
