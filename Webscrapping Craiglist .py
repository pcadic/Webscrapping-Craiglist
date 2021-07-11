import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

print("******************************************************")
print("1. READ 3 PAGES OF ROOM RENTAL : SEARCH WORD = BCIT   ")
print("******************************************************")

# Class Room
class Room:

    # Room Properties
    publishingDate = ""
    adTitle = ""
    price = 0

    # Room Constructor
    def __init__(self, publishingDate, adTitle, price):
        self.publishingDate = publishingDate
        self.adTitle = adTitle
        self.price = price

    # Print room properties
    def showDetail(self):
        print("========")
        print("Date:      " + self.publishingDate)
        print("Title:     " + self.adTitle)
        print("Price:     " + self.price)


# Function extractText: Extracts text from scraped content.
def extractText(data):
    text = data.get_attribute('innerHTML')
    soup = BeautifulSoup(text, features="lxml")
    content = soup.get_text()
    return content


# Open website with chrome driver
#PATH = "/Users/pm/Documents/ChromeDriver/chromedriver"
PATH = "C:\\TRASH\\chromedriver.exe"
URL = "https://vancouver.craigslist.org/d/housing/search/hhh"
browser = webdriver.Chrome(PATH)
browser.get(URL)

# Give the browser time to load all content.
WAIT = 5
time.sleep(WAIT)

# Search query
SEARCH_TERM = "bcit"
search = browser.find_element_by_css_selector("#query")
search.send_keys(SEARCH_TERM)

# Press search button
button = browser.find_element_by_css_selector(".searchbtn")
button.click()  # Click the button.
time.sleep(WAIT)

# Initialize a list of rooms
roomList = []

#For each web page
for i in range(0, 3):

    # content finding
    dateContents = browser.find_elements_by_css_selector(".result-date")
    titleContents = browser.find_elements_by_css_selector(".hdrlnk")
    priceContents = browser.find_elements_by_css_selector(".result-price")

    # Initialize lists for content parts
    dateList = []
    titleList = []
    priceList = []

    # For each content found
    for dt in range(0, len(dateContents)):

        # Extract text
        date = extractText(dateContents[dt])
        dateList.append(date)
        title = extractText(titleContents[dt])
        titleList.append(title)
        price = extractText(priceContents[dt])
        priceList.append(price)

        # *** Part d ***
        # Create a room object and append to the list
        newRoom = Room(date, title, price)
        roomList.append(newRoom)

    # Page i processed
    print("Page ", str(i + 1), " done")

    # Click on the button "next"
    if i <= 1:
        button = browser.find_element_by_css_selector(".next")
        button.click()  # Click the button.
        time.sleep(WAIT)


#Loop on all room objects in print them
print("\nPrint the listing:")
for room in roomList:
    room.showDetail()

# Declare empty dataframe and add data to it.
df = pd.DataFrame()
for r in range(0, len(roomList)):
    roomDictionary = {'publishingDate': roomList[r].publishingDate,
                      'adTitle': roomList[r].adTitle,
                      'price': roomList[r].price}
    df = df.append(roomDictionary, ignore_index=True)

#Write the dataframe content into a csv file
DRIVER_PATH = "C:\\TRASH\\"
CSV_FILE = 'RoomWebScrap.csv'
df.to_csv(DRIVER_PATH+ CSV_FILE, sep=',')

#Read the csf file to another dataframe
dfIn = pd.read_csv(DRIVER_PATH + CSV_FILE, skiprows=1, sep=',',names=( 'adTitle', 'price','publishingDate'))
print("\nPrint the first 2 lines:")
print(dfIn.head(2))
print("\nPrint the last 2 lines:")
print(dfIn.tail(2))
















