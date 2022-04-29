# 4) h - Considere o vetor


v = list ( range (50) )
print(v)
print("")

#alenea a)
print("A)")
a = v[:11]
print(a)
print("")

#alenea b)
print("B)")
b = v[40:50]
print(b)
print("")

#alenea c)
print("C)")
c = v[10:21]
print(c)
print("")

#alenea d)
print("D)")
d = v
d.pop(4) #pop tira a posição 4 da lista
print(d)
print("")

#alenea e)
print("E)")
e = v
e.remove(20) #remove o 20 da lista
print(e)
print("")

#alenea f)
print("F)")
f = v[::-1]
print(f)
print("")

#alenea g)
print("G)")
g = ['a','b','c']
gg = v+g
print(gg)
print("")
