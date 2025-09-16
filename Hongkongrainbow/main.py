import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Generate placeholder rainbow frequency data for Hong Kong
np.random.seed(42)
years = np.arange(2015, 2025)
months = [f"{m:02d}" for m in range(1, 13)]
data = []
for year in years:
    for month in months:
        freq = np.random.poisson(lam=2) + np.random.binomial(1, 0.2)
        data.append({"Year": year, "Month": month, "Frequency": freq})
df = pd.DataFrame(data)
df["Date"] = df["Year"].astype(str) + "-" + df["Month"]

# Interactive rainbow frequency line chart
fig = px.line(df, x="Date", y="Frequency", title="Hong Kong Rainbow Frequency (2015-2024)",
              markers=True, color_discrete_sequence=["#FFB6C1", "#FFD700", "#00FF00", "#00BFFF", "#8A2BE2"])
fig.update_traces(line=dict(width=4), marker=dict(size=10, symbol="circle"))
fig.update_layout(
    plot_bgcolor="#f0f8ff",
    paper_bgcolor="#f0f8ff",
    font=dict(size=16),
    title_font=dict(size=24, color="#8A2BE2"),
    xaxis_title="Month",
    yaxis_title="Rainbow Frequency",
    hovermode="x unified"
)
fig.show()
