import streamlit as st
import pandas as pd
from skimpy import clean_columns
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

df_raw = pd.read_csv("/Users/richard/Downloads/HDB Legacy Current Client List - Current Wave Breakdown.csv")
df = clean_columns(df_raw, case = 'snake')

migrated_counts = df['is_migrated'].value_counts(normalize=True) * 100
fig, ax = plt.subplots()

plt.subplots(figsize=(20, 10))
migrated_counts.plot(kind='bar', ax=ax)
ax.set_ylabel('Count')
# Set the title
ax.set_title('Count and Percentage of Each Category')

st.bar_chart(migrated_counts)


unique_waves = df['wave'].unique()
waves = st.multiselect("wave", unique_waves, unique_waves)

responses = st.multiselect("has_responded_to_comms", df['has_responded_to_comms'].unique())
clients = st.multiselect("client_name", df['client_name'].unique())
csms = st.multiselect("Customer Success Manager", df['csm'].unique())



df = df[df['wave'].isin(waves)]
if clients:
    df = df[df['client_name'].isin(clients)]
if responses:
    df = df[df['has_responded_to_comms'].isin(responses)]
if csms:
    df = df[df['csm'].isin(csms)]

st.table(df)
