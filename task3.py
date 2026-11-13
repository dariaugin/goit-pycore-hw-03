import re
def normalize_phone(phone_number):
    """Normalize a phone number to the format +380XXXXXXXXX.

    Removes all non-digit characters, then adds the missing country code:
    '+' if the number starts with 380, '+38' otherwise.
    """
    
    phone_number = re.sub(r"\D","", phone_number.strip())

    if phone_number.startswith("380"): 
        new_phone_number = "+" + phone_number
    else:
        new_phone_number = "+38" + phone_number
    
    return new_phone_number

    
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "+380+8989\+676+81",
    "3803456++32+145+",
    "38078787"
]

if __name__ == "__main__":
    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


