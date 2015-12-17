#Authors: Lanyu Shang; Minqing Zhuang; Xing Cui
#GS-DS-1007 Final Project
#12/15/2015
#Instructor: Gregory R Watson


This is the instruction of our FINAL project for DS 1007, the Programming for Data Science.
Our project is going to let the user, who wants to open a restaurant with certain cuisine, know how other restaurants in this cuisine are.

1. Data is directly extracted from yelp.com by using BeautifulSoup within two separate python files. They are located in a folder named “Data" at the top level.
	a. "get_business_link_Yelp.py" is helping us to get all links of all restaurants in Manhattan, and it is formatted in a .csv file.
	b. "get_business_info_Yelp.py" is helping us to get all business information for all restaurant with orderred categories. Data is formatted into a .csv file as well, and the name of the file is data_Yelp.csv.

2. "main" fucntion and other functions including “UserChoice.py”, "MapVisualization.py”, and "PlotVisualization.py” in the “FoodiesFavorite” folder. There are comments inside those .py files, which explained their usage in details.

3. The user guide is going to explain as the following:

	A. $python FoodiesFavorite.py 			to run the main program.

	B. It will be loading data from data_Yelp.csv first.

	C. Once loading data is completed, the program will be asking user input.
		-Type "quit" will exit the program.
		-Type "n or no" will not make any cuisine or neighborhood choices and go to result to 	see the overview.
		-Type "y or yes" will let user to do the next choices.

	D. Next, the program will ask user to choice a cuisine category by enter the "letter" in front of the cuisine category name. Example: if user wants to choose "EastAsian", then enter "B" or "b" would complete this and go to next.

	E. Then the program is asking choose a specific cuisine within the category. This time, user has to enter the name of the cuisine. Example: if user wants to choose "ramen", then enter "ranmen" or "Ramen" or any upper case or lower case combination would complete this step and go to next.

	F. After finishing choosing cuisine, neighborhood decision is required. The process is similar to choose a cuisine category and a cuisine. By entering a letter option to record neighborhood category and type the name of specific neighborhood to complete. By the way, when choosing a specific neighborhood, any upper case and lower case combination of the name would do as long as the word is correct.

	G. Now our system has received user's decision and has started to compute the result and draw graph for the user. User needs to choose "y" to see the result open automatically, or the user could type anything else to quit. After quitting, user could open the result.html file manually.

	H. The graphs are in two types. First, the user would see the first part is the map of Manhattan that colored by neighborhood categories. The rest graphs are about distributions of the selected cuisine and neighborhood.

	I. Unittest
		$python test_LoadData.py   
		$python test_PlotVisualization.py	 
		or
		$python -m unittest discover




Example:
Welcome! Please wait while loading data...

Data loaded.

Please enter 'Y'(Yes) to start a new business.Enter 'N'(No) to see the overview of Manhattan.
Type 'quit' anytime to quit the program. ---->y

How would like to CHOOSE a cuisine category?
You can type 'back' to go back.
A. African
B. EastAsian
C. SouthAsian
D. LatinAmerican
E. NorthAmerican
F. European
G. MiddleEastern
H. Cafes
I. Bars
J. Vegan
K. OtherBusiness
---->b
Please TYPE the name of a cuisine of the following opitions: 
Asian Fusion,
Cantonese,
Chinese,
Dim Sum,
Japanese,
Korean,
Ramen,
Shanghainese,
Singaporean,
Himalayan/Nepalese,
Hot Pot,
Sushi Bars,
Szechuan,
Taiwanese,
Teppanyaki
You can type 'back' to go back. ---->ramen
Please CHOOSE a neighborhood within Manhattan where you want to start your business
A. Central Harlem 
B. Chelsea and Midtown West
C. East Harlem
D. Gramercy Park and Murray Hill
E. Greenwich Village and Soho
F. Lower Manhattan
G. Lower East Side
H. Upper East Side
I. Upper West Side
J. Inwood and Washington Heights
---->b
Please TYPE the name of a specific area in the neighborhood you chose: 
Chelsea,
Meatpacking District,
Hells Kitchen,
Koreatown,
Midtown West,
Theater District,
Union Square
You can type 'back' to go back. ---->chelsea


Ah, I see.

The major cuisine of the restaurant that you want to start with is Ramen belongs to EastAsian!

Your location preference is Chelsea of Chelsea and Midtown West in Manhattan.

Let me help you with this.
I would give you a better location for your stomach.
Otherwise I have few recommendation of cuisine in your favorite neighborhood.
I only need a MOMENT.:P

Calculating....

Your choice of restaurants received.
Your result has been saved as 'results.html'.
Enter 'Y' to see the result or anything else to exit. y
Mission Accomplished!




