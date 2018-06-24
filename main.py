import pandas as pd
import plotly
from plotly.offline import init_notebook_mode
import plotly.graph_objs as go
plotly.offline.init_notebook_mode(connected=True)



def read_file():
    month = input('Enter the Month, format:xxxx(year)xx(month), period:201501-201804\n')
    file_path = 'data/ADL07p_1hr'+ month +'.csv'

    raw_data = pd.read_csv(file_path)

    cleaned_data = raw_data[raw_data['PM2.5 BAM ug/m3'].notnull()]


    rows_to_be_dropped = []
    for index, row in cleaned_data.iterrows():
        if row['PM2.5 BAM ug/m3']<0:
            rows_to_be_dropped.append(index)

    cleaned_data = cleaned_data.drop(labels=rows_to_be_dropped)

    print('Success!')
    return cleaned_data




def plot_exceeded_data(cleaned_data):
    ex_pm25 = cleaned_data[cleaned_data['PM2.5 BAM ug/m3'] >= 25]

    trace = go.Scatter(
    x = ex_pm25['Date/Time'],
    y = ex_pm25['PM2.5 BAM ug/m3']
    )

    data = [trace]
    layout = dict(title = 'Exceeded_Data',
              xaxis = dict(title = 'Time'),
              yaxis = dict(title = 'PM2.5 BAM ug/m3'),
              )

    fig = dict(data=data, layout=layout)

    plotly.offline.plot(fig, filename='plot_exceeded_data')




def calculate_AQI(cleaned_data):
    cleaned_data['Index'] = cleaned_data['PM2.5 BAM ug/m3']/25*100

    def convert_aqi(i):
            if i <= 33:
                return 'Very Good'
            elif i <= 66 and i > 33:
                return 'Good'
            elif i <= 99 and i > 66:
                return 'Fair'
            elif i <= 149 and i > 99:
                return 'Poor'
            elif i > 149:
                return 'Very Poor'

    cleaned_data['aqi'] = cleaned_data.Index.apply(convert_aqi)



def plot_proportion_of_AQI(cleaned_data):
    VG = cleaned_data[cleaned_data['aqi'] == 'Very Good'].shape[0]
    G = cleaned_data[cleaned_data['aqi'] == 'Good'].shape[0]
    F = cleaned_data[cleaned_data['aqi'] == 'Fair'].shape[0]
    P = cleaned_data[cleaned_data['aqi'] == 'Poor'].shape[0]
    VP = cleaned_data[cleaned_data['aqi'] == 'Vert Poor'].shape[0]


    fig = {
        'data': [
            {
                'labels': ['Very Good','Good','Fair','Poor','Very Poor'],
                'values': [VG,G,F,P,VP],
                'type': 'pie',
                'marker': {'colors': ['#8FCFDB', '#E47500', '#BF0001', '1F4DFF', 'A70CE8']},
                'hoverinfo':'value',
                'textinfo':'label+percent'
            }
        ],
        'layout': {'title': 'Proportion of AQI',
                   'showlegend': True},

    }

    plotly.offline.plot(fig, filename='plot_proportion_of_AQI')
