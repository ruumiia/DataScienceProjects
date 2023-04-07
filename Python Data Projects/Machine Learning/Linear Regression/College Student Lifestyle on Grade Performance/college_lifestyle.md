<h1> Multiple Linear Regression Analysis on DLSL College Students’ Current Lifestyle Choices towards their Overall Grade Performance </h1>

<img style="padding: 5px; margin: 5px auto;" width="100%" src="figure_images\mabini_bldg.png" alt="DLSL">

<h2> Background </h2>

The recent pandemic situation caused a significant impact towards every DLSL student’s lifestyle, resulting to changes in daily habits and routines over the previous lifestyle that was tied to their student life. This abrupt change caused students to partition their daily activities in various ways and timelines to fit their current study at home and quarantine situation. 

Depending on the lifestyle the student had before, these changes could range from minimal impact to significant lifestyle changes that highly influences the student life of the individual. 

Considering that each student now has different dedicated lifestyles due to the pandemic, it is an interesting viewpoint to see whether the currently adapted lifestyles of students influence their overall performance in school. 

From such, the aim is to investigate into variables such as the daily average time they currently dedicate to games, exercise, and schoolwork and identify whether it has a significant relationship towards their overall average grade performance in DLSL. 

By identifying the relationships between these variables, the study would be able to provide insights towards what activities or routines should students dedicate into more to improve their school performance while they live a home-based or hybrid lifestyle.

<h2> Background of the Community </h2>

The community in which the study was conducted upon are the college student community of De La Salla Lipa. The college students of DLSL were particularly chosen to get a more specific perspective into the current lifestyle and school performance of students at a higher and more mature level, as they have more control into what they want to do in a daily basis. 

<h2> Questions of of the Community </h2>

The student respondents were asked to provide questions they have in relation to the provided data asked in the survey, which would be answered in the exploratory data analysis (EDA) process of the project. Five questions provided by the respondents are:
1. Is there a better way to delegate my time wisely [to improve my overall grade performance]?
2. How significant is the relationship between social media hours and one's overall average grades?
3. How high is the correlation between hours spent playing video games to average grade compared to the correlation between hours spent in social media and average grade?
4. Is there a relationship between time spent with games with performance in grades?
5. Which factor is highest/that influences the most when it comes to overall average grades of a student?

<h2> Data Gathering Methodology </h2>

The data gathered were separated as two sections. First section asks for the student’s demographic information, which entails their gender, age, and course taken. The second section refers to questions in relation to their overall average grade from 1st semester, S.Y. 2021 - 2022, as well as details regarding their daily activities as a borderless education student. The overall average grade will serve as the dependent variable, while the other lifestyle variables would serve as the independent variables. The lifestyle activities that were asked are the following:

<ul>
    <li>Daily average time using computer/mobile devices</li>
    <li>Daily average playtime with games</li>
    <li>Number of games actively playing recently</li>
    <li>Daily average time spent in schoolwork</li>
    <li>Average meal eaten in a day</li>
    <li>Daily average time spent outside of the house</li>
    <li>Daily average time spent being active in social media</li>
    <li>Daily average time spent exercising</li>
</ul>

There is a total of 28 students considered for the study’s dataset, comprised of a 75% male and 25% female demographic. The ages of the respondents span between 19 to 23, with 67.9% of respondents being 21. The courses of the respondents comprise of BSBIO, BSCS, BSECE, BSEE, BSIE, BSIT, and BSPSYC, which 71.4% being BS Computer Science students. 

The demographic data served only as a background description about the respondents and not taken seriously in the actual correlation tests, due to the sampling of the survey were gathered based on convenience. From such, the demographic data is highly likely to be skewed towards the male demographic, 21 yrs old students, 3rd year level BSCS students, which would not be useful as a general indicator of college students.

The data from the survey are both discrete (questions with multiple choices) and continuous (grade and time related responses) variables to be used in the EDA and ML model. Time and grade related inputs are formatted in hh:mm and xx.xx respectively during the survey to make data preprocessing easier to perform. 

Initial preprocessing was performed through Microsoft Excel, in which time format is converted to decimal hours, as well as fixing inputs that were given in the wrong formats. 

<h2> Data Dictionary </h2>

