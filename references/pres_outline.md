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
1|introduce the subject| 
2|describe the base problem and solution (work and temper)|
3|introduce the data and modelling goal|
4|data processing PCA | correlation plots
5|structure of multioutput problem| label balancing, pre/post. accuracy... didn't work
6|return to a simpler regression problem| introduce the regression problem, and the prediction
7|show GBR regression result, and improvement in R2 result when using NN.
8|
9|


## Script Notes
1. I'm going to be talking the tempering of steel today. I'm sure we've all bent a piece of metal back and forth until it breaks. Bending it, putting it through roller to thin a sheet, drawing it through a die to stretch a bar into wire, are called "working" a metal. All metal working causes different stresses to accumulate in the metal, and result in work hardening. Contiuned working makes the metal brittle and results in irrepairable cracking.

2. So, for example, we're halfway through bending a tube of steel into a chair, a fairly conplex shape. But we have work hardened it thoroughly in the process, making it stiff and brittle. Annealing a steel by heating it to a few hundred, or even several hundred degrees Celcius can soften the metal again so that more work can be done. Tempering is an almost identical process, but where annealing targets making the steel as soft as possible, tempering is done with a final target hardness in mind.

3. The dataset I'll be working with is from kaggle and has about 1500 rows. It was provided to the public by the company Raiipa, an metalurgical engineering firm focus on AI applications. The data is pulled from 3 scientific reviews, dating from 1945 to 2010. I chose to use this dataset to build an engineering tool that would allow the prediction of the tempering conditions, temperature and time, to reach a target hardness. 

4. To this end I build a multi-output multi-label classification problem. That is, I targetted 5 and 11 labels in the tempering time and tempering temperature in two different output columns.  I only had 1300 rows by the end of my data processing. I was suspected from my domain knowledge that this dataset might struggle to contain enough information to predict what I was trying to, so I attempted to add features through web scraping. I had to drop 7 materials (~200 rows) that I not could access additional informaion about online.And to indicate the multicolinearity of the resulting dataset, here is a correlation matrix before and after the PCA analysis I decided to do. 

5. I also struggled with data balancing. This dataset was made up of metric and imperial measurements, some of which had different labels for very similar actual temperatures, and some of which just were not represented throughly in the dataset. Here is a few plots on my data balance before and after processing. I attempted to use Extra forests Classifier and a two headed deep neural network to handle this complex classification problem, but even with extensive tuning I could not break a combined accuracy of 40% across my two columns, each with 5 and 11 labels. I figure I may have been able to improve performance by using the other target in the training data, and running 2 parallel models, but that is future work.

6. I wanted to have a better model, so I figured I could simplify my system. Instead of predicting the tempering conditions that result in a final hardness, I could predict the continuous final hardness measure from the dataset tempring conditions and material characteristics. A lot of my code was simply reused.