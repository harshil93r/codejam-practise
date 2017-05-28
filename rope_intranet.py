f = open('A-large-practice.in')
o = open('output', 'w+')

total_cases = int(f.readline())

for case in range(total_cases):
    total_wires = int(f.readline())
    old_wires = []
    total = 0
    for wire in range(total_wires):
        _wire = [int(i) for i in f.readline().strip().split()]
        for old_wire in old_wires:
            if (_wire[0] > old_wire[0]) != (_wire[1] > old_wire[1]):
                total += 1
        old_wires.append(_wire)

    print 'Case #%d: %d' % (case + 1, total)
