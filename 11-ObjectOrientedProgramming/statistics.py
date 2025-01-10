class Statistics:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def display_numbers(self):
        print("Numbers:", " ".join(map(str, self.numbers)))

    def get_max(self):
        return max(self.numbers) if self.numbers else None

    def get_min(self):
        return min(self.numbers) if self.numbers else None

    def get_mean(self):
        return sum(self.numbers) / len(self.numbers) if self.numbers else None

    def get_median(self):
        if not self.numbers:
            return None
        sorted_numbers = sorted(self.numbers)
        n = len(sorted_numbers)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
        else:
            return sorted_numbers[mid]

    def show_statistics(self):
        print(f"Minimum: {self.get_min()}")
        print(f"Maximum: {self.get_max()}")
        print(f"Mean: {self.get_mean()}")
        print(f"Median: {self.get_median()}")
