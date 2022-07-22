# 20220715 - Python Code
# Notes 07 - Animate Time

# https://www.onlinegdb.com/

import os
import time


# It may not work correctly on all IDEs!

def animate_text(text):
    num_chars = 1

    while True:
        print('\n')
        print(text[0: num_chars])
        num_chars += 1

        if num_chars >= len(text):
            num_chars = 0

        time.sleep(0.05)
        os.system('clear')


animate_text('Learning to program will save humanity one day!')
