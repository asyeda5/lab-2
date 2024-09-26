#!/usr/bin/env python3
# Author: Aliza Jafferi Syeda
# Author ID: asyeda5@myseneca.ca
# Date Created: 2024/09/23  

import sys

# Assign the first command line argument to timer
timer = int(sys.argv[1])
 

while timer > 0:
    print(timer)
    timer -= 1
print('blast off!')
