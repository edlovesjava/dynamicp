# simple fibonacci series module for python using memoization

def fib(n, memo=None):
    if memo is None:
        memo = {}
    global turn_count
    turn_count += 1
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


if __name__ == '__main__':
    n = 40
    turn_count = 0
    print(f'fib({n}) = {fib(n)} in {turn_count} turns')