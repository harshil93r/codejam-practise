f = open('A-small-practice.in')
o = open('output', 'w+')

total_cases = int(f.readline())

for case in range(total_cases):
    _sum = 0
    vector_lenght = int(f.readline())
    first_vector = [int(i) for i in f.readline().strip().split()]
    second_vector = [int(i) for i in f.readline().strip().split()]

    first_vector.sort()
    second_vector.sort(reverse=True)

    for i in range(vector_lenght):
        _sum += first_vector[i] * second_vector[i]

    o.write('Case #%d: %d' % (case + 1, _sum) + '\n')
