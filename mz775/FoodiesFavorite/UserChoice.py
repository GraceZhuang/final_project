#Authors: Lanyu Shang; Minqing Zhuang; Xing Cui
#GS-DS-1007 Final Project
#Fall 2015
#Instructor: Gregory R Watson

from LoadData import *


class UserChoice:

    """
    This class contains all process that asking user input of choosing cuisine category, cuisine, neighborhood category,
    and neighborhood.
    User could go back or exit follow the instruction.
    """
    def __init__(self):
        self.user_decision = {'Cuisine_Category': None, 'Cuisine': None,
                              'Neighborhood_Category': None, 'Neighborhood': None}
        self.cuisine = Cuisine()
        self.nbhd = Neighborhood()

    def get_user_input(self):
        while True:
            main_input = raw_input('\nPlease enter \'Y\'(Yes) to start a new business.'
                                   'Enter \'N\'(No) to see the overview of Manhattan.\n'
                                   'Type \'quit\' anytime to quit the program. ---->')

            if main_input.lower() == 'quit':
                return "quit"

            elif main_input.lower() in ['n','nope','no','nop']:
                return "overview"

            elif main_input.lower() in ['y','yes','yep','yeah']:
                cuisine_category_choice = self.select_cuisine_category()
                if cuisine_category_choice == 'quit':
                    return 'quit'
                elif cuisine_category_choice == 'back':
                    continue
                else:
                    cuisine_choice = self.select_cuisine()
                    if cuisine_choice == 'quit':
                        return 'quit'
                    elif cuisine_choice == 'back':
                        continue
                    else:
                        nbhd_category_choice = self.select_neighborhood_category()
                        if nbhd_category_choice == 'quit':
                            return 'quit'
                        elif nbhd_category_choice == 'back':
                            continue
                        else:
                            nbhd_choice = self.select_neighborhood()
                            if nbhd_choice == 'quit':
                                return 'quit'
                            elif nbhd_choice == 'back':
                                continue
                            else:
                                self.print_user_decision()
                                return self.user_decision

    def print_user_decision(self):
        """
        We are letting user know their final choice in text before let them understand in visualization.
        """
        print '\n\nAh, I see.\n\n' \
              'The major cuisine of the restaurant that you want to start with is ' \
              + self.user_decision['Cuisine']\
              + ' belongs to ' + self.user_decision['Cuisine_Category']+'!\n'
        print 'Your location preference is ' + self.user_decision['Neighborhood'] \
               + ' of ' + self.user_decision['Neighborhood_Category'] + ' in Manhattan.\n'

        print 'Let me help you with this.\n' \
              'I would give you a better location for your stomach.\n' \
              'Otherwise I have few recommendation of cuisine in your favorite neighborhood.\n' \
              'I only need a MOMENT.:P\n'

        print 'Calculating....\n'

    def select_cuisine_category(self):
        while True:
            choice = raw_input('\nHow would like to CHOOSE a cuisine category?\n'
                               'You can type \'back\' to go back.\n'
                               'A. African\n'
                               'B. EastAsian\n'
                               'C. SouthAsian\n'
                               'D. LatinAmerican\n'
                               'E. NorthAmerican\n'
                               'F. European\n'
                               'G. MiddleEastern\n'
                               'H. Cafes\n'
                               'I. Bars\n'
                               'J. Vegan\n'
                               'K. OtherBusiness\n'
                               '---->')
            choice = choice.lower().rstrip().lstrip()
            if choice == 'quit':
                return 'quit'
            elif choice == 'back':
                return 'back'
            elif choice in ['a','b','c','d','e','f','g','h','i','j','k']:
                self.user_decision['Cuisine_Category'] = self.cuisine.cuisine_category[choice]
                return 'selected'
            else:
                print 'Invalid Input. Please enter again.\n'

    def select_cuisine(self):
        while True:
            choice = raw_input('Please TYPE the name of a cuisine of the following opitions: \n' +
                               ',\n'.join(self.cuisine.cuisine_map[self.user_decision['Cuisine_Category']]) +
                               '\nYou can type \'back\' to go back. ---->')

            choice = ' '.join(choice.split()).lower()
            if choice == 'quit':
                return 'quit'
            elif choice == 'back':
                return 'back'
            elif choice.title() in self.cuisine.cuisine_map[self.user_decision['Cuisine_Category']]:
                self.user_decision['Cuisine'] = choice.title()
                return 'selected'
            else:
                print '**Invalid Input. Please enter again.**\n'

    def select_neighborhood_category(self):
        while True:
            choice = raw_input('Please CHOOSE a neighborhood within Manhattan '
                               'where you want to start your business\n'
                               'A. Central Harlem \n'
                               'B. Chelsea and Midtown West\n'
                               'C. East Harlem\n'
                               'D. Gramercy Park and Murray Hill\n'
                               'E. Greenwich Village and Soho\n'
                               'F. Lower Manhattan\n'
                               'G. Lower East Side\n'
                               'H. Upper East Side\n'
                               'I. Upper West Side\n'
                               'J. Inwood and Washington Heights\n'
                               '---->')
            choice = choice.lower().rstrip().lstrip()
            if choice == 'quit':
                return 'quit'
            elif choice == 'back':
                return 'back'
            elif choice in ['a','b','c','d','e','f','g','h','i','j']:
                self.user_decision['Neighborhood_Category'] = self.nbhd.nbhd_category[choice]
                return 'selected'
            else:
                print '**Invalid Input. Please enter again.**\n'

    def select_neighborhood(self):
        while True:
            choice = raw_input('Please TYPE the name of a specific area in the neighborhood you chose: \n' +
                               ',\n'.join(self.nbhd.nbhd_map[self.user_decision['Neighborhood_Category']]) +
                               '\nYou can type \'back\' to go back. ---->')
            choice = ' '.join(choice.split()).lower()
            if choice == 'quit':
                return 'quit'
            elif choice == 'back':
                return 'back'
            elif choice.title() in self.nbhd.nbhd_map[self.user_decision['Neighborhood_Category']]:
                self.user_decision['Neighborhood'] = choice.title()
                return 'selected'
            else:
                print '**Invalid Input. Please enter again.**\n'
