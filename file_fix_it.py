f = open('A-large-practice.in')
o = open('output', 'w+')

total_cases = int(f.readline())

for case in range(total_cases):
    (started_cases, required_cases) = [int(i)
                                       for i in f.readline().strip().split()]
    fil_sys = {}
    total = 0
    for started_case in range(started_cases):
        dirs = f.readline().strip().split('/')[1:]
        temp = fil_sys
        for _dir in dirs:
            if _dir in temp:
                temp = temp[_dir]
            else:
                temp[_dir] = {}
                temp = temp[_dir]

    for required_case in range(required_cases):
        dirs = f.readline().strip().split('/')[1:]
        temp = fil_sys
        for _dir in dirs:
            if _dir in temp:
                temp = temp[_dir]
            else:
                temp[_dir] = {}
                temp = temp[_dir]
                total += 1

    print 'Case #%d: %d' % (case + 1, total)
    o.write('Case #%d: %d\n' % (case + 1, total))
