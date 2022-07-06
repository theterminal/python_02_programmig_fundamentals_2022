# 20220615 - Python Code - Functions - More Exercise
# 03 - Longer Line - judge url: https://judge.softuni.org/Contests/Practice/Index/1729#2

import math


# !!! NOT 100% VERSION - IT IS 40% ONLY !!!

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
    if (l_ab_x_diff + l_ab_y_diff) < (l_cd_x_diff + l_cd_y_diff):
        lst_res = [cdx1, cdy1, cdx2, cdy2]
        return lst_res

    # if 'CD = AB'
    else:
        lst_res = [abx1, aby1]
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
    if len(from_longer) == 2:
        print(f'({math.floor(from_longer[0])}, {math.floor(from_longer[1])}, {math.floor(abx2)}, {math.floor(aby2)})')
        return

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

    print(f'({math.floor(x1_out)}, {math.floor(y1_out)})({math.floor(x2_out)}, {math.floor(y2_out)})')
    return


ab_x1 = float(input())
ab_y1 = float(input())
ab_x2 = float(input())
ab_y2 = float(input())

cd_x1 = float(input())
cd_y1 = float(input())
cd_x2 = float(input())
cd_y2 = float(input())

longer_line(ab_x1, ab_y1, ab_x2, ab_y2, cd_x1, cd_y1, cd_x2, cd_y2)
