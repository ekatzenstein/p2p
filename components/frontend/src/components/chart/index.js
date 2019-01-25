import React from 'react';
import * as d3 from 'd3';
import responsive from './hoc/responsive';
import Axis from './format/Axis';
import Grid from './format/Grid';
import { NodeGroup } from 'react-move';
import { easeCubicInOut } from 'd3-ease';

class Chart extends React.Component {
  get xKey() {
    return this.props.x;
  }
  get yKey() {
    return this.props.y;
  }
  get rKey() {
    return this.props.r;
  }
  get colorKey() {
    return this.props.color;
  }

  get data() {
    return this.props.data;
  }
  get binCount() {
    return this.props.bins || 10;
  }

  margin = {
    top: 20,
    bottom: 60,
    left: 0,
    right: 0
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

  get histo() {
    const {
      scale: { x }
    } = this;
    return d3
      .histogram()
      .domain(x.domain())
      .thresholds(x.ticks(this.binCount));
  }

  get bins() {
    const { data, xKey, histo } = this;
    return histo(data.map((d) => +d[xKey]));
  }

  yScaleHisto = (data) => {
    const {
      h,
      margin: { top }
    } = this;
    return d3
      .scaleLinear()
      .domain([0, d3.extent(data.map((bin) => bin.length))[1]])
      .range([h, top]);
  };

  get scale() {
    const {
      margin: { top, left }
    } = this;
    const { w, h } = this;
    const { xKey, yKey, rKey, colorKey, data } = this;

    return {
      x: d3
        .scaleLinear()
        .domain(d3.extent(data.map((d) => +d[xKey])))
        .range([left, w]),
      y: d3
        .scaleLinear()
        .domain(d3.extent(data.map((d) => +d[yKey])))
        .range([h, top]),
      color: (value) => {
        return d3.interpolateYlGnBu(
          d3
            .scaleLinear()
            .domain(d3.extent(data.map((d) => +d[colorKey])))
            .range([0.4, 1])(value)
        );
      },
      r: d3
        .scaleLinear()
        .domain(d3.extent(data.map((d) => +d[rKey])))
        .range([4, 30])
    };
  }

  ticks = 10;

  get binData() {
    const {
      scale: { x, y, r, yHisto, color },
      bins,
      h
    } = this;
    const yScaleHisto = this.yScaleHisto(bins);
    return bins.map((bin, i) => {
      return {
        x0: bin.x0,
        x1: bin.x1,
        length: bin.length,
        p2pIndex: i,
        x: x(bin.x0),
        y: yScaleHisto(bin.length),
        width: (x(bin.x1) - x(bin.x0)) * 0.9,
        height: h - yScaleHisto(bin.length)
      };
    });
  }

  render() {
    const { ticks, gridTicks } = this;
    const {
      margin,
      margin: { top, left, bottom },
      w,
      h,
      scale,
      scale: { x, y, r, yHisto, color },
      bins,
      binCount
    } = this;
    const { width, height, xOptions, chartType, handleHover } = this.props;
    const { xKey, yKey, rKey, colorKey, data } = this;
    const yScaleHisto = this.yScaleHisto(bins);

    if (width === 0 || !data.length) return null;

    return (
      <div className='svg-container'>
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
            yScaleHisto={yScaleHisto}
            chartType={chartType}
          />
          {chartType === 'scatter' && (
            <Grid
              margin={margin}
              w={w}
              h={h}
              orientation={'vertical'}
              scale={scale}
              ticks={ticks}
            />
          )}
          <Axis
            margin={margin}
            w={w}
            h={h}
            orientation={'horizontal'}
            name={yKey}
            scale={scale}
            ticks={ticks}
            yScaleHisto={yScaleHisto}
            chartType={chartType}
          />
          <Axis
            margin={margin}
            w={w}
            h={h}
            orientation={'vertical'}
            name={xKey}
            scale={scale}
            ticks={ticks}
          />

          {chartType === 'scatter' && (
            <g className='scatter-plot'>
              <NodeGroup
                data={data.map((d, i) => ({ ...d, p2pIndex: i }))}
                keyAccessor={(d, i) => d.p2pIndex}
                start={(datum) => ({
                  cx: x(+datum[xKey]),
                  cy: y(+datum[yKey]),
                  r: 0,
                  fill: color(+datum[colorKey]),
                  opacity: 0
                })}
                enter={(datum, i) => ({
                  cx: [x(+datum[xKey])],
                  cy: [y(+datum[yKey])],
                  r: [r(+datum[rKey]) || 3],
                  fill: [color(+datum[colorKey])],
                  opacity: [rKey || colorKey ? 0.6 : 1],
                  timing: {
                    duration: 1200,
                    ease: easeCubicInOut
                  }
                })}
                update={(datum, i) => ({
                  cx: [x(+datum[xKey])],
                  cy: [y(+datum[yKey])],
                  r: [r(+datum[rKey]) || 3],
                  fill: [color(+datum[colorKey])],
                  opacity: [rKey || colorKey ? 0.6 : 1],
                  timing: {
                    duration: 800,
                    delay: (i / data.length) * 1000,
                    ease: easeCubicInOut
                  }
                })}
              >
                {(nodes) => {
                  return (
                    <g>
                      {nodes.map((node, i) => {
                        const {
                          data,
                          state: { cx, cy, r, fill, opacity }
                        } = node;
                        return (
                          <circle
                            ref={(node) => {
                              this[`circle-${i}`] = node;
                            }}
                            key={i}
                            style={{
                              fill,
                              opacity
                            }}
                            cx={cx}
                            cy={cy}
                            r={r}
                            onMouseOver={() => {
                              handleHover(
                                data,
                                this[`circle-${i}`],
                                [
                                  { label: 'x', key: xKey },
                                  { label: 'y', key: yKey },
                                  { label: 'radius', key: rKey },
                                  { label: 'color', key: colorKey }
                                ].filter((el) => el.key)
                              );
                            }}
                          />
                        );
                      })}
                    </g>
                  );
                }}
              </NodeGroup>
            </g>
          )}
          {chartType === 'histogram' && (
            <g className='histogram'>
              <NodeGroup
                data={this.binData}
                keyAccessor={(b, i) => {
                  return b.p2pIndex + '-key-' + xKey;
                }}
                start={(bin) => ({
                  x: bin.x,
                  y: h,
                  width: bin.width,
                  height: 0
                })}
                enter={(bin, i) => ({
                  x: [bin.x],
                  y: [bin.y],
                  width: [bin.width],
                  height: [bin.height],
                  timing: {
                    duration: 800,
                    delay: 800 + (i / binCount) * 1000,
                    ease: easeCubicInOut
                  }
                })}
                update={(bin, i) => ({
                  x: [bin.x],
                  y: [bin.y],
                  width: [bin.width],
                  height: [bin.height],
                  timing: {
                    duration: 800,
                    delay: (i / binCount) * 1000,
                    ease: easeCubicInOut
                  }
                })}
                leave={(bin, i) => {
                  return {
                    x: [bin.x],
                    y: [h],
                    width: [bin.width],
                    height: [0],
                    timing: {
                      duration: 800,
                      ease: easeCubicInOut
                    }
                  };
                }}
              >
                {(nodes) => {
                  return (
                    <g>
                      {nodes.map((node, i) => {
                        const { data, state } = node;
                        return <rect {...state} key={i} />;
                      })}
                    </g>
                  );
                }}
              </NodeGroup>
            </g>
          )}
        </svg>
      </div>
    );
  }
}

Chart.defaultProps = {
  xOptions: [],
  yOptions: [],
  rOptions: [],
  colorOptions: []
};

export default responsive(Chart);
