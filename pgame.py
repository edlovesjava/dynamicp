# Description: Count the number of paths in a grid of various sizes

# count paths in grid of various sizes using dynamic programming technique of
# breaking down the problem into smaller sub-problems
# and memoization to store results of sub-problems
def count_paths_memo(width, height, memo):
    global turn_count
    print(f' >> count_paths({width}, {height})')
    turn_count += 1
    # memoization
    # compute hash of width, height order independent
    memo_hash = (width, height) if width < height else (height, width)
    if (width, height) in memo:
        print(f' >> memo hit on {memo_hash}: {memo[memo_hash]}')
        return memo[memo_hash]
    if width == 0 or height == 0:
        return 0
    if width == 1 or height == 1:
        return 1
    # recursively break down the problem into smaller sub-problems
    paths = count_paths_memo(width - 1, height, memo) + count_paths_memo(width, height - 1, memo)
    memo[memo_hash] = paths
    return paths

# count paths in grid of various sizes using dynamic programming technique of
# breaking down the problem into smaller sub-problems
def count_paths(width, height):
    global turn_count
    print(f' >> count_paths({width}, {height})')
    turn_count += 1
    if width == 0 or height == 0:
        return 0
    if width == 1 or height == 1:
        return 1
    # recursively break down the problem into smaller sub-problems
    paths = count_paths(width - 1, height) + count_paths(width, height - 1)
    return paths


if __name__ == '__main__':

    turn_count = 0
    memo = {}

    width = 4
    height = 4

    count22 = count_paths_memo(width, height, memo)
    print(f'count_paths_memo of {width}x{height} grid = {count22} in {turn_count} turns')
    print(f'memo = {memo}')

