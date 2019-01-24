import React from 'react';
import Chart from './chart/container';
import * as d3 from 'd3';
import './style.css';

export default function Thing(props) {
  console.log(props);
  return (
    <div className='app-container'>
      <Chart data={d3.csvParse(props.data)} group={props.group} />
    </div>
  );
}
