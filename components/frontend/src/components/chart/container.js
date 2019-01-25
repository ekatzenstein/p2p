import React from 'react';
import Chart from './index';
import cx from 'classnames';
// import { ReactComponent as Logo } from './img/logo.svg';
import * as d3 from 'd3';

class Title extends React.Component {
  render() {
    return <h1>{this.props.data}</h1>;
  }
}
class Options extends React.Component {
  render() {
    const { options, name, handleClick, active } = this.props;
    return (
      <div className='options'>
        <div className='option-label'>{name}:</div>
        {options.map((option, j) => {
          return (
            <div
              className={cx({ option: true, active: option === active })}
              key={j}
              onClick={() => {
                handleClick(option);
              }}
            >
              {option}
            </div>
          );
        })}
      </div>
    );
  }
}
class ScatterPlot extends React.Component {
  state = {
    xKey: this.props.x,
    yKey: this.props.y,
    colorKey: this.props.color,
    rKey: this.props.r
  };
  render() {
    const { xOptions, yOptions, rOptions, colorOptions } = this.props;
    const { xKey, yKey, colorKey, rKey } = this.state;

    return (
      <div className='svg-container'>
        {xOptions.length ? (
          <Options
            name='x-axis'
            options={xOptions}
            active={xKey}
            handleClick={(value) => {
              this.setState({ xKey: value });
            }}
          />
        ) : null}
        {yOptions.length ? (
          <Options
            name='y-axis'
            options={yOptions}
            active={yKey}
            handleClick={(value) => {
              this.setState({ yKey: value });
            }}
          />
        ) : null}
        {rOptions.length ? (
          <Options
            name='radius'
            options={rOptions}
            active={rKey}
            handleClick={(value) => {
              this.setState({ rKey: value });
            }}
          />
        ) : null}
        {colorOptions.length ? (
          <Options
            name='color'
            options={colorOptions}
            active={colorKey}
            handleClick={(value) => {
              this.setState({ colorKey: value });
            }}
          />
        ) : null}
        <div className='enigma-chart-container' id='main-chart'>
          <Chart
            id='main-chart'
            {...this.props}
            x={xKey}
            y={yKey}
            color={colorKey}
            r={rKey}
            chartType='scatter'
          />
        </div>
      </div>
    );
  }
}

ScatterPlot.defaultProps = {
  xOptions: [],
  rOptions: [],
  colorOptions: [],
  yOptions: []
};
class Histogram extends React.Component {
  state = {
    xKey: this.props.x,
    yKey: this.props.y,
    colorKey: this.props.color,
    rKey: this.props.r
  };
  render() {
    const { xOptions, yOptions, rOptions, colorOptions } = this.props;
    const { xKey, yKey, colorKey, rKey } = this.state;

    return (
      <div className='svg-container'>
        {xOptions.length ? (
          <Options
            name='x-axis'
            options={xOptions}
            active={xKey}
            handleClick={(value) => {
              this.setState({ xKey: value });
            }}
          />
        ) : null}

        <div className='enigma-chart-container' id='main-chart'>
          <Chart
            id='main-chart'
            {...this.props}
            x={xKey}
            y={yKey}
            color={colorKey}
            r={rKey}
            chartType='histogram'
          />
        </div>
      </div>
    );
  }
}

Histogram.defaultProps = {
  xOptions: [],
  rOptions: [],
  colorOptions: [],
  yOptions: []
};

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
        return (
          <ScatterPlot
            {...item}
            data={this.props.data.df1 || this.props.data || []}
            key={index}
          />
        );
      case 'histogram':
        return (
          <Histogram
            {...item}
            data={this.props.data.df2 || this.props.data || []}
            key={index}
          />
        );
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
        <div className='header-content'>
          {/* <img src='/img/logo.svg' height='60px' /> */}
        </div>
        {this.props.group.map((item, i) => {
          return this.getItem(item, i);
        })}
      </div>
    );
  }
}

export default ChartContainer;
