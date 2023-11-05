def max_even_sum(numbers: list) -> int:
    odd = [i for i in numbers if i % 2 == 1]
    result = sum(numbers)

    if result % 2 != 0 and odd:
        return result - min(odd)
    else:
        return result


def solution() -> int:
    numbers = [int(x) for x in input().split()]
    result = max_even_sum(numbers)
    print(result)


solution()
