import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt


file = "C:\\Users\\Vitusa\\Desktop\\WorldAplications\\7.DataVisualisationPart2\Jupyter\\reviews.csv"
data = pandas.read_csv(file, parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_crs = data.groupby(['Month','Course Name'])['Rating'].count().unstack()

# The way you can find any type of styling - quasar style, https://quasar.dev/style

chart_def = """
{
    chart: {
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },

    // Make sure connected countries have similar colors

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },

    

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            }
        }
    },

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }

}

"""


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analasys of Course Reviews", classes="text-h3 text-center q-pa-md")
    
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = "Average rating by month"
    hc.options.xAxis.categories = list(month_average_crs.index)
    hc_data = [{"name":v1, "data":[v2 for v2 in month_average_crs[v1]]}for v1 in month_average_crs.columns]
    hc.options.series = hc_data

    return wp

jp.justpy(app)
