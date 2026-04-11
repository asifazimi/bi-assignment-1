# 📊 [Project Title – Games]

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

- Define analytical questions ✅ (Completed)
- Design ER model (3NF) and Star Schema
- Build a data processing pipeline
- Create a Tableau dashboard
- Extract meaningful insights
- Presentation & report

---

## 📌 Topic Description

This project analyzes **video game success and player engagement** using data from multiple sources.

We combine:

- **Steam dataset** → business performance (price, owners, peak players)
- **RAWG dataset** → user perception (ratings, reviews, popularity)

---

## ❓ Analytical Questions

### 1. How does game price affect popularity and engagement?

**Columns used:**

- Steam: `price`
- RAWG: `rating`, `ratings_count`

---

### 2. Are highly rated games always widely recognized?

**Columns used:**

- RAWG: `rating`, `ratings_count`, `suggestions_count`

👉 Goal: Identify high-quality but less popular (hidden gem) games

---

### 3. Do multi-platform games perform better than PC-only games?

**Columns used:**

- RAWG: `platforms`
- Steam: `average`, `median`
- ***

### 4. Do higher Metacritic scores lead to higher popularity?

**Columns used:**

- RAWG: `metacritic`, `user score`
- Steam: `twitch`

---

### 5. Which game genres have grown the most over time?

**Columns used:**

- RAWG: `genres`, `released`
- Steam: `release_date`

👉 Measure:

- Number of games per genre per year

---

## 📂 Datasets

We use two main datasets from Kaggle:

### Dataset 1 – Steam Games Dataset

- Contains information about games available on Steam
- Key attributes:
  - `app_id`
  - `name`
  - `release_date`
  - `price`
  - `estimated_owners`
  - `peak_ccu`
  - `dlc_count`

---

### Dataset 2 – RAWG Games Dataset

- Contains aggregated game ratings and metadata
- Key attributes:
  - `id`
  - `name`
  - `released`
  - `rating`
  - `ratings_count`
  - `reviews_text_count`
  - `suggestions_count`
  - `metacritic`
  - `platforms`
  - `genres`

---

### 🔗 Data Connection

Datasets will be connected using:

- `name` (game title)

⚠️ Note:

- Names may differ slightly → preprocessing required:
  - lowercase conversion
  - removing special characters
  - trimming spaces

---

## 🧱 Data Modeling

### 🔹 Fact Table

One row represents:

> A single game with its performance and engagement metrics

**Measures:**

- `estimated_owners`
- `peak_ccu`
- `rating`
- `ratings_count`
- `suggestions_count`

---

### 🔹 Dimensions

- 📅 Date (release year, month)
- 🎮 Game (name, id)
- 🏷️ Genre
- 💻 Platform
- 💰 Price category (derived: low / medium / high)

---

### ⭐ Star Schema

- Fact table: Game Performance
- Dimension tables:
  - Game
  - Date
  - Genre
  - Platform
  - Price Category

---

## ⚙️ Data Processing Pipeline

Implemented in Python.

### 🔄 Data Transformation

- Select relevant columns
- Convert data types (dates, numeric)
- Create derived features:
  - release year
  - price categories

---

### 🔗 Data Integration

- Merge Steam and RAWG datasets using cleaned game names

---

### 🧹 Data Cleaning

- Handle missing values
- Normalize inconsistent naming
- Remove duplicates

---

### 📤 Output

- Clean dataset structured in star schema format
- Ready for Tableau

---

## 📊 Data Analytics (Tableau)

Dashboard will include:

- Price vs popularity (scatter plot)
- Ratings vs owners (correlation)
- Genre trends over time (line chart)
- Platform comparison (bar chart)
- Filters (genre, year, platform)

---

## 💡 Key Insights

[TO BE FILLED AFTER ANALYSIS]

---

## 🛠️ Tools & Technologies

- Python (Pandas, NumPy)
- Tableau
- GitHub / GitLab

---

## 📅 Timeline & Task Assignment

### Week 1 – Data Modeling

**Tasks:**

- ER model (3NF)
- Star schema design

**Assigned to:**

- Dogu Nelin Icimsu
- Ilic Marko

---

### Week 2 – Data Processing Pipeline

**Tasks:**

- Data cleaning
- Data transformation
- Data integration

**Assigned to:**

- Salman Muhammad
- Rehman Zia Ur

---

### Week 3 – Dashboard & Visualization

**Tasks:**

- Build Tableau dashboard
- Create visualizations for all analytical questions

**Assigned to:**

- Azimi Mohammad Asif
- Salman Muhammad
- Rehman Zia Ur
- Dogu Nelin Icimsu
- Ilic Marko

---

### Final Stage

**Tasks:**

- Extract insights
- Prepare presentation & report

**All members involved**

---

## 📁 Repository Structure
