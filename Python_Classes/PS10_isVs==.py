# is vs ==
list1  = ["Rishikesh", "Somanth", "Ujjain", "Kashi"]
list2  = ["Rishikesh", "Somanth", "Ujjain", "Kashi"]

print(list1 == list2)

list3  = ["Rishikesh", "Somanth", "Ujjain", "Kashi"]
list4  = ["Rishikesh", "Somanth", "Omkreshwar", "Kashi"]

print(list3 == list4)

list1  = ["Rishikesh", "Somanth", "Ujjain", "Kashi"]
list2  = ["Rishikesh", "Somanth", "Ujjain", "Kashi"]

print(list1 is list2)

list7  = ["Rishikesh", "Somanth", "Ujjain", "Kashi"]
list8  = list7

print(list7 is list8)

list8[0] = "Uttarakhand"
print(list7)
print(list8)

