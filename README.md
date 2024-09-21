[![Install](https://github.com/nogibjj/Individual_Project1_jdc154/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/Individual_Project1_jdc154/actions/workflows/hello.yml)

[![Lint](https://github.com/nogibjj/Individual_Project1_jdc154/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Individual_Project1_jdc154/actions/workflows/lint.yml)

[![Format](https://github.com/nogibjj/Individual_Project1_jdc154/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Individual_Project1_jdc154/actions/workflows/format.yml)

[![Test](https://github.com/nogibjj/Individual_Project1_jdc154/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Individual_Project1_jdc154/actions/workflows/test.yml)

# Netflix Movie and TV Shows Project Overview

## About the Project
The purpose of this project is to generate descriptive statistics and look into trends of movie and TV show releases on Netflix over the years. This dataset is from [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows?resource=download)

### Summary Statistics of Movie and TV Show Release Years:
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>release_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>8807.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2014.180198</td>
    </tr>
    <tr>
      <th>std</th>
      <td>8.819312</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1925.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2013.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2017.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2019.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2021.000000</td>
    </tr>
  </tbody>
</table>
</div>

### Visualizations
![alt text](images/TV_ratings.png)

![alt text](images/Movie_ratings.png)

## Note on the repository and directions:
This project contains:
* requirements.txt detailing the requirements needed for this project
* Makefile to install requirements; lint with Ruff; format with black; and test your notebook, script, and lib files
* github actions with separate YAML files for Install, Lint, Format, and Test in the github workflows folder
* DockerFile and devcontainer for environment set up
* Jupyter notebook performing descriptive statistics and tested with nbval
* script.py Python script for statistics and generating data visualizations
* test_script.py to test the script
* lib.py Python script file that shares code between the script and notebook
* test_lib.py to test library script
* Summary pdf containing the walkthrough and conclusions found in the data analysis

## Preparation
1. Open codespaces 
2. Load repo to code spaces
2. Wait for installation of all requirements in requirements.txt

## Check format and test errors
1. Format code `make format`
![image](https://github.com/user-attachments/assets/7688b60a-9f2b-45a2-acf3-8a7f66f346e1)

2. Lint code `make lint`
![image](https://github.com/user-attachments/assets/5b73ef36-a462-468c-9aab-40e1a66079ff)

3. Test code `make test`
![image](https://github.com/user-attachments/assets/47b3bd24-96d8-4a3a-a1ec-7cc8f935e802)

(alternatively, do all with `make all`)

## Walkthrough Video
Here is the link to my [demo video](https://youtu.be/mOJkvNA_WrI)




