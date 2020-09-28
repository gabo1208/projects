from collections import Counter, defaultdict
import heapq


def leastInterval(tasks, n):
    ts = [f for k, f in Counter(tasks).items()]
    heapq.heapify(ts)
    t = 0
    while ts:
        rec = []
        for i in range(n + 1):
            if ts:
                rec.append(heapq.heappop(ts))
            else:
                break

        for r in rec:
            r -= 1
            if r > 0:
                heapq.heappush(ts, r)

        t += n + 1 if ts else len(rec)
    return t


print(leastInterval(["A", "A", "A", "A", "A",
                     "A", "B", "C", "D", "E", "F", "G"], 2))
