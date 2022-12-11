# Tamilnadu Agricultural Analysis
## Abstract
----------------
The goal for this project was to analyze the Tamilnadu agriculture data to figure out the factors that causes a high production rate. However, during our analysis of our features and target, we encountered a problem that no longer allowed us to continue further with our machine learning. 


## Main
-----------
### Data Structure
<img src="./images/null_amount.PNG" height="200" width="200">
In order to proceed with our data analysis, we first need to pre-process our data. The first steps we took in our pre-processing was to check the amount of null values in our data. We found out that the shape of our dataset was 13547 by 7 and that we have 281 null values for production. 


### Preprocessing 
<img src="./images/pre_processing_code.PNG">
To fix the issue of having the null values, we took the median of the production values and filled in the null values. However, for our "State_Name" column, it was decided that this information would not be of great use to us and decided to remove it. 

<img src="./images/fill_null.PNG" height="250" width="250">
As shown, the median of the production values, 841, was used to replace all of the null values in the dataset. 


### Analysis
<img src="./images/area_year.png" height="500" width="700"><img src="./images/tamilnadu_image.png" height="300" width="300">
<h4> - (M = million(1,000,000)) (x = year, y = average area)</h4>
As shown in the image, Tamilnadu is a state in the most southern part of India. This graph shows the relationship between the average area used for the production of crops and the year in which it was recorded. The graph presents a point of max of around 12M in the year of 1998 and a low of around 3M in 2012. 

<img src="./images/district_year.png" height="500" width="700">
The districts of Tamilnadu that were used for the purpose of agriculture can be shown with the graph above. This graph depicts the accumulation of land that were used from the year of 1997 to 2013 with a high of 459,259M of land was used from in the district of Villupuram and a low of 5496M of land was used in the district of The Nilgiris. 
