# Mild-Steel-Tempering
---


Description
---
This project aims to enhance the understanding of mild steel tempering through predictive modeling, ultimately aiding in the optimization of heat treatment processes in engineering applications. This will reduce the need for manual consultation of large tempering tables, and will allow for improved engineering workflow.

I do not succeed in providing such an engineering tool, this dataset is too limited,a nd the mutli-output, mutli-label models result in severe overfitting. However, this data is sufficent to provide a final hardness prediction from a given steel and tempering proceedure. I provide a set of next steps, both in how to build such an tempering process predition application from the available data, and what data may be collected to improve such a direct prefiction model. Sadly, both extensions of the project are outside the scope of the proposal.

Context
---
Tempering of steel is an important process in engineering. It ensures that the steel is homogeneous and has the mechanical properties desired of the final product. Where annealing is a similar heat treatement aimed at making a metal as soft as possible for continued working, tempering is a heat treatment aimed at reaching a target final hardness. This target hardness is indicatative of a set of other mechanical properties, but hardness is used as the metric because it can easily be non-destructively tested in a manufacturing setting for quality control.

Broadly, tempering is one of several heat treatments that can transform a certain grade of steel to be better suited for specific applications. It may also help undo internal stresses accumulated through shaping during manufacturing.

Results
---
This project is largely an exploration into data analytics and data science skills learned at the UCB data analytics bootcamp. The inital approach was certainly too ambitious given my knowledge of the dataset, but that is how we learn.

For the Tempering time and temperatature classification problem, I attempted several simpler, models, and settled on Extra Trees Classifier as a baseline. It severely overfit the data, with 90% training combined accuracy and 25% combined testing accuracy. The neural network classifier performed better with respect to overfitting, but the combined accuracy did not break 40%.

Moving to a regression models to predict the final hardness as a continuous measure, gradient boosting regression had a R-squared of 0.93. Using a neural network for the same prediction resulted in similar MSE and R2. Plotting the GBR model predicted vs actual showed a linear relationship with some noise, indicating the more complex NN model was uncessessary. 

### Lessons Learned

Spend more time in exploratory data analysis. The issues that arose in the classification model were evident from the data initially, however I did not have the experiecne and expertise to identify that. This whole project was a huge learning experience, from using polars, a dataframe tool I had never used before, to building a mutli-output model, which I had also never done.

I initially gravitated towards PCA as a tool to reduce multicollinearity, as there was a substantial amount in my data, but found it eliminated the explainability of the model, so am learning additional ways to handle that issue, as I hope to go into chemical applications of machine learning.


### Models used
* Extra Trees Classifier
* Deep Neural Network Classifier
* Gradient Boosting Regressor
* Neural Network Regressor

For classification models the metrics accuracy and loss were used.

For regression models the metrics Mean Squared Error and loss were used.

Sources
---
[Raiipa Technologies Kaggle dataset](https://www.kaggle.com/datasets/rgerschtzsauer/tempering-data-for-carbon-and-low-alloy-steels)

[The Effects of Alloying Elements on Steels](https://www.semanticscholar.org/paper/Christian-Doppler-Laboratory-for-Early-Stages-of-of-Maalekian/8b2503ef6e92e0452156547acb3f59e6c53e266c)

Bringas, J. E. (2002). Handbook of Comparative World Steel Standards. ASTM International.
 ### Scraped data
 * [AZO Materials](https://www.azom.com/)
 * [MakeItFrom](https://www.makeitfrom.com/)

Author
--- 
Nathan Sheibley

* [Proposal](references/Nathan_project4_proposal.docx)

* [Presentation](references/Mild-Steel-Tempering-Presentation.pptx)

* [Presentation Script](references/pres_outline_and_script.md)


UC Berkeley-Ext Data Analytics Boot Camp Final Project - Solo
