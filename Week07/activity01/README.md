## Question 1
Code Execution
Run the code and verify whether it executes successfully.
    Are there any compilation or runtime errors?
    If yes, briefly describe them.

## Answer
    No error.

## Question 2
Factory Design Pattern Usage
Identify which part of the project demonstrates the Factory design pattern.
    Explain this usage briefly and clearly.
    What problem does the Factory pattern solve in this context?

## Answer

factory.py is the key part of the project that demonstrates the Factory pattern. It takes care of creating the required notification object as required.

The problem solved by this pattern in this context is the user of the notification classes can create the required notification type on the fly.

## Question 3
Without Using the Factory Pattern  (can I develop this project without design pattern - push the project in two version into your GitHub including current and updated version?)
Discuss what changes would be required if the Factory design pattern were not used.
    How would the client code need to be modified?
    What impact would this have on flexibility, maintainability, and scalability?

## Answer
Answer is inline in main_nodp.py.