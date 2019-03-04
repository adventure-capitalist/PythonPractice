DOB = (raw_input("What is your DOB DD-MM-YYY? ")

date_extraction = DOB.split("-")
day = date_extraction[0]
month = date_extraction[1]
year = date_extraction[2]

result = calculate_gen(int(year))


while raw_input is not int:
    try:
        birth_year = int(raw_input("What year were you born? "))
        break
    except ValueError:
        print("Please enter a valid number")
def calculate_gen()
    if year >= 1901: gen = "Interbellum"
    if year >= 1910: gen = "Greatest"
    if year >= 1946: gen = "Baby Boomer"
    if year >= 1965: gen = "X"
    if year >= 1975: gen = "Xennial"
    if year >= 1985: gen = "Millennial"
    if year >= 1995: gen = "Z"
    if year >= 2013: gen = "Alpha"


print "So, you're part of the %s generation." % gen
