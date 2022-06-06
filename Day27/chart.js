async function drawChart() {

  // 1. Access data

  const dataset = await d3.json("./../../my_weather_data.json")
  console.table(dataset[0])
  const temperatureMinAccessor = d => d.temperatureMin
 const temperatureMaxAccessor = d => d.temperatureMax
 const uvAccessor = d => d.uvIndex
 const precipitationProbabilityAccessor = d => d.precipProbability
 const precipitationTypeAccessor = d => d.precipType
 const cloudAccessor = d => d.cloudCover
 const dateParser = d3.timeParse("%Y-%m-%d")
 const dateAccessor = d => dateParser(d.date)
  // 2. Create chart dimensions

  const width = 600
  let dimensions = {
    width: width,
    height: width,
    radius: width / 2,
    margin: {
      top: 120,
      right: 120,
      bottom: 120,
      left: 120,
    },
  }
  dimensions.boundedWidth = dimensions.width - dimensions.margin.left - dimensions.margin.right
  dimensions.boundedHeight = dimensions.height - dimensions.margin.top - dimensions.margin.bottom
  dimensions.boundedRadius = dimensions.radius - ((dimensions.margin.left + dimensions.margin.right) / 2)
  
  const getCoordinatesForAngle = (angle, offset=1) => [
    Math.cos(angle - Math.PI / 2) * dimensions.boundedRadius * offset,
    Math.sin(angle - Math.PI / 2) * dimensions.boundedRadius * offset,
  ]
  // 3. Draw canvas

  const wrapper = d3.select("#wrapper")
    .append("svg")
      .attr("width", dimensions.width)
      .attr("height", dimensions.height)


  const defs = wrapper.append("defs")
  const gradientId = "temperature-gradient"
  const gradient = defs.append("radialGradient")
    .attr("id", gradientId)
  
  const numberOfStops = 10
  const gradientColorScale = d3.interpolateYlOrRd
  d3.range(numberOfStops).forEach(i => {
    gradient.append("stop")
      .attr("offset", `${i * 100 / (numberOfStops - 1)}%`)
      .attr("stop-color", gradientColorScale(i / (numberOfStops - 1)))
  })
  const bounds = wrapper.append("g")
      .style("transform", `translate(${dimensions.margin.left + dimensions.boundedRadius}px, ${dimensions.margin.top + dimensions.boundedRadius}px)`)

  // 4. Create scales
  const angleScale = d3.scaleTime()
    .domain(d3.extent(dataset, dateAccessor))
    .range([0, Math.PI * 2])

  const radiusScale = d3.scaleLinear()
    .domain(d3.extent([
      ...dataset.map(temperatureMaxAccessor),
      ...dataset.map(temperatureMinAccessor),
    ]))
    .range([0, dimensions.boundedRadius])
    .nice()

    const getXFromDataPoint = (d, offset=1.4) => getCoordinatesForAngle(
      angleScale(dateAccessor(d)),
      offset
    )[0]
    const getYFromDataPoint = (d, offset=1.4) => getCoordinatesForAngle(
      angleScale(dateAccessor(d)),
      offset
    )[1]

    const cloudRadiusScale = d3.scaleSqrt()
    .domain(d3.extent(dataset, cloudAccessor))
    .range([1, 10])

  // 5. Draw data

  const containsFreezing = radiusScale.domain()[0] < 32
  if (containsFreezing) {
    const freezingCircle = bounds.append("circle")
    .attr("r", radiusScale(32))
    .attr("class", "freezing-circle")
    }

  const areaGenerator = d3.areaRadial()
    .angle(d => angleScale(dateAccessor(d)))
    .innerRadius(d => radiusScale(temperatureMinAccessor(d)))
    .outerRadius(d => radiusScale(temperatureMaxAccessor(d)))

  const area = bounds.append("path")
    .attr("class", "area")
    .attr("d", areaGenerator(dataset))
    .style("fill", `url(#${gradientId})`)

  const uvIndexThreshold = 8
  const uvGroup = bounds.append("g")
  const uvOffset = 0.95
  const highUvDays = uvGroup.selectAll("line")
      .data(dataset.filter(d => uvAccessor(d) > uvIndexThreshold))
      .enter().append("line")
        .attr("class", "uv-line")
        .attr("x1", d => getXFromDataPoint(d, uvOffset))
        .attr("x2", d => getXFromDataPoint(d, uvOffset + 0.1))
        .attr("y1", d => getYFromDataPoint(d, uvOffset))
        .attr("y2", d => getYFromDataPoint(d, uvOffset + 0.1))

    const cloudGroup = bounds.append("g")
    const cloudOffset = 1.27
    const cloudDots = cloudGroup.selectAll("circle")
          .data(dataset)
          .enter().append("circle")
            .attr("class", "cloud-dot")
            .attr("cx", d => getXFromDataPoint(d, cloudOffset))
            .attr("cy", d => getYFromDataPoint(d, cloudOffset))
            .attr("r", d => cloudRadiusScale(cloudAccessor(d)))
  // 6. Draw peripherals
  const months = d3.timeMonths(...angleScale.domain())
  
  
  const peripherals = bounds.append("g")
  const temperatureTicks = radiusScale.ticks(4)
  const gridCircles = temperatureTicks.map(d => (
    peripherals.append("circle")
      .attr("r", radiusScale(d))
      .attr("class", "grid-line")
  ))
  
  months.forEach(month => {
    const angle = angleScale(month)
    const [x, y] = getCoordinatesForAngle(angle)

    peripherals.append("line")
      .attr("x2", x)
      .attr("y2", y)
      .attr("class", "grid-line")

    const [labelX, labelY] = getCoordinatesForAngle(angle, 1.38)
    peripherals.append("text")
      .attr("x", labelX)
      .attr("y", labelY)
      .attr("class", "tick-label")
      .text(d3.timeFormat("%b")(month))
      .style("text-anchor",
      Math.abs(labelX) < 5 ? "middle" :
      labelX > 0 ? "start" :      "end"
)
  })
const tickLabelBackgrounds = temperatureTicks.map(d => {
  if (!d) return
  return peripherals.append("rect")
    .attr("y", -radiusScale(d) - 10)
    .attr("width", 40)
    .attr("height", 20)
    .attr("fill", "#f8f9fa")
})
const tickLabels = temperatureTicks.map(d => {
  if (!d) return
  return peripherals.append("text")
  .attr("x", 4)
  .attr("y", -radiusScale(d) + 2)
  .attr("class", "tick-label-temperature")
  .html(`${d3.format(".0f")(d)}°F`)
})
  const gridLines = months.forEach(month => {
    const angle = angleScale(month)
      return peripherals.append("line")

    })

  // 7. Set up interactions


}
drawChart()