eq = '4x^2 +4x +    (-8) =  0'

a = int(eq.split('x^2')[0])
b = int(eq.split('x^2')[1].split('x')[0])
c = int(eq.split('x^2')[1].split('x')[1].split('+')[1].split('=')[0].replace('(', '').replace(')', ''))


print(a, b, c)

d = (b ** 2) - (4 * a * c)

x1 = (-b + d ** 0.5) / (2 * a)
x2 = (-b - d ** 0.5) / (2 * a)

print(x1 , x2)