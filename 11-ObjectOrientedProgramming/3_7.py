from statistics import Statistics

def main():
    stats = Statistics()

    while True:
        try:
            number = float(input("Enter a number (or type 'stop' to finish): "))
            stats.add_number(number)
        except ValueError:
            break

    stats.display_numbers()
    stats.show_statistics()

if __name__ == "__main__":
    main()
