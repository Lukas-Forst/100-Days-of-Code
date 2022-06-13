import React, { createContext, useContext } from "react"
import { dimensionsPropsType } from "./utils"

import "./Chart.css"

export const useChartDimensions = () => {}
const ChartContext = createContext()

const Chart = ({ dimensions, children }) => (
  <ChartContext.Provider value={dimensions}>
  <svg
    className="Chart"
    width={dimensions.width}
    height={dimensions.height}>
    { children }
    </svg>
  </ChartContext.Provider>
  )

Chart.propTypes = {
  dimensions: dimensionsPropsType,
}

Chart.defaultProps = {
  dimensions: {},
}

export default Chart
