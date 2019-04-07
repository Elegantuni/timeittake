#!/usr/bin/env python3

import sys
import math

if len(sys.argv) == 3:
    number1 = float(sys.argv[2])

    total1 = float(sys.argv[1])

    timetakes = total1 / number1

    years = int(timetakes / 12)

    months = int(math.ceil(timetakes % 12))

    if months == 12:
        months = 0
        years = years + 1

    print("The total amount of years and months to produce $", total1, "saving $", number1, "is", years, "years and", months, "months")
else:
    print(sys.argv[0], "<total price> <money saved per month>")

