
#determine whether or not a is a quadratic residue modulo p
def legendre_symbol(a, p):
    return pow(a, (p - 1) // 2, p)

def tonelli_shanks(a, p):
    #is a quadratic residue
    if legendre_symbol(a, p) != 1:
        return None  
    
    #Simple case where p % 4 == 3
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    
    # Decompose 
    Q, S = p - 1, 0
    #repeatedly divide p -1 until until is odd
    while Q % 2 == 0:
        Q //= 2
        S += 1
    
    # Find a non-quadratic residue z
    for z in range(2, p):
        if legendre_symbol(z, p) == p - 1:
            break
    # initialise variables
    M = S
    c = pow(z, Q, p)
    t = pow(a, Q, p)
    R = pow(a, (Q + 1) // 2, p)
    #loop until t = 1
    while t != 1:
        t2i = t
        for i in range(1, M):
            t2i = pow(t2i, 2, p)
            if t2i == 1:
                break
        b = pow(c, 2 ** (M - i - 1), p)
        R = (R * b) % p
        t = (t * b * b) % p
        c = (b * b) % p
        M = i
    
    return R

# Example usage
p =   "Replace with 2048-bit prime"
a =   "Replace with integer a"
result = tonelli_shanks(a, p)
if result:
    smaller_root = min(result, p - result)
    print("Root:", smaller_root)
else:
    print("No square root.")