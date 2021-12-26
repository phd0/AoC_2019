def solve(part, lines):
    result = 0
    for i in lines:
        if part == 1:
            result += ((i//3)-2)
        else:
            result += solve2(i)-i
    return result


def solve2(carb):
    if carb <= 0:
        return 0
    else:
        return carb + solve2((carb//3)-2)


if __name__ == '__main__':
    lines = []
    lines = list(map(int, open('day01.txt').read().split('\n')))
    print("1 ->", solve(1, lines))
    print("2 ->", solve(2, lines))
