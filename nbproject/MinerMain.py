#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import random
import hashlib
import sys
print sys.version_info

"returns random number from Mersenne Twister algorithm"
def get_random_mt(seed = 1, bits = 64, size = 20):
    random.seed(seed)
    rn = {}
    for i in range(0, size):
        rn[i] = random.getrandbits(bits)
    return rn

def hash_val(input):
    h = hashlib.sha256()
    h.update(input)
    return h.hexdigest()
    

if __name__ == "__main__":
    hvar = '00000000000000000000000000000000000000000000000000000000000000000'
    new_hvar = hash_val(hvar)
    seed = ''
    for i in range(0, 8):
        seed = seed + new_hvar[14- i*2] + new_hvar[15 - i*2]
    print get_random_mt(int(seed, 16), 64)


