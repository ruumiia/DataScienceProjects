<h1 id="fire-case"> Fire Case Reports </h1>

<h2> Business Problem / Problem Domain </h2>

The given data are records of fire cases reported in months of January, February, March, and April from year 2002 until 2009. 
It also includes the temperature recorded from each month when cases occurred and places where fire cases are happen.

<i>Strictly change the column names of the given data set.  Use “Year” for 0, “Month” for 1, “Temperature” for 2, “Place” for 3, and “Number” for 4.</i>

<hr>

Answer the following questions through EDA (Exploratory Data Analysis)

<ul>
    <li>Which place has the most numerous cases of fire in general?</li>
    <li>What is the average temperature in Winchester when number of cases is higher than 2?</li>
    <li>What is the maximum temperature during January?</li>
    <li>Which year/s has/have the most number of cases?</li>
    <li>Which month has the least number of cases?</li>
    <li>Which place has the greatest number of cases during April?</li>
    <li>What is the least temperature during February of 2002 to 2004?</li>
    <li>Which place has the least temperature from 2008 to 2009?</li>
    <li>What is the highest temperature from 2003 to 2007?</li>
    <li>Which place has the least case of fire?</li>
</ul>

<h2> Data Source </h2>

The data source was sourced as a sample dataset from the Data Science Course subject of my university.

<h2> Data Dictionary </h2>
<ul>
  <li><strong>Year</strong> - the year that the fire case occurred</li>
  <li><strong>Month</strong> - the month of the recorded fire case</li>
  <li><strong>Temperature</strong> - the temperature recorded when cases occurred, as recorded by month</li>
  <li><strong>Place</strong> - the area in which the fire case happened</li>
</ul>

<h2> Method/s or Technique/s Applied </h2>

<ul>
  <li>Exploratory Data Analysis</li>
</ul>

<h3> Technology Applied </h3>

<ul>
  <li>Python</li>
  <li>Jupyter Notebook</li>
</ul>

<h2> Exploratory Data Analysis Results </h2>

<h3> Q1. Which place has the most numerous cases of fire in general? </h3>

<div align="center">

<img style="padding: 5px;" src="figure_images\Q1_1.png" alt="python code for Q1">

<img style="padding: 5px;" src="figure_images\Q1_2.png" alt="Q1 bar graph">

</div>

<h3> Analysis </h3>

> Winchester and Spring Valley have attained the highest number of cases during a monthly duration, with Winchester getting 7 cases in March 2002 and April 2004 and Spring Valley getting the same number of cases in March 2009.

> Winchester has the most number of fire cases in the span of 2002 to 2009, with a total number of 50 fire cases. This is followed by Spring Valley with 28 cases, then Porterville with the least amount of 26 cases.

> Winchester has the most number of records on fire cases among the 3 places, with a number of 13, which is followed by Porterville with 10, and then Spring Valley with 9. 

<br>

<h3> Q2. What is the average temperature in Winchester when number of cases is higher than 2? </h3>

<img style="padding: 5px;" src="figure_images\Q2_1.png" alt="python code for Q2">

<h3> Analysis </h3>

> From the 9 monthly recorded Winchester fire incidents, the average temperature experienced during those months is around 32.83 C.

<h3> Q3. What is the maximum temperature during January? </h3>

<img style="padding: 5px;" src="figure_images\Q3_1.png" alt="python code for Q3">

<h3> Analysis </h3>

> The maximum temperature recorded during the month of January can be found in Porterland during January 2007, in which there was a recorded 25.94 C temperature.

<h3> Q4. Which year/s has/have the most number of cases? </h3>

<div align="center">

<img style="padding: 5px;" src="figure_images\Q4_1.png" alt="python code for Q4 - 1">

<img style="padding: 5px;" src="figure_images\Q4_2.png" alt="Q4 bar graph">

<img style="padding: 5px;" src="figure_images\Q4_3.png" alt="python code for Q4 - 2">

</div>

<h3> Analysis </h3>

> The years that have been found to have the most number of fire cases among the three places are during 2002, 2008, and 2009, with a total amount of 15 cases each.

<h3> Q5. Which month has the least number of cases? </h3>

<div align="center">

<img style="padding: 5px;" src="figure_images\Q5_1.png" alt="python code for Q5 - 1">

<img style="padding: 5px;" src="figure_images\Q5_2.png" alt="Q5 bar graph">

<img style="padding: 5px;" src="figure_images\Q5_3.png" alt="python code for Q5 - 2">

</div>

<h3> Analysis </h3>

> The month that has the least number of cases recorded among the three places is January, which only has a total of 8 cases overall.

<h3> Q6. Which place has the greatest number of cases during April? </h3>

<img style="padding: 5px;" src="figure_images\Q6_1.png" alt="python code for Q6">

<h3> Analysis </h3>

> Winchester is the place with the greatest number of cases out of all recorded April cases, with a number of 7 fire cases during 2004.

<h3> Q7. What is the least temperature during February of 2002 to 2004? </h3>

<img style="padding: 5px;" src="figure_images\Q7_1.png" alt="python code for Q7">

<h3> Analysis </h3>

> The least temperature recorded during the month of February from 2002 to 2004 was from Porterville during 2002, in which there was a recorded 26.12 C. 

<h3> Q8. Which place has the least temperature from 2008 to 2009? </h3>

<img style="padding: 5px;" src="figure_images\Q8_1.png" alt="python code for Q8">

<h3> Analysis </h3>

> Porterville has the least temperature recorded during the years of 2008 to 2009, with a temperature value of 24.53 C during January of 2009.

<h3> Q9. What is the highest temperature from 2003 to 2007? </h3>

<img style="padding: 5px;" src="figure_images\Q9_1.png" alt="python code for Q9">

<h3> Analysis </h3>

> Winchester has the highest recorded temperature during the years of 2003 to 2007, with a recorded temperature value of 36.9 C.

<h3> Q10. Which place has the least case of fire? </h3>

<div align="center">

<img style="padding: 5px;" src="figure_images\Q10_1.png" alt="python code for Q10 - 1">

<img style="padding: 5px;" src="figure_images\Q10_2.png" alt="Q10 bar graph">

<img style="padding: 5px;" src="figure_images\Q10_3.png" alt="python code for Q10 - 2">

</div>

<h3> Analysis </h3>

> Porterville has the least cases of fire incidents among the three places from 2002 to 2009, with only 26 cases. This is followed by Spring Valley with a total of 28 cases, and then Winchester with the highest amount of 50 cases.

<h2> Conclusion </h2>

In this data analysis, the fire incident situations of three places, which are Porterville, Spring Valley, and Winchester, were inspected. Based from analyses on the temperature values recorded from these places, Winchester has seen to be prominent across the given timeframes in terms of recording the highest temperature value, which supports the highest number of fire cases that is also discovered from the the place. Alongside this, Porterville is the complete opposite of Winchester's results, having the least temperature value recorded as well as the least amount of fire cases recorded. Aside from this, the month of January is also the coolest month for these three places, while April can be considered the hottest month. With such conclusions, fire action should be provided the most on Winchester, especially during the month of April, due to the level of temperature and amount of fire cases found from the records of the area.

<nav>
<p><a href="https://github.com/vergaraac/Data-Portfolio/blob/main/README.md">Return to Table of Contents</a></p>
</nav>