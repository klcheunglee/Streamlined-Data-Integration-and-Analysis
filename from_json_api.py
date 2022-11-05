# use requests.get() to query the Yelp Business Search API for cafes in New York City.
# extract the data from the response with its json() method, and pass it to pandas's DataFrame() function to make a dataframe.
# The Yelp documentation is here: https://www.yelp.com/developers/documentation/v3/authentication
# The categories attribute in the Yelp API response contains lists of objects.
# To flatten this data, I employ json_normalize() arguments to specify the path to categories and pick other attributes to include in the dataframe.
# I also change the separator to facilitate column selection and prefix the other attributes to prevent column name collisions.
# APIs often limit the amount of data returned, since sending large datasets can be time- and resource-intensive. The Yelp Business Search API limits the results returned in a call to 50 records. However, the offset parameter lets a user retrieve results starting after a specified number. By modifying the offset, I get results 1-50 in one call and 51-100 in another to append the dataframes.



import requests
# Load json_normalize()
from pandas.io.json import json_normalize

api_url = "https://api.yelp.com/v3/businesses/search"

# Create dictionary to query API for cafes in NYC
params = {"term": "cafe",
          "location": "NYC"}

# Create dictionary that passes Authorization and key string
headers = {"Authorization": "Bearer {}".format(api_key)}

# Query the Yelp API with headers and params set
response = requests.get(api_url, headers=headers, params=params)

# Extract JSON data from response
data = response.json()

# Load other business attributes and set meta prefix
cafes = json_normalize(data["businesses"],
                       sep='_')
print(cafes.head())

flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                            record_path="categories",
                            meta=['name',
                                  'alias',
                                  'rating',
                                  ['coordinates', 'latitude'],
                                  ['coordinates', 'longitude']],
                            meta_prefix="biz_")

# Add an offset parameter to get cafes 51-100
params = {"term": "cafe",
          "location": "NYC",
          "sort_by": "rating",
          "limit": 50,
          "offset": 50}

result = requests.get(api_url, headers=headers, params=params)
next_50_cafes = json_normalize(result.json()["businesses"])
# Built a dataset of the top 100 cafes in New York City according to Yelp.
# Append the results, setting ignore_index to renumber rows
cafes = top_50_cafes.append(next_50_cafes, ignore_index=True)

# Print shape of cafes
print(cafes.shape)

#  Combine that with demographic data to investigate which neighborhood has the most good cafes per capita.

# Merge crosswalk into cafes on their zip code fields
cafes_with_pumas = cafes.merge(crosswalk, left_on="location_zip_code", right_on="zipcode")

# Merge pop_data into cafes_with_pumas on puma field
cafes_with_pop = cafes_with_pumas.merge(pop_data, on="puma")

# View the data
print(cafes_with_pop.head())
