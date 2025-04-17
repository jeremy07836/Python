input_filename = 'country_info.txt'
countries = {}

with open(input_filename) as country_file:
    print(country_file.readline())
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(data)
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict
        # code_lookup[code.casefold()] = country
        countries[code.casefold()] = country_dict

# print(countries)
# name, capital, country_code, cc3, dcode, timezone, curr
for key, country in countries.items():
    # to skip the
    if len(key) == 2:
        continue
    if country['capital'] == '':
        print(f"{key} has no capital")
        print(f"\tCountry code: {country['country_code']}")
        for field, value in country.items():
            if value == '':
                print(f"\t{field} is blank")

while True:
    chosen_country = input('Please enter the name of a country: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {country_data['name']} is {country_data['capital']}")
    elif chosen_country == 'exit' or chosen_country == 'quit':
        break
    else:
        print("Invalid country, please enter a country")
