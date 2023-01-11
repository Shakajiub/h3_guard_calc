#!/usr/bin/env python3

ZONE_STRENGTH    = [-1, 0, 1 ]
MONSTER_STRENGTH = [ 2, 3, 4 ]

MIN_VAL_1 = [ 2500, 1500, 1000,  500,    0 ]
MIN_VAL_2 = [ 7500, 7500, 7500, 5000, 5000 ]

COEFFICIENT_1 = [ 0.5, 0.75, 1, 1.5, 1.5 ]
COEFFICIENT_2 = [ 0.5, 0.75, 1,   1, 1.5 ]

AVG_AI_VALUE = [  72.590909091, 187.565217391,  334.260869565,
                 552.434782609, 841.869565217, 1778.636363636, 5691.6 ]

def calc_AI_value(z, m, o, cm):
    protection_index = ZONE_STRENGTH[z] + MONSTER_STRENGTH[m] - 1

    m1 = MIN_VAL_1[protection_index]
    m2 = MIN_VAL_2[protection_index]
    c1 = COEFFICIENT_1[protection_index]
    c2 = COEFFICIENT_2[protection_index]

    total_AI = 0

    if o - m2 < 0:
        total_AI = (o - m1) * c1
    elif o - m1 > 0:
        total_AI = (o - m1) * c1 + (o - m2) * c2

    return round(total_AI * cm)

def get_avg(v, l):
    return v / AVG_AI_VALUE[l - 1]

def main():
    zones    =   int(input("Enter zone strength (0-2): ........ "))
    monst    =   int(input("Enter monster strength (0-2): ..... "))
    custom_m = float(input("Enter custom multiplier (float): .. "))

    while True:
        treasure = input("\r\nEnter treasure value ('q' to quit): ")
        if treasure == 'q':
            break

        value = calc_AI_value(zones, monst, int(treasure), custom_m)
        print("Guard value is: ...................", value)

        level = int(input("Enter guard level (1-7): .......... "))
        print("Average amount of guards is: ......", get_avg(value, level))

if __name__ == "__main__":
    main()
