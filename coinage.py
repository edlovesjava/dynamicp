# compute smallest number of coins to make change for a given amount
# using dynamic programming technique of breaking down the problem into smaller
# sub-problems and memoization to store results of sub-problems


def make_change_memo(amount, coins, memo, current_coins=None):
    if current_coins is None:
        current_coins = []
    global turn_count
    turn_count += 1
    if amount in memo:
        return memo[amount]
    if amount == 0:
        print(f' >> make_change_memo {current_coins} len: {len(current_coins)}')
        return len(current_coins)
    min_coins = float('inf')
    for coin in coins:
        if amount - coin >= 0:
            num_coins = make_change_memo(amount - coin, coins, memo, current_coins + [coin])
            if num_coins < min_coins:
                min_coins = num_coins

    memo[amount] = min_coins
    return memo[amount]



if __name__ == '__main__':
    amount = 63
    coins = [25, 10, 5, 1]
    memo = {}
    turn_count = 0

    print(f'make change for amount {amount} using coins {coins}')
    change = make_change_memo(amount, coins, memo)
    print(change)
    print(f' >> make_change for amount {amount} took {turn_count} turns')
