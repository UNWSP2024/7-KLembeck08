# Author: Kael
# Date: March 2026
# Program Title: US Population by Year

def main():
    data = []

    print("Enter population data. Type 'done' as the year to stop.")

    while True:
        year_input = input("Enter year: ")

        if year_input.lower() == "done":
            break

        try:
            year = int(year_input)
            state = input("Enter state name: ")
            population = int(input("Enter population: "))
            data.append([year, state, population])
        except ValueError:
            print("Invalid input. Try again.")

    year_to_sum = int(input("\nEnter a year to total population for: "))

    total = 0
    for entry in data:
        if entry[0] == year_to_sum:
            total += entry[2]

    print(f"\nTotal population for {year_to_sum}: {total}")

main()
