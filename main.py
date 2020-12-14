# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]
#print(str(deaths))

# write your update damages function here:
def damages_data(old_damages_list):
  new_damages_data = []
  for item in old_damages_list:
    if item == "Damages not recorded":
      new_damages_data.append("Damages not recorded")
    elif "M" in item:
      millions = item.split("M") 
      new_damages_data.append(float(millions[0]) * 1000000)
    elif "B" in item:
      billions = item.split("B")
      new_damages_data.append(float(billions[0]) * 1000000000)
  return new_damages_data

new_damages_data = damages_data(damages)  
#print(damages_data(damages))

# write your construct hurricane dictionary function here:
def combine_hurricane_info():
  hurricanes = {}
  for i in range(0, len(names)):
    hurricane_stuff = {}
    hurricane_stuff["Name"] = names[i]
    hurricane_stuff["Month"] = months[i]
    hurricane_stuff["Year"] = years[i]
    hurricane_stuff["Max Sustained Wind"] = max_sustained_winds[i]
    hurricane_stuff["Areas Affected"] = areas_affected[i]
    hurricane_stuff["Damages"] = new_damages_data[i]
    hurricane_stuff["Death"] = deaths[i]
    hurricanes[names[i]] = hurricane_stuff
  return hurricanes
#print(combine_hurricane_info())

# write your construct hurricane by year dictionary function here:
def hurricane_by_date():
  hurricane_by_date = {}
  hurricane_stuff = combine_hurricane_info()
  for key in hurricane_stuff:
    hurricane_data = hurricane_stuff.get(key)
    if hurricane_by_date.get(hurricane_data.get("Year")) == None:
      hurricane_by_date[hurricane_data["Year"]] = [hurricane_data] 
    else: 
      #print(hurricane_by_date.get("Year"))
      hurricane_by_date[hurricane_data["Year"]] = hurricane_by_date.get(hurricane_data.get("Year")) + [hurricane_data]
  return hurricane_by_date

#print(hurricane_by_date())



# write your count affected areas function here:
def count_area_affected():
  hurricane_count_by_area = {}
  for areas in areas_affected:
    for area in areas:
      if area in hurricane_count_by_area:
        number = hurricane_count_by_area.get(area)
        hurricane_count_by_area[area] = number + 1
      else:
        hurricane_count_by_area[area] = 1
  return hurricane_count_by_area
  
#print(count_area_affected())


# write your find most affected area function here:
def most_affected_area():
  most_hurricanes = ""
  hurricane_count_by_area = count_area_affected()
  for key in hurricane_count_by_area:
    if hurricane_count_by_area.get(key) > hurricane_count_by_area.get(most_hurricanes, 0):
      most_hurricanes = key 
  return most_hurricanes, hurricane_count_by_area.get(most_hurricanes)

highest = most_affected_area()

#print("{0} had the most hurricanes with {1}.".format(highest[0], highest[1]))

# write your greatest number of deaths function here:
def most_deaths():
  most_deaths = ""
  hurricane_stuff = combine_hurricane_info()
  for hurricane in hurricane_stuff:
    all_info = hurricane_stuff.get(hurricane)
    if all_info.get("Death") > hurricane_stuff.get(most_deaths, {}).get("Death", 0):
      most_deaths = all_info.get("Name")
  return most_deaths, hurricane_stuff.get(most_deaths).get("Death")

highest_deaths = most_deaths()

print("{0} had the most deaths with {1}.".format(highest_deaths[0], highest_deaths[1]))

# write your catgeorize by mortality function here:
def hurricane_rating():
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  hurricanes_by_ratings = {0:[], 1:[], 2:[], 3:[], 4:[]}
  hurricane_stuff = combine_hurricane_info()
  for hurricane in hurricane_stuff:
    all_info = hurricane_stuff.get(hurricane)
    death_toll = all_info.get("Death")
    for key in mortality_scale:
      if death_toll <= mortality_scale.get(key):
        hurricanes_by_ratings[key].append(all_info.get("Name")) 
        break
  return hurricanes_by_ratings

#print(hurricane_rating())

# write your greatest damage function here:
def most_costly():
  highest_cost = ""
  hurricane_stuff = combine_hurricane_info()
  for hurricane in hurricane_stuff:
    all_info = hurricane_stuff.get(hurricane)
    if all_info.get("Damages") == "Damages not recorded":
      continue
    elif all_info.get("Damages") > hurricane_stuff.get(highest_cost, {}).get("Damages", 0):
      highest_cost = all_info.get("Name")  
  return highest_cost, hurricane_stuff.get(highest_cost).get("Damages")

highest_cost = most_costly()

print("{0} had the most costly damages with {1}.".format(highest_cost[0], highest_cost[1]))

# write your catgeorize by damage function here:
def hurricane_damage_rating():
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  hurricanes_by_damages = {0:[], 1:[], 2:[], 3:[], 4:[]}
  hurricane_stuff = combine_hurricane_info()
  for hurricane in hurricane_stuff:
    all_info = hurricane_stuff.get(hurricane)
    damages = all_info.get("Damages")
    if damages == "Damages not recorded":
        hurricanes_by_damages[0].append(all_info.get("Name"))
        continue
    for key in damage_scale:
      if damages <= damage_scale.get(key):
        hurricanes_by_damages[key].append(all_info.get("Name")) 
        break
  return hurricanes_by_damages

print(hurricane_damage_rating())
