import plotly.graph_objects as go
from plotly.subplots import make_subplots
from re import search

import pandas as pd
import re
number = "10"
word = "sheet" + number + ".csv"
out  = "fig" + number + ".pdf"
location = "C:/Users/maint/Documents/plot/3a1115VPP5HZ/"

df = pd.read_csv(location+word)
testName = "Test " + df.iloc[0][1]
currDate = df.iloc[0][9]
#, *DATE || NUMBER-TRANSATCION || OUTPUT-VOLUME || MARKET-PRICE || *HAST-RATE || COST-PER-TRANS-USD || *MINING-REVENUE-USD || TRANSACTION-FEE
# Time	Test	                    Leg 1	    Leg 2	    Leg 3	    Leg 4	    Leg 5	    Leg 6	    Drive
# 0	3.a.1.1 1.5V P-P .5 HZ	0.003051758	0.01373291	0.005187988	-0.003051758	0.009155273	0.005187988	-0.000915527

for i, row in enumerate(df["Time"]):
    p = re.compile("0.00")
    datetime = row
    df.iloc[i, 1] = datetime

fig = make_subplots(
    rows=8, cols=1,
    shared_xaxes=True,
    vertical_spacing=0.01,
    specs=[[{"type": "scatter"}],
           [{"type": "scatter"}],
           [{"type": "scatter"}],
           [{"type": "scatter"}],
           [{"type": "scatter"}],
           [{"type": "scatter"}],
           [{"type": "scatter"}],
           [{"type": "table"}]]
)

fig.add_trace(
    go.Scatter(
        x=df["Time"],
        y=df["Drive"],
        mode="lines",
        name="Drive"
    ),
    row=7, col=1
)

fig.add_trace(
    go.Scatter(
        x=df["Time"],
        y=df["Leg 6"],
        mode="lines",
        name="Leg 6"
    ),
    row=6, col=1
)

fig.add_trace(
    go.Scatter(
        x=df["Time"],
        y=df["Leg 5"],
        mode="lines",
        name="Leg 5"
    ),
    row=5, col=1
)

fig.add_trace(
    go.Scatter(
        x=df["Time"],
        y=df["Leg 4"],
        mode="lines",
        name="Leg 4"
    ),
    row=4, col=1
)

fig.add_trace(
    go.Scatter(
        x=df["Time"],
        y=df["Leg 3"],
        mode="lines",
        name="Leg 3"
    ),
    row=3, col=1
)

fig.add_trace(
    go.Scatter(
        x=df["Time"],
        y=df["Leg 2"],
        mode="lines",
        name="Leg 2"
    ),
    row=2, col=1
)

fig.add_trace(
    go.Scatter(
        x=df["Time"],
        y=df["Leg 1"],
        mode="lines",
        name="Leg 1"
    ),
    row=1, col=1
)

#fig.add_trace(
#    go.Table(
#        header=dict(
#            values=["Time", "Leg 1", "Leg 2", "Leg 3", 
#                    "Leg 4", "Leg 5", "Leg 6",
#                    "Drive"],
#            font=dict(size=10),
#            align="left"
#        ),
#        cells=dict(
#            values=[df[k].tolist() for k in df.columns[1:]],
#            align = "left")
#    ),
#    row=1, col=1
#)
fig.update_layout(
    height=816,
    width=1056,
    showlegend=False,
    annotations=[
        go.layout.Annotation(
            x=.22,
            y=.15,
            xref='paper',
            yref='paper',
            showarrow=False,
            text=testName,
            arrowhead=7,
            ax=0,
            ay=-40
        ),
        go.layout.Annotation(
            x=.30,
            y=.28,
            xref='paper',
            yref='paper',
            showarrow=False,
            text="Leg 6",
            arrowhead=7,
            ax=0,
            ay=-40
        ),
        go.layout.Annotation(
            x=.30,
            y=.42,
            xref='paper',
            yref='paper',
            showarrow=False,
            text="Leg 5",
            arrowhead=7,
            ax=0,
            ay=-40
        ),
        go.layout.Annotation(
            x=.30,
            y=.55,
            xref='paper',
            yref='paper',
            showarrow=False,
            text="Leg 4",
            arrowhead=7,
            ax=0,
            ay=-40
        ),
        go.layout.Annotation(
            x=.30,
            y=.69,
            xref='paper',
            yref='paper',
            showarrow=False,
            text="Leg 3",
            arrowhead=7,
            ax=0,
            ay=-40
        ),
        go.layout.Annotation(
            x=.30,
            y=.82,
            xref='paper',
            yref='paper',
            showarrow=False,
            text="Leg 2",
            arrowhead=7,
            ax=0,
            ay=-40
        ),
        go.layout.Annotation(
            x=.30,
            y=.95,
            xref='paper',
            yref='paper',
            showarrow=False,
            text="Leg 1",
            arrowhead=7,
            ax=0,
            ay=-40
        ),
        go.layout.Annotation(
            x=0,
            y=1.05,
            xref='paper',
            yref='paper',
            showarrow=False,
            text=currDate,
            arrowhead=7,
            ax=0,
            ay=-40
        )
    ]
    #title_text="I typed this",
)

#fig.update_xaxes(dtick=.5, showgrid=True, gridwidth=1, gridcolor='LightPink')
#fig.update_yaxes(dtick=.20, showgrid=True, gridwidth=1, gridcolor='LightPink')

fig.write_image(location+out)

fig.show()
