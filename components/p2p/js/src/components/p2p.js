import React from 'react';
import Chart from './chart/container';
import * as d3 from 'd3';
import './style.css';

export default function P2PBaseComponent(props) {
  console.log(props);
  const { groups } = props;
  const newGroups = groups.map(group => {
    const { render_type, ...rest } = group;
    return { renderType: render_type, ...rest };
  });
  console.log(newGroups);
  return (
    <div className='app-container'>
      <Chart group={newGroups} />
    </div>
  );
}
