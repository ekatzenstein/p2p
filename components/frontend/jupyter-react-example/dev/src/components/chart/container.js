import React from 'react';
import Chart from './index';
import { ReactComponent as Logo } from '../../assets/img/logo.svg';

class ChartContainer extends React.Component {
  render() {
    return (
      <div className='content-container'>
        <div className='header-content'>
          <Logo height='40px' />
        </div>
        <h1>Hack Week 2019</h1>
        <div className='enigma-chart-container' id='main-chart'>
          <Chart id='main-chart' {...this.props} />
        </div>
        <h2>Why We Hack</h2>
        <p>
          While last year’s Hack Week was our first, it helped us start the year
          with a fresh perspective, stretch our thinking and pull the company
          together in a fun, collaborative way. A week dedicated to data-driven
          projects outside the scope of our normal work, Hack Week is not only a
          chance for us to flex our creative muscles and get our hands dirty
          with code, it’s also an opportunity to work with new people and build
          rapport.
        </p>
      </div>
    );
  }
}

export default ChartContainer;
