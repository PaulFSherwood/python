from plotly.subplots import make_subplots
import plotly.graph_objects as go
from re import search
import pandas as pd
import fileinput
import time
import sys
import re
import os

# example for command line
# python script    test folder  sheet number(orignal)
# python plotMe.py 3a1115VPP5HZ 11
location = str(sys.argv[1]) + "/"
number = str(sys.argv[2])
word = "sheet" + number + ".csv"

csvfile = open(location+word, 'r').readlines()
filename = 1

#out  = "fig" + number + ".pdf"
#print(location + "||" + number)

# loop through the file
for i in range(len(csvfile)):
    # save the first line to use later
    insertLine = csvfile[0]
    # save the test name
    #testName = csvfile[1][2:18]
    #=========================================================================
    # capture specific set of lines
    if i % 992 == 0:
        # make a new file and populate it
        newfile = csvfile[i:i+1000]
        # push saved line to the top of the new file
        if (newfile[0] != insertLine):
            newfile.insert(0, insertLine)
        # push everything out to a numbered csv file
        open(location+str(filename) + '.csv', 'w+').writelines(newfile)
        #=========================================================================
        # capture smaller file
        df = pd.read_csv(location+str(filename)+'.csv')
        #print(df)
        if (filename == 1):
            testName = "Test " + df.iloc[0][1]  # pull out test name
            currDate = df.iloc[0][9]            # get the test date
		##
        print(testName)
		
        print(currDate)

        for i, row in enumerate(df["Time"]):
            p = re.compile("0.00")
            datetime = row
            df.iloc[i, 1] = datetime

        # make a figure that has 7 graphs and a table
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
                   [{"type": "table"}]]  # this could be removed
        )
        # setup Drive signal graph
        fig.add_trace(
            go.Scatter(
                x=df["Time"],
                y=df["Drive"],
                mode="lines",
                name="Drive"
            ),
            row=7, col=1
        )
        # setup Leg 6 signal graph
        fig.add_trace(
            go.Scatter(
                x=df["Time"],
                y=df["Leg 6"],
                mode="lines",
                name="Leg 6"
            ),
            row=6, col=1
        )
        # setup Leg 5 signal graph
        fig.add_trace(
            go.Scatter(
                x=df["Time"],
                y=df["Leg 5"],
                mode="lines",
                name="Leg 5"
            ),
            row=5, col=1
        )
        # setup Leg 4 signal graph
        fig.add_trace(
            go.Scatter(
                x=df["Time"],
                y=df["Leg 4"],
                mode="lines",
                name="Leg 4"
            ),
            row=4, col=1
        )
        # setup Leg 3 signal graph
        fig.add_trace(
            go.Scatter(
                x=df["Time"],
                y=df["Leg 3"],
                mode="lines",
                name="Leg 3"
            ),
            row=3, col=1
        )
        # setup Leg 2 signal graph
        fig.add_trace(
            go.Scatter(
                x=df["Time"],
                y=df["Leg 2"],
                mode="lines",
                name="Leg 2"
            ),
            row=2, col=1
        )
        # setup Leg 1 signal graph
        fig.add_trace(
            go.Scatter(
                x=df["Time"],
                y=df["Leg 1"],
                mode="lines",
                name="Leg 1"
            ),
            row=1, col=1
        )
        # Set up the graph size
        fig.update_layout(
            height=816,
            width=1056,
            showlegend=False,
            annotations=[
                # Display the testname
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
                # Display the Leg 6 name
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
                # Display the Leg 5 name
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
                # Display the Leg 4 name
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
                # Display the Leg 3 name
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
                # Display the Leg 2 name
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
                # Display the Leg 1 name
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
                # Display the current date
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
            ]#,
            #title_text="I typed this"  
        )
        # unwanted background grid
        #fig.update_xaxes(dtick=.5, showgrid=True, gridwidth=1, gridcolor='LightPink')
        #fig.update_yaxes(dtick=.20, showgrid=True, gridwidth=1, gridcolor='LightPink')

        # output a pdf file
        fig.write_image(location+str(filename)+".pdf") # changing to number
        print(location+str(filename)+".pdf")
        # output a webpage file
        #fig.show()
        # wait for output to catchup
        time.sleep(5)
        print(str(filename) + " is done.")
        os.remove(location+str(filename)+".csv")
        #=========================================================================
        #=========================================================================
        filename += 1
