import React, { Component } from 'react';
import { connect } from 'react-redux';
import { mapDispatchToProps } from './util/withActions';
import Chart from './chart/container';

const group = [
  {
    data: 'Hack Week 2019',
    renderType: 'title'
  },
  {
    x: 'fin',
    y: 'vehic',
    renderType: 'scatter'
  },
  {
    data: 'Why We Hack',
    renderType: 'subtitle'
  },
  {
    data:
      'While last year’s Hack Week was our first, it helped us start the year with a fresh perspective, stretch our thinking and pull the company together in a fun, collaborative way. A week dedicated to data-driven projects outside the scope of our normal work, Hack Week is not only a chance for us to flex our creative muscles and get our hands dirty with code, it’s also an opportunity to work with new people and build rapport.',
    renderType: 'paragraph'
  }
];

class App extends Component {
  componentDidMount() {
    this.props.actions.getData();
  }
  render() {
    const { data } = this.props;
    return (
      <div className='app-container'>
        <Chart data={data} group={group} />
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    data: state.data.data
  };
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(App);
