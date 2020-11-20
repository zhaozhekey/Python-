a = 0xF0384E
b = a>>16
print(b)
c = (a-(b<<16))>>8
print(c)
d = a-(b<<16)-(c<<8)
print(d)


color = 0xF0384E
red = color >> 16
green = color >> 8 & 0xFF
blue = color & 0xFF
print(red, green, blue)
