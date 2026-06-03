s = input().strip()

n = len(s)

for mask in range(1, 1 << n):
    combi = ""

    for i in range(n):
        if mask & (1 << i):
            combi += s[i]

    print(combi)