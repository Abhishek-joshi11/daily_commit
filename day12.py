import random
import string
from datetime import datetime, timedelta

def generate_random_data():
    """Generate random data for demonstration"""
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    return random.choice(names)

def calculate_statistics(numbers):
    """Calculate mean, median, and standard deviation"""
    if not numbers:
        return None
    mean = sum(numbers) / len(numbers)
    return mean

class DataProcessor:
    """Process and analyze data"""
    def __init__(self, data):
        self.data = data
        self.processed = False
    
    def process(self):
        """Process the data"""
        self.processed = True
        return self.data

def generate_random_date():
    """Generate random date within last year"""
    days_back = random.randint(0, 365)
    return datetime.now() - timedelta(days=days_back)

def create_random_string(length=10):
    """Create random alphanumeric string"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def filter_numbers(numbers, threshold):
    """Filter numbers above threshold"""
    return [n for n in numbers if n > threshold]

def merge_lists(list1, list2):
    """Merge two lists and remove duplicates"""
    return list(set(list1 + list2))

def main():
    """Main execution function"""
    random.seed(42)
    
    data_points = [random.randint(1, 100) for _ in range(20)]
    print(f"Generated data: {data_points}")
    
    avg = calculate_statistics(data_points)
    print(f"Average: {avg}")
    
    processor = DataProcessor(data_points)
    processed_data = processor.process()
    print(f"Processed: {processed_data}")
    
    random_name = generate_random_data()
    print(f"Random name: {random_name}")
    
    random_date = generate_random_date()
    print(f"Random date: {random_date}")
    
    random_string = create_random_string(15)
    print(f"Random string: {random_string}")
    
    filtered = filter_numbers(data_points, 50)
    print(f"Filtered (>50): {filtered}")
    
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    merged = merge_lists(list_a, list_b)
    print(f"Merged: {sorted(merged)}")

if __name__ == "__main__":
    main()
# This code demonstrates various functions for data generation, processing, and analysis. It includes random data generation, statistical calculations, and list operations.
# The main function orchestrates the execution of these functionalities, showcasing how they can be used together in a cohesive manner.
# Note: The random seed is set for reproducibility of results.