n = int(input('enter the number of variables'))
a = [[0 for j in range(n)] for i in range(n)]
b = [0 for j in range(n)]
sol = [0 for j in range(n)]

for i in a:
    print(i)

for i in b:
    print(i)

for i in range(n):
    for j in range(n):
        a[i][j] = float(input('enetr the cof of a{} in eq{}'.format(j, i)))
    b[i] = float(input('enter the b{} in eq{}'.format(i, i)))

for i in a:
        print(i)
for i in b:
    print(i)

for k in range(n - 1):
    for i in range(k + 1, n):
        for j in range(n):
            coef = a[i][k] / a[k][k]

        for j in range(n):
            a[i][j] = a[i][j] - coef * a[k][j]

        b[i] = b[i] - coef * b[k]

sol[n - 1] = b[n - 1] / a[n - 1][n - 1]

for r in range(n - 2, -1, -1):
    sum1 = 0

    for j in range(r + 1, n):
        sum1 = sum1 + a[r][j] * sol[j]

    sol[r] = (b[r] - sum1) / a[r][r]

for i in range(n):
    print('sol{}={}'.format(i, sol[i]))
