from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel



load_dotenv()
model=ChatGroq(
    model="llama-3.3-70b-versatile", 
    api_key=os.getenv("api_key"), 
    max_tokens=800, 
    temperature=0.7
    )

parser=StrOutputParser()

text="""
                Types of Logistic Regression
        Logistic regression can be classified into three main types based on the nature of the dependent variable:

        Binomial Logistic Regression: This type is used when the dependent variable has only two possible categories. Examples include Yes/No, Pass/Fail or 0/1. It is the most common form of logistic regression and is used for binary classification problems.
        Multinomial Logistic Regression: This is used when the dependent variable has three or more possible categories that are not ordered. For example, classifying animals into categories like "cat," "dog" or "sheep." It extends the binary logistic regression to handle multiple classes.
        Ordinal Logistic Regression: This type applies when the dependent variable has three or more categories with a natural order or ranking. Examples include ratings like "low," "medium" and "high." It takes the order of the categories into account when modeling.
        Assumptions of Logistic Regression
        Understanding the assumptions behind logistic regression is important to ensure the model is applied correctly, main assumptions are:



        Independent observations: Each data point is assumed to be independent of the others means there should be no correlation or dependence between the input samples.
        Binary dependent variables: It takes the assumption that the dependent variable must be binary, means it can take only two values. For more than two categories SoftMax functions are used.
        Linearity relationship between independent variables and log odds: The model assumes a linear relationship between the independent variables and the log odds of the dependent variable which means the predictors affect the log odds in a linear way.
        No outliers: The dataset should not contain extreme outliers as they 
        Independent Variables: These are the input features or predictor variables used to make predictions about the dependent variable.
        Dependent Variable: This is the target variable that we aim to predict. In logistic regression, the dependent variable is categorical.
        Logistic Function: This function transforms the independent variables into a probability between 0 and 1 which represents the likelihood that the dependent variable is either 0 or 1.


"""
prompt1=PromptTemplate(
    template=" Write short and simple notes from given {text}, \n ",
    input_variables=['text']
  
)

prompt2=PromptTemplate(
    template=" Write 5 short question answers from following {text}, \n ",
    input_variables=['text']
  
)

prompt3=PromptTemplate(
    template=" merge notes and quests in single document and Present notes -> {notes} and quests -> {quests} to the user",
    input_variables=['notes', 'quests']
)

# 2 parallel chains for generating notes and quests are made here 
parallel_chain=RunnableParallel({
    'notes':prompt1 | model | parser,
    'quests' : prompt2 | model | parser
}
)

merged_chain= prompt3 | model | parser

final_chain= parallel_chain | merged_chain
result=final_chain.invoke({'text': text})
print(result)

final_chain.get_graph().print_ascii()