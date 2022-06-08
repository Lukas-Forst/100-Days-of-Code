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

  // 3. Draw canvas

  const wrapper = d3.select("#wrapper")
    .append("svg")
      .attr("width", dimensions.width)
      .attr("height", dimensions.height)

  const bounds = wrapper.append("g")
      .style("transform", `translate(${dimensions.margin.left + dimensions.boundedRadius}px, ${dimensions.margin.top + dimensions.boundedRadius}px)`)

  // 4. Create scales
  const angleScale = d3.scaleTime()
    .domain(d3.extent(dataset, dateAccessor))
    .range([0, Math.PI * 2])
  // 5. Draw data


  // 6. Draw peripherals
  const getCoordinatesForAngle = (angle, offset=1) => []
  const peripherals = bounds.append("g")
  const months = d3.timeMonths(...angleScale.domain())
  
  const gridLines = months.forEach(month => {
    const angle = angleScale(month)
      return peripherals.append("line")
    })

  // 7. Set up interactions


}
drawChart()