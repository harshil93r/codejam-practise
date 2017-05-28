# Source :
# https://www.united-coders.com/christian-harms/google-code-jam-solution-for-alien-language/

import sys
import re
fp = file(sys.argv[1])

# read params
(l, d, n) = [int(x) for x in fp.next().split()]

# read words
words = [fp.next() for x in range(d)]

# read pattern
for i in range(1, n + 1):
    searchStr = fp.next().replace("(", "[").replace(")", "]")
    searchIt = re.compile(searchStr).search
    print "Case #%d: %d" % (i, len(filter(searchIt, words)))
fp.close()
