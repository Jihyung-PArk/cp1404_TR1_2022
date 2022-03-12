countries = ['China', 'India', 'United States', 'Indonesia', 'Pakistan']
populations = [1439323776, 1380004385, 331002651, 273523615, 220892340]
no_of_countries = len(countries)
first_letters = []

#display a menu of countries

for country in countries:
    print(country)
    first_letters.append(countries[0])


choice = input("Enter the first letter of country: ").upper()

print("Population of {} is {}".format(countries[first_letters.index(choice)], populations[first_letters.index(choice)]))

