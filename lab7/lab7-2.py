n1 = '0b11110000'
n2 = '0b10101010'
 
n1 = int(n1,2)
n2 = int(n2,2)
 
bit_or = n1 | n2
bit_and = n1 & n2
bit_xor = n1 ^ n2
 
print("OR: %10s" % bin(bit_or))
print("AND: %10s" % bin(bit_and))
print("XOR: %10s" % bin(bit_xor))
