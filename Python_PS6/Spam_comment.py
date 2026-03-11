p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your comment")
message=message.lower()


if((p1.lower() in message) or (p2.lower() in message) or (p3.lower() in message) or (p4.lower() in message)):
    print("This comment is a spam")
else:
    print("This comment is not a spam")