#!/usr/bin/env python3
# Author: Aliza Jafferi Syeda
# Author ID: asyeda5@myseneca.ca
# Date Created: 2024/09/23  

import sys

# Check for command line arguments
if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3  # Default value if no arguments are provided

while timer > 0:
    print(timer)
    timer -= 1
print('blast off!')

