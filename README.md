![http://gallery.world/wallpaper/494186](Images/horizon_banner.png)
# Mental Health Predictor

## Background
- Defining Mental illness 
  - Disturbance of thought , experience, and emotion that causes functional impairment in people.
  - Interpersonal difficulty, limiting the ability to work and self destructive behavior. 
- In US nearly 1 in 5 adults aged 18 years or older (18.5%) have experienced mental illness (US Burden of Disease Collaborator, 2013).
- Data science can help us to better understand and effectively implement treatments for mental health problems 
- Factors causing mental illness - anxiety, depression, biological, psychological and sociological (environment) approaches. 
## Project Focus
- Our analysis project  focuses  on  identifying factors associated with the prevalence of poor mental health in the US.
  - Population density, income, water and land features 
- Building a machine learning model that can predict mental health risk for an individual based on designated factors
- What are the most and least significant factors (features) in predicting prevalence of poor mental health in the US? 
## Description of Data Sources
- 500 Cities: Local Data for Better Health, 2019. 500 Cities: Mental health not good for >=14 days among adults aged >=18 years ---[Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch](https://chronicdata.cdc.gov/500-Cities-Places/500-Cities-Mental-health-not-good-for-14-days-amon/i2ek-k3pa)
  - Behavioral Risk Factor Surveillance System (BRFSS) data (2017, 2016)
    - Mental Health Severity: Respondents aged ≥18 years who report 14 or more days during the past 30 days during which their mental health was not good. 
- US Household Income Statistics---[Golden Oak Research Group LLC, “U.S. Income Database Kaggle”. Publication: 5, August 2017](https://www.kaggle.com/goldenoakresearch/us-household-income-stats-geo-locations/version/1)
- United States Cities Database---[SimpleMaps.com, Pareto Software LLC, compiled data from U.S. Geological Survey and U.S. Census Bureau](https://simplemaps.com/data/us-cities)
## Tools/Resources
- Creating ERD
  - [QuickDBD](https://github.com/nhafer88/Mental_Health_Predictor/blob/main/final_erd.png)
- Creating Database
   - SQLite
- Analyzing Data
  - Pandas
- Connecting to Database
- Machine Learning
  - Imbalanced-learn
  - Scikit-Learn
  - Tensorflow
  - Dashboard
  - Tableau
  - Flask
  - HTML/CSS
## Machine Learning Model
- We used a binary outcome based on %poor mental health prevalence.
- The binary outcome was calculated by median split:
    - The median % poor mental health of the 500 cities was 13.89%. So…
      - If a city < 13.89% poor mental health → “Good Mental Health” 
      - If a city >= 13.89% poor mental health → “Bad Mental Health”
- Features were log-transformed and scaled to bring them into a normal distribution
- We tried logistic regression, support vector machines (1-3 kernels), decision tree, gradient tree boost (learning rates .05 - 1), random forest, and 1-2 layer deep learning
- We used 10-fold cross-validation - i.e., 10 machine learning instances of randomly allocating 90% of data to training and 10% to testing. We averaged the performance across the 10 instances.

![accuracy](Images/m_accuracy.png)
![f](Images/f_importance.png)
## Summary of Findings
- Multiple machine learning models were used and most of them provided about 80% accuracy in their mental health risk prediction.
- With Random Forest model the most strongest feature in predicting poor mental health was Standard Deviation of Income.
- This suggests that income inequality in a city most predicted the prevalence of poor mental health.
## Limitations
- Mental health data
  - Small sample
  - Limited availability
  - Subjective self-rating
- Differences in time frame of the datasets
## Recommendations for Further Analysis
- Exploring data related to:
  - Impact of COVID-19 
  - Climate
  - Affordable healthcare
  - Availability of mental healthcare providers
  - Data from wearable devices can be used to identify physiological markers associated with mental illness
  - Social media and internet activity can provide insight into a behavioral side of mental health
## Presenation Slides
- The presentation of the project will be found on a Google Slide Presenation,
[Here](https://docs.google.com/presentation/d/1T0pPPJlH2q55Iz5oIuN2MVgiFmE9DHhBDO7ZB3xee1I/edit?usp=sharing)
## Dashboards
- Tableau Dashboard
  - Data Exporation Visuals and Machine Learning Summary
    - https://nhafer88.github.io/Mental_Health_Predictor/
