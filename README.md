# Project Title – Games

## Team Members

- Dogu Nelin Icimsu
- Ilic Marko
- Azimi Mohammad Asif
- Salman Muhammad
- Rehman Zia Ur

---

## Project Goal

This project is part of the _Business Intelligence 1_ course at the University of Vienna.

The goal is to go through the full BI pipeline:

- Define analytical questions (Completed)
- Design ER model (3NF) and Star Schema
- Build a data processing pipeline
- Create a Tableau dashboard
- Extract meaningful insights
- Presentation & report

---

## Topic Description

This project analyzes **video game success and player engagement** using data from multiple sources.

We combine:

- **Steam dataset** -> business performance (price, owners, peak players)
- **RAWG dataset** -> user perception (ratings, reviews, popularity)

---

## Analytical Questions

### 1. How does game price affect popularity and engagement?

**Columns used:**

- Steam: `price`
- RAWG: `rating`, `ratings_count`

---

### 2. Are highly rated games always widely recognized?

**Columns used:**

- RAWG: `rating`, `ratings_count`, `suggestions_count`

Goal: Identify high-quality but less popular (hidden gem) games

---

### 3. Do multi-platform games perform better than PC-only games?

**Columns used:**

- RAWG: `platforms`
- Steam: `average`, `median`

---

### 4. Do higher Metacritic scores lead to higher popularity?

**Columns used:**

- RAWG: `metacritic`, `user score`
- Steam: `twitch`

---

### 5. Which game genres have grown the most over time?

**Columns used:**

- RAWG: `genres`, `released`
- Steam: `release_date`

Measure:

- Number of games per genre per year

---

## Datasets

We use two main datasets from Kaggle:

### Dataset 1 - Steam Games Dataset

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

### Dataset 2 - RAWG Games Dataset

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

### Data Connection

Datasets are connected using:

- `name` (game title)

Note:

- Names may differ slightly, so preprocessing is required:
  - lowercase conversion
  - removing special characters
  - trimming spaces

---

## Data Modeling

### Fact Table - FactGame

One row represents a single game's measurable performance.

**Measures:**

- `price`
- `average_playtime`
- `median_playtime`
- `rating`
- `ratings_count`
- `suggestions_count`

**Foreign keys:** `game_id`, `date_id`

---

### Dimensions

- **DimDate** - `date_id`, `release_date`, `year`, `month`
- **DimGame** - `game_id`, `steam_name`, `rawg_name`, `matched_name`, `pc_only`
- **DimGenre** - `genre_id`, `genre_name`
- **BridgeGameGenre** - `game_id`, `genre_id` (resolves the many-to-many between games and genres)

---

### Star Schema

![Star Schema](https://github-production-user-asset-6210df.s3.amazonaws.com/31056603/583907402-7fccbbc4-9207-4a25-9880-b7b3d2d9b59a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20260426%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260426T192531Z&X-Amz-Expires=300&X-Amz-Signature=cd0c8a878fcbb72cc2736098a71e707eb9a89380dbbf529e9d1426d16c241221&X-Amz-SignedHeaders=host&response-content-type=image%2Fpng)

- Fact table: FactGame
- Dimension tables: DimGame, DimDate, DimGenre
- Bridge table: BridgeGameGenre

---

## Data Processing Pipeline

Implemented in Python (pandas). See `PIPELINE.md` for the full walkthrough.

### Data Transformation

- Select relevant columns
- Convert data types (dates, numeric)
- Create derived features (release year, release month, `pc_only`)

---

### Data Integration

- Merge Steam and RAWG datasets using normalized game names

---

### Data Cleaning

- Handle missing values
- Normalize inconsistent naming
- Remove duplicates

---

### Output

The pipeline produces a flat cleaned table and the star-schema split:

- `output/matched_clean.csv` - cleaned, merged flat table
- `output/star/fact_game.csv`
- `output/star/dim_game.csv`
- `output/star/dim_date.csv`
- `output/star/dim_genre.csv`
- `output/star/bridge_game_genre.csv`

Run with:

```bash
.venv/bin/python main.py
```

---

## Data Analytics (Tableau)

Dashboard will include:

- Price vs popularity (scatter plot)
- Ratings vs owners (correlation)
- Genre trends over time (line chart)
- Platform comparison (bar chart)
- Filters (genre, year, platform)

---

## Key Insights

[TO BE FILLED AFTER ANALYSIS]

---

## Tools & Technologies

- Python (Pandas, NumPy)
- Tableau
- GitHub / GitLab

---

## Timeline & Task Assignment

### Week 1 - Data Modeling

**Tasks:**

- ER model (3NF)
- Star schema design

**Assigned to:**

- Dogu Nelin Icimsu
- Ilic Marko

---

### Week 2 - Data Processing Pipeline

**Tasks:**

- Data cleaning
- Data transformation
- Data integration

**Assigned to:**

- Salman Muhammad
- Rehman Zia Ur

---

### Week 3 - Dashboard & Visualization

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

## Repository Structure
