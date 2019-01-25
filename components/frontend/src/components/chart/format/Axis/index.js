import React from 'react';
import * as d3 from 'd3';

const Axis = (props) => {
  const {
    margin: { top, left, right, bottom },
    scale: { x, y },
    w,
    h,
    orientation,
    ticks,
    name,
    chartType,
    bins,
    yScaleHisto
  } = props;

  const labelOffset = 55;

  const t = chartType === 'scatter' ? ticks : bins;
  const yy = chartType === 'histogram' ? yScaleHisto : y;

  return (
    <g>
      {orientation === 'horizontal' ? (
        <g transform={`translate(${left},${0})`}>
          <g
            ref={(g) =>
              d3.select(g).call(
                d3
                  .axisLeft(yy)
                  .ticks(t)
                  .tickFormat(d3.format('.2s'))
              )
            }
          />
          <g transform={`translate(${0},${top})`}>
            <text
              className='axis-label-enigma'
              dx={0}
              dy={-labelOffset}
              textAnchor='end'
              transform='rotate(-90)'
            >
              {chartType !== 'histogram' && name}
            </text>
          </g>
        </g>
      ) : (
        <g>
          <g
            transform={`translate(0,${h})`}
            ref={(g) =>
              d3.select(g).call(
                d3
                  .axisBottom(x)
                  .ticks(ticks)
                  .tickFormat(d3.format('.2s'))
              )
            }
          />
          <g transform={`translate(${w},${h})`}>
            <text
              className='axis-label-enigma'
              dx={0}
              dy={labelOffset}
              textAnchor='end'
            >
              {name}
            </text>
          </g>
        </g>
      )}
    </g>
  );
};

export default Axis;
