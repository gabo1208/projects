from collections import defaultdict, Counter
import heapq


def findCheapestPrice(n, flights, src, dst, K):
    g = defaultdict(list)
    visited = defaultdict(bool)
    stps = defaultdict(int)

    for f in flights:
        g[f[0]].append((f[1], f[2]))

    visited[src] = True
    pq = [(0, 0, src)]
    heapq.heapify(pq)
    while pq:
        cost, stops, current = heapq.heappop(pq)
        if current == dst:
            return cost

        visited[current] = True
        stps[current] = stops

        if stops <= K:
            stops += 1
            for node, c in g[current]:
                if not visited[node] or stops < stps[node]:
                    heapq.heappush(pq, (cost + c, stops, node))

    return -1


def leastInterval(tasks, n):
    freq = Counter(tasks)
    counter = len(freq)
    pr = defaultdict(int)
    ts = [(-freq[t], t) for t in freq]
    heapq.heapify(ts)
    t = 0
    while counter > 0:
        rec = []
        auxF, auxT = 0, ''
        while True and ts:
            auxF, auxT = heapq.heappop(ts)
            if pr[auxT] <= 0:
                break
            else:
                rec.append((auxF, auxT))
                auxF, auxT = 0, ''

        if auxT:
            freq[auxT] -= 1
            pr[auxT] = n + 1
            if freq[auxT] > 0:
                heapq.heappush(ts, (-freq[auxT], auxT))
            else:
                counter -= 1

        for r in rec:
            heapq.heappush(ts, r)

        for e in ts:
            pr[e[1]] -= 1

        print(freq)
        print(pr)
        t += 1
    return t


class Test:
    res = []

    def subsets(self, s, curr):
        self.res.append(curr)
        for i in range(len(s)):
            self.subsets(s[i+1:], curr + [s[i]])

    def permutations(self, s, curr):
        if not s:
            self.res.append(curr)

        for i in range(len(s)):
            self.permutations(s[:i] + s[i+1:], curr + [s[i]])


def repeated3Tiimes(arr):
    one = 0
    two = 0

    for n in arr:
        print(n)
        one = (one ^ n) & (~two)
        print(bin(one))
        two = (two ^ n) & (~one)
        print(bin(two))

    return one


# productLessSelf
# print(findCheapestPrice(11, [[0, 3, 3], [3, 4, 3], [4, 1, 3], [0, 5, 1], [5, 1, 100], [0, 6, 2], [
#     6, 1, 100], [0, 7, 1], [7, 8, 1], [8, 9, 1], [9, 1, 1], [1, 10, 1], [10, 2, 1], [1, 2, 100]], 0, 2, 4))
print(leastInterval(["A", "A", "A", "A", "A",
                     "A", "B", "C", "D", "E", "F", "G"], 2))
x = Test()
y = []
x.permutations('abc', y)
print(x.res)
x.res = []
x.subsets('abc', y)
print(x.res)
print(repeated3Tiimes([3, 7, 3, 7, 3, 7, 4]))
