import React from 'react';
import { AreaChart } from 'react-easy-chart';
import * as d3 from 'd3';
export default class App extends React.Component {
  componentDidMount() {}
  render() {
    const { data } = this.props;
    return (
      <div className='app-container'>
        <Chart data={d3.csvParse(data)} />
      </div>
    );
  }
}
