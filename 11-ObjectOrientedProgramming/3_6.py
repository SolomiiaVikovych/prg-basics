from bank import Card
def main():
    my_card_acc = '22 1234 1234 1234 1234 1234 1234'
    my_card = Card(my_card_acc)
    my_card.show_info()
    my_card.deposit(25.30)
    my_card.show_info()
    my_card.withdraw(31.70)
    my_card.show_info()
    my_card.withdraw(14)
    my_card.show_info()

if __name__ == "__main__":
    main()

