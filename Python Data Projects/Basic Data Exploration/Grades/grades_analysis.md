<h1> Grades Analysis </h1>

<h2> Business Problem / Problem Domain </h2>

The given data are recorded grades of students from different subjects such as Physics, Mathematics, English and Literature.

Questions:

1. Which subject do students excel the most? Support your answer with analysis and explanation.

2. How many students are below 87 in both Math and Physics?

        (For example student A got 83 in Math and 86 in Physics, this is counted because they are both below 87. If student B got 87 in Math and 83 in Physics, don't include.)

3. What is/are the grade/s of the student/s in math who got the highest grade/s in Physics?

4. What is/are the grade/s of the student/s in English who got the lowest grade/s in Math?

5. How can you describe the relationship between Math and English?

<h2> Data Source </h2>

The data source was sourced as a sample dataset from the Data Science Course subject of my university.

<h2> Data Dictionary </h2>

<ul>
    <li><strong>Physics</strong> - student grade on Physics</li>
    <li><strong>Math</strong> - student grade on Math</li>
    <li><strong>English</strong> - student grade on English</li>
    <li><strong>Literature</strong> - student grade on Literature</li>
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

<h3> Q1. Which subject do students excel the most? Support your answer with analysis and explanation. </h3>

<div align="center"> 

<img style="padding: 5px; margin: 5px auto;" width="30%" src="figure_images\Q1_1.png" alt="python code for Q1 - 1">

<img style="padding: 5px; margin: 5px auto;" width="50%" src="figure_images\Q1_2.png" alt="python code for Q1 - 2">

</div>

<h3> Analysis </h3>

> Out of all subjects' overall mean results, Math has the highest average score of 86.06 among students.

> In terms of the highest score gotten by students, Physics and English resulted with the highest attained score of 93. 

> In terms of the lowest score, Math resulted with the lowest possible score of 78.

> Based on the standard deviation scores, Literature have the least amount of deviation from the average score.

<h3> Q2. How many students are below 87 in both Math and Physics? </h3>

<div align="center">

<img style="padding: 5px; margin: 5px auto;" width="50%" src="figure_images\Q2_1.png" alt="python code for Q2">

</div>

<h3> Analysis </h3>

> There is an overall count of 15 students who have Math and Physics grades below 87.

<h3> Q3. What is/are the grade/s of the student/s in math who got the highest grade/s in Physics? </h3>

<div align="center"> 

<img style="padding: 5px; margin: 5px auto;" width="70%" src="figure_images\Q3_1.png" alt="python code for Q3">

</div>

<h3> Analysis </h3>

> The Math grade of the student who got the highest Physics grade of 93 is 91.

<h3> Q4. What is/are the grade/s of the student/s in English who got the lowest grade/s in Math? </h3>

<div align="center"> 

<img style="padding: 5px; margin: 5px auto;" width="70%" src="figure_images\Q4_1.png" alt="python code for Q4">

</div>

<h3> Analysis </h3>

> The English grade of the student who got the lowest Math grade of 78 is 93.

<h3> Q5. How can you describe the relationship between Math and English? </h3>

<div align="center"> 

<img style="padding: 5px; margin: 5px auto;" width="50%" src="figure_images\Q5_1.png" alt="Q5 scatter plot - 1">

<img style="padding: 5px; margin: 5px auto;" width="50%" src="figure_images\Q5_2.png" alt="Q5 scatter plot - 2">

</div>

<h3> Analysis </h3>

> Based on the either the matplotlib or seaborn plots, the points on the Math and English relationship starts up and proceeds to go downwards from a left to right reading. 

> The points are fairly close to each other and does not deviate much from a diagonal formation. 

> Reading from left to right, Math scores become higher while English scores becomes lower.

<h2> Conclusion </h2>

> The subject of Math recieves both the highest mean and lowest possible score, while Physics and English resulted with the highest attainable score, and Literature recieved the most consistent scores in relation to its average. From these results, we can conclude that in terms of considering overall student performance, we would consider Math as the subject where there are a good amount of students excelling due to having the highest average score, enough to pull the class average with low grade students alongside having no student getting the highest grade equivalent to the other subjects.

> In terms of relationships, the pairs of Math-Physics and English-Literature have shown positive correlation or direct relationship with each other. Meanwhile, these subjects compared with other subjects outside of the pairing (e.g. Math-English, Math-Literature, etc.) displayed a negative correlation with each other.

<nav>
<p><a href="https://github.com/vergaraac/Data-Portfolio">Return to Main Page / Table of Contents</a></p>
</nav>
