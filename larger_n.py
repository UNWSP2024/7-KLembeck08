# Author: Kael
# Date: March 2026
# Program Title: Larger Than n Function

def larger_than_n(values, n):
    for num in values:
        if num > n:
            print(num)

def main():
    nums = [3, 10, 5, 22, 8, 1]
    n = int(input("Enter a number n: "))
    print(f"Numbers greater than {n}:")
    larger_than_n(nums, n)

main()
