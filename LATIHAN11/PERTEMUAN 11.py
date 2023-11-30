import math

a = lambda x: x**2
b = lambda x, y: math.sqrt(x**2 + y**2)
c = lambda *args: sum(args)/len(args)
d = lambda s: "".join(set(s))

# Memanggil fungsi lambda a(x)
result_a = a(9)
print(result_a)

# Memanggil fungsi lambda b(x, y)
result_b = b(6, 8)
print(result_b)

# Memanggil fungsi lambda c(*args)
result_c = c(2, 3, 4, 5, 6)
print(result_c)

# Memanggil fungsi lambda d(s)
result_d = d("hello")
print(*result_d, sep="")


