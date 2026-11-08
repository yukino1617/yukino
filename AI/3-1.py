import sys
def function(a):
    for i in range(1, a + 1):
        print(' ' * (a - i) + '*' * (2 * i - 1))
    for i in range(a - 1, 0, -1):
        print(' ' * (a - i) + '*' * (2 * i - 1))
for line in sys.stdin:
    n = int(line.strip())
    function(n)


