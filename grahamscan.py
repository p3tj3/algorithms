# based on https://iq.opengenus.org/graham-scan-convex-hull/ by Pankaj Sharma


def partition(array, start, end):
    pivot = array[start]
    low, high = start + 1, end

    while low <= high:

        while low <= high and compare(array[high], pivot) == 1:
            high -= 1

        while low <= high and compare(array[low], pivot) == -1:
            low += 1

        if low <= high:
            array[low], array[high] = array[high], array[low]

    array[start], array[high] = array[high], array[start]
    return high


def quicksort(array, start, end):
    if start >= end: return

    p = partition(array, start, end)
    quicksort(array, start, p - 1)
    quicksort(array, p + 1, end)


def distsq(p1, p2):
    return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])


def orientation(p, q, r):
    v = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if v == 0: return 0
    return 1 if v > 0 else 2


def compare(p1, p2):
    o = orientation(p0, p1, p2)
    if o == 0: return -1 if distsq(p0, p2) >= distsq(p0, p1) else 1
    return -1 if o == 2 else 1


def convexhull(points, n):
    ymin, mini = points[0][1], 0
    for i in range(n):
        y = points[i][1]
        if y < ymin or ymin == y and points[i][0] < points[mini][0]:
            ymin, mini = points[i][1], i
    points[0], points[mini] = points[mini], points[0]

    global p0
    p0 = points[0]

    quicksort(points, 1, n - 1)

    m = 1
    for i in range(1, n - 1):
        if orientation(p0, points[i], points[i + 1]) == 0:
            continue
        points[m] = points[i]
        m += 1
    points = points[0:m] + [points[-1]]

    if m < 3:
        return []

    S = points[0:3]
    for i in range(3, m + 1):
        while orientation(S[-2], S[-1], points[i]) != 2:
            S.pop()
        S.append(points[i])

    return S