import requests
import re
from bs4 import BeautifulSoup
import mysql.connector
wanted_car = input("دنبال چه ماشینی میگردی؟\n")
ans_cars,finally_cars,ans_cars_model,ans_cars_work,ans_cars_price,answer,search_time,car_repeat = [],[],[],[],[],[],0,0
string_url = "https://bama.ir/car/all-brands/all-models/all-trims?page="
while car_repeat<20 :
    search_time +=1
    print("page {0}".format(search_time))
    r = requests.get(string_url+ str(search_time))
    soup = BeautifulSoup(r.text,'html.parser')
    all_cars_model = soup.find_all("h2",attrs={"class":"persianOrder","itemprop":"name"})
    all_cars_work  = soup.find_all("p" ,attrs={"class":"price hidden-xs"})
    all_cars_price = soup.find_all("p" ,attrs={"class":"cost"})
    for i in range(len(all_cars_model)):
        model,work,price = all_cars_model[i],all_cars_work [i],all_cars_price[i]
        model=re.sub(r"\s+","", model.text)
        work=re.sub(r"\s+","", work.text)
        price=re.sub(r"\s+","", price.text)
        if model.find(wanted_car)!= -1 and len(answer)<20:
            answer.append([model,work,price])
            car_repeat +=1
            print("item {0} found in page {1}".format(car_repeat,search_time))
mydb = mysql.connector.connect(host="127.0.0.1",user="root",password="")
cur= mydb.cursor()
cur.execute("CREATE DATABASE sample")
made_db = mysql.connector.connect(host="127.0.0.1",user="root",password="",database="sample")
cur1= made_db.cursor()
cur1.execute("CREATE TABLE car (model varchar(255),work varchar(255),price varchar(255))")
for item in answer:
    model,work,price =item[0],item[1],item[2]
    print("{0}\n{1}\n{2}\\n\n\n".format(model,work,price))
    sql = "INSERT INTO car (model, work,price) VALUES (%s, %s,%s)"
    val = (model,work,price)
    cur1.execute(sql, val)
    made_db.commit()
made_db.close()
