"""
Project for Week 3 of "Python Data Visualization".
Unify data via common country name.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal

def reconcile_countries_by_name(plot_countries, gdp_countries):
    """
    Inputs:
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country names used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country names from
      gdp_countries The set contains the country codes from
      plot_countries that were not found in gdp_countries.
    """
    dic = {}
    sets = set()
    for keys in plot_countries:
        for key in gdp_countries:
            if plot_countries[keys] == key:
                dic[keys] = key
    for keys in plot_countries:
        if keys not in dic.keys():
            sets.add(keys)
    return dic, sets


def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    dic = {}
    code = set()
    values = set()
    fileinput = {}
    with open(gdpinfo["gdpfile"], newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=gdpinfo["separator"],quotechar=gdpinfo["quote"])
        for row in reader:
            fileinput[row[gdpinfo["country_name"]]] = row
            
    for country in plot_countries:
        if plot_countries[country] in fileinput:
            if year in fileinput[plot_countries[country]]:
                if fileinput[plot_countries[country]][year] != '':
                    dic[country] = math.log10(float(fileinput[plot_countries[country]][year]))
                else:
                    values.add(country)
        else:
            code.add(country)
    return dic, code, values


def render_world_map(gdpinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for
      map_file       - Name of output file to create

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data for the given year and
      writes it to a file named by map_file.
    """
    dic, code, values = build_map_dict_by_name(gdpinfo, plot_countries, year)
    chart = pygal.maps.world.World()
    chart.title = "GDP datas {}".format(year)
    chart.add('GDP for {}'.format(year), dic)
    chart.add('Missing from World Bank Data', code)
    chart.add('No GDP data', values)
    chart.render_in_browser()


def test_render_world_map():
    """
    Test the project code for several years.
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, pygal_countries, "1960", "isp_gdp_world_name_1960.svg")

    # 1980
    render_world_map(gdpinfo, pygal_countries, "1980", "isp_gdp_world_name_1980.svg")

    # 2000
    render_world_map(gdpinfo, pygal_countries, "2000", "isp_gdp_world_name_2000.svg")

    # 2010
    render_world_map(gdpinfo, pygal_countries, "2010", "isp_gdp_world_name_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

 #test_render_world_map()
