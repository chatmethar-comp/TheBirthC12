# birth of c12
import csv
import datetime
# csv file (database)

# collect date from databases
with open('Birthday.csv','r') as birth:
    rawData = []
    birth.readline()
    birth.readline()
    header = ['name','day','month','year']
    reader = csv.DictReader(birth, fieldnames=header)
    for row in reader:
        rawData.append(row)

# check that member whether is in C1 room 2
def isInC12(name:str):
    name = name.capitalize()
    try:
        next(person for person in rawData if person["name"] == name)
        return True
    except:
        return False

# input some age ; return who has that age
def whoOld(age:int):
    result = []
    for person in rawData:
        birthDate = datetime.datetime(int(person["year"]), int(person["month"]), int(person["day"]))
        if birthDate > datetime.datetime.now():
            checkYear = datetime.datetime.now().year - age
        else:
            checkYear = datetime.datetime.now().year - age- 1
        if int(person["year"]) == checkYear:
            result.append(person["name"])
    return result

# duration from now to his coming birthbay 
def countdowntobirth(name:str):
    name = name.capitalize()
    if isInC12(name):
        person = next(person for person in rawData if person["name"] == name)
        birth = datetime.datetime(int(person["year"]), int(person["month"]), int(person["day"]))
        now = datetime.datetime.now()
        now = int(now.strftime("%j"))
        birth = int(birth.strftime("%j"))
        if birth >= now:
            return birth-now
        else:
            return 365+birth-now

# the nearest coming birthday in C1 room 2
def nearestBirthDay():
    people = [person["name"] for person in rawData]
    duration = float('inf')
    for person in people:
        if countdowntobirth(person) < duration:
            result = person
        duration = min(countdowntobirth(person), duration)
    return result


def whoBornIn(day=-1, weekday=-1, month=-1, year=-1):
    weekdayFormat = {
        "Mon" : 0,
        "Tue" : 1,
        "Wed" : 2,
        "Thu" : 3,
        "Fri" : 4,
        "Sat" : 5,
        "Sun" : 6
    }
    monthFormat = {
        "Jan" : 1,
        "Feb" : 2,
        "Mar" : 3,
        "Apr" : 4,
        "May" : 5,
        "Jun" : 6,
        "Jul" : 7,
        "Aug" : 8,
        "Sep" : 9,
        "Oct" : 10,
        "Nov" : 11,
        "Dec" : 12
    }
    if type(weekday) == str:
        weekday = weekday.capitalize()
        weekday = weekdayFormat[weekday]
    if type(month) == str:
        month = month.capitalize()
        month = monthFormat[month]
    dayList = -1
    weekdayList = -1
    monthList = -1
    yearList = -1
    if day != -1:
        dayList = [person["name"] for person in rawData if int(person["day"]) == day]
    if weekday != -1:
        weekdayList = [person["name"] for person in rawData if datetime.datetime(int(person["year"]), int(person["month"]), int(person["day"])).weekday() == weekday]
    if month != -1:
        monthList = [person["name"] for person in rawData if int(person["month"]) == month]
    if year != -1:
        yearList = [person["name"] for person in rawData if int(person["year"]) == year]
    Set = [item for item in (dayList,weekdayList,monthList,yearList) if item != -1]
    def sameElement(list1, list2):
        result = []
        for item in list1:
            if item in list2:
                result.append(item)
        return result

    if len(Set) == 1:
        return Set[0]
    elif len(Set) == 2:
        return sameElement(Set[0], Set[1])
    elif len(Set) == 3:
        return sameElement(Set[0], sameElement(Set[1], Set[2]))
    elif len(Set) == 4:
        return sameElement(sameElement(Set[0],Set[1]), sameElement(Set[2], Set[3]))

def timeLived(name:str):
    name = name.capitalize()
    for person in rawData:
        if name==person["name"]:
            actual = datetime.datetime.now() - datetime.datetime(int(person["year"]), int(person["month"]), int(person["day"]))
            daylived=actual.days
    return daylived

def checkDate(days:int):
    for person in rawData:
        day_check = timeLived((person["name"]))
        if days == day_check:
            return person["name"]

def theOldest():
    list_day=[]
    for person in rawData:
        day=timeLived(person["name"])
        list_day.append(day)
        list_day.sort()
    return checkDate(list_day[-1])

def theYoungest():
    list_day = []
    for person in rawData:
        day = timeLived(person["name"])
        list_day.append(day)
        list_day.sort()
    return checkDate(list_day[0])

def isZodiac(name:str):
    name = name.capitalize()
    for person in rawData:
        if name==person["name"]:
            day=int(person["day"])
            month=int(person["month"])
            if month==1:
                if day>=15: return "Capicorn"
                else: return "Sagittarius"
            if month==2:
                if day>13: return "Aquarius"
                else: return "Capicorn"
            if month==3:
                if day>=15: return "Pisces"
                else: return "Aquarius"
            if month==4:
                if day>=13: return "Aries"
                else: return "Pisces"
            if month==5:
                if day>=15: return "Taurus"
                else: return "Aries"
            if month==6:
                if day>=15: return "Gemini"
                else: return "Taurus"
            if month==7:
                if day>=15: return "Cancer"
                else: return "Gemini"
            if month==8:
                if day>=16: return "Leo"
                else: return "Cancer"
            if month==9:
                if day>=17: return "Virgo"
                else: return "Leo"
            if month==10:
                if day>=17: return "Libra"
                else: return "Virgo"
            if month==11:
                if day>=16: return "Scorpio"
                else: return "Libra"
            if month==12:
                if day>=16: return "Sagittarius"
                else: return "Scorpio"

def whoInZodiac(zodiac:str):
    zodiac = zodiac.capitalize()
    result = []
    for person in rawData:
        if isZodiac(person["name"]) == zodiac:
            result.append(person["name"])
    return result

# ราศีมังกร ARIES
# ราศีกุมภ์ TAURUS)
# ราศีมีน PISCES
# ราศีเมษ AQUARIUS
# ราศีพฤษภ CAPRICORN
# ราศีเมถุน GEMINI
# ราศีกรกฎ CANCER
# ราศีสิงห์ LEO
# ราศีกันย์ VIRGO
# ราศีตุลย์ LIBRA
# ราศีพิจิก SCORPIO
# ราศีธนู SAGITTARIUS