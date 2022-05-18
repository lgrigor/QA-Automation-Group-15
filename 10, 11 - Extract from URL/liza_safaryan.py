import re

"""Extracting the year, month, and date from the URL"""

url = r"washingtonpost.com/news/1735/1211/94/football-insider/wp/2016/9/2/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

date = re.search(r"(\d{4})/(\d{1,2})/(\d{1,2})", url) 

d = {"1": "հունվար", "2": "փետրվար", "3": "մարտ", "4": "ապրիլ", "5": "մայիս", "6": "հունիս", "7": "հուլիս", "8": "օգոստոս", "9": "սեպտեմբեր", "10": "հոկտեմբեր", "11": "նոյեմբեր", "12": "դեկտեմբեր"}
month = date.group(2)

print(date.group(3), d[month], date.group(1))