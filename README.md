# About The Project
Teaming up with <a href="https://unitedwaytopeka.org/">United Way</a>, a group and I where asked a question: In areas with higher median household income, will there be more
food resources available in that area than areas with lower median income?
<br>
To answer this question, our group decided to collect data from the Google Places API and from the Census Bureau. After collecting the data we would create a <a href="https://public.tableau.com/profile/adipersio#!/vizhome/TopekaFoodResouces/Dashboard?publish=yes">Tableau page</a> to visulize what we had collected and show our findings to <a href="https://unitedwaytopeka.org/">United Way</a>. Lastly, our group wanted to make a machine learning model for the data to test the inital question. 
<br>
<h2>Gathering the Data</h2>
To pull the data from the Google Places API, our group decided to do a nearbysearch and pass the API some coordinates and a radius of 1 mile. The coordinates would be updated for every call made to the API to move it over all of Topeka, gathering specific types of places (ie. Bakeries). To get what Census Tract each location fell into, we used <a href="https://pypi.org/project/censusgeocode/">censusgeocode</a>, "light weight Python wrapper for the US Census Geocoder API." 
<br>
For the Census Data, we went straight to the source,<a href="https://www.census.gov/acs/www/data/data-tables-and-tools/data-profiles/"> The American Community Survey</a>.

<h1>Built With</h1>
<h3>Python and Tableau</h3>
 pandas, censusgeocode, Machine Learing
 
 <h1>Contributers</h1>
 <ul>
 <li>
  <a href="https://github.com/adipersio">Adipersio</a>
  </li>
  <li>
  <a href="https://github.com/benanza">Benanza</a>
  </li>
  <li>
  <a href="https://github.com/markmessick">MarkMessick</a>
  </li>
  <li>
  <a href="https://github.com/Zachary-R-Wilson">Zachary-R-Wilson</a>
  </li>
 </ul>  

