# Mild-Steel-Tempering
---
UC Berkeley-Ext Data Analytics Boot Camp Project 4 - Solo

[Proposal](references/Nathan_project4_proposal.docx)

Description
---
This project aims to enhance the understanding of mild steel tempering through predictive modeling, ultimately aiding in the optimization of heat treatment processes in engineering applications. This will reduce the need for manual consultation of large tempering tables, and will allow for improved engineering workflow.

I do not succeed in providing such an engineering tool, this dataset is too limited. I do provide a set of next steps, both in how to build such an application form the available data, and what data may be collected to improve such a direct prefiction model. Sadly, both extensions of the project are outside the scope of the proposal and deadline.

Context
---
Tempering of steel is an important process in engineering. It ensures that the steel is homogeneous and has the mechanical properties desired of the final product. Where annealing is a similar heat treatement aimed at making a metal as soft as possible for continued working, tempering is a heat treatment aimed at reaching a target final hardness. This target hardness is indicatative of a set of other mechanical properties, but hardness is used as the metric because it can easily be non-destructively tested in a manufacturing setting for quality control.

Broadly, tempering is one of several heat treatments that can transform a certain grade of steel to be better suited for specific applications. It may also help undo internal stresses accumulated through shaping during manufacturing.

Sources
---
[Raiipa Technologies Kaggle dataset](https://www.kaggle.com/datasets/rgerschtzsauer/tempering-data-for-carbon-and-low-alloy-steels)

[The Effects of Alloying Elements on Steels](https://www.semanticscholar.org/paper/Christian-Doppler-Laboratory-for-Early-Stages-of-of-Maalekian/8b2503ef6e92e0452156547acb3f59e6c53e266c)

Bringas, J. E. (2002). Handbook of Comparative World Steel Standards. ASTM International.
 ### Scraped data
 * [AZO Materials](https://www.azom.com/)
 * [MakeItFrom](https://www.makeitfrom.com/)


Approach
---
This project is largely an exploration into data analytics and data science skills. The inital approach was certainly too ambitious given my knowledge of the dataset, but that is how we.

### Models used
* Extra Trees Classifier
* Deep Neural Network Classifier
* Gradient Boosting Regressor
* Neural Network Regressor

For classification models the metrics accuracy and loss were used.

For regression models the metrics Mean Squared Error and loss were used.