<ul>
    <li><strong>Gender</strong></li>
    <li><strong>Age</strong></li>
    <li><strong>Course</strong> - college student's field of study or major</li>
    <li><strong>Grade</strong> - overall grade average in 1st semester, S.Y. 2021 - 2022</li>
    <li><strong>Device Use</strong> - daily average time spent using computers or handheld devices (hrs)</li>
    <li><strong>Playtime</strong> - daily average playtime of the college student (hrs)</li>
    <li><strong>No. of Games</strong> - number of games being played by the student</li>
    <li><strong>Schoolwork Time</strong> - student grade on Literature</li>
    <li><strong>Meals</strong> - average meals eaten in a day</li>
    <li><strong>Outside</strong> - daily average time spent outside (hrs)</li>
    <li><strong>Social Media</strong> - daily average time spent in social media (hrs)</li>
    <li><strong>Exercise</strong> - daily average time spent exercising (hrs)</li>
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
  <li>Microsoft Excel
  <li>Google Forms</li>
</ul>

<h2> Machine Learning Model </h2>

In forming the ML model of the study, the independent and dependent variables must be selected first from the data frame. In variable selection for this model, forward selection method was performed, in which the model starts as empty, and variables are added one by one to see which variable gives the single best improvement to the model. 

To identify this, the model will be using the r-squared value of the regression. Through this method, the regression equation of the model can also be formed, which is the formula used to predict the dependent variable. 

The formula for this equation is: 

$y=\beta_0+\beta_1X_1+...+\beta_nX_n$

where $y$ is the dependent variable, $X$ are the independent variables, $\beta_n$ is the slope coefficient of the line, and $\beta_0$ is the intercept coefficient. The linear component of the formula $(\beta_0+\beta_1X_1+...+\beta_nX_n)$ extends as the number of independent variables used for the model increase. For this method, we attempted up to four-variable iterations to see which gives the best r-squared score as well as the lowest mean squared error value. The following are the iterations:

One-Variable Iteration: $y = \beta_0 + \beta_1X_1$
| $y$ regressed only on: | Device Use | Playtime | No. of Games | **Schoolwork time** | Meals | Outside | Social Media | Exercise |
|----------------------|------------|----------|--------------|-----------------|-------|---------|--------------|----------|
| $r^2$                | -0.151     | -0.018   | -0.093       | **0.407**          | -0.193 |-0.552   | -0.164       | 0.069    |

Highest $r^2$: Schoolwork time (0.407)

Two-Variable Iteration: $y = \beta_0 + \beta_1(Schoolwork\:time) + \beta_2X_2$
| $y$ regressed on Schoolwork time and: | Device Use | **Playtime** | No. of Games | Meals | Outside | Social Media | Exercise |
|-------------------------------|------------|----------|--------------|-----------------|-----------|--------------|----------|
| $r^2$                         | -0.176      | **0.388**    | 0.350        | 0.248           | -0.324 | 0.214        | -0.052    |

Highest $r^2$: Schoolwork time + Playtime (0.388)

Three-Variable Iteration: $y = \beta_0 + \beta_1(Schoolwork\:time) + \beta_2(Playtime) + \beta_3X_3$
| $y$ regressed on Schoolwork time, Playtime, and: | Device Use | **No. of Games** | Meals | Outside | Social Media | Exercise |
|---------------------------------------|----------------|----------|--------------|-----------------|--------------|----------|
| $r^2$                                 | -0.356      | **0.403**    | 0.088       | -0.428           | 0.172        | -0.060    |

Highest $r^2$: Schoolwork time + Playtime + No. of Games (0.403)

Four-Variable Iteration: $y = \beta_0 + \beta_1(Schoolwork\:time) + \beta_2(Playtime) + \beta_3(No.\:of\:Games) + \beta_4X_4$
| $y$ regressed on Schoolwork time, Playtime, No. of Games, and: | Device Use | Meals | Outside | **Social Media** | Exercise |
|---------------------------------------------------|----------|--------------|-----------------|------------------|----------|
| $r^2$                                             | -0.159    | -0.004        | -0.494           | **0.277**        | -0.143    |

Highest $r^2$: Schoolwork time + Playtime + No. of Games + Social Media (0.277)

Final Equation:

$y = \beta_0 + \beta_1(Schoolwork\:time) + \beta_2(Playtime) + \beta_3(No.\:of\:Games) + \beta_4(Social\:Media)$

Looking at the following iterations, the model can have the best r-squared value if we have a three-variable model, using schoolwork time, playtime, and number of games as our independent variables to predict the grade. 

After getting the independent and dependent variables, the dataset is split into training and test sets, divided with 80% training data and 20% test data. The linear regression model is then imported and fitted in with the given dataset, to produce a prediction of grades using the test set of independent variables. 

The model performance displayed an r-squared score of 0.403, which can be considered a good score for studies attempting to predict human behavior. 

The model also attained mean squared error value of 1.707, which is satisfactory enough in predicting a value such as a student’s grade performance. The following figures below shows the actual vs prediction values using the model.

