#Authors: Lanyu Shang; Minqing Zhuang; Xing Cui
#GS-DS-1007 Final Project
#Fall 2015
#Instructor: Gregory R Watson

import pandas as pd


class Neighborhood:
    def __init__(self):
        self.nbhd_map = dict()
        # neighborhoods are divided into ten large neighborhoods that each one contains few neighborhoods.
        self.nbhd_category = {'a': 'Central Harlem', 'b': 'Chelsea and Midtown West', 'c': 'East Harlem',
                              'd': 'Gramercy Park and Murray Hill', 'e': 'Greenwich Village and SoHo',
                              'f': 'Lower Manhattan', 'g': 'Lower East Side', 'h': 'Upper East Side',
                              'i': 'Upper West Side', 'j': 'Inwood and Washington Heights'}
        self.set_nbhd_map()

    def set_nbhd_map(self):
        self.nbhd_map['Central Harlem']                  = ['Harlem']
        self.nbhd_map['Chelsea and Midtown West']        = ['Chelsea', 'Meatpacking District', 'Hells Kitchen',
                                                            'Koreatown', 'Midtown West', 'Theater District',
                                                            'Union Square']
        self.nbhd_map['East Harlem']                     = ['East Harlem']
        self.nbhd_map['Gramercy Park and Murray Hill']   = ['Flatiron', 'Gramercy', 'Kips Bay', 'Midtown East',
                                                            'Murray Hill']
        self.nbhd_map['Greenwich Village and SoHo']      = ['Greenwich Village', 'Little Italy', 'Noho', 'Nolita',
                                                            'Soho', 'Tribeca', 'West Village']
        self.nbhd_map['Lower Manhattan']                 = ['Battery Park', 'Financial District',
                                                            'South Street Seaport', 'South Village']
        self.nbhd_map['Lower East Side']                 = ['Alphabet City', 'Civic Center', 'Chinatown',
                                                            'East Village', 'Lower East Side',
                                                            'Stuyvesant Town', 'Two Bridges']
        self.nbhd_map['Upper East Side']                 = ['Upper East Side', 'Yorkville']
        self.nbhd_map['Upper West Side']                 = ['Manhattan Valley', 'Morningside Heights',
                                                            'Upper West Side']
        self.nbhd_map['Inwood and Washington Heights']   = ['Inwood', 'Marble Hill', 'Washington Heights']


class Cuisine:
    def __init__(self):
        self.cuisine_map = dict()
        # cuisine categories are ranked by origin first and then business type.
        self.cuisine_category = {'a':'African', 'b':'EastAsian', 'c':'SouthAsian', 'd':'LatinAmerican',
                                 'e':'NorthAmerican', 'f':'European', 'g':'MiddleEastern', 'h':'Cafes',
                                 'i':'Bars', 'j':'Vegan', 'k':'OtherBusiness'}
        self.set_cuisine_map()

    def set_cuisine_map(self):
        self.cuisine_map['African']       = ['Moroccan', 'African', 'South African', 'Ethiopian', 'Senegalese',
                                            'Egyptian']
        self.cuisine_map['EastAsian']     = ['Asian Fusion', 'Cantonese', 'Chinese', 'Dim Sum', 'Japanese', 'Korean',
                                            'Ramen', 'Shanghainese', 'Singaporean', 'Himalayan/Nepalese', 'Hot Pot',
                                            'Sushi Bars', 'Szechuan', 'Taiwanese', 'Teppanyaki']
        self.cuisine_map['SouthAsian']    = ['Bangladeshi', 'Filipino', 'Himalayan Nepalese', 'Indian', 'Pakistani',
                                            'Sri Lankan', 'Indonesian', 'Malaysian', 'Thai', 'Vietnamese', 'Cambodian']
        self.cuisine_map['LatinAmerican'] = ['Brazilian', 'Argentine', 'Caribbean', 'Colombian', 'Cuban', 'Dominican',
                                            'Latin American', 'Mexican', 'Peruvian', 'Puerto Rican', 'Salvadoran',
                                            'Venezuelan', 'Tex Mex', 'Trinidadian', ]
        self.cuisine_map['NorthAmerican'] = ['American New', 'American Traditional', 'Armenian',
                                            'Haitian', 'Hawaiian', 'Southern', 'Soul Food', 'Steakhouses', 'Hot Dogs']
        self.cuisine_map['European']      = ['Greek', 'Mediterranean', 'Portuguese', 'British', 'Belgian', 'Australian',
                                            'Austrian', 'French', 'German', 'Irish', 'Italian', 'Iberian', 'Czech',
                                            'Modern European', 'Polish', 'Scandinavian', 'Spanish', 'Tapas Small Plates',
                                            'Russian', 'Kosher', 'Ukrainian']
        self.cuisine_map['MiddleEastern'] = ['Arabian', 'Afghan', 'Falafel', 'Middle Eastern', 'Turkish',
                                             'Persian Iranian', 'Lebanese']
        self.cuisine_map['Cafes']         = ['Cafes', 'Bakeries', 'Bubble Tea', 'Cafeteria', 'Candy Stores',
                                            'Coffee Tea','Creperies', 'Desserts', 'Donuts', 'Gelato',
                                            'Internet Cafes', 'Ice Cream Frozen Yogurt','Juice Bars Smoothies',
                                            'Tea Rooms', 'Chocolatiers Shops']
        self.cuisine_map['Bars']          = ['Cocktail Bars', 'Bars', 'Champagne Bars', 'Irish Pub', 'Beer',
                                            'Beer Gardens', 'Breweries', 'Wine Bars', 'Music Venues', 'Lounges',
                                             'Jazz Blues', 'Pubs', 'Nightlife', 'Sports Bars', 'Hookah Bars',
                                             'Pool Halls', 'Dive Bars', 'Tapas Bars', 'Wine Spirits']
        self.cuisine_map['Vegan']         = ['Vegetarian', 'Vegan']
        self.cuisine_map['OtherBusiness'] = ['Delis', 'Food Stands', 'Halal', 'Food Court', 'Gastropubs', 'Pizza',
                                             'Bagels', 'Breakfast Brunch', 'Cheesesteaks', 'Burgers', 'Chicken Wings',
                                             'Barbeque', 'Soup', 'Sandwiches', 'Salad', 'Seafood Markets',
                                             'Live/Raw Food', 'Seafood', 'Fish Chips']


