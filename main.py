daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysOfMonthsLeap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#sums all numbers in a list
def sum(nums):
    output = 0
    for num in nums:
        output += num
    return output

#retruns true if a given year y is leap, else returns false 

isLeap = lambda y: y % 4 is 0

#Counts the number of leap years until given year y
def leapUntil(y):
    if isLeap(y):
        return y//4
    else:
        return y//4 + 1

#converts a date to the number of days passed from 1st Jan 0 to that date
def dateToDays(d, m, y):
    if(m > 12 or d > 31):
        return
    else:
        if isLeap(y):
            days_in_that_year = sum(daysOfMonthsLeap[:m-1]) + d #counts the number of days just in the given year
            days_wo_leap = 365*(y-1) + days_in_that_year
            days = days_wo_leap + leapUntil(y)
            return days
        else:
            days_in_that_year = sum(daysOfMonths[:m-1]) + d #counts the number of days just in the given year
            days_wo_leap = 365*(y-1) + days_in_that_year
            days = days_wo_leap + leapUntil(y)
            return days

def differnece(d1, m1, y1, d2, m2, y2):
    return abs(dateToDays(d1, m1, y1) - dateToDays(d2, m2, y2))

print(differnece(9, 11, 2047, 2, 2, 1923))