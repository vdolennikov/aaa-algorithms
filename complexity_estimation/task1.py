def max_even_sum(numbers: list) -> int:
    result = 0
    even_nums = []
    for num in numbers:
        if num % 2 == 0:
            result += num
        else:
            even_nums.append(num)

    result += sum(sorted(even_nums,
                         reverse=True)[:(len(even_nums) // 2 * 2)])

    return result


def solution():
    numbers = [int(x) for x in input().split()]
    result = max_even_sum(numbers)
    print(result)


solution()
