import streamlit as st
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

st.write("# Know the trending jobs / skills in every country for every field")

# image section
image = Image.open('images/programming.jpg')

st.image(image)

# country selection

header1 = st.subheader("Select the country")
country = st.selectbox(
    "",
    ('United States', 'India', 'United Kingdom', 'Australia', 'Germany', 'Canada', 'France'))


# field selection
header2 = st.subheader("Select the field")
field = st.selectbox(
    "",
    ('Education', 'Entertainment', 'Finance', 'Healthcare', 'Software and IT Services', 'Manufacturing', 'Media and Communications', 'Real Estate'))


# united states
if country == "United States" and field == "Education":
    data_path = "Dataset/United States/UnitedStates_All_2021-05-31_Education.csv"

if country == "United States" and field == "Entertainment":
    data_path = "Dataset/United States/UnitedStates_All_2021-05-31_Entertainment.csv"

if country == "United States" and field == "Finance":
    data_path = "Dataset/United States/UnitedStates_All_2021-05-31_Finance.csv"

if country == "United States" and field == "Healthcare":
    data_path = "Dataset/United States/UnitedStates_All_2021-05-31_Healthcare.csv"

if country == "United States" and field == "Software and IT Services":
    data_path = "Dataset/United States/UnitedStates_All_2021-05-31_Software&ITServices.csv"

if country == "United States" and field == "Manufacturing":
    data_path = "Dataset/United States/UnitedStates_All_2021-05-31_Manufacturing.csv"

if country == "United States" and field == "Media and Communications":
    data_path = "Dataset/United States/UnitedStates_All_2021-05-31_Media&Communications.csv"

if country == "United States" and field == "Real Estate":
    data_path = "Dataset/United States/UnitedStates_All_2021-05-31_RealEstate.csv"

# india
if country == "India" and field == "Education":
    data_path = "Dataset/India/India_All_2021-05-31_Education.csv"

if country == "India" and field == "Entertainment":
    data_path = "Dataset/India/India_All_2021-05-31_Entertainment.csv"

if country == "India" and field == "Finance":
    data_path = "Dataset/India/India_All_2021-05-31_Finance.csv"

if country == "India" and field == "Healthcare":
    data_path = "Dataset/India/India_All_2021-05-31_Healthcare.csv"

if country == "India" and field == "Software and IT Services":
    data_path = "Dataset/India/India_All_2021-05-31_Software&ITServices.csv"

if country == "India" and field == "Manufacturing":
    data_path = "Dataset/India/India_All_2021-05-31_Manufacturing.csv"

if country == "India" and field == "Media and Communications":
    data_path = "Dataset/India/India_All_2021-05-31_Media&Communications.csv"

if country == "India" and field == "Real Estate":
    data_path = "Dataset/India/India_All_2021-05-31_RealEstate.csv"

# united kingdom

if country == "United Kingdom" and field == "Education":
    data_path = "Dataset/United Kingdom/UnitedKingdom_All_2021-05-31_Education.csv"

if country == "United Kingdom" and field == "Entertainment":
    data_path = "Dataset/United Kingdom/UnitedKingdom_All_2021-05-31_Entertainment.csv"

if country == "United Kingdom" and field == "Finance":
    data_path = "Dataset/United Kingdom/UnitedKingdom_All_2021-05-31_Finance.csv"

if country == "United Kingdom" and field == "Healthcare":
    data_path = "Dataset/United Kingdom/UnitedKingdom_All_2021-05-31_Healthcare.csv"

if country == "United Kingdom" and field == "Software and IT Services":
    data_path = "Dataset/United Kingdom/UnitedKingdom_All_2021-05-31_Software&ITServices.csv"

if country == "United Kingdom" and field == "Manufacturing":
    data_path = "Dataset/United Kingdom/UnitedKingdom_All_2021-05-31_Manufacturing.csv"

if country == "United Kingdom" and field == "Media and Communications":
    data_path = "Dataset/United Kingdom/UnitedKingdom_All_2021-05-31_Media&Communications.csv"

if country == "United Kingdom" and field == "Real Estate":
    data_path = "Dataset/United Kingdom/UnitedKingdom_All_2021-05-31_RealEstate.csv"


# australia

if country == "Australia" and field == "Education":
    data_path = "Dataset/Australia/Australia_All_2021-05-31_Education.csv"

if country == "Australia" and field == "Entertainment":
    data_path = "Dataset/Australia/Australia_All_2021-05-31_Entertainment.csv"

if country == "Australia" and field == "Finance":
    data_path = "Dataset/Australia/Australia_All_2021-05-31_Finance.csv"

if country == "Australia" and field == "Healthcare":
    data_path = "Dataset/Australia/Australia_All_2021-05-31_Healthcare.csv"

if country == "Australia" and field == "Software and IT Services":
    data_path = "Dataset/Australia/Australia_All_2021-05-31_Software&ITServices.csv"

if country == "Australia" and field == "Manufacturing":
    data_path = "Dataset/Australia/Australia_All_2021-05-31_Manufacturing.csv"

if country == "Australia" and field == "Media and Communications":
    data_path = "Dataset/Australia/Australia_All_2021-05-31_Media&Communications.csv"

if country == "Australia" and field == "Real Estate":
    data_path = "Dataset/Australia/Australia_All_2021-05-31_RealEstate.csv"


# germany

