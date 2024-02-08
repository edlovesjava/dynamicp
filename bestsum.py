# implementation of best sum problem using memoization
def main():
    best_combination = best_sum(7, [2, 3, 4])
    print(best_combination)

    best_combination1 = best_sum(13, [2, 3, 4])
    print(best_combination1)

    best_combination2 = best_sum(8, [2, 3])
    print(best_combination2)

    best_combination3 = best_sum(100, [1, 2, 5, 25])
    print(best_combination3)


def best_sum(value, numbers, memo=None):
    if memo is None:
        memo = {}
    if value in memo:
        return memo[value]
    if value == 0:
        return []
    if value < 0:
        return None
    shortest_combination = None
    for num in numbers:
        remainder = value - num
        if remainder >= 0:
            remainder_combination = best_sum(remainder, numbers, memo)
            if remainder_combination != None:
                combination = remainder_combination + [num]
                if shortest_combination == None or len(combination) < len(shortest_combination):
                    shortest_combination = combination

    memo[value] = shortest_combination
    return memo[value]


if __name__ == '__main__':
    main()
