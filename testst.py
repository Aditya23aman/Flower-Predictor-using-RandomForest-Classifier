import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

st.write("test test")



def load_data():
    iris = load_iris()

    df = pd.DataFrame(iris.data, columns = iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df, target = load_data()

st.write(df)