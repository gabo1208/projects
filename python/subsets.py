test = [3, 6, 5, 1]


def subsets(s):
    if not s:
        return [[]]

    h, t = s[0], s[1:]
    excl = subsets(t)
    incl = [[h] + ss for ss in excl]
    return excl + incl


def aux(s, res, cur):
    res.append(cur)
    for i in range(len(s)):
        aux(s[i+1:], res, cur + [s[i]])


def subsetsIno(s):
    if len(s) == 0:
        return [[]]

    ans = []
    aux(s, ans, [])
    return ans


def auxGreater(s, res, cur, k):
    res.append(cur)
    for i in range(len(s)):
        if s[i] >= k:
            auxGreater(s[i+1:], res, cur + [s[i]], k)


def subsetsGreater(s, k):
    if len(s) == 0:
        return [[]]

    ans = []
    auxGreater(s, ans, [], k)
    return ans


print(subsetsIno(test))
print(subsetsGreater(test, 3))
# print(subsetsIno(test))
