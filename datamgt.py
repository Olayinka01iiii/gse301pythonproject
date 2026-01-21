# Dataset Management and Basic Analysis System

class DataSet:
    def __init__(self, number_file, category_file):
        self.number_file = number_file
        self.category_file = category_file
        self.data = []
        self.categories = set()
        self.total = 0
        self.average = 0
        self.minimum = None
        self.maximum = None

    # 1. Variables & File Handling + 2. Error Handling
    def load_data(self):
        # Load numerical data
        try:
            with open(self.number_file, 'r') as file:
                content = file.read().strip()
                if not content:
                    raise ValueError("Numerical data file is empty")

                for value in content.replace(',', '\n').split():
                    try:
                        self.data.append(float(value))
                    except ValueError:
                        print(f"Invalid value ignored: {value}")

            if not self.data:
                raise ValueError("No valid numeric data found")

        except FileNotFoundError:
            print("Error: Numerical data file not found.")
            exit()
        except ValueError as e:
            print("Error:", e)
            exit()

        # Load categorical data
        try:
            with open(self.category_file, 'r') as file:
                for line in file:
                    if line.strip():
                        self.categories.add(line.strip())
        except FileNotFoundError:
            print("Warning: Category file not found. Continuing without categories.")

    # 3. Functions + 4. Operators & Loops
    def calculate_statistics(self):
        self.total = 0
        count = 0

        self.minimum = self.data[0]
        self.maximum = self.data[0]

        for value in self.data:
            self.total += value           # Total
            count += 1                    # Count for average

            if value < self.minimum:      # Minimum
                self.minimum = value
            if value > self.maximum:      # Maximum
                self.maximum = value

        self.average = self.total / count

    # 5. Conditional Statements + Display
    def display_results(self):
        print("\n--- Dataset Statistics ---")
        print("Total:", self.total)
        print("Average:", self.average)
        print("Minimum:", self.minimum)
        print("Maximum:", self.maximum)

        threshold = 50
        if self.average > threshold:
            print("Performance: High Performance")
        else:
            print("Performance: Needs Improvement")

        print("\nUnique Categories:", self.categories)
        print("Number of Unique Categories:", len(self.categories))

    # 8. Saving Results (File Handling)
    def save_report(self, report_file):
        with open(report_file, 'w') as file:
            file.write("Dataset Analysis Report\n")
            file.write("------------------------\n")
            file.write(f"Total: {self.total}\n")
            file.write(f"Average: {self.average}\n")
            file.write(f"Minimum: {self.minimum}\n")
            file.write(f"Maximum: {self.maximum}\n")

            if self.average > 50:
                file.write("Performance: High Performance\n")
            else:
                file.write("Performance: Needs Improvement\n")

            file.write("\nUnique Categories:\n")
            for category in self.categories:
                file.write(f"- {category}\n")

            file.write(f"\nTotal Unique Categories: {len(self.categories)}\n")


# 7. Object Creation and Execution
dataset = DataSet("numbers.csv", "categories.txt")
dataset.load_data()
dataset.calculate_statistics()
dataset.display_results()
dataset.save_report("report.txt")
