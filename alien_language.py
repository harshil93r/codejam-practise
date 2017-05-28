import re

f = open('A-large-practice.in')
o = open('output', 'w+')

headers = f.readline().strip().split()
total_words = int(headers[1])
total_tests = int(headers[2])

words = [f.readline().strip() for i in range(total_words)]


def count_match(total, final_word, all_sets, wildcards, words):
    for pos, s in enumerate(all_sets):
        if s not in wildcards:
            final_word = final_word + s
            if final_word in words:
                total += 1
            elif any(item.startswith(final_word) for item in words):
                return count_match(
                    total,
                    final_word,
                    all_sets[pos + 1:],
                    wildcards,
                    [i for i in words if i.startswith(final_word)]
                )
            else:
                return total

        else:
            for _s in s:
                if final_word + _s in words:
                    total += 1
                elif any(item.startswith(final_word + _s) for item in words):
                    total += count_match(
                        0,
                        final_word + _s,
                        all_sets[pos + 1:],
                        wildcards,
                        [i for i in words if i.startswith(final_word)]
                    )

    return total

for test in range(total_tests):
    line = f.readline()
    all_sets = re.findall(r"[\w']+", line)
    wildcards = re.findall(r"\(([^\)]+)\)", line)

    total = count_match(0, '', all_sets, wildcards, words)

    print 'Case #%d: %d' % (test + 1, total)
