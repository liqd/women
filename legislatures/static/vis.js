document.addEventListener('DOMContentLoaded', function () {

    var newData = data.map(function(d){return parseFloat(d)});

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
    series: [{
        name: 'Weimarer Republik und Bundesrepublik Deutschland',
        data: newData
    }]
    });

})



