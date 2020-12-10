def mul(a,b):
    ret = set()
    for e in a:
        for e2 in b:
            ret.add(str(e)+str(e2))
    return ret

def iteralt(a):
    ret = set("E")
    for e in a:
        ret.add(e)
    for e in mul(a,a):
        ret.add(e)
    for e in mul(mul(a,a),a):
        ret.add(e)
    for e in mul(mul(mul(a,a),a),a):
        ret.add(e)
    return ret

a = {'a','b','c'}
b = {'a','d'}

print(a-b) # a \ b
print(a.union(b)) #a U B
print(a.intersection(b)) # a ∩ b
print(mul(a,b))
print(iteralt(b))

print(iteralt(a)-iteralt(b))