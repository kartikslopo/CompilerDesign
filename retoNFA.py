expr = input("Enter an expression: ")
m = [""]*20
for x in range(len(expr)):
    m[x] = expr[x]
t = [[' ' for _ in range(10)] for _ in range(10)]
r = 0
c = 0
for i in range(len(m)-1):
    if m[i] == "|":
        t[r][r + 1] = 'E'
        t[r + 1][r + 2] = m[i - 1]
        t[r + 2][r + 5] = 'E'
        t[r][r + 3] = 'E'
        t[r + 4][r + 5] = 'E'
        t[r + 3][r + 4] = m[i + 1]
        r = r + 5
    elif m[i] == "*":
        t[r - 1][r] = 'E'
        t[r][r + 1] = 'E'
        t[r][r + 3] = 'E'
        t[r + 1][r + 2] = m[i - 1]
        t[r + 2][r + 1] = 'E'
        t[r + 2][r + 3] = 'E'
        r = r + 3
    elif m[i] == "+":
        t[r][r + 1] = m[i - 1]
        t[r + 1][r] = 'E'
        r = r + 1
    else:
        if c == 0:
            if m[i].isalpha() and m[i+1].isalpha():
                t[r][r + 1] = m[i]
                t[r + 1][r + 2] = m[i + 1]
                r = r + 2
                c = 1
            c = 1
        elif c == 1:
            if m[i+1].isalpha():
                t[r][r + 1] = m[i + 1]
                r = r + 1
                c = 2
        else:
            if m[i+1].isalpha():
                t[r][r + 1] = m[i + 1]
                r = r + 1
                c = 3

for j in range(r+1):
    print(j, end=" ")
print("\n_____\n")
for i in range(r+1):
    for j in range(r+1):
        print(t[i][j], end=" ")
    print("|", i)
print("Start state: 0\nFinal state:", i-1)

