"""
US0203
Author: Xinyi Ye
Date: 02/26/2020
"""

from datetime import datetime, timedelta


def birth_b_marriage_us02(fam):
    """ US02: birth before marriage"""
    for key, value in fam.items():

        id_h = value.husband[0]
        birth_h = id_h.birthday
        h_birth_date = datetime.strptime(birth_h[0], "%d %b %Y")
        id_w = value.wife[0]
        birth_w = id_w.birthday
        w_birth_date = datetime.strptime(birth_w[0], "%d %b %Y")

        date_married = value.married
        marriage_date = datetime.strptime(date_married[0], "%d %b %Y")

        if h_birth_date >= marriage_date:
            print(f"Error: FAMILY: US02 birth before marriage：line {birth_h[1]} and {date_married[1]}: "
                        f"{id_h.indi_id[0]}: {birth_h[0]} isn't before {date_married[0]}")

        if w_birth_date >= marriage_date:
             print(f"Error: FAMILY: US02 birth before marriage：line {birth_w[1]} and {date_married[1]}: {id_w.indi_id[0]}: "
                        f"{birth_w[0]} isn't before {date_married[0]}")
        else:
            continue


def birth_b_death_us03(indi):
    """ US03: birth before death"""
    for key, value in indi.items():
        birth = value.birthday
        death = value.death

        if death != 'N/A':
            death_date = datetime.strptime(death[0], "%d %b %Y")
        else:
            continue
        birth_date = datetime.strptime(birth[0], "%d %b %Y")

        if birth_date >= death_date:
            print(f"Error: INDIVITUAL: US03 birth before death："
                     f"line {birth[1]} and {death[1]}: {key}: {birth[0]} isn't before {death[0]}")
        else:
            continue






