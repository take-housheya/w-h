a,b=13.42,42.13
ai,bi=int(a),int(b)
print(int(a))
print(int(b))
af=print((a-ai)*100)
bf=int((b-bi)*100)
print(ai)
print(af)
print(bi)
print(bf)
print(ai==bf or bi==af)

#or
s=13.42
d=42.13
ss=(str(13.42)[0:2])
print(ss)
ds=(str(42.13)[3:5])
print((ss) == (ds))

#or

a1=13.42
b1=42.13
a11=int(a1)
b11=(str(42.13)[3:5])
print(a11)
print(b11)
b12=int(b1)
a12=(str(13.42)[3:5])
print(b12)
print(a12)
print(a11==(int(b11)) or b12==(int(a12)))
print(a11==(int(b11)) and b12==(int(a12)))
