<h1> Haberman's Survival Data </h1>

<img style="padding: 5px; margin: 5px auto;" width="100%" src="figure_images\haberman.png" alt="breast lymph node">

<h2> Background </h2>

The dataset contains cases from a study that was conducted between 1958 and 1970 at the University of Chicago's Billings Hospital on the survival of patients who had undergone surgery for breast cancer.

<h2> Data Source </h2>
<ul>
   <li> Donor:  Tjen-Sien Lim (limt@stat.wisc.edu) </li>
   <li> Date:    March 4, 1999 </li>
   <li> Link: <a href="https://archive.ics.uci.edu/ml/datasets/Haberman%27s+Survival">Haberman's Survival Data Set</a></li>
</ul>

<h3> <strong> Past Usage </strong> </h3>
<ol>
    <li> Haberman, S. J. (1976). Generalized Residuals for Log-Linear Models, Proceedings of the 9th International Biometrics Conference, Boston, pp. 104-122.</li>
    <li>Landwehr, J. M., Pregibon, D., and Shoemaker, A. C. (1984), Graphical Models for Assessing Logistic Regression Models (with discussion), Journal of the American Statistical Association 79: 61-83.</li>
    <li>Lo, W.-D. (1993). Logistic Regression Trees, PhD thesis, Department of Statistics, University of Wisconsin, Madison, WI.</li>
</ol>

<h2> Data Dictionary </h2>

<ul>
    <li><strong>Age</strong> - age of patient at time of operation (numerical)</li>
    <li><strong>Year</strong> - patient's year of operation (year - 1900, numerical) </li>
    <li><strong>Axillary</strong> - number of positive axillary nodes detected (numerical)</li>
    <li><strong>Status</strong> - survival status (class attribute)</li>
         <ul>
            <li>1 = the patient survived 5 years or longer</li>
            <li>2 = the patient died within 5 year</li>
         </ul>
</ul>

<h2> Method/s or Technique/s Applied </h2>

<ul>
  <li>Binary Classification</li>
  <li>Deep Learning</li>
</ul>

<h3> Technology Applied </h3>

<ul>
  <li>Python</li>
  <li>Jupyter Notebook</li>
</ul>

<h2> Interpretation and Discussion of the Result </h2>

> The data set chosen for the experiment was acquired from James D. McCaffrey’s personal blog site where he provides benchmark datasets to test various binary classification techniques. Out of the datasets available, the group chose Haberman’s Survival dataset which contains information about 306 patients relating to their breast cancer operation and survival status afterwards.

> The dataset was converted from a .data file into a .csv file and was given column headers to determine the type of data stored in each column. The preprocessing of the data took place using Python to convert it into a data frame. From here, the number “2” column values under “Status“ were replaced with 0s in order to fit better with the binary classification used. From here, a couple of dataframe functions were performed to describe the dataset and its contents and characteristics as well as checking if there are null values in the dataset. For the EDA, there is a general description set that describes the dataset, and then there is a variable analysis set that performs bivariate analysis between the dataset variables. This documentation will only provide the general description part to establish context for the dataset utilized for the deep learning experiments. 

<div align="center">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\age_chart.png" alt="age chart">

<img style="padding: 5px; margin: 5px auto;" width="50%" src="figure_images\age_table.png" alt="age table">

</div>

> From the pie chart, 14.1% of the patients are under the age group 30 - 40, 30.4% are ages 41 - 50, 30.4% as well are under 51-60, 20.6% are 61-70 years old, and 4.6% are aged 71 and above. We can see here that the age group with most of the patients who have undergone the surgery were in the age range of 41 - 60 counting both of the the top age ranges in this category, which is then followed by ages 61-70. 

<div align="center">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\year_chart.png" alt="year chart">

<img style="padding: 5px; margin: 5px auto;" width="50%" src="figure_images\year_table.png" alt="year table">

</div>

> From the graph above, it can be seen that the surgery year group with the most number of patients is 1958-1960 with 29.7% of the patients meaning most of the operations took place in this time period. This is followed by 1964 - 1966 with 28.4% of the patients, then 1961 - 1963 with 25.8%, and finally 1967 -1969 with 16.0% of the patients. 

<div align="center">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\axillary_chart.png" alt="axillary chart">

<img style="padding: 5px; margin: 5px auto;" width="50%" src="figure_images\axillary_table.png" alt="axillary table">

</div>

> With the given information, it can be said that nearly half of the patients, specifically 44.44% of them, did not have any axillary nodes counted. 13.40% only had 1 count, 6.54% had 2, 6.54% again had 3, 4.25% counted 4 nodes, 1.95% had 5 nodes, 9.80% had 6 - 10, 8.50% counted 11 - 20, and 4.58% had counted more than 20 axillary nodes. 

<div align="center">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\status_chart.png" alt="status chart">

<img style="padding: 5px; margin: 5px auto;" width="50%" src="figure_images\status_table.png" alt="status table">

