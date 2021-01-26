# January 2021 - Data Gathering Lab Project
Creators - Maxim Matyash 318828761 | Avi Simkin 312485816

# Instructions:

In the Project folder open the app.ipynb notebook in databricks environment.
In the notebook you will see input boxes where you can enter you query. The Longitude and Latitude boxes define the center of
your search area and the Radius of Search defines its size (recommended to keep under 0.1).
After entering your query run the notebook, it may take a few minutes for it to finish.
The final cell should display a heatmap of your search area, however, if databricks fails to show it correctly here are altternative methods:
1) The heatmap will be saved as and html file at "/dbfs/FileStore/tables/output_map.html", you can download it there and view it through your browser.
2) A seperate python script is provided called visualize.py . You can download the table created in cell 16 as a csv to the same folder as this script.
Then run the script like so: python visualize.py <name of the downloaded csv file> <latitude> <longitude>
where latitude and longitude are the same as you provided in the query. The script will open a new window in your browser where you will see the heatmap.

For method (2) to work you need to have gmplot installed in your python environtment. If you don't have it, install it through the command line like so:
pip install gmplot 
(also appears in requirements.txt)

# More about our project:
For better visualizations see the .pptx file instead (this is a copy paste from it)

The Problem:

In many cases municipalities and companies would like to close a street, for example to do maintenance work or organize a street festival. One of the key issues of such events is their impact on the traffic flow in the city which the municipality will want to minimize in order to keep the city efficient.

The Solution:

We offer an API solution where our users can select an area and time window and we will provide them with a heatmap of average congestion probability in that area over the time window.
A data frame of relevant area IDs (approximate to streets) is generated for the relevant time window, both of which we get from a user query, and the areas within the search zone are ranked based on the probability of congestion and distance from the center of the search area.

Methodology:

We use a simple Neural network that uses geographical, and time features along with the number of traffic lights which we added from an external dataset. The model is constantly updated from an incoming data stream, and the latest model is loaded for a given query.

Limitations:

 – Area IDs are only an approximation of streets and sometimes aggregate multiple streets. Some users may want to go even finer and predict congestion on parts of streets.
 – The results are ranked by their average probability of congestion which may be problematic for long time windows.​
 – There aren’t a lot of features for the model yet, and most of the bus data becomes obsolete.
 
 Further explanations on methodology:
 
 The query consists of year, month, day, hour, minute, duration, longitude and latitude of the center of the search area and its radius.

Given the query, we generate a data frame of the centroids of areaIds in the search area for each hour of the duration. We then calculate the distance of each centroid to the center of the search area and normalize by the sum of those distances.
Afterwards, we compute the probability of not having congestion in each area using our model and multiply it by the normalize distance. 
Finally, we order the results in descending order.

A heatmap is built using the resulting scores via gmplot and is saved as an html file which can then be viewed.

We integrated weather data into our model and there was no missing data, also in such data outliers are very important and may be more helpful than unreliable, so unfortunately imputation was not necessary for our case. 








