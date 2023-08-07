
def f(x):

    y = x * x - 4 * x + 2 
    return y

a = float(input('Enter the lower interval'))
b = float(input('Enter the upper interval'))
e_limit = float(input('enter the acceptance error'))
n_limit = int(input('enter the max iteration'))
print(f'{a}, {f(a)}')
print(f'{b}, {f(b)}')

while f(a) * f(b) > 0:
    print('your input is not valid, please insert another one')
    a = float(input('Enter the lower interval'))
    b = float(input('Enter the upper interval'))
    print(f'{a}, {f(a)}')
    print(f'{b}, {f(b)}')

print('this input is valid')

if f(a) * f(b) == 0:
    print('a == root or b == root')
    if f(a) == 0:
        print('{} is root'.format(a))
    else:
        print('{} is root'.format(b))
    exit()

print('start bisection method')

n = 0
error = 100
old_root = a

while n < n_limit and error > e_limit:
    n = n + 1
    root = (a + b) / 2
    print('new approx root', root)
    print('the function at the new root', f(root))

    if f(root) == 0:
        print('{} is root'.format(root))
        exit()

    if f(a) * f(root) > 0:
        a = root
    else:
        b = root

    error = abs(root - old_root)
    old_root = root

print('the root is = {}, number of iterations = {}, error = {}'.format(root, n, error))
  
