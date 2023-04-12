def phone_directory(phone_number):
    country_code = phone_number[0:2]
    area_code = phone_number[2:5]
    prefix = phone_number[5:8]
    line_number = phone_number[8:]

    print(f"Phone directory for {phone_number}:")
    print(f"1. +{country_code} ({area_code}) {prefix}-{line_number}")
    print(f"2. +{country_code} ({area_code}) {prefix}-{line_number}")
    print(f"3. +{country_code} ({area_code}) {prefix}-{line_number}")
    print(f"4. +{country_code} ({area_code}) {prefix}-{line_number}")
    print(f"5. +{country_code} ({area_code}) {prefix}-{line_number}")

phone_number = input("Enter a phone number: ")
phone_directory(phone_number)