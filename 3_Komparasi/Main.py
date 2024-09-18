
bilangan1 = 1
bilangan2 = 2
bilangan3 = 3
bilangan4 = 2

print(bilangan1 != bilangan2)
print(bilangan2 == bilangan4)

print(bilangan1 > bilangan2)
print(bilangan1 < bilangan2)

print(bilangan4 <= bilangan2)

print(bilangan1 < bilangan2 and bilangan4 == bilangan2 )

print(bilangan1 < bilangan2 and bilangan3 > bilangan4)

print(bilangan1 > bilangan3 or bilangan1 < bilangan3)

a = True
b = False
c = not a
print("not %r  = %r" % (a,c))


# Bitwise
a = 15
b = 5
# Bitwise OR "|"
c = a | b
print("Nilai : ", c, "biner : ", format(c, '08b'))

# Bitwise AND "&"
c = a & b
print("Nilai : ", c, "biner : ", format(c, "08b"))

# Bitwise XOR "^"
c = a ^ b
print("Nilai : ", c, "biner : ", format(c, "08b"))

# Shift
# Shftright
c = a >> 2
print("Nilai : ", c, format(c, "08b"))

# Shiftleft
c = a << 2
print("Nilai : ", c, format(c, "08b"))