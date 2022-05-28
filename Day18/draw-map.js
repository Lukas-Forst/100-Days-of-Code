async function drawMap() {
  // your code goes here
  const countryShapes = await d3.json("./../world-geojson.json")
  const countryNameAccessor = d => d.properties["NAME"]
  const countryIdAccessor = d => d.properties["ADM0_A3_IS"]
  const dataset = await d3.csv("./../data_bank_data.csv")
  const metric = "Population growth (annual %)"
  let metricDataByCountry = {}
  dataset.forEach(d => {
     if (d["Series Name"] != metric) return
     metricDataByCountry[d["Country Code"]] = +d["2017 [YR2017]"] || 0
     })
  let dimensions = {
    width: window.innerWidth * 0.9,
    margin: {
      top: 10,
      right: 10,
      bottom: 10,
      left: 10,
    },
  }
  dimensions.boundedWidth = dimensions.width
    - dimensions.margin.left
    - dimensions.margin.right
  const sphere = ({type: "Sphere"})
  const projection = d3.geoEqualEarth()
    .fitWidth(dimensions.boundedWidth, sphere)

  const pathGenerator = d3.geoPath(projection)
  const [[x0, y0], [x1,y1]] = pathGenerator.bounds(sphere)

  dimensions.boundedHeight = y1
  dimensions.height = dimensions.boundedHeight
    + dimensions.margin.top
    + dimensions.margin.bottom

  const wrapper = d3.select("#wrapper")
    .append("svg")
      .attr("width", dimensions.width)
      .attr("height", dimensions.height)

  const bounds = wrapper.append("g")
    .style("transform", `translate(${
    dimensions.margin.left
    }px, ${
      dimensions.margin.top
    }px)`)
  
  const metricValues = Object.values(metricDataByCountry)
  const metricValueExtent = d3.extent(metricValues)

  const maxChange = d3.max([-metricValueExtent[0], metricValueExtent[1]])
  const colorScale = d3.scaleLinear()
    .domain([-maxChange,0, maxChange])
    .range(["indigo", "white", "darkgreen"])

  const earth = bounds.append("path")
    .attr("class", "earth")
    .attr("d", pathGenerator(sphere))
  
  //A graticule is a grid of latitudinal and longitudinal lines
  const graticuleJson = d3.geoGraticule10()
  const countries = bounds.selectAll(".country")
    .data(countryShapes.features)
    .enter().append("path")
      .attr("class", "country")
      .attr("d", pathGenerator)
      .attr("fill", d => {
        const metricValue = metricDataByCountry[countryIdAccessor(d)]
        if (typeof metricValue == "undefined") return "#e2e6e9"
        return colorScale(metricValue)
      })

  const legendGroup = wrapper.append("g")
      .attr("transform", `translate(${
        120
      },${
        dimensions.width < 800
        ? dimensions.boundedHeight - 30
        : dimensions.boundedHeight * 0.5
      })`)
  const legendTitle = legendGroup.append("text")
      .attr("y", -23)
      .attr("class", "legend-title")
      .text("Population growth")
  
  const legendByline = legendGroup.append("text")
      .attr("y", -9)
      .attr("class", "legend-byline")
      .text("Percent change in 2017")
  
  const defs = wrapper.append("defs")
  const legendGradientId = "legend-gradient"
  const gradient = defs.append("linearGradient")
      .attr("id", legendGradientId)
    .selectAll("stop")
    .data(colorScale.range())
    .enter().append("stop")
      .attr("stop-color", d => d)
      .attr("offset", (d, i) => `${
        i * 100 / 2 //2 is one less than the length of our array
      }%`)
  const legendWidth = 120
  const legendHeight = 16
  const legendGradient = legendGroup.append("rect")
      .attr("x", -legendWidth / 2)
      .attr("height", legendHeight)
      .attr("width", legendWidth)
      .style("fill", `url(#${legendGradientId})`)
  const legendValueRight = legendGroup.append("text")
      .attr("class", "legend-value")
      .attr("x", legendWidth / 2 + 10)
      .attr("y", legendHeight / 2)
      .text(`${d3.format(".1f")(maxChange)}%`)

  const legendValueLeft = legendGroup.append("text")
      .attr("class", "legend-value")
      .attr("x", -legendWidth / 2 - 10)
      .attr("y", legendHeight / 2)
      .text(`${d3.format(".1f")(-maxChange)}%`)
      .style("text-anchor", "end")
  

  navigator.geolocation.getCurrentPosition(myPosition => {
           const [x, y] = projection([
           myPosition.coords.longitude,
           myPosition.coords.latitude
           ])
  const myLocation = bounds.append("circle")
           .attr("class", "my-location")
           .attr("cx", x)
           .attr("cy", y)
           .attr("r", 0)
           .transition().duration(500)
           .attr("r", 10)
           })
}
drawMap()