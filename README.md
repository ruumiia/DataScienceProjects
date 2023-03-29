<h1> DataScienceProjects </h1>
A repository of my Data Analysis / Science related projects. Datasets for the following are sourced from examples given in my university, my own surveyed information, as well as from online data repositories such as Kaggle.
<br /><br />
<h1 id="table-of-contents"> Table of Contents </h1>

<nav>
<h3> Basic Data Exploration </h3>

<ul>
  <li><a href="#fire-case">Fire Case Reports</a></li>
  <li>Grades Analysis</li>
</ul>

<h3> EDA with Machine Learning / Deep Learning </h3>
<ul>
<li>Linear Regression 
  <ol>
    <li>College Student Lifestyle on Grade Performance</li>
    <li>House Prediction</li>
  </ol>
</li>
<li>Deep Learning
  <ol>
    <li>Basic Neural Network</li>
    <li>Binary Classification
      <ul>
        <li>Haberman's Survival Dataset</li>
        <li>Tech Specifications for Office or Gaming Use</li>
      </ul>
    </li>
  </ol>
</li>
</ul>

</nav>

<h1> Basic Data Exploration </h1>

<h2 id="fire-case"> Fire Case Reports </h2>

<h3> Business Problem / Problem Domain </h3>

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

<h3> Data Source </h3>

The data source was sourced as a sample dataset from the Data Science Course subject of my university.

<h3> Method/s or Technique/s Applied </h3>

<ul>
  <li>Exploratory Data Analysis</li>
</ul>

<h3> Technology Applied </h3>

<ul>
  <li>Python</li>
  <li>Jupyter Notebook</li>
</ul>

<h3> Exploratory Data Analysis Results </h3>

<h3> Q1. Which place has the most numerous cases of fire in general? </h3>

<div align="center">

<img style="padding: 5px;" src="DataScienceProjects\Basic Data Exploration\Fire Case Reports\Q1_1.png" alt="python code for Q1">

<img style="padding: 5px;" src="DataScienceProjects\Basic Data Exploration\Fire Case Reports\Q1_2.png" alt="Q1 bar graph">

</div>

<h3> Analysis </h3>

> Winchester and Spring Valley have attained the highest number of cases during a monthly duration, with Winchester getting 7 cases in March 2002 and April 2004 and Spring Valley getting the same number of cases in March 2009.

> Winchester has the most number of fire cases in the span of 2002 to 2009, with a total number of 50 fire cases. This is followed by Spring Valley with 28 cases, then Porterville with the least amount of 26 cases.

> Winchester has the most number of records on fire cases among the 3 places, with a number of 13, which is followed by Porterville with 10, and then Spring Valley with 9. 

<br>

<h3> Q2. What is the average temperature in Winchester when number of cases is higher than 2? </h3>

<img style="padding: 5px;" src="DataScienceProjects\Basic Data Exploration\Fire Case Reports\Q2_1.png" alt="python code for Q2">

<h3> Analysis </h3>

> From the 9 monthly recorded Winchester fire incidents, the average temperature experienced during those months is around 32.83 C.

<h3> Q3. What is the maximum temperature during January? </h3>

<img style="padding: 5px;" src="DataScienceProjects\Basic Data Exploration\Fire Case Reports\Q3_1.png" alt="python code for Q3">

<h3> Analysis </h3>

> The maximum temperature recorded during the month of January can be found in Porterland during January 2007, in which there was a recorded 25.94 C temperature.

<h3> # Q4. Which year/s has/have the most number of cases? </h3>


<nav>
<p><a href="#table-of-contents">Return to Table of Contents</a></p>
</nav>
