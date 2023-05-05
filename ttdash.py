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
pio.renderers.default = "iframe"
# %matplotlib inline

st.set_page_config(layout="wide")
df = pd.read_csv("taton.csv")

tab1, tab2, tab3 = st.tabs(
    ["correlation :bar_chart:", "cek detail :tea:", "scatter_3D"]
)

with tab1:
    col1, col2 = st.columns([2, 3])

    with col1:
        st.write("heatmap")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        df.corr()
        sns.set(font_scale=0.5)
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(), ax=ax, annot=True, cmap="Blues")
        st.pyplot(fig)

    with col2:
        st.write("overview")
        fig = px.scatter_matrix(
            data_frame=df,
            dimensions=["B_L", "B_a", "B_b", "B_G", "gray_scale"],
            color="judge",
            opacity=0.5,
        )
        st.plotly_chart(fig, theme=None, use_container_width=True)

# df_ok = df[df['judge'] == 1]
# df_ng = df[df['judge'] == 0]

with tab2:
    col3, col4 = st.columns([1, 1])

    with col3:
        col5, col6, col7 = st.columns(3)
        with col5:
            xa = st.selectbox(
                "x-axis", ["B_L", "B_a", "B_b", "B_G", "inkT", "gray_scale"]
            )
        with col6:
            ya = st.selectbox(
                "y-axis", ["B_a", "B_b", "B_G", "inkT", "gray_scale", "B_L"]
            )
        with col7:
            clr = st.selectbox("color", ["judge", "sample_no"])
        fig = px.scatter(
            df,
            x=xa,
            y=ya,
            color=clr,
            hover_name="sample_no",
            title="cek detail",
            opacity=0.5,
        )
        st.plotly_chart(fig, theme=None, use_container_width=True)

    with col4:
        fig = px.scatter_matrix(
            data_frame=df,
            dimensions=["B_L", "B_a", "B_b", "B_G", "gray_scale"],
            color="judge",
            opacity=0.5,
        )
        st.plotly_chart(fig, theme=None, use_container_width=True)

with tab3:
    fig = px.scatter_3d(
        df,
        x="B_a",
        y="B_b",
        z="B_L",
        color="color_code",
        opacity=0.5,
    )
    st.plotly_chart(fig, theme=None, use_container_width=True)
