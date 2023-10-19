import heapq


def max_even_sum(numbers: list) -> int:
    s = sum(numbers)
    r = s % 3
    if r == 0:
        return s
    h1, h2 = [], []
    for v in numbers:
        if v % 3 == 1:
            if len(h1) < 2:
                heapq.heappush(h1, -v)
            elif v < -h1[0]:
                heapq.heappop(h1)
                heapq.heappush(h1, -v)
        elif v % 3 == 2:
            if len(h2) < 2:
                heapq.heappush(h2, -v)
            elif v < -h2[0]:
                heapq.heappop(h2)
                heapq.heappush(h2, -v)

    r11 = -heapq.heappop(h1) if h1 else s
    r12 = -heapq.heappop(h1) if h1 else s

    r21 = -heapq.heappop(h2) if h2 else s
    r22 = -heapq.heappop(h2) if h2 else s

    if r == 1:
        return s - min(r12, r11, r21+r22)

    return s - min(r11 + r12, r22, r21)


def solution():
    numbers = [int(x) for x in input().split()]
    result = max_even_sum(numbers)
    print(result)


solution()
