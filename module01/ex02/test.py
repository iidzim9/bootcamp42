from vector import Vector

print('--------add-----------')
v1 = Vector((10,16))
print(v1.__dict__)
v2 = v1 + 6
print(v2)
v2 = 6 + v1
print(v2)
print('--------sub-----------')
v1 = Vector((10,16))
print(v1.__dict__)
v2 = v1 - 6
print(v2)
v2 = 6 - v1
print(v2)
print('--------mult-----------')
v1 = Vector((10,16))
print(v1.__dict__)
v2 = v1 * 6
print(v2)
v2 = 6 * v1
print(v2)
print('--------div-----------')
v1 = Vector((10,16))
print(v1.__dict__)
v2 = v1 / 6
print(v2)
v2 = 6 / v1
print(v2)
print(str(v1))

print(str(v1))
print(repr(v1))
