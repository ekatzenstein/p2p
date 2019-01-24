import React from 'react';
import Chart from './index';
// import { ReactComponent as Logo } from './img/logo.svg';
import { data } from './csv';
import * as d3 from 'd3';

class Title extends React.Component {
  render() {
    return <h1>{this.props.data}</h1>;
  }
}

class ScatterPlot extends React.Component {
  render() {
    return (
      <div className='enigma-chart-container' id='main-chart'>
        <Chart id='main-chart' {...this.props} />
      </div>
    );
  }
}

class Subtitle extends React.Component {
  render() {
    return <h2>{this.props.data}</h2>;
  }
}

class Paragraph extends React.Component {
  render() {
    return <p>{this.props.data}</p>;
  }
}

class ChartContainer extends React.Component {
  getItem = (item, index) => {
    switch (item.renderType) {
      case 'scatter':
        return <ScatterPlot {...item} data={this.props.data} key={index} />;
      case 'title':
        return <Title {...item} key={index} />;
      case 'subtitle':
        return <Title {...item} key={index} />;
      case 'paragraph':
        return <Paragraph {...item} key={index} />;
      default:
        return null;
    }
  };
  render() {
    return (
      <div className='content-container'>
        <div className='header-content'>{/* <Logo height='40px' /> */}</div>
        {this.props.group.map((item, i) => {
          return this.getItem(item, i);
        })}
      </div>
    );
  }
}

export default ChartContainer;
