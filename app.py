from textwrap import fill
import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)

st.code(
''' 
x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(1, 101, 1, dtype=int)

# Create a random array of data that we will use for our y values
y_data = np.random.randint(100, size=100)

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)''',language='python')

x_axis = np.arange(1, 101, 1, dtype=int)
y_data = np.random.randint(100, size=100)
df = pd.DataFrame({'x': x_axis,'y': y_data})
st.write(df)


st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)

st.code(
''' 
scatter = alt.Chart(df).mark_point().encode(x=alt.X('x'),y=alt.Y('y'))

st.altair_chart(scatter, use_container_width=True)''',language='python')

slider = alt.binding_range(min=1, max=101, step=1, name='cutoff:')
selector = alt.selection_single(name="SelectorName", fields=['cutoff'],
                                bind=slider, init={'cutoff': 50})
scatter = alt.Chart(df).mark_circle().encode(x=alt.X('x'),y=alt.Y('y'),
color=alt.condition(
        alt.datum.x < selector.cutoff,
        alt.value('red'), alt.value('blue'))
).add_selection(
    selector).properties(
        title='Scatter Plot'
)
scatter.configure_title(
    fontSize=20,
    font='Courier',
    anchor='start',
    color='gray'
)

st.altair_chart(scatter, use_container_width=True)


st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

st.markdown("The five changes I made were.....")
st.markdown("""
The 5 changes I made were:
- Change 1 Added a title with font format
- Change 2 Changed mark from point to circle
- Change 3 Added one condition to show a cutoff vertical reference line
- Change 4 Selected different colors for marks separated by the cutoff line
- Change 5 Added an interactive slider to move the cutoff line 
""")


st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html. \n"
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual. \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)

from vega_datasets import data

source = data.stocks()
st.write(source)

linechart = alt.Chart(source).mark_area(
    color="lightblue",
    interpolate='step-after',
    line=True
).encode(
    x='date',
    y='price'
).transform_filter(alt.datum.symbol == 'GOOG').properties(
        title='Google Stock Price ($)'
).configure_view(fill='#FFEEDD'
)

st.altair_chart(linechart, use_container_width=True)


st.markdown("""
The 2 changes I made were:
- Change 1 Added title "Google Stock Price ($)"
- Change 2 Changed line chart background color from white to light yellow
"""
)

