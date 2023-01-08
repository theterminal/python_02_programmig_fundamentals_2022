# 20220615 - Python
# Longer Line

import math


# -------------- version 1 -------------------------- judge ???%
# NOT A WORKING VERSION !!!

# A(2,4)
# B(-1, 2)

# C(-5,-5)
# D(4, -3)

# To test the code, enter coordinates for A, B, C, D - one by one with 'Enter' after each one

# returns the coordinates of the longer line
def longer(abx1, aby1, abx2, aby2, cdx1, cdy1, cdx2, cdy2):
    # Line AB
    l_ab_x_diff = l_ab_y_diff = None

    if ((abx1 < 0) and (abx2 < 0)) or ((abx1 >= 0) and (abx2 >= 0)):
        l_ab_x_diff = abs(abs(abx1) - abs(abx2))

    elif ((abx1 < 0) and (abx2 > 0)) or ((abx1 > 0) and (abx2 < 0)):
        l_ab_x_diff = abs(abs(abx1) + abs(abx2))

    if ((aby1 < 0) and (aby2 < 0)) or ((aby1 >= 0) and (aby2 >= 0)):
        l_ab_y_diff = abs(abs(aby1) - abs(aby2))

    elif ((aby1 < 0) and (aby2 > 0)) or ((aby1 > 0) and (aby2 < 0)):
        l_ab_y_diff = abs(abs(aby1) + abs(aby2))

    # Line CD
    l_cd_x_diff = l_cd_y_diff = None

    if ((cdx1 < 0) and (cdx2 < 0)) or ((cdx1 >= 0) and (cdx2 >= 0)):
        l_cd_x_diff = abs(abs(cdx1) - abs(cdx2))

    elif ((cdx1 < 0) and (cdx2 > 0)) or ((cdx1 > 0) and (cdx2 < 0)):
        l_cd_x_diff = abs(abs(cdx1) + abs(cdx2))

    if ((cdy1 < 0) and (cdy2 < 0)) or ((cdy1 >= 0) and (cdy2 >= 0)):
        l_cd_y_diff = abs(abs(cdy1) - abs(cdy2))

    elif ((cdy1 < 0) and (cdy2 > 0)) or ((cdy1 > 0) and (cdy2 < 0)):
        l_cd_y_diff = abs(abs(cdy1) + abs(cdy2))

    # if 'AB > CD'
    if (l_ab_x_diff + l_ab_y_diff) > (l_cd_x_diff + l_cd_y_diff):
        lst_res = [abx1, aby1, abx2, aby2]
        return lst_res

    # if 'CD > AB'
    elif (l_ab_x_diff + l_ab_y_diff) < (l_cd_x_diff + l_cd_y_diff):
        lst_res = [cdx1, cdy1, cdx2, cdy2]
        return lst_res

    # if 'CD = AB'
    else:
        lst_res = [abx1, aby1, abx2, aby2]
        return lst_res


# returns the closest of 2 points to the coordinate center
def center_point(x1, y1, x2, y2):
    if (abs(x1) + abs(y1)) == (abs(x2) + abs(y2)):
        return f'({math.floor(x1)}, {math.floor(y1)})'

    elif (abs(x1) + abs(y1)) < (abs(x2) + abs(y2)):
        return [math.floor(x1), math.floor(y1)]

    else:
        return [math.floor(x2), math.floor(y2)]


# main function
def longer_line(abx1, aby1, abx2, aby2, cdx1, cdy1, cdx2, cdy2):

    from_longer = longer(abx1, aby1, abx2, aby2, cdx1, cdy1, cdx2, cdy2)
    from_center_point = center_point(from_longer[0], from_longer[1], from_longer[2], from_longer[3])

    if (from_center_point[0] == from_longer[0]) and (from_center_point[1] == from_longer[1]):
        x1_out = from_center_point[0]
        y1_out = from_center_point[1]
        x2_out = from_longer[2]
        y2_out = from_longer[3]
    else:
        x1_out = from_center_point[0]
        y1_out = from_center_point[1]
        x2_out = from_longer[0]
        y2_out = from_longer[1]

    return f'({x1_out}, {y1_out})({x2_out}, {y2_out})'


l_ab_x1 = int(input())
l_ab_y1 = int(input())
l_ab_x2 = int(input())
l_ab_y2 = int(input())

l_cd_x1 = int(input())
l_cd_y1 = int(input())
l_cd_x2 = int(input())
l_cd_y2 = int(input())

result = longer_line(l_ab_x1, l_ab_y1, l_ab_x2, l_ab_y2, l_cd_x1, l_cd_y1, l_cd_x2, l_cd_y2)
print(result)


# ---------------------------------------

