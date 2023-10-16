# Prompt the years and indicated chinese zodiac signs based on a 12-year cycle
rat_sign = (1924, 1936,1948, 1960, 1972, 1984, 1996, 2008, 2020)
ox_sign = (1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021)
tiger_sign = (1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022)
rabbit_sign = (1927, 1940, 1951, 1963, 1975, 1987,1999, 2011, 2023)
dragon_sign = (1928, 1941, 1952, 1964,1976,1988, 2000,2012, 2024)
snake_sign = (1929, 1942, 1952, 1965, 1977, 1989, 2001, 2013, 2025)
horse_sign = (1930, 1943, 1953, 1966, 1979, 1990, 2002, 2014, 2026)
goat_sign = (1931, 1944, 1954, 1967, 1980, 1991, 2003, 2015, 2027)
monkey_sign = (1932, 1945, 1955, 1968, 1981, 1992, 2004, 2016, 2028)
rooster_sign = (1933, 1946, 1956, 1969, 1982, 1993, 2005, 2017, 2029)
dog_sign = (1934, 1945, 1957, 1970, 1983, 1994, 2006, 2018, 2030)
pig_sign = (1935, 1946, 1958, 1971, 1984, 1995, 2007, 2019, 2031)

# Let the user use the input function to input their birth year
year = eval(input("What is your birth year?\n"))

# Make an If-else statement for each represented year
if year in rat_sign:
    print("Your Chinese Zodiac sign is Rat.")
elif year in ox_sign:
    print("Your Chinese Zodiac sign is Ox.")
elif year in tiger_sign:
    print("Your Chinese Zodiac sign is Tiger. ")
elif year in rabbit_sign:
    print("Your Chinese Zodiac sign is Rabbit. ")
elif year in dragon_sign:
    print("Your Chinese Zodiac sign is Dragon. ")
elif year in snake_sign:
    print("Your Chinese Zodiac sign is Snake. ")
elif year in horse_sign:
    print("Your Chinese Zodiac sign is Horse. ")
elif year in goat_sign:
    print("Your Chinese Zodiac sign is Goat. ")
elif year in monkey_sign:
    print("Your Chinese Zodiac sign is Monkey. ")
elif year in rooster_sign:
    print("Your Chinese Zodiac sign is Rooster. ")
elif year in dog_sign:
    print("Your Chinese Zodiac sign is Dog. ")
elif year in pig_sign:
    print("Your Chinese Zodiac sign is Pig. ")







