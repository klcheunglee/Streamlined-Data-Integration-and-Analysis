# Streamlined-Data-Ingestion-with-pandas-Projects

<h3> Extract, transform, load dataset from SQL</h3>
Assembling a dataset to investigate how the number of heating complaints to New York City's 311 line varies with temperature.
<br>In addition to the hpd311calls table, data.db has a weather table with daily high and low temperature readings for NYC. We want to get each day's count of heat/hot water calls with temperatures joined in. This can be done in one query, which we'll build in parts.

<h3> Extract, transform, load from API, json</h3>
Using requests.get() to query the Yelp Business Search API for cafes in New York City.
<br>Extracting the data from the response with its json() method, and pass it to pandas's DataFrame() function to make a dataframe.
<br>The Yelp documentation is here: https://www.yelp.com/developers/documentation/v3/authentication
<br>The categories attribute in the Yelp API response contains lists of objects.
<br>To flatten this data, I employ json_normalize() arguments to specify the path to categories and pick other attributes to include in the dataframe.
<br>I also change the separator to facilitate column selection and prefix the other attributes to prevent column name collisions.
<br>APIs often limit the amount of data returned, since sending large datasets can be time- and resource-intensive. The Yelp Business Search API limits the results returned in a call to 50 records. However, the offset parameter lets a user retrieve results starting after a specified number. By modifying the offset, I get results 1-50 in one call and 51-100 in another to append the dataframes.
