# text_utils.py

def count_letter(text, letter):
    """Counts how many times a specific letter appears in the given text."""
    return text.lower().count(letter.lower())
