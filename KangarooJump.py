#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    # if (int(x1-x2))/(int(v2-v1)) > 0:
    #     if (int(x1-x2)%int(v2-v1)) is 0:
    #         return "YES"
    #     else:
    #         return "NO"
    # else:
    #     return "NO"

    #BCZ x1+y*v1=x1 + y*v2 where x are the positions and v are the distance covered per jump and y are the jumps.
    if (x2 - x1) * (v2 - v1) < 0 and (x2 - x1) % (v2 - v1) == 0:
        return "YES"
    else:
         return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
