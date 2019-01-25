import React from 'react';
import Chart from './chart/container';
import * as d3 from 'd3';
import './style.css';

export default function P2PBaseComponent(props) {
  const { groups } = props;
  const newGroups = groups.map((group) => {
    const { render_type, data, ...rest } = group;
    let newData = data;
    if (['boxplot', 'scatter', 'histogram'].indexOf(render_type) != -1) {
      newData = d3.csvParse(data);
    }
    return {
      renderType: render_type,
      data: newData,
      ...rest
    };
  });
  return (
    <div className='app-container'>
      <Chart group={newGroups} />
    </div>
  );
}
