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
