## Question: 
### Explain your understanding of at least three design patterns used in the code below, and discuss the advantages and disadvantages of each pattern. Share your GitHub link here when you have done.

## Answer:
Three design patterns used in the codes are:
1. Fatctory pattern (Maker class)
2. Singleton pattern (Keeper class)
3. Observer pattern (Watcher class)

### Advantages

#### Factory pattern: 
Decoupling: The main code doesn't need to know the names of specific classes (Helper, Friend). 
Consistency: It ensures that every object is created with the correct parameters every time.

#### Singleton pattern: 
Resource control: The instance (Keeper) can be accessed from anywhere in the project and it is the same one (There is only ONE instance of the class).
Global access:It prevents multiple objects from fighting over the same data or resource.

#### Observer pattern:
Expandability: New functionality (notification types in example) can be added without touching the logic of the other class (Bot / Unit-based classes in the example).
Clean code: Businness logic of one class (Bot / Unit-based classes in the example) and the business logic of Watcher are separated.

### Disadvantages

#### Factory pattern:
Complexity: It can be seen in a way that a extra class and method is written just to instantiate objects.
Maintenance: To add a new type, Factory logic must be adjusted accordingly.

#### Singleton pattern:
Test Nightmare: Since the state persists, one test can "pollute" the next one, leading to confusing bugs.
Hidden Dependencies: It makes it harder to see how data is flowing through the app since the Singleton is "just there" globally.

#### Observer pattern:
Order of operations: In the real world scenario, there is no easy control which Observer reacts first (e.g., does it log to the file before or after the screen?).
Memory Leak: In the case of failing to "detach" observers when it is done with them, they can stay in memory forever.
