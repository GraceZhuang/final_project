#Authors: Lanyu Shang; Minqing Zhuang; Xing Cui
#GS-DS-1007 Final Project
#Fall 2015
#Instructor: Gregory R Watson


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class PlotVisualization:
    """
    This class generates plots for different neighborhoods and cuisines depending on users' choices.
    """
    def __init__(self, data):
        """ receive data frame and user choices"""
        self.df = data
        self.user_choice = dict()
        # two dictionaries used for renaming xticks labels of graphs
        # because some original names are too long to be displayed fully in graphs
        self.xticks_nbhd_names = {'Central Harlem': 'Ctl. Harlem',
                                  'Chelsea and Midtown West': 'Midtown W.',
                                  'Gramercy Park and Murray Hill': 'Gramercy',
                                  'East Harlem': 'E. Harlem',
                                  'Greenwich Village and SoHo': 'SoHo',
                                  'Lower Manhattan': 'Lo. MHTN',
                                  'Lower East Side': 'LES',
                                  'Upper East Side': 'UES',
                                  'Upper West Side': 'UWS',
                                  'Inwood and Washington Heights': 'Inwood'}
        self.xticks_feature_names = {'Good_for_Groups': 'Groups',
                                     'Good_for_Kids': 'Kids',
                                     'Good_for_Working': 'Working',
                                     'Happy_Hour': 'H.H.',
                                     'Outdoor_Seating': 'Outdoor',
                                     'Takes_Reservations': 'RESV',
                                     'Waiter_Service': 'Waiter'}

    def plot_overview(self):
        self.plot_total_by_nbhd()
        self.plot_total_by_cuisine()

    def plot_search_results(self, user_choice):
        self.user_choice = user_choice
        self.plot_overview()
        self.plot_num_of_restaurants_in_nbhds_given_cuisine()
        self.plot_num_of_restaurants_in_cuisine_category_given_nbhd_category()
        self.plot_features_of_cuisine_category()
        self.plot_features_of_nbhd_category()
        self.plot_review_of_cuisine_category()
        self.plot_rating_of_cuisine_category()

    def plot_total_by_nbhd(self):
        """ This function plots a histogram with neighborhoods as x-axis and the number of restaurant in each neighborhood as y-axis"""
        data = self.df['Neighborhood_Category']
        data_to_plot = data.value_counts().T
        plt.figure()
        cm = plt.get_cmap('RdYlBu_r')
        colors = [cm(x) for x in [0.167, 0.333, 0.5, 0.666, 0.833, 1]]
        data_to_plot.plot(kind='bar',stacked=True,color=colors)
        # change xtick labels using self defined function since original labels are too long
        labels = self.change_xticklabels(plt.gca().get_xticklabels())
        plt.gca().set_xticklabels(labels, size=9, rotation=45)
        plt.ylim(0,data_to_plot.max()+100)
        plt.ylabel('The Number of Restaurants',fontsize=14)
        plt.title('Distribution of Restaurant across all Neighborhood Category')
        plt.savefig('total_by_nbhd.jpg', format='jpg')

    def plot_total_by_cuisine(self):
        """ This function plots a histogram with cuisines as x-axis and the number of restaurant in each cuisine as y-axis """
        data = self.df['Cuisine_Category']
        data_to_plot = data.value_counts().T
        cm = plt.get_cmap('RdYlBu_r')
        colors = [cm(x) for x in [0.167, 0.333, 0.5, 0.666, 0.833, 1]]
        # change format of the plot so labels can be displayed fully
        plt.figure().autofmt_xdate()
        data_to_plot.plot(kind = 'bar',stacked=True,color=colors)
        plt.gca().set_xticklabels(data_to_plot.index, size=9, rotation=45)
        plt.ylim(0, data_to_plot.max()+100)
        plt.ylabel('The Number of Restaurants', fontsize=14)
        plt.title('Distribution of Restaurant across all Cuisine Category')
        plt.savefig('total_by_cuisine.jpg',format='jpg')

    def plot_num_of_restaurants_in_cuisine_category_given_nbhd_category(self):
        """ This function generates a histogram that depends on user's choice of cuisine
            with neighborhoods as x-axis and the number of restaurant in each neighborhood as y-axis
            so that the user can see distribution of the cuisine across different neighborhoods in Manhattan"""
        cuisine_Category = self.user_choice.get('Cuisine_Category')
        data = self.df[['Neighborhood_Category','Cuisine_Category','Price_range']]
        data_cuisine = data[data['Cuisine_Category']==cuisine_Category]
        data_count = data_cuisine.groupby(['Neighborhood_Category','Price_range']).size().unstack()
        # The following steps are for creating a new data frame for plotting
        # We want the stacked histogram to show color blocks in this order, ['Under $10', '$11-30 and Inexpensive','$31-60 and Moderate','Above $61 and Pricey']
        # Some cuisines might not have any restaurant belonging to the category 'Above $61 and Pricey'
        # So we create a new column filled with zeros and with the category name as column name. So we can arrange the order of color blocks and manage information in legend easily
        n = len(data_count.index)
        data_to_plot = {}
        for i in ['Under $10', '$11-30 and Inexpensive','$31-60 and Moderate','Above $61 and Pricey']:
            data_to_plot.setdefault(i,np.zeros(n))
            if i in data_count.columns:
                data_to_plot[i] = data_count[i]
        data_to_plot = pd.DataFrame(data_to_plot,index=data_count.index)
        # rearrange the order of columns
        data_to_plot = data_to_plot[['Under $10', '$11-30 and Inexpensive','$31-60 and Moderate','Above $61 and Pricey']]
        plt.figure()
        cm = plt.get_cmap('RdYlBu_r')
        colors = [cm(x) for x in [0.167, 0.333, 0.5, 0.666, 0.833, 1]]
        data_to_plot.plot(kind = 'bar',stacked=True,color=colors)
        labels = self.change_xticklabels(plt.gca().get_xticklabels())
        plt.gca().set_xticklabels(labels, size=9, rotation=45)
        plt.ylim(0,data_to_plot.max().sum()+data_to_plot.mean().mean())
        plt.ylabel('The Number of Restaurants',fontsize=14)
        plt.legend(loc=0, prop={'size':10})
        plt.title('Distribution of {}'.format(cuisine_Category))
        plt.savefig('num_of_restaurants_in_cuisines_given_nbhd.jpg',format='jpg')

    def plot_num_of_restaurants_in_nbhds_given_cuisine(self):
        """ This function generates a histogram that depends on user's choice of neighborhood
            with cuisine as x-axis and the number of restaurant in each cuisine as y-axis
            so that the user can see distribution of the cuisine in chosen neighborhood """
        nbhd_Category = self.user_choice.get('Neighborhood_Category')
        data = self.df[['Neighborhood_Category','Cuisine_Category','Price_range']]
        data_cuisine = data[data['Neighborhood_Category']==nbhd_Category]
        data_count = data_cuisine.groupby(['Cuisine_Category','Price_range']).size().unstack()
        # again we want to rearrange the order of color blocks
        n = len(data_count.index)
        data_to_plot = {}
        for i in ['Under $10', '$11-30 and Inexpensive','$31-60 and Moderate','Above $61 and Pricey']:
            data_to_plot.setdefault(i,np.zeros(n))
            if i in data_count.columns:
                data_to_plot[i] = data_count[i]
        data_to_plot = pd.DataFrame(data_to_plot,index=data_count.index)
        data_to_plot = data_to_plot[['Under $10', '$11-30 and Inexpensive','$31-60 and Moderate','Above $61 and Pricey']]
        cm = plt.get_cmap('RdYlBu_r')
        colors = [cm(x) for x in [0.167, 0.333, 0.5, 0.666, 0.833, 1]]
        plt.figure()
        data_to_plot.plot(kind = 'bar',stacked=True,color=colors)
        plt.gca().set_xticklabels(data_to_plot.index, size=9, rotation=45)
        plt.ylim(0,data_to_plot.max().sum()+data_to_plot.mean().mean())
        plt.ylabel('The Number of Restaurants',fontsize=14)
        plt.legend(loc=0,prop={'size':10})
        plt.title('Distribution of {}'.format(nbhd_Category))
        plt.savefig('num_of_restaurants_in_nbhds_given_cuisine.jpg',format='jpg')

    def plot_features_of_cuisine_category(self):
        """ This function generates plot that shows percentage of restaurants in chosen cuisine with certain features """
        cuisineC = self.user_choice.get('Cuisine_Category')
        feature_list = ['Cuisine_Category','Alcohol','Caters','Delivery','Good_for_Groups','Good_for_Kids','Good_for_Working','Happy_Hour','Outdoor_Seating','Takes_Reservations', 'Waiter_Service']
        df = self.df[feature_list]
        data = df[df['Cuisine_Category'] == cuisineC]
        data.drop('Cuisine_Category',1)
        data_count = pd.DataFrame(data.apply(pd.Series.value_counts))
        data_percentage = data_count.apply(lambda x: x/float(x.sum())).T
        data_percentage = data_percentage.drop('No',1)
        data_percentage = data_percentage.drop('Cuisine_Category',0)
        data_percentage = data_percentage.drop(cuisineC,1)
        cm = plt.get_cmap('RdYlBu_r')
        colors = [cm(x) for x in [0.167, 0.333, 0.5, 0.666, 0.833, 1]]
        plt.figure()
        data_percentage.plot(kind='bar',stacked=True,color=colors)
        labels = self.change_xticklabels(plt.gca().get_xticklabels())
        plt.gca().set_xticklabels(labels, size=9, rotation=45)
        plt.ylim(0,1)
        plt.ylabel('The Percentage of Restaurants with the Features', fontsize=13)
        plt.legend(loc=0, prop={'size': 10})
        plt.title('Restaurant Features in {}(100% in Total)'.format(cuisineC))
        plt.savefig('features_of_cuisine.jpg',format='jpg')

    def plot_features_of_nbhd_category(self):
        """ This function generates plot that shows percentage of restaurants in chosen neighborhood with certain features """
        nbhdC = self.user_choice.get('Neighborhood_Category')
        feature_list = ['Neighborhood_Category','Alcohol','Caters','Delivery','Good_for_Groups','Good_for_Kids','Good_for_Working','Happy_Hour','Outdoor_Seating','Takes_Reservations', 'Waiter_Service']
        df = self.df[feature_list]
        data = df[df['Neighborhood_Category'] == nbhdC]
        data.drop('Neighborhood_Category',1)
        data_count = pd.DataFrame(data.apply(pd.Series.value_counts))
        data_percentage = data_count.apply(lambda x: x/float(x.sum())).T
        data_percentage = data_percentage.drop('No',1)
        data_percentage = data_percentage.drop('Neighborhood_Category',0)
        data_percentage = data_percentage.drop(nbhdC,1)
        cm = plt.get_cmap('RdYlBu_r')
        colors = [cm(x) for x in [0.167, 0.333, 0.5, 0.666, 0.833, 1]]
        plt.figure()
        data_percentage.plot(kind='bar',stacked=True,color=colors)
        labels = self.change_xticklabels(plt.gca().get_xticklabels())
        plt.gca().set_xticklabels(labels, size=9, rotation=45)
        plt.ylim(0,1)
        plt.ylabel('The Percentage of Restaurants with the Features',fontsize=13)
        plt.legend(loc=0,prop={'size':10})
        plt.title('Restaurant Features in {}(100% in Total)'.format(nbhdC))
        plt.savefig('features_of_nbhd.jpg',format='jpg')

    def plot_review_of_cuisine_category(self):
        """ This function generates a plot that shows the number of reviews of chosen cuisine across neighborhoods in Manhattan """
        cuisineC = self.user_choice.get('Cuisine_Category')
        df = self.df[['Review_Counts','Cuisine_Category','Neighborhood_Category']]
        data = df[df['Cuisine_Category'] == cuisineC]
        plt.figure()
        data.boxplot('Review_Counts', by='Neighborhood_Category')
        labels = self.change_xticklabels(plt.gca().get_xticklabels())
        plt.gca().set_xticklabels(labels, size=9, rotation=45)
        plt.ylim(-50,2500)
        plt.ylabel('Number of Reviews', fontsize=13)
        plt.title('Review Counts in {}'.format(cuisineC))
        plt.suptitle('')
        plt.savefig('reviews_of_cuisine.jpg',format='jpg')

    def plot_rating_of_cuisine_category(self):
        """ This function generates a plot that shows rating of chosen cuisine across neighborhoods in Manhattan """
        cuisineC = self.user_choice.get('Cuisine_Category')
        df = self.df[['Rating','Cuisine_Category','Neighborhood_Category']]
        data = df[df['Cuisine_Category']==cuisineC]
        plt.figure()
        data.boxplot('Rating', by='Neighborhood_Category')
        labels = self.change_xticklabels(plt.gca().get_xticklabels())
        plt.gca().set_xticklabels(labels, size=9, rotation=45)
        plt.ylim(0, 6)
        plt.ylabel('Rating', fontsize=13)
        plt.title('Rating in {}'.format(cuisineC))
        plt.suptitle('')
        plt.savefig('ratings_of_cuisine.jpg',format='jpg')

    def change_xticklabels(self, xticklabels):
        """ This function converts original xticks labels to shorter version using dictionaries defined before """
        labels = [item.get_text() for item in xticklabels]
        for i in labels:
            if i in self.xticks_nbhd_names.keys():
                labels[labels.index(i)] = self.xticks_nbhd_names[i]
            elif i in self.xticks_feature_names.keys():
                labels[labels.index(i)] = self.xticks_feature_names[i]
        return labels