</div>

> From the given chart above, it is shown that 73.5% of the patients who have undergone the operation had survived for 5 years or more while 26.5% have died within those 5 years. This shows that at least a quarter of the patients only lived within 5 years following their surgery.

<h3> <strong> Variable Analysis </strong> </h3>

For the variable analysis, each of the independent variables of **age, year, and # of axillary nodes** are each analyzed in pairs with the overall **survival status** of the patients. The **# of axillary nodes** is also analyzed together with **age** to check any relationship. The values are visualized through a pairplot scatter grid and a bivariate correlation heatmap.

<h3> Status and Age </h3>

<div align="center">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\age_status_chart.png" alt="age-status chart">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\age_status_table.png" alt="age-status table">

</div>

> In the analysis between **the patients' age and survival status**, the data is analyzed in terms of the 5 age groups and each age separately.
*   In terms of the **5 age groups**, it could be easily seen that patients who were **51-60** during their operations had the most individuals who survived for 5 years or longer with **67 patients**, while only **10 patients** for **71+**. Meanwhile, the age group of **41-50** have the most patients who only survived within 5 years with **29 patients** while both ages **30-40 and 71+** have the least with **4 patients** each. It should be pointed out there is an imbalance in the dataset that contributes to these results. Regardless, the frequency result still displays that most of the patients regardless of the age groups were able to survive for 5 years or longer.

<div align="center">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\age_status_chart_within_5.png" alt="age-status chart for within 5 years survival status">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\age_status_chart_5_years_longer.png" alt="age-status chart for 5 years or longer survival status">

</div>

*   In terms of **individual age**, the top patient ages that survived within 5 years include **age 53** with **6 patients** and **ages 46, 52, 54, 65, and 43** with **4 patients** each. Meanwhile, the ages with the most patients surviving 5 years or longer are **ages 50 and 52** with **10 patients**, and **ages 38 and 54** with **9 patients**. 

> Looking at the results, there is no clear visible or patterns keypoints that differentiates the two results other than there are more patients surviving 5 years or longer after surgery. However, it could be pointed out that most of these top results are mostly within the 41-50 and 51-60 ranges, as most patients in the dataset are within these age groups.

<h3> Status and Year </h3>

<div align="center">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\year_status_chart.png" alt="year-status chart">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\year_status_table.png" alt="year-status table">

</div>

> In the analysis between the **patient's year of operation and survival status**, the data is analyzed in terms of 4 year groups and each year separately.
*   The **year group** with the most patients who survived for 5 years or longer is **1958-1960** with **66 patients**, while the lowest one is **1967-1969** with **38 patients**. For patients who only survived within 5 years, the highest count is during **1964-1966** with **27 patients** while the lowest count is with **1967-1969** with **11 patients**. In general, the frequency result displays that a good majority of patients during these years were able to survive for 5 years or longer.

<div align="center">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\year_status_chart_within_5.png" alt="year-status chart for within 5 years survival status">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\year_status_chart_5_years_longer.png" alt="year-status chart for 5 years or longer survival status">

</div>

*   The **top years** in which the patients who only survived within 5 years since surgery year are **1965** with **13 patients**, **1958** with **12 patients**, and **1959** with **9 patients**. Meanwhile, the top 3 for patients who survived for 5 years or longer include **ages 58 and 60** with **24 patients**, **ages 61 and 64** with **23 patients**, and **ages 63 and 66** with **22 patients**. 

> Aside from such, it could also be seen that in general, the more latter the date, the smaller the amount of patients that underwent breast cancer surgery, especially during 1967-1969. This could be due to improving technology, experience, and expertise in the surgery process or lesser breast cancer cases due to external factors.

<h3> Status and # of Axillary Nodes </h3>

<div align="center">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\axillary_status_chart.png" alt="axillary-status chart">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\axillary_status_table.png" alt="axillary-status table">

</div>

> In the analysis between the **detected number of positive axillary nodes on patients and their survival status**, the data is analyzed in terms of 9 axillary node count/groups based on count and each axillary node count separately.
*   In the **grouped axillary node count**, the highest count of patients surviving 5 years or longer is with **0 nodes** with **117 patients**, while the lowest are patients with **5 nodes** detected with **2 patients**. For patients surviving within 5 years, the highest count goes to **0 nodes** detected as well, with **19 patients**. The lowest count goes to **4 nodes** detected, with **3 patients**. In terms of frequency, most of the patients in each group/value were able to survive for 5 years or longer, except for the node counts of 5, 11-20, and 20+.

<div align="center">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\axillary_status_chart_within_5.png" alt="axillary-status chart for within 5 years survival status">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\axillary_status_chart_5_years_longer.png" alt="axillary-status chart for 5 years or longer survival status">

</div>

