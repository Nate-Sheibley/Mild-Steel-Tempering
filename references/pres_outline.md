# Presentation Reqs
## Clear Objective and Purpose
1. Goal-Oriented: Start with a clear understanding of the purpose of your presentation. What are you trying to convey? Is it to inform, persuade, or explore
data? Define your key message or insight.
2. Target Audience: Tailor your visualizations and explanations to the knowledge level and interests of your audience. Consider what they need to know and
how best to communicate that information to them.
## Relevant and Accurate Data
1. Relevant Data: for example, if your story is about hourly changes in rainfall, your visualization data shouldn’t be in months.
2. Contextualization: if warranted, provide context for the data. Explain where it comes from, the time period it covers, and any assumptions or limitations.
## Effective Visual Design
1. Choosing the Right Chart Type: Use appropriate visualizations (bar charts, line graphs, scatter plots, etc.) that best represent the data and the insights you
want to convey.
2. Simplicity: Avoid clutter and unnecessary details. Strive for simplicity in design while ensuring all necessary information is included.
3. Consistency: Maintain consistent use of colors, fonts, and design elements throughout the presentation to avoid confusion and enhance readability.
4. Accessibility [OPTIONAL]: Ensure that the design is accessible to all viewers, including those with color blindness or other visual impairments. Use color
palettes that are colorblind-friendly and provide sufficient contrast.

Slide|Story Beat|Content
---|---|---
1|introduce the subject| Hook, we've all bent metal til it breaks. manufacturing
2|describe the base problem and solution (work and temper)| https://d2ykdomew87jzd.cloudfront.net/Blog/Ulbrich-Manufacturing-Process-Illustration-1200x628.jpg
3|introduce the data and modelling goal| data summary table. ref Raiipa, AZoM, MIF 
4|data processing, PCA | obviously there were a few fields like source that were unnecessary for my consideration. correlation plots
5|structure of multioutput problem| label balancing, pre/post. accuracy... didn't work. two headed model diagram.
6|return to a simpler regression problem| introduce the regression problem, and the prediction. scatter/ling plot. table of R2 for NN and GBR
7| compare NN model results across the two problems | plot 2 headed loss on left, single regression on right.
8|Downsides of the data processing|talk about GBR explainability and PCA. Feature importance plot. inability to correlate with features irl.know from domain knowlegde alloy elements significantly change steel microstructure behavior at temperature. show Mo plot from paper. https://www.semanticscholar.org/paper/Christian-Doppler-Laboratory-for-Early-Stages-of-of-Maalekian/8b2503ef6e92e0452156547acb3f59e6c53e266c
9|Thank you!


## Script Notes (8-10 minutes)
1. I'm going to be talking the tempering of steel today. I'm sure we've all bent a piece of metal back and forth until it breaks. Working a metal by bending it, putting it through roller to thin it, drawing it through a die to stretch it into wire; these all cause stresses to accumulate in the metal, and result in work hardening. Contiuned working makes metal brittle and results in cracking, which is obviously undesirable when making product. (30s)

2. So, for example, we have a roll of steel that is raw stock that is nominally 1/4 inch thick. But as a manufacturer we must thin it to 1/4" or 1/8th"  to match sales specification. This will work hardened it thoroughly, making it stiff, brittle, and difficult to trim to final size. Annealing a steel by heating it to a few hundred, or even several hundred degrees Celcius can soften the metal again so that more work can be done without cracking. Tempering is an almost identical process, but where annealing targets making the steel as soft as possible for continued working, tempering is done with a final target hardness in mind. (1:15)

3. The dataset I'll be working with is from kaggle and has about 1500 rows. It was provided to the public by the company Raiipa, a metalurgical engineer consulting firm focus on AI applications. The data is pulled from 3 scientific reviews, dating from 1945 to 2010. I chose to use this dataset to build an engineering tool that would allow the prediction of the tempering conditions, time and temperature, to reach a target hardness. (1:45)

