f = open('B-large-practice.in')
o = open('output', 'w+')

total_cases = int(f.readline())

for case in range(total_cases):
    words = f.readline().strip().split()
    words.reverse()
    print words
    o.write('Case #%d: ' % (case + 1) + ' '.join(words) + '\n')
