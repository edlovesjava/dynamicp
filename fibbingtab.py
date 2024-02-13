# simple fibonacci series module for python using tabulation (bottom up)

def main():
    n = 40
    print(f'fib({n}) = {fib(n)}')


def fib(n, tab=None):
    if tab is None:
        tab = {}
    for (i, v) in enumerate(range(0, n + 1)):
        if v <= 2:
            tab[v] = 1
        else:
            tab[v] = tab[v - 1] + tab[v - 2]
    return tab[n]


if __name__ == '__main__':
    main()