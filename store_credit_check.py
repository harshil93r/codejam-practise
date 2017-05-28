f = open('A-large-practice.in')
o = open('output')

total_cases = int(f.readline())

for case in range(total_cases):
    credits = int(f.readline())
    f.readline()
    prices = [int(i) for i in f.readline().strip().split()]
    x = o.readline().strip().split()
    i = prices[int(x[2])]
    j = prices[int(x[3])]
    if credits != i + j:
        print credits
        print i + j
