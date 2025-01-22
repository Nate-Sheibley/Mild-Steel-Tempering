# Mild Steel Tempering
---
# Description
This project aims to speed quantitative decision making of steel tempering conditions decision making through predictive modeling, ultimately aiding in the automation of heat treatment workflow in engineering applications. Using primarily polars and scikit-learn I revise my UC Berkeley Data Analytics captone project into the engineering tool descriped in the proposal and above. To aid in this I use vega-altair for quick visualizations and seaborn for statistical visualizations. The next step for this project is to use FastAPI to build a funcitonal interface for the tool that does not require runing the notebook.

## Context
Tempering of steel is an important process in engineering. It ensures that the steel is homogeneous and has the mechanical properties desired of the final product. Where annealing is a similar heat treatement aimed at making a metal as soft as possible for continued working, tempering is a heat treatment aimed at reaching a target final hardness. This target hardness is indicatative of a set of other mechanical properties, but hardness is used as the metric because it can easily be non-destructively tested in a manufacturing setting for quality control.

Broadly, tempering is one of several heat treatments that can transform a certain grade of steel to be better suited for specific applications. It may also help undo internal stresses accumulated through shaping during manufacturing.

# Revised (-revised) vs Capstone (-main) Notebooks

There are two notebooks in this repository. 

1. The *-main.ipynb was turned in for the final project of the UC Berkeley Data Analytics boot camp. I had 3 weeks to find a dataset, submit a business case proposal, then complete a notebook that showed at least 2 models of machine learning, appropriate preprocessing of the data, had > 0.75 accuracy. This notebook has 4 distinct models, and explores many optimization tweaks to these models.

2. The *-revised.ipynb notebook is currently in progress (Dec 2, '24). It is a reconstruction of the project based on lessons learned from completing the capstone project. The end goal of the revised notebook is to fully implement a scalable version of the business idea presented in the proposal. That is, build a pipeline, model, and application that can accept steel compositions and a desired final hardness, and output the appropriate tempering conditions, in a user friendly 

## Original Result '-main.ipynb'
This project is largely an exploration into data analytics and data science skills learned at the UCB data analytics bootcamp. The inital approach was certainly too ambitious given my knowledge of the dataset, but that is how we learn.

For the Tempering time and temperatature classification problem, I attempted several simpler, models, and settled on Extra Trees Classifier as a baseline. It severely overfit the data, with 90% training combined accuracy and 25% combined testing accuracy. The neural network classifier performed better with respect to overfitting, but the combined accuracy did not break 40%.

Moving to a regression models to predict the final hardness as a continuous measure, gradient boosting regression had a R-squared of 0.93. Using a neural network for the same prediction resulted in similar MSE and R2. Plotting the GBR model predicted vs actual showed a linear relationship with some noise, indicating the more complex NN model was uncessessary. 

I do not succeed in providing such an engineering tool, this dataset is too limited,a nd the mutli-output, mutli-label models result in severe overfitting. However, this data is sufficent to provide a final hardness prediction from a given steel and tempering proceedure. I provide a set of next steps, both in how to build such an tempering process predition application from the available data, and what data may be collected to improve such a direct prefiction model. Sadly, both extensions of the project are outside the scope of the proposal.

### Models used in both files
* Extra Trees Classifier
* Deep Neural Network Classifier
* Gradient Boosting Regressor
* Neural Network Regressor

For classification models the metrics accuracy and loss were used.

For regression models the metrics Mean Squared Error and loss were used.

### Lessons Learned from the capstone project
Spend more time in exploratory data analysis. The issues that arose in the classification model were evident from the data initially, however I did not have the experiecne and expertise to identify that. This whole project was a huge learning experience, from using polars, a dataframe tool I had never used before, to building a mutli-output model, which I had also never done.

I initially gravitated towards PCA as a tool to reduce multicollinearity, as there was a substantial amount in my data, but found it eliminated the explainability of the model, so am learning additional ways to handle that issue, as I hope to go into chemical applications of machine learning.

# Result
Numnber of lines of code was cut in half. Excessive data augmentation and processing was removed. EDA pipeline readability and thoroughness was improved. Model preprocessing done with a pipeline object to allow scaling. Bugs resulting from erronious preprocessing resolved. 

Function developed that takes in a trained model and steel input, with desired hardness, and outputs a tempering temperature for a given amount of tempering time to reach a target hardness. The model scores 0.98 which is very good and better than found in the original project.

![Model fit](/images/revised/GBR_fit.png)

TODO: add an API and localhost for the github page (Jan 22, '25)

---
## Sources
### Data
[Raiipa Technologies Kaggle dataset](https://www.kaggle.com/datasets/rgerschtzsauer/tempering-data-for-carbon-and-low-alloy-steels)

[The Effects of Alloying Elements on Steels](https://www.semanticscholar.org/paper/Christian-Doppler-Laboratory-for-Early-Stages-of-of-Maalekian/8b2503ef6e92e0452156547acb3f59e6c53e266c)

Bringas, J. E. (2002). Handbook of Comparative World Steel Standards. ASTM International.
 ### Scraped data
 * [AZO Materials](https://www.azom.com/)
 * [MakeItFrom](https://www.makeitfrom.com/)

---
## Generated Documents
* [Proposal](references/Nathan_project4_proposal.docx)

* [Main Notebook](Mild_Steel_Tempering-main.ipynb)

* [Presentation](references/Mild-Steel-Tempering-Presentation.pptx)

* [Presentation Script](references/pres_outline_and_script.md)

## Author
Nathan Sheibley

UC Berkeley-Ext Data Analytics Boot Camp Final Project - Solo
