# 🧪 Python OOP Practical Questions 

## 🚗 1. Vehicle, Car, and Bus – Abstract Class
**Problem:**  
Write a program that comprises of three classes, `Vehicle`, `Car`, and `Bus`, where `Car` and `Bus` are derived from `Vehicle`. Define an abstract method `movingSpeed()` in `Vehicle`, which must be implemented by `Car` and `Bus` to calculate the moving speed of car and bus objects.

**Expected Output:**  
```
Car Speed: 100 km/h  
Bus Speed: 60 km/h
```

---

## 🐾 2. Animal, Cat, and Dog – Abstract Method
**Problem:**  
Write a program consisting of an abstract class, `Animal`, that derives the classes `Cat` and `Dog`. Define an abstract method `sound()` which prints the sounds produced by a cat and a dog.

**Expected Output:**  
```
Meow  
Bark
```

---

## 🏢 3. Company, RioLearning, and AMCSquare
**Problem:**  
Write a program that consists of a completely abstract class, `Company`, which derives classes, `RioLearning` and `AMCSquare`. Class `Company` should contain general abstract methods about a company which will be redefined by `RioLearning` and `AMCSquare`.

**Expected Output:**  
```
RioLearning Details  
AMCSquare Details
```

---

## ➕ 4. Arithmetic Operations – Abstract Class
**Problem:**  
Write a program comprising of an abstract class `Arithmetic` that derives classes, `Divide`, `Multiply`, `Sum`, and `Subtract`. `Arithmetic` should contain an abstract method `performOperation()` which when called from derived class instances should perform relevant arithmetic operations.

**Expected Output:**  
```
Sum: 15
```

---

## 📺 5. TV Series Characters – Abstract Class
**Problem:**  
Write a program that consists of an abstract class `TVSeries` deriving classes `GameOfThrones`, `Narcos`, and `Vikings`. `TVSeries` should contain an abstract method `display()`, which when called through derived class instances displays the character list of the respective TV series.

**Expected Output:**  
```
Jon Snow, Arya Stark, Tyrion Lannister
```

---

## 🔺 6. Triangle and Trapezium – Area Calculation
**Problem:**  
Write a program comprising of two classes, `Triangle` and `Trapezium`. Both the classes must define a method, `calculate()`, that returns the area of the shape. Take relevant attributes in both the classes.

**Expected Output:**  
```
Area of Triangle: 25.0
```

---

## 📐 7. Shape – Area Method Overloading
**Problem:**  
Write a program consisting of a single class `Shape`, which defines a method `area()`. Overload the method `area()` to return the area of the shapes, triangle and rectangle, one at a time.

**Expected Output:**  
```
Area of Triangle: 25.0  
Area of Rectangle: 50.0
```

---

## 🔁 8. Multilevel Inheritance: A -> B -> C
**Problem:**  
Write a program consisting of three classes, A, B, and C, related through multilevel inheritance. The order of derivation is A -> B -> C and each class defines a method `display()`. Create an instance of the class C, which accesses the method `display()` in the following class order: B -> C -> A.

**Expected Output:**  
```
Display from B  
Display from C  
Display from A
```

---

## 🧬 9. Constructors without `super()` – Base & Derived
**Problem:**  
Write a program that consists of two classes, `Base` and `Derived`, where `Base` derives `Derived`. Define a constructor and a method in each class. Access the method of the class `Base` through an instance of the class `Derived` without using `super()` method.

**Expected Output:**  
```
Base Variables: x=10, y=20
```

---

## 🧱 10. Shape and Cuboid – Inheritance
**Problem:**  
Write a program that contains two classes, viz., `Shape` and `Cuboid`. Derive the class `Cuboid` from class `Shape`, where `Shape` contains basic shape attributes and methods, and `Cuboid` contains information related to cuboid only.

**Expected Output:**  
```
Volume of Cuboid: 150.0
```

---

## 👥 11. Person, Employee and Student
**Problem:**  
Write a program with three classes, viz., `Person`, `Employee`, and `Student`. The classes `Employee` and `Student` are the subclasses of the class `Person`. Each class should have at least three methods.

**Expected Output:**  
```
Name: John  
Gender: Male  
Age: 30  
Position: Software Engineer
```

---

## 🏦 12. Bank and Account – Superclass Inheritance
**Problem:**  
Write a program that contains a super class `Bank`. Derive a class `Account` from the class `Bank`, which contains details about a specific account.

**Expected Output:**  
```
Bank Name: State Bank  
Account Holder: Deep  
Account No: 123456789
```

---

## 🏆 13. Tournament Teams and Players
**Problem:**  
Write a program that models a tournament of 10 teams with 11 players in each team. Maintain a record of each player, and the number of wins and losses of each team.

**Expected Output:**  
```
Team A - Wins: 1, Losses: 0
```

---

## 🦘 14. Animal, Dog, Cat, Kangaroo – Information Storage
**Problem:**  
Write a program that consists of four classes, viz., `Animal`, `Dog`, `Cat`, and `Kangaroo`. The class `Animal` is the super class and stores common properties. Other classes should contain animal-specific info and be able to store and display all details.

**Expected Output:**  
```
Animal: Dog  
Legs: 4  
Weight: 15kg  
Name: Tommy
```

---