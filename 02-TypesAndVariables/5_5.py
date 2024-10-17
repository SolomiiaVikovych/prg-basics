price_str = input("enter price")
price=float(price_str)
discount_str= input("discount in %")
discount=float(discount_str)
final_emount= price*(100 - discount)/100
print (" emount before discount =", price , "and emount after discount = ", final_emount)