class LoadData:
    """
    This Class is going to import data into a pandas DataFrame.
    Then CLEAN data by get hundreds different cuisines into certain bigger categories.
    The same method is used to clean neighborhood.
    ADD two new columns into origin DataFrame, which would help to make comparison later.
    """
    def __init__(self):
        print 'Welcome! Please wait while loading data...'
        self.df = pd.read_csv('data_Yelp.csv', sep=',', skipinitialspace=True, encoding='utf8', engine='python')
        self.cuisine = Cuisine()
        self.nbhd = Neighborhood()
        self.clean_data()
        self.add_cuisine_category()
        self.add_nbhd_category()
        print '\nData loaded.'


    def clean_data(self):
        self.replace_space_in_colnames()
        col_fill_no = ['Accepts_Bitcoin', 'Accepts_Credit_Cards', 'Alcohol', 'Best_Nights', 'Bike_Parking', 'Caters',
                       'Coat_Check', 'Delivery', 'Dogs_Allowed', 'Drive-Thru', 'Good_For_Dancing',
                       'Good_for_Groups', 'Good_for_Kids', 'Good_for_Working', 'Happy_Hour', 'Has_Pool_Table', 'Has_TV',
                       'Music', 'Outdoor_Seating', 'Smoking', 'Take-out', 'Takes_Reservations', 'Waiter_Service',
                       'Wheelchair_Accessible', 'Wi-Fi']
        for i in col_fill_no:
            self.df[i] = self.df[i].fillna('No')

        self.df.Ambience = self.df.Ambience.fillna('Casual')
        self.df.Attire = self.df.Attire.fillna('Casual')
        self.df.Noise_Level = self.df.Noise_Level.fillna('Average')
        self.df.Parking = self.df.Parking.fillna('Street')
        self.df.Rating = self.df.Rating.fillna(0.0)
        self.df = self.df.dropna(subset=['Cuisine'])
        self.df = self.df.dropna(subset=['Neighborhood1'])

    def replace_space_in_colnames(self):
        col_names = []
        for i in list(self.df.columns.values):
            col_names.append(i.replace(' ', '_'))
        self.df.columns = col_names

    def add_cuisine_category(self):
        """ This function will classify cuisine into 12 major categories. """
        self.categorize_cuisine()
        self.remove_uncategorized_cuisine()

    def remove_uncategorized_cuisine(self):
        self.df = self.df.dropna(subset=['Cuisine_Category'])

    def categorize_cuisine(self):
        cuisine_categories = self.cuisine.cuisine_category.values()
        for i in self.df.Cuisine:
            cuisine = i.split(';')
            cuisine_map_index = []
            for j in cuisine:
                for key, value in self.cuisine.cuisine_map.iteritems():
                    if j in value:
                        cuisine_map_index.append(cuisine_categories.index(key))
                        break
            if len(cuisine_map_index) > 0:
                # consider cuisine origin first
                # if not available, substitute with business type
                self.df.loc[self.df.Cuisine == i, 'Cuisine_Category'] = cuisine_categories[min(cuisine_map_index)]
            else:
                self.df.loc[self.df.Cuisine == i, 'Cuisine_Category'] = None

    def add_nbhd_category(self):
        """ This function is going to separate 42 neighborhoods into 10 groups."""
        for i in self.df.Neighborhood1:
            for key, value in self.nbhd.nbhd_map.iteritems():
                if i in value:
                    self.df.loc[self.df.Neighborhood1 == i, 'Neighborhood_Category'] = key
                    break

    def get_data(self):
        return self.df[['Review_Counts','Rating','Alcohol','Caters','Delivery','Good_for_Groups','Good_for_Kids',
                        'Good_for_Working','Happy_Hour','Outdoor_Seating','Takes_Reservations', 'Waiter_Service',
                        'Price_range', 'Neighborhood1','Neighborhood_Category', 'Cuisine_Category','Cuisine']]














