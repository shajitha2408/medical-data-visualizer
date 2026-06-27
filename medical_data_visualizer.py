import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add overweight column
df["overweight"] = (
    (df["weight"] / ((df["height"] / 100) ** 2)) > 25
).astype(int)

# Normalize cholesterol and glucose
df["cholesterol"] = (
    df["cholesterol"] > 1
).astype(int)

df["gluc"] = (
    df["gluc"] > 1
).astype(int)


# Draw categorical plot
def draw_cat_plot():

    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=[
            "cholesterol",
            "gluc",
            "smoke",
            "alco",
            "active",
            "overweight"
        ]
    )

    df_cat["total"] = 1

    df_cat = (
        df_cat
        .groupby(
            ["cardio", "variable", "value"],
            as_index=False
        )
        .count()
    )

    fig = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar"
    )

    fig.savefig("catplot.png")

    return fig


# Draw heat map
def draw_heat_map():

    return None