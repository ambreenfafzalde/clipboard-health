# Healthcare Nurse Staffing Analysis

## Project Overview

This project analyzes nursing staffing data from the Payroll-Based Journal (PBJ) Daily Nurse Staffing dataset for Q2 2024.

The analysis uses Python, Pandas, and Streamlit to explore staffing patterns, patient census, and the use of contract nursing staff across healthcare facilities and states.

## Project Objectives

1. Analyze nurse staffing levels across states and facilities.
2. Examine the relationship between nurse staffing hours and patient census.
3. Identify states with higher reliance on contract nursing staff.
4. Calculate average patient census by facility and state.
5. Identify facilities reporting the highest staffing hours.
6. Investigate missing values, duplicates, and potential staffing outliers.

## Technologies Used

- **Python:** Data processing and analysis
- **Pandas:** Data cleaning, transformation, and aggregation
- **Streamlit:** Interactive dashboard development
- **VS Code:** Development environment
- **GitHub:** Version control and project documentation

## Dataset Description

**Dataset:** PBJ_Daily_Nurse_Staffing_Q2_2024.csv

The dataset includes nursing staffing hours, facility information, reporting dates, and resident census.

### Important Columns

| Column | Description |
|---|---|
| PROVNUM | Facility identifier |
| PROVNAME | Facility name |
| STATE | State |
| WorkDate | Staffing reporting date |
| MDScensus | Resident census |
| Hrs_RN | Registered nurse hours |
| Hrs_LPN | Licensed practical nurse hours |
| Hrs_CNA | Certified nursing assistant hours |
| Hrs_RN_ctr | Contract RN hours |
| Hrs_LPN_ctr | Contract LPN hours |
| Hrs_CNA_ctr | Contract CNA hours |

## Data Cleaning and Preparation

The analysis includes:

- Loading CSV data using `cp1252` encoding.
- Converting `WorkDate` into a datetime format.
- Checking for missing values and duplicate records.
- Reviewing negative staffing hours and extreme outliers.
- Creating derived staffing metrics.
- Grouping records by state, facility, and reporting period.

### Derived Metrics

**Total Nurse Staffing Hours**

Total Nurse Hours = RN Hours + LPN Hours + CNA Hours

**Total Contract Hours**

Contract Hours = Contract RN Hours + Contract LPN Hours + Contract CNA Hours

**Contract Staffing Percentage**

Contract Staffing % = (Contract Hours / Total Nurse Hours) × 100

These metrics help compare staffing patterns across facilities and states.

## Analytics Questions

### 1. What is the relationship between staffing levels and patient census?

Compare nurse staffing hours with resident census to understand staffing resources relative to facility size.

A useful normalized metric is nursing hours per resident day.

### 2. What are the average staffing levels by state?

Aggregate staffing hours by state and compare staffing intensity using resident census.

### 3. Are certain states relying more on contract nurses?

Calculate the percentage of nursing hours provided by contract staff for each state.

Higher percentages indicate greater reliance on contract nursing hours relative to total reported nursing hours.

### 4. What is the average patient census?

Calculate mean resident census by facility and state to examine differences in facility size and resident population.

### 5. Which facilities report the highest staffing hours?

Rank facilities by total staffing hours for the reporting period.

## Analytics Insights and Interpretation

The project is designed to investigate the following patterns:

**Staffing and Patient Census**

Facilities with larger resident populations may report more total staffing hours. Comparing hours per resident day provides a more meaningful staffing measure than comparing raw hours alone.

**Contract Nurse Utilization**

Contract staffing percentages help identify geographic differences in staffing models. A high percentage indicates greater use of contract nursing hours but does not independently establish a staffing shortage.

**Facility Staffing Differences**

Facilities may vary considerably in total nursing hours because of differences in resident population, facility size, and staffing requirements.

**Data Quality**

Missing values, duplicate records, negative staffing hours, and extreme observations should be investigated before interpreting results.

## Limitations

- Analysis covers Q2 2024 rather than multiple years.
- Staffing hours do not directly measure the number of individual nurses.
- Contract staffing reliance does not necessarily indicate a shortage.
- Total staffing hours should be normalized by resident census when comparing facilities.
- Overtime cannot be reliably determined from staffing-hour totals alone without overtime-specific information.
- The dataset is excluded from the GitHub repository because of its large size.

## Dashboard

The Streamlit dashboard presents nursing staffing analysis and summary tables, including staffing hours, contract utilization, and average patient census.

## Future Improvements

- Add interactive state and facility filters.
- Visualize staffing hours per resident day.
- Add state-level contract staffing comparisons.
- Explore monthly staffing trends.
- Optimize large-data handling in Streamlit.
- Expand the analysis to additional quarters.

## Conclusion

This project demonstrates practical skills in healthcare data analysis, data cleaning, feature engineering, aggregation, and dashboard development.

The analysis provides a framework for understanding nursing staffing patterns, resident census, and contract staff utilization across healthcare facilities.