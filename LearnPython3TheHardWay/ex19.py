def cheese_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheeses = 10
amount_of_carackers = 50

cheese_crackers(amount_of_cheeses, amount_of_carackers)


print("We can even do math inside too:")
cheese_crackers(10+20, 5+6)


print("And we can combine the two, variables and math:")
cheese_crackers(amount_of_cheeses + 100, amount_of_carackers + 1000)
