def p1(lines):
    horiz, depth = 0, 0
    for line in lines:
        line = line.strip().split(" ")
        match line:
            case ["forward", dist] if dist.isdigit():
                horiz += int(dist)
            case["up", dist] if dist.isdigit():
                depth -= int(dist)
            case["down", dist] if dist.isdigit():
                depth += int(dist)
            case _:
                print(f"fail {line}")
    print(f"p1: {horiz * depth}")


def p2(lines):
    horiz, depth, aim = 0, 0, 0
    for line in lines:
        line = line.strip().split(" ")
        match line:
            case ["forward", dist] if dist.isdigit():
                dist = int(dist)
                horiz += dist
                depth += (aim * dist)
            case["up", dist] if dist.isdigit():
                dist = int(dist)
                aim -= dist
            case["down", dist] if dist.isdigit():
                dist = int(dist)
                aim += dist
            case _:
                print(f"fail {line}")
    print(f"p2: {horiz * depth}")


if __name__ == "__main__":
    with open('input') as f:
        lines = f.readlines()
        p1(lines)
        p2(lines)
