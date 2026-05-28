# Student Attendance Analysis

## 📌 Project Overview

Student Attendance Analysis is a Python-based data analysis project that reads attendance records from an Excel file, calculates attendance percentages, identifies students with low attendance, and visualizes attendance statistics using a bar chart.

This project demonstrates the use of **Pandas**, **NumPy**, and **Matplotlib** for data processing, analysis, and visualization.

---

## 🚀 Features

* Read attendance data from an Excel file
* Calculate attendance percentage for each student
* Find average class attendance
* Identify students below the minimum attendance requirement (75%)
* Find students with the highest and lowest attendance
* Generate an attendance report
* Export the processed data to a new Excel file
* Visualize attendance using a bar chart

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* OpenPyXL

---

## 📂 Project Structure

```text
Student-Attendance-Analysis/
│
├── StuAtt.py
├── attendance.xlsx
├── attendance_report.xlsx
└── README.md
```

---

## 📊 Input Data Format

The Excel file should contain the following columns:

| student  | classes_Attended | total_classes |
| -------- | ---------------- | ------------- |
| Sanjay   | 92               | 100           |
| Nishanth | 85               | 100           |
| Saran    | 61               | 100           |
| Tarun    | 75               | 100           |

---

## ⚙️ Installation

Install the required Python libraries:

```bash
pip install pandas numpy matplotlib openpyxl
```

---

## ▶️ How to Run

```bash
python StuAtt.py
```

---

## 📈 Output

The program generates:

* Attendance percentage for each student
* Average attendance percentage
* Highest attendance student
* Lowest attendance student
* Students below 75% attendance
* Attendance visualization chart
* Excel report file (`attendance_report.xlsx`)

---

## 📋 Sample Output

```text
Attendance Report

Average Attendance: 68.80%

Highest Attendance:
Sanjay - 92.00%

Lowest Attendance:
matte - 18.00%

Students Below 75% Attendance:
Saran - 61.00%
manikanta - 59.00%
Shyam - 74.00%
matte - 18.00%
siddhu - 55.00%
```

---

## 📉 Visualization

The project displays a bar chart showing:

* Student attendance percentages
* A reference line indicating the minimum required attendance (75%)

This helps quickly identify students who are at risk of falling below attendance requirements.

---

## 🎯 Learning Outcomes

Through this project, I learned:

* Reading Excel files using Pandas
* Data manipulation and analysis
* Statistical calculations using NumPy
* Data visualization using Matplotlib
* Exporting processed data to Excel
* Building real-world data analysis projects

---

## 🔮 Future Enhancements

* Subject-wise attendance analysis
* Monthly attendance tracking
* Pie chart visualization
* Interactive dashboard using Streamlit
* Attendance prediction using Machine Learning

---

## 👨‍💻 Author

**Sanjay Nishanth**

GitHub: https://github.com/pallasanjaynishanth
