def p1(lines):
    gamma, epsilon = 0, 0
    for i in range(len(lines[0])-1):
        ones = 0
        for line in lines:
            ones += int(line[i])
        if ones > (len(lines)//2):
            gamma += 1
        else:
            epsilon += 1
        gamma <<= 1
        epsilon <<= 1
    gamma >>= 1
    epsilon >>= 1
    print(f"gamma:{gamma:b} epsilon:{epsilon:b} power:{gamma * epsilon}")


if __name__ == "__main__":
    with open('input') as f:
        lines = f.readlines()
        p1(lines)
