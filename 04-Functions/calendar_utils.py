# calendar_utils.py

def month(n):
    # Dictionary to map month numbers to names
    month_names = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    # Return the corresponding month name or None if invalid
    return month_names.get(n, "Invalid month number")
