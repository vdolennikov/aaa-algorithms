def max_div3_sum(numbers: list) -> int:
    divmod1 = [i for i in numbers if i % 3 == 1]
    divmod2 = [i for i in numbers if i % 3 == 2]
    result = sum(numbers)

    def min2elem(array):
        e1 = float('+inf')
        e2 = float('+inf')

        for elem in array:
            if elem < e1:
                e2, e1 = e1, elem
            elif elem < e2:
                e2 = elem

        return e1, e2

    if result % 3 == 0:
        return result

    elif result % 3 == 1:
        if divmod1 and len(divmod2) >= 2:
            return result - min(min(divmod1), sum(min2elem(divmod2)))
        elif divmod1:
            return result - min(divmod1)
        elif len(divmod2) >= 2:
            return result - sum(min2elem(divmod2))

    elif result % 3 == 2:
        if divmod2 and len(divmod1) >= 2:
            return result - min(min(divmod2), sum(min2elem(divmod1)))
        elif divmod2:
            return result - min(divmod2)
        elif len(divmod1) >= 2:
            return result - sum(min2elem(divmod1))


def solution():
    numbers = [int(x) for x in input().split()]
    result = max_div3_sum(numbers)
    print(result)


solution()
