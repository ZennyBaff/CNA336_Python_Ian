#checks if two strings are the same regardless of case
#CNA 336 , Spring 2018
#Parker,pdswift@student.rtc.edu, Ian, theholyboots@gmail.com


String_A = input(str("Say Anything: "))

String_B = input(str("Say Anything again: "))

String_A = String_A.upper()

String_B = String_B.upper()

if String_B == String_A:
    print("These two words are the same!")
else:
    print("These words are not the same...")