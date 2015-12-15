#Authors: Lanyu Shang; Minqing Zhuang; Xing Cui
#GS-DS-1007 Final Project
#Fall 2015
#Instructor: Gregory R Watson


import json
import webbrowser
import os
import sys




class GeoJson:
    """This class will generate an interactive map with 10 colored neighborhoods. """
    def __init__(self):
        #coordinates are predetermined using Google GeoJson
        self.coordinates = json.load(open('geojson.json'))
        self.nbhds = ["Greenwich Village and Soho", "Lower Manhattan", "Lower East Side", "Lower East Side",
                      "Gramercy Park and Murray Hill", "Upper East Side", "Upper West Side", "East Harlem",
                      "Inwood and Washington Heights", "Central Harlem"]
        self.colors = ["darkorange", "gold", "maroon", "red", "darkviolet", "cornflowerblue", "orange",
                       "lightseagreen", "green", "yellowgreen"]
        self.properties = []

    def setup_properties(self):
        """Set up properties for each neighborhood. """
        for i in zip(self.nbhds, self.colors):
            prop = dict.fromkeys(['nbhd', 'color'])
            prop['nbhd'] = i[0]
            prop['color'] = i[1]
            self.properties.append(prop)

    def insert_properties(self):
        """Insert properties dictionary to coordinates."""
        for i in range(10):
            self.coordinates['features'][i]['properties'] = self.properties[i]

    def output_to_js(self):
        """Output geojson to a javascript file"""
        try:
            with open('nbhds.js', 'w') as f:
                f.write('var data = ')
                json.dump(self.coordinates, f, sort_keys = True, indent = 4, ensure_ascii=False)
        except IOError:
            print "Cannot export .json to .js file."

    def to_js(self):
        """Add properties to geojson and output to javascript file."""
        self.setup_properties()
        self.insert_properties()
        self.output_to_js()


class Html:
    def __init__(self):
        self.head = """
            <!DOCTYPE html>
            <html>
              <head>
                <title>DSGA1007 Final Project</title>
                <meta name="viewport" content="initial-scale=1.0">
                <meta charset="utf-8">
                <style>
                  html, body {
                    height: 100%;
                    margin: 0;
                    padding: 0;
                  }
                  #map_container {
                    float: left;
                    width: 400px;
                    height: 900px;
                    position: relative;
                    left: 50px;
                  }
                  #map {
                    width: 400px;
                    height: 840px;
                  }
                  #info-box {
                    background-color: white;
                    border: 1px solid black;
                    bottom: 0px;
                    height: 15px;
                    padding: 3px;
                    position: absolute;
                    left: 0px;
                    z-index: 3;
                  }
                  #over-view{
                    float: right;
                    width: 500px;
                    margin-right: 50px;
                    margin-left: 500px;
                    position: absolute;
                  }
                  #wrap{
                     width:1100px;
                     margin: auto;
                  }
                  #image_row{
                    width:1200px;
                    margin: auto;
                    white-space: nowrap;
                  }
                </style>
                <script src="https://maps.googleapis.com/maps/api/js?v=3.exp"></script>
                <script src="nbhds.js"></script>
              </head>"""
        self.body_overview = """
              <body>
                <h1 align="center">Manhattan Restaurants Overview</h1>
                <div id="wrap">
                  <div id="map_container">
                    <h3 align="center">Google Map View</h3>
                    <div id="map"></div>
                    <div id="info-box">Neighborhood Information</div></div>
                  <div id ="over-view">
                    <img src="total_by_nbhd.jpg"
                    alt="Number of Restaurants in Each Neighborhood" width="600" height="450">
                    <img src="total_by_cuisine.jpg"
                    alt="Number of Restaurants of Each Cuisine Category" width="600" height="450
                    "></div></div>
                <script>
                  var map;
                  function initMap() {
                    map = new google.maps.Map(document.getElementById('map'), {
                      zoom: 12,
                      center: {lat: 40.77, lng:  -73.96}
                    });
                    map.data.addGeoJson(data);
                    map.data.setStyle(function(feature) {
                      return ({
                      fillColor: feature.getProperty('color'),
                      strokeColor: feature.getProperty('color'),
                      strokeWeight: 2
                      });
                    });
                    map.data.addListener('mouseover', function(event) {
                      document.getElementById('info-box').textContent =
                      event.feature.getProperty('nbhd');
                    });
                    map.data.addListener('mouseover', function(event) {
                      map.data.revertStyle();
                      map.data.overrideStyle(event.feature, {strokeWeight: 3});
                    });
                    map.data.addListener('mouseout', function(event) {
                      map.data.revertStyle();
                    });
                  }
                </script>"""
        self.body_result = """
                <div style="clear: left;"><br></br><h1 align="center">Your Search Results</h1></div>
                <div id="image_row">
                  <img src="num_of_restaurants_in_nbhds_given_cuisine.jpg"
                    alt="Number of Restaurants in Each Neighborhood of Your Cuisine Choice" width="600" height="450
                    " style="margin:20px 0px">
                  <img src="num_of_restaurants_in_cuisines_given_nbhd.jpg"
                    alt="Number of Restaurants in Each Cuisine of Your Neighborhood Choice" width="600" height="450
                    " style="margin:20px 0px">
                </div>
                <div id="image_row">
                  <img src="features_of_cuisine.jpg"
                    alt="Restaurants Features of Your Cuisine Choice" width="600" height="450
                    " style="margin:20px 0px">
                  <img src="features_of_nbhd.jpg"
                    alt="Restaurants Features of Your Neighborhood Choice" width="600" height="450
                    " style="margin:20px 0px">
                </div>
                <div id="image_row">
                  <img src="reviews_of_cuisine.jpg"
                    alt="Restaurants Number of Reviews of Your Cuisine Choice" width="600" height="450
                    " style="margin:20px 0px">
                  <img src="ratings_of_cuisine.jpg"
                    alt="Restaurants Ratings of Your Neighborhood Choice" width="600" height="450
                    " style="margin:20px 0px">
                </div>
                """
        self.end = """
                <script async defer src=
                "https://maps.googleapis.com/maps/api/js?v=3.exp?key=AIzaSyCZCz-utwfBtcakJUvuiizR3Z2fpmlTUV4&callback=initMap">
                </script>
              </body>
            </html>"""

    def add_content(self, search_result):
        try:
            with open('results.html','w') as f:
                f.write(self.head)
                f.write(self.body_overview)
                if search_result:
                    f.write(self.body_result)
                f.write(self.end)
        except IOError:
            print "Cannot generate result to html file."

    def output_to_file(self, have_result=False):
        """Output program result to html file. """
        GeoJson().to_js()
        self.add_content(have_result)
        print "Your result has been saved as 'results.html'."
        open_html()


def open_html():
    try:
        i = raw_input("Enter 'Y' to see the result or anything else to exit. ")
        if i.lower() in ['y', 'yes']:
            webbrowser.open('file://' + os.path.realpath('results.html'))
        print 'Mission Accomplished!'
    except KeyboardInterrupt:
        print '\nInterrupted!'
        sys.exit()








