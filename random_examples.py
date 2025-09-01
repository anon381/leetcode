import random
import string
from datetime import datetime

def generate_random_string(length=10):
    """Generate a random string of specified length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def random_number_generator(min_val=1, max_val=100):
    """Generate random numbers within a range"""
    return random.randint(min_val, max_val)

def random_list_generator(size=5):
    """Generate a list of random numbers"""
    return [random.randint(1, 50) for _ in range(size)]

def random_color():
    """Generate a random color name"""
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'brown']
    return random.choice(colors)

def random_animal():
    """Generate a random animal name"""
    animals = ['cat', 'dog', 'elephant', 'lion', 'tiger', 'bear', 'rabbit', 'bird']
    return random.choice(animals)

def random_quote():
    """Generate a random inspirational quote"""
    quotes = [
        "The only way to do great work is to love what you do.",
        "Innovation distinguishes between a leader and a follower.",
        "Life is what happens to you while you're busy making other plans.",
        "The future belongs to those who believe in the beauty of their dreams.",
        "It is during our darkest moments that we must focus to see the light."
    ]
    return random.choice(quotes)

def main():
    """Main function to demonstrate random functions"""
    print("=== Random Python Examples ===")
    print(f"Random String: {generate_random_string()}")
    print(f"Random Number: {random_number_generator()}")
    print(f"Random List: {random_list_generator()}")
    print(f"Random Color: {random_color()}")
    print(f"Random Animal: {random_animal()}")
    print(f"Random Quote: {random_quote()}")
    print(f"Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Random matrix
    matrix_size = 3
    random_matrix = [[random.randint(1, 9) for _ in range(matrix_size)] for _ in range(matrix_size)]
    print(f"Random Matrix:")
    for row in random_matrix:
        print(f"  {row}")

if __name__ == "__main__":
    main()

