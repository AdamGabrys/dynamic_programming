# Uses python3
# Compute the length of a longest common subsequence of three sequences.
# ie.
# 5
# 8 3 2 1 7
# 7
# 8 2 1 3 8 10 7
# 6
# 6 8 3 1 5 7
# Output: 3
# longest com seq (8 3 7) or (8 1 7)


import sys


def lcs3(s, t, c):
    d = edit_distance(s, t)
    cs = get_common_string(d, len(s), len(t), s)
    d = edit_distance(cs, c)
    cs = get_common_string(d, len(cs), len(c), cs)
    return len(cs)


def edit_distance(s, t):
    d = [[0 for x in range(len(s)+1)] for x in range(len(t)+1)]
    for i in range(0, len(s)+1):
        d[0][i] = i
    for i in range(len(t)+1):
        d[i][0] = i
    for j in range(1, len(t)+1):
        for i in range(1, len(s)+1):
            insertion = d[j-1][i]+1
            deletion = d[j][i-1]+1
            match = d[j-1][i-1]
            mismatch = d[j-1][i-1]+2
            if s[i-1] == t[j-1]:
                d[j][i] = min(insertion, deletion, match)
            else:
                d[j][i] = min(insertion, deletion, mismatch)
    return d


def get_common_string(d, i, j, s):
    common_string = []
    while i != 0 and j != 0:
        if j > 0 and d[j-1][i]+1 == d[j][i]:
            j -= 1
        if i > 0 and d[j][i-1]+1 == d[j][i]:
            i -= 1
        elif i > 0 and j > 0 and d[j-1][i-1] == d[j][i]:
            common_string.append(s[i-1])
            i -= 1
            j -= 1
        else:
            i -= 1
            j -= 1
    return list(reversed(common_string))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    ans1 = lcs3(a, b, c)
    ans2 = lcs3(c, b, a)
    if ans1 > ans2:
        print(ans1)
    else:
        print(ans2)