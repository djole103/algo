def cool():
        a, b, c, d = int(input()), int(input()), int(input()), int(input())

        if (c < a and b >= 0) or (d < b and a >= 0):
                return False

        if abs(c - a) % b == 0 and abs(d-b) % a == 0:
                return True
        return False

print(cool())
