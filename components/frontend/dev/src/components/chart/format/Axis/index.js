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
    name
  } = props;

  const labelOffset = 55;

  return (
    <g>
      {orientation === 'horizontal' ? (
        <g transform={`translate(${left},${0})`}>
          <g
            ref={(g) =>
              d3.select(g).call(
                d3
                  .axisLeft(y)
                  .ticks(ticks)
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
              {name}
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
