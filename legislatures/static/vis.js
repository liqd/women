    Highcharts.theme = {
    colors: ['#7cb5ec', '#f7a35c', '#90ee7e', '#7798BF', '#aaeeee', '#ff0066',
        '#eeaaee', '#55BF3B', '#DF5353', '#7798BF', '#aaeeee'],
    chart: {
        backgroundColor: null,
        style: {
            fontFamily: 'Dosis, sans-serif'
        }
    },
    title: {
        style: {
            fontSize: '16px',
            fontWeight: 'bold',
            textTransform: 'uppercase'
        }
    },
    tooltip: {
        borderWidth: 0,
        backgroundColor: 'rgba(219,219,216,0.8)',
        shadow: false
    },
    legend: {
        itemStyle: {
            fontWeight: 'bold',
            fontSize: '13px'
        }
    },
    xAxis: {
        gridLineWidth: 1,
        labels: {
            style: {
                fontSize: '12px'
            }
        }
    },
    yAxis: {
        minorTickInterval: 'auto',
        title: {
            style: {
                textTransform: 'uppercase'
            }
        },
        labels: {
            style: {
                fontSize: '12px'
            }
        }
    },
    plotOptions: {
        candlestick: {
            lineColor: '#404048'
        }
    },


    // General
    background2: '#F0F0EA'

};

Highcharts.setOptions(Highcharts.theme);


document.addEventListener('DOMContentLoaded', function () {

    var newData = data.map(function(d){
        return {
            name: d.name,
            data: d.data.map(function(p){
                return parseFloat(p)
            })
        }
    });

    Highcharts.chart('container', {
    chart: {
        type: 'line'
    },

    title: {
        text: 'Frauenanteil in Deutschen Parlamenten'
    },
        /*subtitle: {
        text: 'Source: WorldClimate.com'
    },*/
        xAxis: {
        categories: years
    },
    yAxis: {
        title: {
            text: 'Frauenanteil in Prozent'
        }
    },
    plotOptions: {
    line: {
        dataLabels: {
            enabled: true
        },
        enableMouseTracking: false
        }
    },
    series: newData
    });

})



