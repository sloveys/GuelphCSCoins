#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import hashlib
import sys
print sys.version_info

class MMinerMain: 
    w = 64
    n = 312
    m = 156
    r = 31
    a = 0xB5026F5AA96619E9
    u = 29
    d = 0x5555555555555555
    s = 17
    b = 0x71D67FFFEDA60000
    t = 37
    c = 0xFFF7EEE000000000
    l = 43
    f = 6364136223846793005
    
    lower_mask = 0x7FFFFFFF
    upper_mask = 0xffffffff80000000
    
    def hash_val(input):
        h = hashlib.sha256()
        h.update(input)
        return h.hexdigest()


    if __name__ == "__main__":
        hvar = '00000000000000000000000000000000000000000000000000000000000000000'
        new_hvar = hash_val(hvar)
        seed = ''
        for i in range(0, 8):
            seed = seed + new_hvar[14 - i*2] + new_hvar[15 - i*2]
        print seed
        print int(seed, 16)
        print get_random_mt(int(seed, 16), 64, 20)


