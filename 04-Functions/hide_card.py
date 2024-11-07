def hide(card_number):
    number = input('enter card number')
    modified_text = number[:2] + '*' * (12 - 2 + 1) + number[13:]
    return modified_text

        