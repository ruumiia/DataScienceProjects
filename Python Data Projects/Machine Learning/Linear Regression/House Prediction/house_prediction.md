<h1> House Prediction </h1>

<img style="padding: 5px; margin: 5px auto;" width="100%" src="figure_images\house.png" alt="House">

<h2> Background </h2>

You are provided house data comprising of four columns with 28 records: (1) the area of the house in $m^2$, (2) the house's age, (3) the house's distance from the city in $km$ and (4) the price of the house.

Clean and explore the dataset, then create a machine learning model to predict the house price.

<h2> Data Source </h2>

The data source was sourced as a sample dataset from the Data Science Course subject of my university.

<h2> Data Dictionary </h2>

<ul>
    <li><strong>Lot No.</strong> - lot number of the house</li>
    <li><strong>Area</strong> - area of the house </li>
    <li><strong>Age</strong> - how long the house has been</li>
    <li><strong>Distance</strong> - distance of the house from the city</li>
    <li><strong>Price</strong> - price of the house</li>
</ul>

<h2> Method/s or Technique/s Applied </h2>

<ul>
  <li>Linear Regression</li>
  <li>Machine Learning</li>
</ul>

<h3> Technology Applied </h3>

<ul>
  <li>Python</li>
  <li>Jupyter Notebook</li>
</ul>

<h2> Interpretation and Discussion of the Result </h2>

<div align="center">

<img style="padding: 5px; margin: 15px auto;" width="70%" src="figure_images\correlation_heatmap.png" alt="correlation heatmap">

<img style="padding: 5px; margin: 15px auto;" width="70%" src="figure_images\plot.png" alt="scatter plot">

</div>

> In terms of price, strong relationships can be found when paired with area and distance. Area has a perfect positive correlation (1.00) and distance has a strong positive correlation (0.65).

> In terms of distance, strong relationships can be found when paired with price, age, and area. Price has a strong positive correlation (0.65), Age has a very strong positive correlation (0.85), and area has a strong positive correlation with area (0.64)

> Age only has a strong relationship with distance, with a very strong positive correlation (0.85).

> Area has a strong relationship with distance and price, with a strong positive correlation with distance (0.64) and a perfect positive correlation with price (1.00)

> Lot no. has no strong relationships with price, age, area, or distance.

<h2> Conclusion </h2>

Distance and area values are to be considered due to its direct strong positive correlation with the price value, meaning if either or both of the two goes up or down, it will also significantly affect the rise and fall of house prices. 

As distance serves to be a signficant variable related to house prices, age is also considered due to its strong positive correlation with distance, making it such that an age value change will significantly impact distance, which indirectly affects price values significantly as well. 

<h2> Machine Learning Model </h2>

With the following EDA results, it is concluded that in order to predict the house price, the distance, area, and age values should be considered in creating the model. 

<img style="padding: 5px; margin: 15px auto;" width="70%" src="figure_images\model_performance.png" alt="model performance">

Slope values for area, distance, and age respectively are 0.99971163, 0.00562097, and 0.97123501. Meanwhile the intercept value is 0.4004304764197286.

The r-squared score is 0.9999986951321892 or 1 when rounded up, indicating that the model is approximately perfect or perfect. The mean squared error value is approximately 0.009, indicating that the model is great with minimal error.

The model that resulted from these variables has shown to be near perfect as seen from its r-squared score and mean squared error value. This makes it a great model to use for predicting house prices.

<nav>
<p><a href="https://github.com/vergaraac/Data-Portfolio">Return to Main Page / Table of Contents</a></p>
</nav>
