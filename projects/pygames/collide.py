from math import sqrt, abs
from typing import Tuple


def ccCollideInfo(center0: Tuple, radius0, center1: Tuple, radius1, rvx, rvy):
    x0, y0 = center0
    x1, y1 = center1
    c0 = (radius0 + radius1) ** 2
    if rvx == 0:  # x = x1
        x = x1
        if c0 - (x0 - x1) ** 2 >= 0:
            y = sqrt(c0 - (x0 - x1) ** 2) + y0
            t = 1 - (y1 - y) / rvy
            if 0 < t <= 1:
                return (t, x, y)
    elif rvy == 0:  # y = y1
        y = y1
        if c0 - (y0 - y1) ** 2 >= 0:
            x = sqrt(c0 - (y0 - y1) ** 2) + x0
            t = 1 - (x1 - x) / rvx
            if 0 < t <= 1:
                return (t, x, y)
    else:
        c1 = x1 + (y0 - y1) * rvx / rvy
        c2 = (rvy / rvx) ** 2
        b = (x0 + c1 * c2) / (1 + c2)
        c = (x0 ** 2 + c2 * c1 ** 2 - c0) / (1 + c2)
        if b ** 2 - c >= 0:
            x_solve1 = b + sqrt(b ** 2 - c)
            x_solve2 = b - sqrt(b ** 2 - c)
            result = 10
            for i in (x_solve1, x_solve2):
                t = 1 - (x1 - i) / rvx
                if 0 < t <= 1:
                    result = min(t, result)
            if result != 10:
                t = result
                x = x1 + (t - 1) * rvx
                y = y1 + (t - 1) * rvy
                return (t, x, y)
    # (x-x1)/rvx - (y-y1)/rvy = 0
    # y = (rvy/rvx)((x-x1)+y1(rvx/rvy))
    # (x-x0)**2 + (y-y0)**2 = (radius0+radius1)**2 = c0
    # (x-x0)**2 + c2(x-x1+(y1-y0)(rvx/rvy))**2 = c0
    # (x-x0)**2 + c2(x-c1)**2 = c0
    # x**2 - 2*x*x0 + x0**2 + c2(x**2 - 2*c1*x+c1**2) - c0 = 0
    # x**2 - 2*(x0+c1*c2)/(1+c2) + (x0**2+c2*(c1**2) - c0)/(1+c2) = 0


def lpCollideInfo(first_x, first_y, second_x, second_y, center1, rvx, rvy):
    # (x-fx)*a + (y-fy)*b = 0
    pass


def rpCollideInfo(center0, width, height, center1, rvx, rvy):
    x0, y0 = center0
    x1, y1 = center1
    if rvx == 0:  # x = x1
        x = x1
        if abs(x1 - x0) < width / 2:
            result = 10
            for i in (y0 + height / 2, y0 - height / 2):
                t = 1 - (y1 - i) / rvy
                if 0 < t <= 1:
                    result = min(t, result)
            if result != 10:
                t = result
                y = y1 + (t - 1) * rvy
                return (t, x, y)
    elif rvy == 0:  # y = y1
        y = y1
        if abs(y1 - y0) < height / 2:
            result = 10
            for i in (x0 + width / 2, x0 - width / 2):
                t = 1 - (x1 - i) / rvx
                if 0 < t <= 1:
                    result = min(t, result)
            if result != 10:
                t = result
                x = x1 + (t - 1) * rvx
                return (t, x, y)
    else:
        x = x1
        if abs(x1 - x0) < width / 2:
            result = 10
            for i in (y0 + height / 2, y0 - height / 2):
                t = 1 - (y1 - i) / rvy
                if 0 < t <= 1:
                    result = min(t, result)
            if result != 10:
                t = result
                x = x1 + (t - 1) * rvx
                y = y1 + (t - 1) * rvy
                return (t, x, y)


def cpCollideInfo(center1, radius, center2, rvx, rvy):
    pass


def rrCollideInfo(center1, width1, height1, center2, width2, height2, rvx, rvy):
    pass


def rcCollideInfo(center1, width, height, center2, radius2, rvx, rvy):
    pass


print(ccCollideInfo((0, 0), 2, (3, 4), 5, -12, -16))
