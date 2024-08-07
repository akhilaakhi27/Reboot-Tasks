def list_manipulation():
    numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    largest = max(numbers)
    smallest = min(numbers)
    average = sum(numbers) / len(numbers)
    
    print(f"Largest number: {largest}")
    print(f"Smallest number: {smallest}")
    print(f"Average: {average}")
list_manipulation()