import React from 'react';
import * as d3 from 'd3';
import responsive from './hoc/responsive';
import Axis from './format/Axis';
import Grid from './format/Grid';
class Chart extends React.Component {
  get xKey() {
    return this.props.x || 'vehic';
  }
  get yKey() {
    return this.props.y || 'fin';
  }

  get data() {
    return this.props.data;
  }

  margin = {
    top: 20,
    bottom: 60,
    left: 150,
    right: 150
  };

  get w() {
    const {
      margin: { right, left }
    } = this;
    const { width } = this.props;
    return width - right;
  }
  get h() {
    const {
      margin: { bottom, top }
    } = this;
    const { height } = this.props;
    return height - bottom;
  }

  get scale() {
    const {
      margin: { top, left }
    } = this;
    const { w, h } = this;
    const { xKey, yKey, data } = this;

    return {
      x: d3
        .scaleLinear()
        .domain(d3.extent(data.map((d) => +d[xKey])))
        .range([left, w]),
      y: d3
        .scaleLinear()
        .domain(d3.extent(data.map((d) => +d[yKey])))
        .range([h, top])
    };
  }

  ticks = 10;

  render() {
    const { ticks, gridTicks } = this;
    const {
      margin,
      margin: { top, left, bottom },
      w,
      h,
      scale,
      scale: { x, y }
    } = this;
    const { width, height } = this.props;
    const { xKey, yKey, data } = this;

    if (width === 0 || !data.length) return null;

    return (
      <svg
        ref={(node) => (this.svg = node)}
        className='enigma-chart'
        width={width}
        height={height}
      >
        <Grid
          margin={margin}
          w={w}
          h={h}
          orientation={'horizontal'}
          scale={scale}
          ticks={ticks}
        />
        <Grid
          margin={margin}
          w={w}
          h={h}
          orientation={'vertical'}
          scale={scale}
          ticks={ticks}
        />
        <Axis
          margin={margin}
          w={w}
          h={h}
          orientation={'horizontal'}
          name={xKey}
          scale={scale}
          ticks={ticks}
        />
        <Axis
          margin={margin}
          w={w}
          h={h}
          orientation={'vertical'}
          name={yKey}
          scale={scale}
          ticks={ticks}
        />
        {/* Scatter Plot */}
        <g className='scatter-plot'>
          {data.map((datum, i) => {
            return (
              <circle key={i} cx={x(+datum[xKey])} cy={y(+datum[yKey])} r={4} />
            );
          })}
        </g>

        <rect
          x={x(0)}
          width={x(1) - x(0)}
          y={y(1)}
          height={y(0) - y(1)}
          style={{ opacity: 0.2 }}
        />
      </svg>
    );
  }
}

export default responsive(Chart);
