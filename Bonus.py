# B01 - LCG

import time, os
from function import *

def randomseed(x):
    now = time.perf_counter()
    ProcessId = os.getpid()
    seed = int(now*ProcessId*x)

    return seed
    
def lcg(min: int ,max: int ,x: int) -> int : 
    seed = randomseed(x)
    a = 1662533
    c = 1283463648
    m = 2**32
    r = (a*seed+c) % m
    hasil = min + int((max-min+1) * (r/(m+1)))

    return hasil