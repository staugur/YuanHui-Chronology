# coding:utf8

"""
邵雍提出“元、会、运、世”的时间单位，其中：

    1元统12会。
    1会统30运。
    1运统12世。
    1世统30年。
"""

#: 1元统12会，共129600年。
YUAN: int = 129600

#: 1会统30运，共10800年（一万零八百年）。
HUI: int = 10800

#: 1运统12世，共360年。
YUN: int = 360

#: 1世统30年。
SHI: int = 30


def Chronology(year: int) -> str:
    # 元 取整
    Y: int = year // YUAN
    # 不足1元后的取余年数
    year1 = year % YUAN

    # 会 取整
    H: int = year1 // HUI
    # 不足1会后的取余年数
    year2 = year % HUI

    # 运 取整
    N: int = year2 // YUN
    # 不足1运后的取余年数
    year3 = year2 % YUN

    # 世 取整
    S: int = year3 // SHI
    # 不足1世后的取余年数
    y = year3 % SHI

    return f"{Y}元 {H}会 {N}运 {S}世 {y}年"


if __name__ == "__main__":
    from sys import argv

    try:
        year = int(argv[1])
        if year < 0:
            raise ValueError
    except (IndexError, ValueError, TypeError):
        print(f"Usage: {argv[0]} Year")
    else:
        print(Chronology(year))
