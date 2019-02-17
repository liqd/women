$( document ).ready(function() {
    var nodeData = parties

    var width = 600;
    var height = 600;
    var radius = Math.min(width, height) / 2;
    var color = function(d) {
        switch(d.depth) {
            case 0: return d3.rgb('#000000')
            case 1: return d3.rgb(d.data.colour)
            case 2: return d3.rgb(d.parent.data.colour)
        }
    }

    var opacity = function(d) {
        switch(d.depth) {
            case 0: return 1
            case 1: return 0.4
            case 2: return (d.data.name == 'Frauen') ? 1 : 0.4
        }
    }

    var svg = d3.select("#chart2")
        .append("svg")
        .attr('width', width)
        .attr('height', height)

    var g = svg.append('g')
        .attr('width', width)
        .attr('height', height)
        .attr('transform', 'translate(' + width / 2 + ',' + height / 2 + ')');


    var partition = d3.partition()
        .size([2 * Math.PI, radius]);

    var root = d3.hierarchy(nodeData)
        .sum(function (d) { return d.size});

    partition(root);
    var arc = d3.arc()
        .startAngle(function (d) { return d.x0 })
        .endAngle(function (d) { return d.x1 })
        .innerRadius(function (d) { return d.y0 })
        .outerRadius(function (d) { return d.y1 });

    g.selectAll('g')
        .data(root.descendants())
        .enter().append('g').attr("class", "node").append('path')
        .attr("display", function (d) { return d.depth ? null : "none"; })
        .attr("d", arc)
        .style('stroke', '#fff')
        .style('opacity', function (d) {
            return opacity(d)
        })
        .style("fill", function (d) {return color(d); });


        // Populate the <text> elements with our data-driven titles.
        g.selectAll(".node")
            .append("text")
            .attr("transform", function(d) {
                return "translate(" + arc.centroid(d) + ")rotate(" + computeTextRotation(d) + ")"; })
            .attr("dx", "-20") // radius margin
            .attr("dy", ".5em") // rotation align
            .text(function(d) { return d.parent ? d.data.name : "" });

    function computeTextRotation(d) {
        var angle = (d.x0 + d.x1) / Math.PI * 90;

        // Avoid upside-down labels
        return (angle < 120 || angle > 270) ? angle : angle + 180;  // labels as rims
        //return (angle < 180) ? angle - 90 : angle + 90;  // labels as spokes
    }
})