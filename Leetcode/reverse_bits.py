#190

def reverseBits(n: int) -> int:
        s = bin(n)
        dig0 = (32-len(s) + 2)*'0'
        s = s.replace('0b',dig0)
        # s = format(43261596,"032b") # Same as above 3 lines
        # s = '{:032b}'.format(43261596) # Same as above
        s1= s[::-1]
        i = int(s1,2)
        return i
        # int('{:032b}'.format(n)[::-1],2) # one line solution

print(reverseBits(43261596)) 