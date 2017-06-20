def trib_recursive(n):
    if n == 0: return 0
    elif n == 1: return 1
    elif n == 2: return 2
    else: return trib_recursive(n-1)+ trib_recursive(n-2) + trib_recursive(n-3)
        
print (trib_recursive(10))


def trib_dep(n):
	tribTable = [0 for x in range(n+1)]
	tribTable[0] = 0
	tribTable[1] = 1
	tribTable[2] = 2
	for i in range(3, n+1):
		tribTable[i] = tribTable[i-1] + tribTable[i-2] + tribTable[i-3] 
	return tribTable[n]
      
print(trib_dep(10))	

def trib_iterative(n):
	a, b, c = 0, 1, 2
	for i in range(n):
		a, b, c = b, c, a + b + c
	return a
      
print(trib_iterative(10))	
