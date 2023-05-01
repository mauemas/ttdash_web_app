# SPDX-FileCopyrightText: 2023 Kazuo Toda

import streamlit as st
import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
import seaborn as sns
import plotly.graph_objects as go
# or 'colab' or 'iframe_connected' or 'sphinx_gallery'
pio.renderers.default = 'iframe'
# %matplotlib inline

st.set_page_config(layout="wide")
df = pd.read_csv('taton.csv')

col1, col2 = st.columns([1, 2])

with col1:
    st.write('heatmap')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    df.corr()
    sns.set(font_scale=0.5)
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), ax=ax, annot=True, cmap='Blues')
    st.pyplot(fig)


with col2:
    st.write('overview')
    fig = px.scatter_matrix(
        data_frame=df,
        dimensions=['B_L', 'B_a', 'B_b', 'B_G', 'gray_scale'],
        color='judge',
    )
    st.plotly_chart(fig, theme=None, use_container_width=True)

df_ok = df[df['judge'] == 1]
df_ng = df[df['judge'] == 0]

col3, col4 = st.columns(2)

with col3:
    fig = px.scatter(df, x="B_L", y="B_a", color='judge',
                     hover_name="sample_no", title='L-a/judge')
    st.plotly_chart(fig, theme=None, use_container_width=True)

with col4:
    fig = px.scatter(df, x="B_L", y="B_a", color='sample_no',
                     hover_name="judge", title='L-a/opsi no.')
    st.plotly_chart(fig, theme=None, use_container_width=True)
