#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import random

"returns random number from Mersenne Twister algorithm"
def get_random_mt(seed = 1, bits = 32):
    random.seed(seed)
    rn = random.getrandbits(bits)
    return rn


if __name__ == "__main__":
    rn = get_random_mt()
    print rn


