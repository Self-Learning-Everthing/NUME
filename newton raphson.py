def f(x):
    y = (x * x * x) - (2 * x * x) + x - 3
    return y

def df(x):
    y = (3 * x * x) - (4 * x) + 1
    return y

a = float(input('enter the initial guess: '))
e_limit = float(input('enter the acceptance error: '))
n_limit = int(input('enter the max number of iteration: '))

if f(a) == 0:
    print('{} is a root'.format(a))
    exit()

n = 0
error = 1000
old_root = a
error_old = 1000
counter = 0

while n < n_limit and error > e_limit:
    n = n + 1

    if df(old_root) == 0:
        print('df=0, we have a problem')
        exit()

    root = old_root - (f(old_root) / df(old_root))

    print('new approximation:', root)
    print('the function at the new root:', f(root))

    error = abs(root - old_root)
    old_root = root

    if error > error_old:
        counter = counter + 1
        if counter == 3:
            print('the system is diverging')
            exit()
    else:
        counter = 0

    error_old = error

print('the root is {}, number of iterations: {}, error: {}'.format(root, n, error))