if country == "Germany" and field == "Education":
    data_path = "Dataset/Germany/Germany_All_2021-05-31_Education.csv"

if country == "Germany" and field == "Entertainment":
    data_path = "Dataset/Germany/Germany_All_2021-05-31_Entertainment.csv"

if country == "Germany" and field == "Finance":
    data_path = "Dataset/Germany/Germany_All_2021-05-31_Finance.csv"

if country == "Germany" and field == "Healthcare":
    data_path = "Dataset/Germany/Germany_All_2021-05-31_Healthcare.csv"

if country == "Germany" and field == "Software and IT Services":
    data_path = "Dataset/Germany/Germany_All_2021-05-31_Software&ITServices.csv"

if country == "Germany" and field == "Manufacturing":
    data_path = "Dataset/Germany/Germany_All_2021-05-31_Manufacturing.csv"

if country == "Germany" and field == "Media and Communications":
    data_path = "Dataset/Germany/Germany_All_2021-05-31_Media&Communications.csv"

if country == "Germany" and field == "Real Estate":
    data_path = "Dataset/Germany/Germany_All_2021-05-31_RealEstate.csv"


# Canada

if country == "Canada" and field == "Education":
    data_path = "Dataset/Canada/Canada_All_2021-05-31_Education.csv"

if country == "Canada" and field == "Entertainment":
    data_path = "Dataset/Canada/Canada_All_2021-05-31_Entertainment.csv"

if country == "Canada" and field == "Finance":
    data_path = "Dataset/Canada/Canada_All_2021-05-31_Finance.csv"

if country == "Canada" and field == "Healthcare":
    data_path = "Dataset/Canada/Canada_All_2021-05-31_Healthcare.csv"

if country == "Canada" and field == "Software and IT Services":
    data_path = "Dataset/Canada/Canada_All_2021-05-31_Software&ITServices.csv"

if country == "Canada" and field == "Manufacturing":
    data_path = "Dataset/Canada/Canada_All_2021-05-31_Manufacturing.csv"

if country == "Canada" and field == "Media and Communications":
    data_path = "Dataset/Canada/Canada_All_2021-05-31_Media&Communications.csv"

if country == "Canada" and field == "Real Estate":
    data_path = "Dataset/Canada/Canada_All_2021-05-31_RealEstate.csv"

# France

if country == "France" and field == "Education":
    data_path = "Dataset/France/France_All_2021-05-31_Education.csv"

if country == "France" and field == "Entertainment":
    data_path = "Dataset/France/France_All_2021-05-31_Entertainment.csv"

if country == "France" and field == "Finance":
    data_path = "Dataset/France/France_All_2021-05-31_Finance.csv"

if country == "France" and field == "Healthcare":
    data_path = "Dataset/France/France_All_2021-05-31_Healthcare.csv"

if country == "France" and field == "Software and IT Services":
    data_path = "Dataset/France/France_All_2021-05-31_Software&ITServices.csv"

if country == "France" and field == "Manufacturing":
    data_path = "Dataset/France/France_All_2021-05-31_Manufacturing.csv"

if country == "France" and field == "Media and Communications":
    data_path = "Dataset/France/France_All_2021-05-31_Media&Communications.csv"

if country == "France" and field == "Real Estate":
    data_path = "Dataset/France/France_All_2021-05-31_RealEstate.csv"

# data processing

data = pd.read_csv(data_path)

button = st.button("View Raw")
if button:
    st.write(data)

data_trending_employers = data[data['categoryType']
                                == "Top Trending Employers"]
location = data_trending_employers["countryName"].to_numpy()[0]
data_trending_jobs = data[data['categoryType'] == "Top Trending Jobs"]
data_trending_skills = data[data['categoryType'] == "Top Trending Skills"]

# st.subheader("Select the trending")
# genre = st.radio(
#     "",
#     ('Trending Employers', 'Trending Jobs', 'Trending Skills'))

# if genre == 'Trending Employers':

st.header("Which companies are hiring ? (Top Trending Employers)")

fig = plt.figure(figsize=(6, 6))
sns.barplot(y=data_trending_employers['categoryName'],
            x=data_trending_employers['categoryValue'],)
st.pyplot(fig)

fig = plt.figure(figsize = (7, 7))
plt.pie(data_trending_employers['categoryValue'], 
labels=data_trending_employers['categoryName'],
autopct='%.0f%%')
st.pyplot(fig)

# if genre == 'Trending Jobs':

st.header("What jobs are available ? (Top Trending Jobs)")

fig = plt.figure(figsize=(6, 6))
sns.barplot(y=data_trending_jobs['categoryName'],
            x=data_trending_jobs['categoryValue'],)
st.pyplot(fig)

fig = plt.figure(figsize=(7, 7))
plt.pie(data_trending_jobs['categoryValue'],
        labels=data_trending_jobs['categoryName'],
        autopct='%.0f%%')
st.pyplot(fig)

# if genre == 'Trending Skills':

st.header("What skills are needed to get the job ? (Top Trending Skills)")

fig = plt.figure(figsize=(6, 6))
sns.barplot(
    y=data_trending_skills['categoryName'], x=data_trending_skills['rank'],)
st.pyplot(fig)

fig = plt.figure(figsize= (7, 7))
plt.pie(data_trending_skills['rank'],
        labels=data_trending_skills['categoryName'],
        autopct='%.0f%%')
st.pyplot(fig)