*   Analyzing **the axillary nodes separately**, the top 3 for patients who only survived within 5 years are **0 nodes** found with **19 patients**, **1 node** found with **8 patients**, and **3 nodes** found with **7 patients**. Meanwhile, the top 3 for patients who survived for 5 years or longer starts with a significant amount of **117 patients** with **0 nodes** detected, followed by **33 patients** with **1 node** detected, and then by **15 patients** with **2 nodes** detected. 
> Analyzing the dataset, it could be seen that having 0 to a few number of axillary nodes is the common occurrance for breast cancer surgery patients. It could also be pointed out that patients who have a node count between 0-4 may have a higher survival rate, however due to the rarity of patients getting a much higher axillary node count, it is not easily identifiable on how significant the difference is due to data imbalance.

<h3> Age and # of Axillary Nodes </h3>

<div align="center">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\age_axillary_chart.png" alt="age_axillary chart">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\age_axillary_table.png" alt="age_axillary table">

</div>

> For the analysis between **age and number of axillary nodes detected**, the data is analyzed in terms of the 5 age groups and the total axillary nodes detected among each.
*   The age group with the most positive axillary nodes detected are with the **ages 51-60** with **453 nodes**, while the lowest are with the **ages 71+** with **15 nodes**. Overall, the amount of positive axillary nodes detected from the 306 patients are **1232 nodes**. 
> Similar to the previous analyses, the imbalance of the dataset significantly affects the amount of axillary nodes on each age group. This makes it not as reliable to identify whether the two variables have a relationship.

<h3> <strong> Correlation Plot / Heatmap </strong> </h3>

<div align="center">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\scatter_plot.png" alt="scatter plot">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\heat_map.png" alt="heat map">

</div>

> In terms of the **correlation heatmap/scatterplot** visualization of the dataset, only one relationship has some degree of correlation between each other. This is between the patient's **survival status** and **number of positive axillary nodes detected**, with a **weak negative correlation** value of **-0.29**. This being the only significant result may be due to the imbalance in the dataset involving age and year, which makes it more difficult to make a correlation with the survival status variable.

<h2> Conclusion </h2>

From the following analysis and interpretation results, the following could be concluded:

*   Most patients who were able to survive were around ages 40-60.
*   Most patients were operated during 1958 to 1966, and there is a decrease in amount of surgery patients by 1967 to 1969.
*   Most patients who were able to survive longer were found to have between 0 to 4 positive axillary nodes as a breast cancer patient.
*   The breast cancer surgery is mostly successful in making patients live with a longer life expectancy, with a 73.53% chance of giving a patient 5 years or longer life.
*   There is a weak inverse relationship between the patient's survival status and the number of positive axillary nodes detected. Therefore the higher the positive nodes detected from the patient, the lower their chances of surviving for 5 years or longer after the surgery.
*   The dataset is not able to accurately represent correlations between variables for the most part due to dataset imbalances.

<h2> Deep Learning Model </h2>

<h3> <strong>Train_test_split</strong> details: </h3>

| Random State | Test size | Shuffle |
|--------------|-----------|---------|
| 10           | 0.3       | True    |

<h3> <strong>Layers</strong>: </h3>

| Layers         | No. of Nodes | Activation |
|----------------|--------------|------------|
| Hidden Layer 1 | 100          | relu       |
| Hidden Layer 2 | 79           | relu       |
| Output Layer   | 1            | sigmoid    |

<h3> <strong>Compile and Fit</strong> details: </h3>

| Loss                | Optimizer | Metrics      | Validation split | Epochs | Batch size |
|---------------------|-----------|--------------|------------------|--------|------------|
| Binary_crossentropy | adam      | ['accuracy'] | 0.40             | 100    | 30         |

<h3> <strong>Results from Fitting</strong>: </h3>

Final Epoch:

Epoch 100/100

5/5 [==============================] - 0s 11ms/step - loss: 0.4920 - accuracy: 0.7891 - val_loss: 0.6392 - val_accuracy: 0.6860

<h3> <strong>Model Evaluation Result</strong>: </h3>

From evaluating testing data:

3/3 [==============================] - 0s 3ms/step - loss: 0.5586 - accuracy: 0.7717

[0.5586131811141968, 0.77173912525177]

From evaluating training data:

7/7 [==============================] - 0s 2ms/step - loss: 0.5328 - accuracy: 0.7523

[0.5328477025032043, 0.7523364424705505]

<h3> <strong>Loss Graph</strong>: </h3>

<div align="center">

<img style="padding: 5px; margin: 5px auto;" width="80%" src="figure_images\loss_graph.png" alt="loss graph">

</div>

<h3> <strong>Confusion Matrix</strong> Result: </h3>

array([[8, 12],
       [9, 63]], dtype=int64)


<h3> <strong>Prediction</strong>: </h3>

<div align="center>

<img style="padding: 5px; margin: 5px auto;" width="90%" src="figure_images\prediction.png" alt="predictions">

</div>

<nav>
<p><a href="https://github.com/vergaraac/Data-Portfolio">Return to Main Page / Table of Contents</a></p>
</nav>
