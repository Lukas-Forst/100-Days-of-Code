import React from "react"
import PropTypes from "prop-types"
import * as d3 from 'd3'

const Axis = ({ dimension, scale, ...props }) => {
  return (
    <g {...props}
      className="Axis"
    />
  )
}

const dimensions = useChartDimensions()

const axisGeneratorsByDimension = {
  x: "axisBottom",
  y: "axisLeft",
  }
const axisGenerator = d3[axisGeneratorsByDimension[dimension]]()
  .scale(scale)
Axis.propTypes = {
  dimension: PropTypes.oneOf(["x", "y"]),
  scale: PropTypes.func,
}

const formatNumber = d3.format(",")
Axis.defaultProps = {
  dimension: "x",
}

export default Axis
