# lol this is janky but just get the ball rolling

def main(lines):
    increasing_count = 0
    for i in range(0, len(lines)-2):
        if sum(lines[i+1:i+4]) > sum(lines[i:i+3]):
            increasing_count += 1
    print(increasing_count)


if __name__ == "__main__":
    lines = []
    while True:
        try:
            i = input()
            lines.append(int(i))
        except:
            break
    main(lines)
