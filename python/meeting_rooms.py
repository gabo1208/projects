from heapq import heapify, heappop, heappush

test = [[0, 30], [20, 50], [30, 50]]


def meetingRoomsII(arr):
    if not arr:
        return 0

    arr.sort(key=lambda x: x[1])
    rooms = [arr[0][1]]
    heapify(rooms)
    for i in range(1, len(arr)):
        tried = []
        found = False
        while rooms and not found:
            tried.append(heappop(rooms))
            if tried[-1] <= arr[i][0]:
                found = True
                tried[-1] = arr[i][1]

        if found:
            for endTime in tried:
                heappush(rooms, endTime)
        else:
            rooms = tried
            rooms.append(arr[i][0])
            heapify(rooms)

    return len(rooms)


print(meetingRoomsII(test))