<div align="center">

<img style="padding: 5px; margin: 5px auto;" width="30%" src="figure_images\actual_vs_predicted.png" alt="actual vs predicted values">

<img style="padding: 5px; margin: 5px auto;" width="70%" src="figure_images\plot_actual_vs_predicted.png" alt="actual vs predicted values">

</div>

<h2> Interpretation and Discussion of the Result </h2>

<div align="center">

<img style="padding: 5px; margin: 5px auto;" width="70%" src="figure_images\correlation_heatmap.png" alt="correlation heatmap">

</div>

In performing the EDA for the dataset, the following heatmap is formed. From such, the analysis and interpretation determined from the data are the following:

> In terms of positive correlation, device use time and schoolwork time provide the highest values in relation to the grade, with a positive weak correlation of 0.31 with device use and a positive weak correlation of 0.21 with schoolwork time. The two variables are also positively weakly correlated with each other, with 0.34.

> In terms of negative correlation, time spent outside and exercising provide the highest values in relation to grade, with a negative moderate correlation of -0.44 with time outside and negative weak correlation of -0.36 with time spent exercising. The two variables are in a positively moderate correlation with each other, with a value of 0.43.

> Playtime, No. of games, Meals, and social media have very weak correlation towards grades but have some fairly weak to moderate correlation to device use time, schoolwork time, outside time, and exercise time, causing an indirect relationship with grades.

> Forward selection method in variable selection for the ML model resulted in selection of schoolwork time, no. of games, and playtime as the chosen regressor variables. This results to an r-squared score of 0.403 and a mean squared error value of 1.707. An r-squared value of 50% or less is usually the result of a studies attempting to predict human behavior. 

> Slope values for schoolwork time, no. of games, and playtime are 0.22208662, -0.37271045, and 0.0419289, while the intercept value is 91.36377937438614.

The community questions were also addressed with the findings from the EDA, which are the following:

1. Is there a better way to delegate my time wisely [to improve my overall grade performance]?
> Considering the EDA results, the best way to delegate one's time to maximize their overall grade performance is striking a balance between increasing device use and schoolwork time and outside and exercise time, due to their direct and inverse relationship with grade. Students who spend more time doing schoolworks and using their devices should consider doing outdoor and exercise activities more, and vice versa. This data proves that a quality life-work balance is needed to improve performance.

2. How significant is the relationship between social media hours andone's overall average grades?
> The relationship has a very weak positive correlation hinting to only a minimal direct increase of overall grades from the hours spent in social media.

3. How high is the correlation between hours spent playing video gamesto average grade compared to the correlation between hours spent insocial media and average grade?
> The correlation between game playtime and overall grade is a negligible negative one compared to the positive very weak correlation that social media and grades have. However, social media has a higher value of correlation of 0.16 compared to playtime's 0.0079, making it more influential compared to playtime, albeit in a very weak degree.

4. Is there a relationship between time spent with games with performance in grades?
> It has a negligible inverse correlation, which means it has a very minimal connection with increasing grade performance as the playtime value goes down.

5. Which factor is highest/that influences the most when it comes to overall average grades of a student?
> In terms of a direct correlation with the grades, device use has the highest positive influence. This could be attributed to how schoolworks are performed through online methodologies, leading to higher device use. This also contributed to making time spent on schoolworks the 2nd highest positive influence to grades. In terms of an inverse correlation, time spent outside has the highest negative influence. This could be that the more time spent outside, the less time to be focused on school related lifestyle, leading to a lower grade performance. This also contributes to making time spent on exercise the 2nd highest inverse relationship, as spending time outside could also be for exercising outdoor, although it could also be done indoors.

<h2> Conclusions </h2>

With the following results, it is concluded that device use, schoolwork, outside, and exercise time have a significant relationship towards influencing overall grade performance, in terms of individual correlation with the grade variable. 

Increasing the device use and schoolwork time can help increase grade performance of students in a weak to moderate level. Decreasing time spent outside and exercising can also increase grade performance to a moderate level. 

However, it should also be pointed out that balancing these variables are also important in ensuring a high-grade performance. In terms of building the model, the variables of schoolwork time, no. of games playing, and total play time contributes to the highest possible r-squared value and lowest mean squared error value through the forward selection method. 

It should also be pointed out that the results of this study can be further improved through getting a higher number of respondents and to make the data gathering method wider and more randomized to minimize selection bias. 

Doing such could also improve the correlation in the heatmap as well as make the model more fit into a generalized data set, making it better overall.

<nav>
<p><a href="https://github.com/vergaraac/Data-Portfolio">Return to Main Page / Table of Contents</a></p>
</nav>