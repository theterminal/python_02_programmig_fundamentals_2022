# 20220722 - Python Code - Regular Expressions - Lecture
# Note 04 - Flags

# use the link to construct the regex: https://regex101.com/

import re


# ----------------- .IGNORCASE ----------------------


txt = 'Mario is annoying. MARIO needs to study before the lectures. MaRiO does a slappy job. mario misses a lot of things during lectures.'

regex = re.findall('Mario', txt)
print(regex)

regex = re.findall('Mario', txt, re.IGNORECASE)
print(regex)


# ----------------- .X -------------------------------


txt = 'Mario is a good guy, and he is 32'
result = re.search(r'''(^\w{5})# comment
                      .+(\d{2}$)# comment''',
                   txt, re.X)

print(result.group(1))
print(result.group(2))
