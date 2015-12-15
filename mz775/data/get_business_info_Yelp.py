#Authors: Lanyu Shang; Minqing Zhuang; Xing Cui
#GS-DS-1007 Final Project
#Fall 2015
#Instructor: Gregory R Watson


"""This program is extracting data directly from website resourses.
    We are using BeautifulSoup to do this.
    After finishing writing this program, we kept saveral lines of code that were 
    used to check if the program ran correctly.
"""

from bs4 import BeautifulSoup
import urllib
import collections

featurefile = open("data_Yelp.csv","w")

business_info_key = ["Restaurant name","Price range","Today","Takes Reservations","Delivery","Take-out","Accepts Credit Cards",
                 "Good For","Parking","Bike Parking","Good for Kids","Good for Groups","Attire","Ambience",
                 "Noise Level","Music","Good For Dancing","Alcohol","Happy Hour","Best Nights","Coat Check",
                 "Smoking","Outdoor Seating","Wi-Fi","Has TV","Waiter Service","Caters","Has Pool Table",
                 "Wheelchair Accessible","Dogs Allowed","Accepts Bitcoin","Drive-Thru","Good for Working",
                 "By Appointment Only","Cuisine","Review Counts","Rating","Hours Mon","Hours Tue","Hours Wed",
                 "Hours Thu","Hours Fri","Hours Sat","Hours Sun"]

business_info_map = dict.fromkeys(business_info_key)
order_map = collections.OrderedDict(sorted(business_info_map.items()))


for key in range(len(order_map.keys())):
    featurefile.write(order_map.keys()[key].encode('utf8') + ",")
featurefile.write("\n")

with open("link_Yelp.csv") as f:
    for line in f:
        business_info_map["Restaurant name"] = line.split(",")[0]
        newlink = urllib.urlopen(line.split(",")[1]).read()
        soup_part = BeautifulSoup(newlink, "html.parser")


        rest_hour_and_price = soup_part.find_all("dl",class_="short-def-list")

        if(len(rest_hour_and_price) == 2):
            price = rest_hour_and_price[1].get_text(",",strip = True)
            price_str = price.split(",")
            #print price_str[0]
            business_info_map[price_str[0]] = price_str[1]

            #add price
            hour = rest_hour_and_price[0].get_text(",",strip = True)
            hour_str = hour.split(",")
            print hour_str,len(hour_str), price_str,len(price_str)
            if(len(hour_str) <= 3):
                open_hour = hour_str[1]
            else:
                open_hour = hour_str[1]+ '-' + hour_str[3]
            business_info_map[hour_str[0]] = open_hour
        #getting hours
        elif(len(rest_hour_and_price) == 1):
            hp = rest_hour_and_price[0].get_text(",",strip = True)
            hp_str = hp.split(",")
            #print hp_str
            if(hp_str[0] == "Today"):
                hp_hour = hp_str[1]+ '-' + hp_str[3]
                business_info_map[hp_str[0]] = hp_hour
            else:
                business_info_map[hp_str[0]] = hp_str[1]



        #print buss_info_map["Today"],buss_info_map["Price range"]

        try:
            business_info = soup_part.find_all("div",class_="short-def-list")[0]
            info_separate =  business_info.find_all("dl")
            #len(info_separate) = 23 17 18 19 18
            for j in range(len(info_separate)):
                info_pair_str = info_separate[j].get_text(",",strip = True)
                info_str = info_pair_str.split(",")

                if(business_info_map.has_key(info_str[0])):
                    business_info_map[info_str[0]] = info_str[1]
                else:
                    print business_info_map, " ", info_str[0]
        except:
            pass

        #category
        try:
            cuisine_category = soup_part.find_all("span", class_="category-str-list")[0]
            categories = cuisine_category.get_text(strip = True)
            categories = categories.replace(',', ';')
            business_info_map['Cuisine'] = categories
        except:
            business_info_map['Cuisine'] = "None"


        #review_counts
        try:
            review_counts = soup_part.find_all("span", class_="review-count rating-qualifier")[0]
            review_count = review_counts.get_text(' ', strip = True)
            business_info_map['Review Counts'] = review_count
        except IndexError:
            business_info_map['Review Counts'] = 0
            pass


        #Hours
        table = soup_part.find('table', {'class': 'table table-simple hours-table'})
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for day in days:
            try:
                th = table.find('th', text=day)
                td = th.findNext('td')
                business_info_map['Hours '+day] = td.get_text(strip = True)
            except:
                business_info_map['Hours '+day] = "None"

        #rating
        rating = soup_part.find('meta', itemprop='ratingValue', content=True)
        try:
            business_info_map['Rating'] = rating['content']
        except:
            business_info_map['Rating'] = "None"


        ordermap = collections.OrderedDict(sorted(business_info_map.items()))
        for item in range(len(ordermap.values())):
            featurefile.write(str(ordermap.values()[item]) + ",")
        featurefile.write("\n")


