"""
code for computing free throw percentage
"""

ftmade = input("How many shots did you make?")
ftatt = input("How many shots did you attempt?")

ftpct = float(ftmade)/float(ftatt)

print("Your free throw percentage is:")
print(ftpct*100, "%")