4. To this end there was substaintail data processing to get done. All the standard scaling and encoding problems, but I also suspected my dataset may be too limited in information to make the kind of prediction I was asking of it. So, I scraped additional mechanical properties data from the AZoM and MakeItFrom websites, these are steel property database websites. This resulted in discovering that some of the older steels were not made to a standard I could identify and had to be thrown out, bringing me from 1500 rows to 1300 rows. Additionally, I know that the alloying elements of the steels greatly effect the phsycial properties, so I was introducing multicolinearity in adding this scraped data. As a result I made the decision to do a primary component analysis as well. As you can see I went from a fair amount of multicolinearity, to absolutely none. (245)

5.  Getting back to the model, in order to predict the tempering process I built a multi-output multi-label classification model. That is, I targetted 5 and 11 labeled bins in the tempering time and tempering temperature dimensions. There was some label balancing issues that arose at this point, as you can see, which is why i decided to bin my target classifications. Many of the tempering times were not well represented, and I went down to only 5 bins there, that covered 10 seconds to 32 hours of tempering. That may be excessively broad, but i did not have the data to support more granular classifcaitons. I attemped Extra Trees Classifer and  classification Deep Neural Networks models but both approached ended up failing to break 40% comnined accuracy, even after after a lot of tuning. Clearly this approach was unsucessful. It should also be fairly obviousy by the complexity of the model that it should be overfitting the data massively, and still can not reach an acceptable accuracy. (4:30)

6. I wanted to have a better model, so I figured I could simplify my system. Instead of predicting the tempering conditions using the alloy properties and the final hardness, I could predict the continuous final hardness measure from the tempering conditions and alloy properties. A lot of my code was able to be reused by simply swapping the target dimensions. I chose Gradient Boosting Regression, and again a Neural Network model to compare. As seen the gradient boosting regression model performed very comparibly with the regresssion neural network model in this problem. The plot on the left clearly show that the gradient boosting regression model fits the data quite well. R2 scores are less than 0.1 which is quite good and looking at that plot, about the best we can expect. The data is plotted using the inverse transform of the y-scaled data, but the reported r-squared is using the scaled data, so that is why there is a bit of disconnect between the graph appearance and the r-squared score. (5:45)

7. Now that I have a satisfactory model I wanted to revist what may have been the cause of the failure of the first approach. Looking at the classification neural network loss over epochs was enlightening. Originally, when looking at the classifcation neural network results it was clear it struggled to predict tempering time, but looking at the loss history it is evident it failed to improve the model for tempering time predicitons at all. I concluded there was simply not enough data to predict tempering time and tempering temperature independantly. Additionally, if I attempted predicting them as paired units, 55 classes, as opposed to 5 and 11 independant classes, my dataset was small enough I would only have only 20-25 rows of support per class, which is insuficcent for modelling. (6:45)

8. Revisiting the goal of the problem. I aimed ot make an engineering tool that would predict the tempering conditions needed to reach a desired final hardness. Having failed to predict the tempering conditions directly, future work would either need to increase the size of the dataset, or implement a search algorythem combined with a non-neural network regression model like the gradient boost regression i used. The application would look much the same, input a steel and desired final hardness, then output the tempering conditions. Under the hood however it would generate batches of tempering conditions, predict the hardness output from the model, then itterate using a search algorythem to find a final output set of tempering conditions. (7:30)

9. The terms of next steps to be taken, I would like to develop an explainable model. Using PCA as I did confounds the ability to pull explainations from the regression model, as seen in the plot. I do not know what input features the PCA features correspond to. Figuring out how to implement some inverse_transformations, or skipping the PCA altogether would be important. However, I am aware that certain alloying elements have a much larger impact on hardness and tempering behaviors, so perhaps using using external domain knowledge and validation testing, someone more knowledgable than I may be able to assign signficance to the PCA model features.

9. Thank you for your time, I hope this was interesting! Do you have any Questions?