#1. Question
a = 16
a = a // 2
print(a**2)
a = a + 11
print(a+1)
a = a - 3
print(a)
# = 16

#  (ignore the "print". esos no te dicen el valor de a



#2. Question
print((3+10**2/2) or 70.0)
# 53.0



# 3. Question
import datetime
a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year
print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)

# a is 7
# b is 7
# c is 14
# d is abcabcabcabc



#4. Question
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False




#!!!!!5 question

#Write a function that finds all the occurrences of a certain pattern,
# that starts with “b” has unlimited number of letters and ends with “Bob”
# The function takes 1 parameter:
# the text to look into, and returns the number of matches


# 6. Question
# a list:
the_list = ["dog", "cat", "rabbit"]
print("Original list:", the_list)

# We modify the list
the_list[0] = "horse"
print("Modified list:", the_list)

#a string
the_string = "aránzazu"
print("Original string:", the_string)

# We modify the string
try:
    the_string[0] = 'A'
except TypeError as e:
    print("Error:", e)



# 7. Question
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
# continue here by removing the odd numbers from the list
# and replacing the even #s with their 2ble value
print("Original List:", random_numbers)
for i in range(len(random_numbers)):
    if random_numbers[i] % 2!= 0: #if this is an odd number
        random_numbers[i] = None
    else:
        random_numbers[i] *= 2 #2ble its value

random_numbers = [num for num in random_numbers if num is not None] # Take out None values (odd numbers = were set to = None)
print("Modified List:", random_numbers)



#8. Question
# Write a function that checks if the passed parameter is a valid URL or not.
# Please also explain your reasoning. Use only the concepts that we learned in class
import re
def match_url(url):
    pattern = r'^https?://.*$'
    return re.match(pattern, url) is not None

urls_example = [
    "http://www.example.com",
    "https://example.com",
    "fjsodtp://example.com",
    "htp://sub.example.com/page",
    "https://www.example.com/page?param=value"
]

for url in urls_example:
    print(f"{url}: {match_url(url)}")



#9. Question
# Given your birthday, in the format "DD-MM-YYYY",
# write a function that calculates how many days have passed since your birthday
# (without counting the days in your birth year and the current year, so just whole years).
def days_passed_since_birthday(birthday):
    day, month, year = map(int, birthday.split('-'))    #We take out day, month and year from the birthday string
    current_date = (1, 3, 2024)
    years_passed = current_date[2] - year - 1  # number of full years between current date and birthday
    total_days_passed = 365 * years_passed    #total days passed since birthday (excluding birth year and current year)
    leap_years = sum(1 for y in range(year + 1, current_date[2]) if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0)  #leap years, adjust it
    total_days_passed += leap_years
    #Assuming 30 days
    total_days_passed += (current_date[1] - 1) * 30 + day  #Add days passed in the current year from the start of the year to the birthday
    total_days_passed -= (12 - month) * 30 + (30 - day)  #Subtract days passed in the birth year from the birthday to the end of the year
    return total_days_passed
birthday = "05-06-2003"
print("Days passed since birthday:", days_passed_since_birthday(birthday))



#10. Question
# Github -->