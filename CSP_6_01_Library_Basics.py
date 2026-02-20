#Please modify the below functions so they fulfill the described process.
#You must use a function from analytics.py in each question to receive credit.
#There is no provided test file. You must make and submit one yourself. (check older test files for reference)

# Modify the below function such that it takes in a list of prices and returns that list with 15% added value
from analytics import get_average
from analytics import get_highest
from analytics import apply_markup
from analytics import clean_text
from analytics import filter_threshold
def process_expenses(rawPrices):
    for i in range(len[rawPrices]):
        rawPrices[i]=apply_markup(rawPrices[i],0.15)

    return rawPrices
    pass


# Modify the below function such that it asks the user for n scores and then returns the highest score and the average score of the list.
def analyze_scores(n):
    scorse=[]
    for i in range(n-1):
        score=input("Give me the score")
        scorse.append(score)
    highest=get_highest(scorse)
    average=get_average(scorse)
    return highest,average

    pass

# Modify the below function such that it takes in a list of strings and returns that list with all spaces removed
#and all letters lower case.
def sanitize_usernames(usernames):
    clean=clean_text(usernames)
    list=[]
    for names in clean:
        list.append(names.replace(" ",""))
    return list


    pass


# Modify the list such that it takes in a list as an argument and returns a version of the list with all values over 100.
def identify_outliers(numbers):
    numbers=filter_threshold(numbers,100)
    return numbers
    pass


# Modify the below function such that it takes in a list of items and asks the user for an item to search for.
#Sanitize the list to only be lower case worsd with no extra spaces
#Then return the location of the word using binary search if the list is in order and linear search if it is not.
#example items = ["  Apple", "Banana ", "  CHERRY  ", " date "]
def search_and_report(items,target):
    clean=clean_text(items)
    target=target.strip().lower()
    if clean==sorted(clean):
        left=0
        right=len(clean)-1
        while left<=right:
            mid=(left+right)//2
            if clean(mid)==target:
                return mid
            elif clean(mid)<target:
                left+=1
            else:
                right-=1
        return -1
    else:
        for i in range(len(clean)):
            if clean(i)==target:
                return i
        return -1
    pass
