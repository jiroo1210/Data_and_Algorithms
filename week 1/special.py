def check_year(year:int):
    # returns true if sum(first half + 2nd half)**2 == year
    return (year//100 + year % 100)**2 == year
""" model solution:
def check_year(year):
    left = int(str(year)[:2])
    right = int(str(year)[-2:])
    return (left + right) ** 2 == year
"""
if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False