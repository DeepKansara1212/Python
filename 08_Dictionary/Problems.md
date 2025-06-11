# 🐍 Python Dictionary Problems

## 🔹 Problem 1: Merge Two Dictionaries

**Task:** Write a Python program to **merge two dictionaries** into one.

**Example:**  
Input:  
`dict1 = {'a': 100, 'b': 200}`  
`dict2 = {'x': 300, 'y': 400}`  
Output:  
`{'a': 100, 'b': 200, 'x': 300, 'y': 400}`

---

## 🔹 Problem 2: Sum All Values in a Dictionary

**Task:** Write a Python program to **sum all the values** in a dictionary.

**Example:**  
Input: `{'a': 10, 'b': 20, 'c': 30}`  
Output: `Total Sum: 60`

---

## 🔹 Problem 3: Count Frequency of Elements in a List

**Task:** Write a Python program to **count the frequency of each element** in a list using a dictionary.

**Example:**  
Input: `['apple', 'banana', 'apple', 'orange', 'banana', 'banana']`  
Output: `{'apple': 2, 'banana': 3, 'orange': 1}`

---

## 🔹 Problem 4: Combine Two Dictionaries (Add Common Key Values)

**Task:** Combine two dictionaries by **adding values for common keys**.

**Example:**  
Input:  
`d1 = {'a': 100, 'b': 200, 'c': 300}`  
`d2 = {'a': 300, 'b': 200, 'd': 400}`  
Output: `{'a': 400, 'b': 400, 'c': 300, 'd': 400}`

---

## 🔹 Problem 5: Check if Key Exists in Dictionary

**Task:** Check whether a given **key exists** in a dictionary.

**Example:**  
Input: `{'name': 'Alice', 'age': 25}`, Key: `'age'`  
Output: `Key exists.`

---

## 🔹 Problem 6: Extract Unique Values from Dictionary

**Task:** Extract all **unique values** from dictionary values (list format).

**Example:**  
Input: `{'A': [1, 2, 3], 'B': [2, 3, 4], 'C': [4, 5]}`  
Output: `{1, 2, 3, 4, 5}`

---

## 🔹 Problem 7: Find the Key with Maximum Value

**Task:** Find the **key(s) with the maximum value** in a dictionary.

**Example:**  
Input: `{'Alice': 87, 'Bob': 91, 'Charlie': 85}`  
Output: `Key(s) with max value: ['Bob']`

---

## 🔹 Problem 8: Invert a Dictionary

**Task:** Invert a dictionary by **swapping keys and values**.

**Example:**  
Input: `{'a': 1, 'b': 2, 'c': 3}`  
Output: `{1: 'a', 2: 'b', 3: 'c'}`

---

## 🔹 Problem 9: Create Dictionary from Two Lists

**Task:** Create a dictionary by **combining two lists** (keys and values).

**Example:**  
Input: `keys = ['name', 'age', 'city']`, `values = ['John', 25, 'New York']`  
Output: `{'name': 'John', 'age': 25, 'city': 'New York'}`

---

## 🔹 Problem 10: Remove Duplicate Values from Dictionary

**Task:** Remove duplicate values from a dictionary, keeping only the **first occurrence**.

**Example:**  
Input: `{'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}`  
Output: `{'a': 1, 'b': 2, 'e': 3}`

---

## 🔹 Project: Student Information Retrieval System

**Task:** Build a **console-based Student Information Retrieval System** using nested dictionaries.  
Each student is identified by a **roll number**, and associated with their **Name**, **Phone Number**, and **Percentage**.

Prompt the user to:
- Enter a roll number
- Choose which information to display:
  - `n` → Name
  - `ph` → Phone Number
  - `p` → Percentage

**Additional Requirement:**
- Show the **total number of students**
- Display output in a user-friendly message format

**Example:**  
Input:  
```python
students = {
  '123': {'Name': 'John', 'Ph': '9999999999', 'Percentage': '82%'},
  '456': {'Name': 'Adam', 'Ph': '8888888888', 'Percentage': '91%'},
  '789': {'Name': 'Eva', 'Ph': '7777777777', 'Percentage': '85%'}
}

User Input:
Enter Roll Number: 456
Choose Detail to Fetch (n/ph/p): n

Output:
The total number of students are: 3
The Name of the Student with roll no: 456 is Adam.