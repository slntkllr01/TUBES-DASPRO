import random
def summaterials() :
    pasir = random.randrange(0,5)
    batu = random.randrange(0,5)
    air = random.randrange(0,5)
    output = ("Jin menemukan", pasir, "pasir",batu, "batu",air,"air")
    return output
print (summaterials())