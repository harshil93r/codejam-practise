f = open('A-large-practice.in')
o = open('output', 'w+')

total_cases = int(f.readline())

for case in range(total_cases):
    credits = int(f.readline())
    f.readline()
    prices = [int(i) for i in f.readline().strip().split()]

    for pos, price in enumerate(prices):
        if (credits - price) in prices:
            if price == (credits - price):
                if prices.count(price) == 1:
                    continue
                prices.pop(pos)
                o.write('Case #%d: %d %d\n' %
                        (case + 1, pos, prices.index(credits - price) + 1))
                break
            else:
                o.write('Case #%d: %d %d\n' %
                        (case + 1, pos, prices.index(credits - price)))
                break
