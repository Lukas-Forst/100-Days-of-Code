async function drawChart() {

  // 1. Access data

  const dataset = await d3.json("./../education.json")
  const sexAccessor = d => d.sex
  const sexes = ["female", "male"]
  const sexIds = d3.range(sexes.length)
  const educationAccessor = d => d.education
  const educationNames = [
     "<High School",
     "High School",
     "Some Post-secondary",
     "Post-secondary",
     "Associate's",
     "Bachelor's and up"
     ]
  const educationIds = d3.range(educationNames.length)
  const sesAccessor = d => d.ses
  const sesNames = ["low", "middle", "high"]
  const sesIds = d3.range(sesNames.length)
  const getStatusKey = ({sex, ses}) => [sex, ses].join("--")

const stackedProbabilities = {}
dataset.forEach(startingPoint => {
    const key = getStatusKey(startingPoint)
    let stackedProbability = 0
    stackedProbabilities[key] = educationNames.map((education, i) => {
      stackedProbability += (startingPoint[education] / 100)
      if (i == educationNames.length - 1) {
         // account for rounding error
         return 1
         } else {
         return stackedProbability
         }
    })
})
  // 2. Create chart dimensions

  const width = d3.min([
    window.innerWidth * 0.9,
    1200
  ])
  let dimensions = {
    width: width,
    height: 500,
    margin: {
      top: 10,
      right: 200,
      bottom: 10,
      left: 120,
    },
  }
  dimensions.boundedWidth = dimensions.width - dimensions.margin.left - dimensions.margin.right
  dimensions.boundedHeight = dimensions.height - dimensions.margin.top - dimensions.margin.bottom

  // 3. Draw canvas

  const wrapper = d3.select("#wrapper")
    .append("svg")
      .attr("width", dimensions.width)
      .attr("height", dimensions.height)

  const bounds = wrapper.append("g")
      .style("transform", `translate(${dimensions.margin.left}px, ${dimensions.margin.top}px)`)

  // 4. Create scales


  // 5. Draw data


  // 6. Draw peripherals


  // 7. Set up interactions

}
drawChart()


// utility functions

const getRandomNumberInRange = (min, max) => Math.random() * (max - min) + min

const getRandomValue = arr => arr[Math.floor(getRandomNumberInRange(0, arr.length))]

const sentenceCase = str => [
  str.slice(0, 1).toUpperCase(),
  str.slice(1),
].join("")