import React from 'react';
import * as d3 from 'd3';

const Grid = (props) => {
  const {
    margin: { top, left, right, bottom },
    scale: { x, y },
    w,
    h,
    orientation,
    ticks
  } = props;

  return (
    <g>
      {orientation === 'horizontal' ? (
        <g
          transform={`translate(${left},${0})`}
          className='grid-axis'
          ref={(g) =>
            d3.select(g).call(
              d3
                .axisLeft(y)
                .ticks(ticks * 2)
                .tickSize(-(w - left))
                .tickFormat('')
            )
          }
        />
      ) : (
        <g
          transform={`translate(0,${h})`}
          className='grid-axis'
          ref={(g) =>
            d3.select(g).call(
              d3
                .axisBottom(x)
                .ticks(ticks * 2)
                .tickSize(-(h - top))
                .tickFormat('')
            )
          }
        />
      )}
    </g>
  );
};

export default Grid;
