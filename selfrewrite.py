#hsh
import random
import hashlib

NkV1SUzFM7U07GUe = open(__file__,mode='r')
UtU5yx7iCW7MYBjS=NkV1SUzFM7U07GUe.read()
UtU5yx7iCW7MYBjS=UtU5yx7iCW7MYBjS.replace("#hsh","#hsh"+str(hex(random.randint(0,255))).replace('0x',''))
NkV1SUzFM7U07GUe.close()
NkV1SUzFM7U07GUe = open(__file__,mode='w')
NkV1SUzFM7U07GUe.write(UtU5yx7iCW7MYBjS)
NkV1SUzFM7U07GUe.close()

print('md5',hashlib.md5(open(__file__,'r').read().encode()).hexdigest())