#
# 20220615 - Python Code
# Longer Line
#
# import math
#
# # A(2,4)
# # B(-1, 2)
#
# # C(-5,-5)
# # D(4, -3)
#
# # To test the code, enter coordinates for A, B, C, D - one by one with 'Enter' after each
#
# l_ab_x_diff = l_ab_y_diff = 0
# l_cd_x_diff = l_cd_y_diff = 0
#
# # Line AB
# if ((l_ab_x1 < 0) and (l_ab_x2 < 0)) or ((l_ab_x1 >= 0) and (l_ab_x2 >= 0)):
#     l_ab_x_diff = abs(abs(l_ab_x1) - abs(l_ab_x2))
#
# elif ((l_ab_x1 < 0) and (l_ab_x2 > 0)) or ((l_ab_x1 > 0) and (l_ab_x2 < 0)):
#     l_ab_x_diff = abs(abs(l_ab_x1) + abs(l_ab_x2))
#
# if ((l_ab_y1 < 0) and (l_ab_y2 < 0)) or ((l_ab_y1 >= 0) and (l_ab_y2 >= 0)):
#     l_ab_y_diff = abs(abs(l_ab_y1) - abs(l_ab_y2))
#
# elif ((l_ab_y1 < 0) and (l_ab_y2 > 0)) or ((l_ab_y1 > 0) and (l_ab_y2 < 0)):
#     l_ab_y_diff = abs(abs(l_ab_y1) + abs(l_ab_y2))
#
# # Line CD
# if ((l_cd_x1 < 0) and (l_cd_x2 < 0)) or ((l_cd_x1 >= 0) and (l_cd_x2 >= 0)):
#     l_cd_x_diff = abs(abs(l_cd_x1) - abs(l_cd_x2))
#
# elif ((l_cd_x1 < 0) and (l_cd_x2 > 0)) or ((l_cd_x1 > 0) and (l_cd_x2 < 0)):
#     l_cd_x_diff = abs(abs(l_cd_x1) + abs(l_cd_x2))
#
# if ((l_cd_y1 < 0) and (l_cd_y2 < 0)) or ((l_cd_y1 >= 0) and (l_cd_y2 >= 0)):
#     l_cd_y_diff = abs(abs(l_cd_y1) - abs(l_cd_y2))
#
# elif ((l_cd_y1 < 0) and (l_cd_y2 > 0)) or ((l_cd_y1 > 0) and (l_cd_y2 < 0)):
#     l_cd_y_diff = abs(abs(l_cd_y1) + abs(l_cd_y2))
#
# # print('-----------------------------')
# # print(l_ab_x_diff, 'Line AB - x diff')
# # print(l_ab_y_diff, 'Line AB - y diff')
# # print('-----------------------------')
# # print(l_cd_x_diff, 'Line CD - x diff')
# # print(l_cd_y_diff, 'Line CD - y diff')
# # print('-----------------------------')
#
# if (l_ab_x_diff + l_ab_y_diff) > (l_cd_x_diff + l_cd_y_diff):
#     print('AB > CD')
#     print(f'({l_ab_x1}, {l_ab_y1})({l_ab_x2}, {l_ab_y2})')
# elif (l_ab_x_diff + l_ab_y_diff) < (l_cd_x_diff + l_cd_y_diff):
#     print('CD > AB')
#     print(f'({l_cd_x1}, {l_cd_y1})({l_cd_x2}, {l_cd_y2})')
# else:
#     print('AB = CD')
#     print(f'({l_ab_x1}, {l_ab_y1})({l_ab_x2}, {l_ab_y2})')
#
#
# # function returns the closest of 2 points to the coordinate center
# def center_point(x1, y1, x2, y2):
#     if (abs(x1) + abs(y1)) == (abs(x2) + abs(y2)):
#         return f'({math.floor(x1)}, {math.floor(y1)})'
#
#     elif (abs(x1) + abs(y1)) < (abs(x2) + abs(y2)):
#         return f'({math.floor(x1)}, {math.floor(y1)})'
#
#     else:
#         return f'({math.floor(x2)}, {math.floor(y2)})'
#
#
# result_center_point = center_point(x_1, y_1, x_2, y_2)
# print(result_result_center_point)
#
#
# # final function
# def longer_line(abx1, aby1, abx2, aby2, cdx1, cdy1, cdx2, cdy2):
#
#     return f'({X1}, {Y1})({X2}, {Y2})'
#
#
# l_ab_x1 = int(input())
# l_ab_y1 = int(input())
# l_ab_x2 = int(input())
# l_ab_y2 = int(input())
#
# l_cd_x1 = int(input())
# l_cd_y1 = int(input())
# l_cd_x2 = int(input())
# l_cd_y2 = int(input())
#
# result = longer_line(l_ab_x1, l_ab_y1, l_ab_x2, l_ab_y2, l_cd_x1, l_cd_y1, l_cd_x2, l_cd_y2)
# print(result)
