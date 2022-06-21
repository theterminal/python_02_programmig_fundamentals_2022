# 20220616 - Python Code - Lists Advance - Lecture
# from lecture - 02


# ------------------------------------------------------------

matrix = [x1 for x1 in range(3) for y1 in range(3)]
print(matrix)

matrix = [[x2 for x2 in range(3)] for y2 in range(3)]
print(matrix)

matrix = [[[x3 for x3 in range(3)] for y3 in range(3)] for z3 in range(3)]
print(matrix)


# ------------------------------------------------------------


matrix = [x1 for x1 in range(3) for _ in range(3)]
print(matrix)

matrix = [[x2 for x2 in range(3)] for _ in range(3)]
print(matrix)

matrix = [[[x3 for x3 in range(3)] for _ in range(3)] for _ in range(3)]
print(matrix)


# ------------------------------------------------------------


word = 'programming'
print([n for n in word if n != 'o'])


# ------------------------------------------------------------


word = 'programming'
nots = 'aouei'
print([n for n in word if n not in nots])


# ------------------------------------------------------------


word = 'programming'
nots = ['a', 'o', 'u', 'e', 'i']
print([n for n in word if n not in nots])

