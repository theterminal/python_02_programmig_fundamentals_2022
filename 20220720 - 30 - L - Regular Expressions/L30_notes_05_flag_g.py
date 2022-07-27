# 20220722 - Python Code
# This file is about Flags -> Global 'g' from https://regex101.com

import re
# use this to construct the regex: https://regex101.com/


regex = r"this"
test_str = "match this and again this"

matches = re.finditer(regex, test_str)

for matchNum, match in enumerate(matches, start=1):
    print(f'Match {matchNum} was found at {match.start()}-{match.end()}: {match.group()}')

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print(f'Group {groupNum} found at {match.start(groupNum)}-{match.end(groupNum)}: {match.group(groupNum)}')
