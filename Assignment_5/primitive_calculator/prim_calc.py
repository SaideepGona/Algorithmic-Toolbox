d = {}

def f(n):
    if n == 1:
        return 1, -1
    if d.get(n) is not None:
        return d[n]
    ans = (f(n - 1)[0] + 1, n - 1)

    if n % 2 == 0:
        ret = f(n // 2)
        if ans[0] > ret[0]:
            ans = (ret[0] + 1, n // 2)

    if n % 3 == 0:
        ret = f(n // 3)
        if ans[0] > ret[0]:
            ans = (ret[0] + 1, n // 3)

    d[n] = ans
    return ans


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(f(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
