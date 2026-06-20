# Saudi Job Market Analysis — Jadarat Dataset

An end-to-end data analytics project exploring the Saudi Arabian job market using listings sourced from the **Jadarat** platform. The project covers data cleaning, exploratory data analysis (EDA) in Python, and an interactive Power BI dashboard.

---

## Dashboard Preview

![Jadarat Dashboard](src/dashboard_preview.png)

> **Key Metrics at a Glance**
>
> | Metric | Value |
> |---|---|
> | Total Job Listings | 1,470 |
> | Average Salary | 5,290 SAR |
> | Maximum Salary | 35,000 SAR |
> | Minimum Salary | 3,000 SAR |
> | Average Experience Required | 1.28 years |

---

## Project Structure

```
jadaratData/
├── data/
│   ├── processed_dataset.csv   # final dataset
│   └── saudi_jobs_cleaned.csv  # intermediate dataset
├── src/
│   └── dashboard_preview.png   # dashboard screenshot
├── analysis.ipynb              # EDA notebook
├── jadaratDashboard.pbix       # Power BI dashboard
└── README.md
```

---

## Dataset

> **Source:** [Jadarat Cleaned Data — Kaggle](https://www.kaggle.com/datasets/shaykhaaldawsari/jadarat-cleaned-data-csv?resource=download)

The processed dataset contains **1,470 rows** and **14 columns** with zero missing values after cleaning.

| Column | Type | Description |
|---|---|---|
| `job_title` | str | Standardized role (e.g., Analyst, Accountant) |
| `job_date` | str | Job posting date (Gregorian) |
| `comp_name` | str | Company name (original Arabic) |
| `comp_type` | int | `1` = Private, `0` = Semi-Governmental |
| `comp_size` | str | Size code (SB = Small B, MA = Medium A, …) |
| `eco_activity` | str | Industry sector (e.g., Trade and Retail, Healthcare) |
| `region` | str | Saudi region — translated & normalized |
| `city` | str | City name — translated & normalized |
| `contract` | int | `1` = Full-time, `0` = Remote |
| `benefits` | int | `1` = Benefits offered, `0` = None |
| `positions` | int | Number of open positions |
| `exper` | int | Years of experience required |
| `gender` | int | `0` = Male, `1` = Female, `2` = Both |
| `Salary` | float | Monthly salary in SAR |

---

## Key Findings

### Top Job Titles
| Rank | Job Title | Count |
|---|---|---|
| 1 | Analyst | 235 |
| 2 | Salesperson | 195 |
| 3 | Accountant | 128 |
| 4 | Manager | 127 |
| 5 | Technician | 112 |

### Average Salary by Region
**Northern Borders** leads with the highest average at **8,300 SAR**, while Jazan is the lowest at **4,020 SAR**.

| Region | Avg. Salary (SAR) |
|---|---|
| Northern Borders | 8,300 |
| Hail | 6,455 |
| Tabuk | 6,345 |
| Al Baha | 5,902 |
| Najran | 5,750 |
| Riyadh | 5,360 |

### Salary by Sector
Technology and Logistics sectors command the highest average salaries, while Food Services and Gym & Fitness are at the lower end.

### Salary vs. Experience
A clear positive correlation — professionals with 10+ years earn significantly more than entry-level candidates.

---

## Machine Learning Model

Trained and compared 3 regression models to predict employee salary in SAR.

### Model Comparison

| Model | MAE (SAR) | R² Score |
|---|---|---|
| **Random Forest** | **913** | **0.43** |
| Decision Tree | 1,066 | — |
| Linear Regression | 1,210 | — |
| Cross Validation (RF) | 1,134 | — |

> **Best Model: Random Forest** with the lowest prediction error.

### Top Predictive Features

| Rank | Feature | Importance |
|---|---|---|
| 1 | Experience | 35% |

---

## Tools & Stack

| Tool | Purpose |
|---|---|
| Python (pandas, numpy) | Data cleaning & transformation |
| Matplotlib / Seaborn | Exploratory visualizations |
| Power BI | Interactive dashboard |

---

## How to Run

**Python Notebook**
```bash
pip install pandas numpy matplotlib seaborn jupyter
jupyter notebook analysis.ipynb
```

**Power BI Dashboard**

Open `jadaratDashboard.pbix` in [Power BI Desktop](https://powerbi.microsoft.com/desktop/).

---

## Data Source

Job listings collected from **Jadarat** (جدارات) — the Saudi national job portal operated under the Human Resources Development Fund (HRDF).

Dataset published on Kaggle: [shaykhaaldawsari/jadarat-cleaned-data-csv](https://www.kaggle.com/datasets/shaykhaaldawsari/jadarat-cleaned-data-csv?resource=download)
