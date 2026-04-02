# 📊 [Project Title – To Be Decided]

## 👥 Team Members

- Dogu Nelin Icimsu
- Ilic Marko
- Azimi Mohammad Asif
- Salman Muhammad
- Rehman Zia Ur

---

## 🎯 Project Goal

This project is part of the _Business Intelligence 1_ course at the University of Vienna.

The goal is to go through the full BI pipeline:

- Define analytical questions
- Collect and integrate datasets
- Design a data model (star schema)
- Build a data processing pipeline
- Create a Tableau dashboard
- Extract meaningful insights

---

## 📌 Topic Description

We analyze how different lifestyle factors of students influence their academic performance. -> Just an example

The project focuses on understanding relationships between:

- study time
- sleep duration
- social activities
- health and habits

and how these factors affect student grades.

This topic is relevant because it can provide insights into how students can improve their academic outcomes by adjusting their daily habits.

---

## ❓ Analytical Questions

1. How does study time affect student performance?
2. Does sleep duration influence grades?
3. How do social activities (e.g., going out) impact academic results?
4. Are there differences in performance across demographic factors (e.g., age, gender)?
5. What combination of factors leads to the best academic outcomes?

---

## 📂 Datasets

We will use at least two datasets.

### Dataset 1 – Student Performance

- Source: Kaggle
- Description: Contains student grades and academic-related attributes
- Key attributes:
  - final grade
  - study time
  - absences
  - school

### Dataset 2 – Student Lifestyle / Habits

- Source: Kaggle
- Description: Contains lifestyle-related information
- Key attributes:
  - sleep duration
  - daily activities
  - social behavior
  - health indicators

---

### 🔗 Data Connection

The datasets will be connected using shared attributes such as:

- student ID (if available), or
- derived grouping (e.g., categories like study time, age group)

If no direct key exists, we will align datasets at an aggregated level.

---

## 🧱 Data Modeling

### 🔹 Fact Table

One row represents:

> A student's academic performance under specific lifestyle conditions

Measures:

- final grade (primary measure)
- absences (optional)

---

### 🔹 Dimensions

- 📅 Date (if applicable or derived)
- Study Time
- Sleep Duration
- Social Activity Level
- Demographics (age, gender, etc.)

---

### ⭐ Star Schema

- Fact table: Student Performance
- Dimension tables:
  - Student
  - Lifestyle
  - Time (optional)
  - Demographics

---

## ⚙️ Data Processing Pipeline

We will implement a pipeline in Python.

### 🔄 Data Transformation

- Select relevant columns
- Convert categorical values
- Create derived features (e.g., grouped study time)

### 🔗 Data Integration

- Merge datasets based on shared attributes or categories

### 🧹 Data Cleaning

- Handle missing values
- Normalize inconsistent values

### 📤 Output

- Clean dataset(s) structured as a star schema
- Ready for Tableau

---

## 📊 Data Analytics (Tableau)

We will build a dashboard that includes:

- Study time vs grades (bar/line chart)
- Sleep vs performance (scatter plot)
- Social activity vs grades
- Filters for demographics

---

## 💡 Key Insights

[TO BE FILLED AFTER ANALYSIS]

---

## 🛠️ Tools & Technologies

- Python (Pandas, NumPy)
- Tableau
- GitHub / GitLab

---

## 📅 Timeline

- Topic & datasets selection: ASAP
- Data modeling: Week 1
- Data processing: Week 2
- Dashboard creation: Week 3
- Final presentation: May 15, 2026

---

## 📁 Repository Structure
