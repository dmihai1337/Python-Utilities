import sys

# Start Date
print("Enter the start day")
bDD = int(input())
print("Enter the start month")
bMM = int(input())
print("Enter the start year")
bYY = int(input())

# End Date
print("Enter the end day")
eDD = int(input())
print("Enter the end month")
eMM = int(input())
print("Enter the end year")
eYY = int(input())

# Some extra conditions for dumb users
if bMM > 12 | eMM > 12:
    sys.exit("Invalid Date")
elif bDD > 31 | eDD > 31:
    sys.exit("Invalid Date")
elif bYY < 0 | eYY < 0:
    sys.exit("Invalid Date")

DD = 0
MM = 0
YY = 0

leap1 = 0
if bYY % 400 == 0 & bYY % 100 == 0:
    leap1 = 1

if bMM == 2 & bDD < 29 & leap1 == 1:
    sys.exit("Invalid Date")


def get_date(bmm, bdd, leap):
    if bmm % 2 == 0 & bmm < 6:
        if bmm == 2:
            if leap == 1:
                dd = 29 - bdd
            else:
                dd = 28 - bdd
        else:
            dd = 30 - bdd
    elif bmm % 2 == 0 & bmm > 6:
        dd = 31 - bdd
    elif bMM % 2 == 1 & bMM < 6:
        dd = 31 - bdd
    else:
        dd = 30 - bdd
    return dd


# Case 1: same year, same month
if bYY == eYY & bMM == eMM:
    YY = 0
    MM = 0
    DD = eDD - bDD
    if DD < 0:
        sys.exit("Invalid Date")

# Case 2: same year
elif bYY == eYY:
    YY = 0
    MM = eMM - bMM
    if MM < 0:
        sys.exit("Invalid Date")
    else:
        DD = get_date(bMM, bDD, leap1)
        DD = DD + eDD
        if eDD - bDD < 0:
            MM = MM - 1

# Case 3: different year
else:
    YY = eYY - bYY - 1
    DD = get_date(bMM, bDD, leap1)
    if YY < 0:
        sys.exit("Invalid Date")
    else:
        MM = 12 - bMM + eMM
        DD = DD + eDD

# Final Conversions

YY = YY + int(MM / 12)
MM = MM % 12
DD = DD % 7
WW = int(DD / 7)
print(DD, "Day(s),", WW, "Week(s),", MM, "Month(s),", YY, "Year(s) until specified date")
input()
