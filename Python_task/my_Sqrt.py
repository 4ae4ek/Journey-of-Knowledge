def square_root(n):
    if n == 0 or n == 1:
        return n
    x = n / 2
    while True:
        y = (x + n / x) / 2
        if abs(y - x) < 1e-7:
            break
        x = y

    return round(y)


# Example usage
number = 17262623632632623662362363262235555556246457457474574574574574574466666666666666666666465364545555555555555555555555
result = square_root(number)
print(result)
