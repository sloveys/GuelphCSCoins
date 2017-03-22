#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import random
import hashlib

"returns random number from Mersenne Twister algorithm"
def get_random_mt(seed = 1, bits = 32):
    random.seed(seed)
    rn = random.getrandbits(bits)
    return rn

def hash_val(input):
    h = hashlib.sha256()
    h.update(input)
    return h.hexdigest()
    

if __name__ == "__main__":
    rn = get_random_mt()
    print rn
    print hash_val("00000000000000000000000000000000000000000000000000000000000000000") == "e531ef0f962409170917abf9de3287afec23dd1c42c9e1fea66c5feab99e8f7c"


