# AQI-Function
This repo is the function for BENV7500 Programmable Cities Assignment 3. A function and dataset to analyze air quality sensor data based on Python.

This function is designed for processing raw air quality sensor data, clean the dataset and give a simple description of the air quality from the sensors. In the ‘read_file’ function, user is required to input a date to access the dataset. The dataset will be cleaned automatically and output a new dataframe. The ‘plot_exceeded_data’ function will find the exceeded data and visualize it as a line chart. Then ‘calculate_AQI’ function will add a new column to the dataset called AQI. Finally, the ‘plot_proportion_of_AQI’ will visualize the data as a pie chart.

The dataset of Adelaide CBD Air Quality monitoring station particle data is provided in the repo. 

This function uses Pandas v0.23.1 Final (June 12, 2018) and Plotly for Python.

The output image will open in the browser as a html file.
