## Question
Analyse the code provided in the attached link and briefly explain how the Factory Design Pattern is implemented. Highlight the relevant parts of the code that demonstrate the use of this pattern. The explanation should be concise and limited to a maximum of one page including what the outcome of the sample code. Share your GitHub link when you have done.

## Answer
    Factory Design Pattern is implemented using NamerFactory class. If the input includes a comma, then it will be assumed the first part (before comma) as lastname, and the remaining part as firstname. If there is no comma in input, the name will be assumed given as first name then first name again. There are two classes for these: LastFirst and FirstFirst. The factory class NamerFactory will choose LastFirst or FirstFirst by checking if the user input has a comma or not.

## Inout and output
    Enter name: Meryl Streep  
    Meryl Streep 
    Enter name: Streep, Meryl  
    Meryl Streep

## Note
Source code is from https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns
