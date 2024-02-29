def function():
    n = int(input("Введите число n: "))
    new_list = []
    for i in range(1, n+1):
        for j in range(i):
            new_list.append(str(i))
    return new_list[:n]


if __name__ == '__main__':
    print(" ".join(function()))
