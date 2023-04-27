import streamlit as st
import pandas as pd
import skimpy
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)


prompt = "Download this Google Sheet as xls"
# st.text("HDB [HDB Migration Tracker](https://docs.google.com/spreadsheets/d/19jhps4LppyoiG2X6wRNm5CNVknsWHNsG8ucQ0vJGqZQ/edit?usp=sharing)")
st.write("1. Download this as an xlsx file [HDB Migration Tracker](https://docs.google.com/spreadsheets/d/19jhps4LppyoiG2X6wRNm5CNVknsWHNsG8ucQ0vJGqZQ/edit?usp=sharing)")

st.write("2. Upload the downloaded xlsx file")
xls = st.file_uploader(label="File Uploader:")
df = None
if xls:
    df = skimpy.clean_columns(pd.read_excel(xls, sheet_name="Current Wave Breakdown"))
    cols = ["Client_name"]

    if xls:
        migration_counts = df['migration_status'].value_counts(normalize=True)
        fig, ax = plt.subplots(figsize=(6, 4))
        migration_counts.plot(kind='barh', ax=ax)
        plt.title('Migration Status')
        plt.xlabel('Percentage')
        plt.ylabel('Migration Status')

        # add percentage labels to the plot
        for i in ax.containers:
            ax.bar_label(i, label_type='edge', labels=[f'{w.get_width() * 100:.1f}%' for w in i], fontsize=8)

        # display the plot in Streamlit
        st.pyplot(fig)
