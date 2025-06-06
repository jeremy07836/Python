import csv

input_filename = 'country_info.txt'

dialect = csv.excel
dialect.delimiter = '|'

countries = {}


with open(input_filename, encoding='utf-8', newline='') as country_file:
    # Get the column headings from the first line of the file
    headings = country_file.readline().strip("\n").split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()
    # print(headings)

    dict_reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headings)
    for row in dict_reader:
        # print(row)
        countries[row['country'].casefold()] = row
        countries[row['cc'].casefold()] = row

# print(countries)
# name, capital, country_code, cc3, dcode, timezone, curr
for key, country in countries.items():
    # to skip the
    if len(key) == 2:
        continue
    if country['capital'] == '':
        print(f"{key} has no capital")
        print(f"\tCountry code: {country['cc']}")
        for field, value in country.items():
            if value == '':
                print(f"\t{field} is blank")

while True:
    chosen_country = input('Please enter the name of a country: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {country_data['country']} is {country_data['capital']}")
    elif chosen_country == 'exit' or chosen_country == 'quit':
        break
    else:
        print("Invalid country, please enter a country")
