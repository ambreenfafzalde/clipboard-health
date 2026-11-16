import streamlit as st
import pandas as pd
from io import StringIO


# Your existing code that loads and prepares provider_data goes here.



df = pd.read_csv('PBJ_Daily_Nurse_Staffing_Q2_2024.csv', 
                 encoding="cp1252"
                )

st.set_page_config(layout="wide")
pd.set_option("display.max_columns", 30)

df['WorkDate'] = pd.to_datetime(
    df['WorkDate'].astype("string"),
    format="%Y%m%d",
    errors="coerce"
)


st.title("Nurse Staffing Analysis")
st.subheader("Daily Staffing Records")
st.dataframe(df.head(100))

provider_data = df[['PROVNUM', 'PROVNAME', 'CITY', 'STATE', 'COUNTY_NAME', 'COUNTY_FIPS', 'WorkDate', 'CY_Qtr', 'MDScensus']]

st.title("Provider Data")
st.subheader("Hospitals and Patient Analytics")
st.dataframe(provider_data.head(100))


# print(provider_data.isna().sum())

# print(provider_data.duplicated().sum())

# print(provider_data.info())


st.subheader("Missing Values")

# Missing values by column
missing_values = (
    provider_data
    .isna()
    .sum()
    .rename_axis("Columns")
    .reset_index(name="Missing values")
    
)
st.dataframe(missing_values, width="stretch")

# Duplicate Values

duplicate_count = provider_data.duplicated().sum()
st.subheader("Duplicate Values")
st.metric("Duplicate Count:", f"{duplicate_count}")

staffing_hours= df[[ 
    'Hrs_RN',
       'Hrs_RN_emp',
     'Hrs_RN_ctr',
 'Hrs_LPN',
 'Hrs_LPN_emp',
 'Hrs_LPN_ctr',
 'Hrs_CNA',
 'Hrs_CNA_emp',
 'Hrs_CNA_ctr',
 'Hrs_NAtrn',
 'Hrs_MedAide'
                   ]]



st.title("Nurses Data")
st.subheader("Nurse Hours - Employees and Contract")
st.dataframe(staffing_hours.head(100))

st.subheader("Missing Data for Nurses")

# Missing values by column
missing_nurse_data = (
    staffing_hours
    .isna()
    .sum()
    .rename_axis("Columns")
    .reset_index(name="Missing values")
    
)
st.dataframe(missing_nurse_data, width="stretch")

# Duplicate Values

duplicate_nurse_count = staffing_hours.duplicated().sum()
st.subheader("Duplicate Values")
st.metric("Duplicate Count:", f"{duplicate_nurse_count}")


# Check unrealistic staffing values (extreme outliers)

st.subheader("Unrealistic staffing values and extreme outliers")
negative_rows = staffing_hours[(staffing_hours < 0).any(axis=1)]
st.dataframe(negative_rows, width="stretch")


# • Create derived columns for total nurse hours
st.subheader("New column added for total nurse hours, this includes fulltime  RN, LPN and CNAs")
staffing_hours["total_nurse_hours"] = staffing_hours[['Hrs_RN', 'Hrs_LPN', 'Hrs_CNA']].sum(
    axis=1
)
st.dataframe(staffing_hours)

# You must select 3–5 metrics that can be calculated from the dataset.


# 1. Nurse-to-Patient Ratio
# Formula:
# (Total RN + LPN + CNA Hours) / Patient Census
# This measures staffing coverage relative to patient load.

provider_data['total_nurse_hours'] = staffing_hours['total_nurse_hours']

provider_data['nurse_to_patient_ratio'] = provider_data['total_nurse_hours']/ provider_data['MDScensus'] 

st.subheader("Nurse-to-Patient Ratio")

st.write('Which facilities have the lowest nurse-to-patient coverage?')


st.write('There are some facilites that are showing 0 patient-to-nurse coverage and some rows are NaN, need to check if this is a data issue')
nurse_to_patient_ratio = provider_data.loc[:,['nurse_to_patient_ratio', 'PROVNAME']]
st.dataframe(nurse_to_patient_ratio,width="content" )

# 2. Total Nurse Hours
# Total nurse hours worked per hospital per month.
# Group by:
# • Hospital
# • State
# • Month

provider_data['month'] = provider_data['WorkDate'].dt.month

result = (
    provider_data
    .groupby(['PROVNAME', 'STATE', 'month'], as_index=False)['total_nurse_hours']
    .sum()
   
)

result = provider_data.loc[:,['PROVNAME','total_nurse_hours', 'month']]



st.subheader("Total nurse hours worked per hospital per month")
st.dataframe(result,width="content")


# 3. Contract vs Permanent Staff Ratio
# Formula:
# Contract Staff Hours / Total Nurse Hours
# Helps understand reliance on temporary staff.


st.subheader("Contract vs Permanent Staff Ratio")
staffing_hours['contract_hours'] = staffing_hours[['Hrs_RN_ctr', 'Hrs_LPN_ctr', 'Hrs_CNA_ctr']].sum(axis=1)
staffing_hours['ctr_emp_ratio'] = staffing_hours['contract_hours']/staffing_hours['total_nurse_hours']
ctr_perm_ratio = staffing_hours.loc[
    staffing_hours['ctr_emp_ratio'] > 0,
    'ctr_emp_ratio'
]
st.dataframe(ctr_perm_ratio, width="content")



# 4. Average Patient Census
# Average number of patients per hospital or per state.

result = (
    provider_data
    .groupby(['PROVNAME', 'STATE'])['MDScensus']
    .mean()
    .reset_index(name="avg_patient_census")

   
)

st.subheader("Average Patient Census")
avg_patient_census = result.loc[:, ['PROVNAME', 'STATE', "avg_patient_census"]]
st.dataframe(avg_patient_census, width="content")


# 5. Hospitals with Highest Staffing Hours
# Identify hospitals with the highest total staffing hours.

result = provider_data.sort_values(by='total_nurse_hours', ascending=False)
st.subheader("Hospitals with Highest Staffing Hours")
st.dataframe(result, width="content")



st.write('Which hospitals have the highest staffing hours?')
st.write('MARIGOLD REHABILITATION HCC, GALESBURG IL has the highest staffing hours at 14079 total staffing hours \nFollowed by ISABELLA GERIATRIC CENTER INC in New York, NY with highest at 693')




avg_staffing_levels = (provider_data
                        .groupby('STATE', as_index=False)['total_nurse_hours']
                        .mean()
                        .round(2)
                        .sort_values(by='total_nurse_hours', ascending=False)
                    

    
)
st.subheader("What are the average staffing levels by state?")
st.write("The total_nurse_hours  staffing_hours['Hrs_RN'] + staffing_hours['Hrs_LPN']  + staffing_hours['Hrs_CNA'] ")
st.dataframe(avg_staffing_levels, width="content")



st.header('Are certain states relying more on contract nurses?')



provider_data['contract_hours']= staffing_hours['contract_hours']
result = (
    provider_data
    .groupby('STATE')[['contract_hours', 'total_nurse_hours']]
    .sum()
)

result['ctr_percentage'] = (
    result['contract_hours']
    / result['total_nurse_hours'].replace(0, float('nan'))
) * 100

result = result.sort_values('ctr_percentage', ascending=False)

st.dataframe(result)




