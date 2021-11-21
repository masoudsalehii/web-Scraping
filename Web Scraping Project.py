import requests
from bs4 import BeautifulSoup
import re
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="P@ssw0rd",
  database="cars"
)

mycursor = mydb.cursor()
brand = input('Brand:').lower()
model = input('Model:').lower()
r = requests.get("https://www.truecar.com/used-cars-for-sale/listings/%s/%s/" %(brand, model))

#r = requests.get("https://www.truecar.com/used-cars-for-sale/listings/ford/escape/")
soup = BeautifulSoup(r.text, 'html.parser')

car_Name = soup.find_all("div", attrs={"data-test": "vehicleCardYearMakeModel"})


car_price = soup.find_all("div", attrs={"data-test": "vehicleCardPricingBlockPrice"})



car_Mileage = soup.find_all("div", attrs={"data-test": "vehicleMileage"})



for car in range(20):
  model= re.sub(r'\s+', ' ', car_Name[car].text)
  model = model.strip()
  price = re.sub(r'\s+', ' ', car_price[car].text)
  price = price.strip()
  Mileage = re.sub(r'\s+', ' ', car_Mileage[car].text)
  Mileage = Mileage.strip()
  sql = "INSERT INTO cars (cardetails, mileage, price) VALUES (%s, %s, %s)"
  val = (model, Mileage, price)
  mycursor.execute(sql, val)
  #print(model, price, Mileage,i)
  mydb.commit()
