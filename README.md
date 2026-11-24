# Sports Performance Analyzer

A Python-based project developed to analyze, compare, and visualize sports players' performance using match scores.

## About the Project

The Sports Performance Analyzer is a Python project that reads player match scores from a CSV file, cleans invalid data, performs statistical analysis, and identifies the top-performing player.

It helps reduce manual calculations and makes player performance analysis easier through data visualization.

## Features

- Load player data from a CSV file.
- Clean invalid, missing, and negative score values.
- Calculate player-wise average, best, and total scores.
- Identify the top performer based on average score.
- Calculate overall statistical values:
  - Mean
  - Median
  - Standard Deviation
  - Maximum Score
  - Minimum Score
- Display match-wise average scores.
- Generate line charts and bar charts for visualization.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| Pandas | Data loading, cleaning, and analysis |
| NumPy | Statistical calculations |
| Matplotlib | Data visualization |
| CSV | Storing player match data |

## Project Structure

```text
Sports-Performance-Analyzer/
│
├── Code/
│   ├── sports_performance_analyzer.py
│   └── scores.csv
│
└── Documentation/
    ├── Sports_Performance_Analyzer_Project_Report.docx
    └── Sports_Performance_Analyzer_Presentation.pptx
```

## How to Run the Project

1. Install Python 3.
2. Install the required libraries:

```bash
pip install pandas numpy matplotlib
```

3. Download or clone this repository.
4. Make sure `scores.csv` is in the same folder as the Python source code.
5. Run the program:

```bash
python sports_performance_analyzer.py
```

## Sample CSV Data

| Player | Match | Score |
|---|---:|---:|
| Aman | 1 | 40 |
| Aman | 2 | 60 |
| Riya | 1 | 30 |
| Riya | 2 | 50 |

## Project Information

- **Project Name:** Sports Performance Analyzer
- **Problem Statement:** PS 23
- **Subject:** Python Programming
- **Programme:** BCA – Artificial Intelligence and Machine Learning
- **University:** Rungta International Skills University

## Future Scope

- Database integration.
- Graphical User Interface (GUI).
- Support for more sports and players.
- Exporting performance reports.

## Author

**Karan Paidumkar**

BCA – Artificial Intelligence and Machine Learning

---

*Developed as an academic project for Python Programming.*
