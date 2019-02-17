$(function () {
    var margin = {top: 20, right: 20, bottom: 50, left: 70},
        width = 1140,
        height = 600;

    var parseDate = d3.timeParse("%Y-%m-%d")
    var formatTime = d3.time.format("%Y")

    var x = d3.time.scale()
        .domain([new Date(1945, 1, 1), new Date(2030, 1, 1)])
        .range([0, width])

    var allValues = parlValues.map(function (d) {
        return parseFloat(d)
    })
    var maxValue = d3.max(allValues)
    var y = d3.scale.linear()
        .domain([0, maxValue])
        .range([height, 0])

    var xAxis = d3.svg.axis().scale(x).orient("bottom")
    var yAxis = d3.svg.axis().scale(y).orient("left")

    var valueline = d3.svg.line()
        .x(function (d) {
            return x(d.year);
        })
        .y(function (d) {
            return y(d.value);
        })

    var div = d3.select("#groupchart").append("div")
        .attr("class", "tooltip")
        .style("opacity", 0);

    var svg = d3.select("#groupchart")
        .append("svg")
        .attr("width", width)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")")

    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)

    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)

    svg.append("text")
        .attr("class", "axis-label")
        .attr("transform",
            "translate(" + (width / 2) + " ," +
            (height + margin.top + 30) + ")")
        .style("text-anchor", "middle")
        .text("Jahr");

    svg.append("text")
        .attr("class", "axis-label")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left)
        .attr("x", 0 - (height / 2))
        .attr("dy", "1em")
        .style("text-anchor", "middle")
        .text("Frauenanteil in %");

    parlData.forEach(function (item, i) {
        var name = item.name
        var data = item.data

        data.forEach(function (d) {
            d.year = parseDate(d.year);
        })

        svg.append("path")
            .attr("data-legend", function() {
                return name
            })
            .attr("data-legend-pos", i)
            .attr("class", "line line-" + i)
            .attr("d", valueline(data));

        svg.selectAll("dot")
            .data(data)
            .enter().append("circle")
            .attr("r", 5)
            .attr("cx", function (d) {
                return x(d.year);
            })
            .attr("cy", function (d) {
                return y(d.value);
            })
            .on("mouseover", function (d) {
                div.transition()
                    .duration(200)
                    .style("opacity", .9);
                div.html(name + " (" + formatTime(d.year) + ")<br/>" + d.info + "<br/>" + d.value + ' %')
                    .style("left", (d3.event.pageX) + "px")
                    .style("top", (d3.event.pageY - 28) + "px");
            })
            .on("mouseout", function (d) {
                div.transition()
                    .duration(500)
                    .style("opacity", 0);
            });

    })

    svg.append("g")
    .attr("class","legend")
    .attr("transform","translate(50,30)")
    .attr("data-style-padding",10)
    .style("font-size","14px")
    .call(d3.legend)

})