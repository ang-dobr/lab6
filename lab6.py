def rot(num):
    num = str(num)
    num = [char for char in num]
    for i in range(len(num)):
        if num[i] == '6':
            num[i] = '9'
            break
    num1 = ''.join(map(str, num))
    return int(num1)


n = int(input())
print(rot(n))
