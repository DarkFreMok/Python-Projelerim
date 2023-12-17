print("2.Dereceden Bir Bilinmeyen Bulma denkleminin Köklerini Bulma")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
delta = b ** 2 - 4 * a * c
x1 = (-b - delta ** 0.5)/(2*a)
x2 = (-b + delta ** 0.5)/(2*a)
print("BirinciKök: {}\nİkinciKök {}\n".format(x1,x2))
