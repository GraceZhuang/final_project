from bs4 import BeautifulSoup
import urllib


# This program gets url links of restaurants, restaurants names, and neighborhoods of restaurants in 42 neighborhoods in Manhattan

restfile = open("restaurants_links.csv", "w")

neighborhood = ["Alphabet_City","Battery_Park","Central_Park", "Chelsea","Chinatown","Civic_Center","East_Harlem",
                "East_Village","Financial_District","Flatiron","Gramercy","Greenwich_Village","Harlem",
                "Hell%27s_Kitchen","Inwood","Kips_Bay,Koreatown","Little_Italy","Lower_East_Side",'Manhattan_Valley'
                'Marble_Hill','Meatpacking_District','Midtown_East','Midtown_West','Morningside_Heights','Murray_Hill'
                'NoHo','Nolita','Roosevelt_Island','SoHo','South_Street_Seaport','South_Village','Stuyvesant_Town',
                'Theater_District','TriBeCa','Two_Bridges','Union_Square','Upper_East_Side','Upper_West_Side'
                'Washington_Heights','West_Village','Yorkville']


for nbhd in neighborhood:

    url_link_per_neighborhood = 'http://www.yelp.com/search?find_desc=Restaurants&find_loc=Manhattan,+NY&start=0&l=p:NY:New_York:Manhattan:' + nbhd
    source_code_per_nbhd = urllib.urlopen(url_link_per_neighborhood).read()
    soup_per_nbhd = BeautifulSoup(source_code_per_nbhd, "html.parser")

    page_count = soup_per_nbhd.find("div",class_="page-of-pages arrange_unit arrange_unit--fill")
    page_str = page_count.get_text(",",strip = True)
    lastpage = int(page_str.split(" ")[-1])

    page = 0
    while page < lastpage:
        pagelink = 'http://www.yelp.com/search?find_desc=Restaurants&find_loc=Manhattan,+NY&start=' + str(page*10)+ '&l=p:NY:New_York:Manhattan:' + nbhd
        source_code_per_page = urllib.urlopen(pagelink).read()
        soup_per_page = BeautifulSoup(source_code_per_page, "html.parser")

        restaurant_all_source = soup_per_page.find_all("h3", class_="search-result-title")
        neighborhood_all = soup_per_page.find_all("span", class_="neighborhood-str-list")
        restaurant_name = []
        restaurant_all_info = {}
        prefix = "http://www.yelp.com"

        for i in range(1,11):

            element = restaurant_all_source[i]
            restaurant_name = (element.a.get_text())
            restaurant_url = prefix + element.a["href"]

            if( i < len(neighborhood_all)+1):
                neighbor = neighborhood_all[i-1].get_text(strip=True)
                if(restaurant_all_info.has_key(neighbor)):
                    restaurant_all_info[neighbor].append(1)

                else:
                    restaurant_all_info[neighbor] = []
                    restaurant_all_info[neighbor].append(1)

                if(len(restaurant_all_info[neighbor]) <= 20):
                    restfile.write(restaurant_name.encode('utf-8') + ",")
                    restfile.write(restaurant_url.encode('utf8') + ",")
                    restfile.write(neighbor.encode('utf8') + "\n")

        page = page+1