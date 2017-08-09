def cheese_and_crackers(cheese_count, cracker_count):
    print(f"cheese:{cheese_count}\ncracker:{cracker_count}")


cheese_and_crackers(10,30)

amount_of_cheese = int(input("amount of cheese?"))
amount_of_cracker = int(input("amount of cracker?"))
cheese_and_crackers(amount_of_cheese, amount_of_cracker+2)
