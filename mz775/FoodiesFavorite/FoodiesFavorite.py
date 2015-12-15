#Authors: Lanyu Shang; Minqing Zhuang; Xing Cui
#GS-DS-1007 Final Project
#Fall 2015
#Instructor: Gregory R Watson

import sys
from LoadData import LoadData
from UserChoice import UserChoice
from MapVisualization import Html
from PlotVisualization import *


def main():
    """
    This is the main program of the project. It calls all functions to get the result and shows it to the user.
    """
    try:
        yelp = LoadData()
        user = UserChoice()
        choice = user.get_user_input()
        plots = PlotVisualization(yelp.get_data())
        h = Html()
        # Output result to html
        if choice == 'quit':
            print "Quitting..."
            pass
        elif choice == "overview":
            plots.plot_overview()
            print "Overview only."
            h.output_to_file(False)
        else:
            plots.plot_search_results(choice)
            print 'Your choice of restaurants received.'
            h.output_to_file(True)

    except ValueError:
        print "Found value error."
        sys.exit()
    except KeyboardInterrupt:
        print "Interrupted!"
        sys.exit()
    except MemoryError:
        print "Memory Error"
        sys.exit()



if __name__ =='__main__':
    main()
