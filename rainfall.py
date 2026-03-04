# Author: Kael
# Date: March 2026
# Program Title: Rainfall Statistics

def main():
    rainfall = []

    print("Enter the total rainfall for each of the 12 months:")

    for month in range(1, 13):
        while True:
            try:
                amount = float(input(f"Month {month}: "))
                rainfall.append(amount)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    total_rainfall = sum(rainfall)
    average_rainfall = total_rainfall / 12
    highest = max(rainfall)
    lowest = min(rainfall)

    print("\n--- Rainfall Report ---")
    print(f"Total rainfall: {total_rainfall}")
    print(f"Average monthly rainfall: {average_rainfall}")
    print(f"Highest rainfall: {highest} (Month {rainfall.index(highest) + 1})")
    print(f"Lowest rainfall: {lowest} (Month {rainfall.index(lowest) + 1})")

main()
