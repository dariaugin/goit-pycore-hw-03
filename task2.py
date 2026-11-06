import random


def get_numbers_ticket(min, max, quantity):
    """Return a sorted list of unique random numbers for a lottery ticket.
        Returns:
        A sorted list of (quantity) unique random numbers from min to max
        (both included) or an empty list if the parameters are invalid.
    """
    numbers_lst = []
    if 1 <= min <= max <= 1000 and  0 < quantity <= max-min+1:
        numbers_lst = sorted(random.sample(range(min, max + 1), quantity))
        
    return numbers_lst


if __name__ == "__main__":
    while True:
        min_val = input("Min value: ")
        max_val = input("Max Value: ")
        quantity = input("Quantity: ")

        if min_val.isdigit() and max_val.isdigit() and quantity.isdigit():
            random_nums = get_numbers_ticket(int(min_val), int(max_val), int(quantity))
            if random_nums:
                print("Your lottery numbers:", random_nums)
                break
            
        print("Enter valid parameters.")


