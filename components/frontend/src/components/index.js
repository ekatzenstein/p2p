import React, { Component } from 'react';
import { connect } from 'react-redux';
import { mapDispatchToProps } from './util/withActions';
import Chart from './chart/container';

const groups = [
  // {
  //   data: 'Hack Week 2019',
  //   renderType: 'title'
  // },
  // {
  //   x: 'fin',
  //   y: 'vehic',
  //   renderType: 'scatter'
  // },
  // {
  //   data: 'Why We Hack',
  //   renderType: 'subtitle'
  // },
  // {
  //   data:
  //     'While last year’s Hack Week was our first, it helped us start the year with a fresh perspective, stretch our thinking and pull the company together in a fun, collaborative way. A week dedicated to data-driven projects outside the scope of our normal work, Hack Week is not only a chance for us to flex our creative muscles and get our hands dirty with code, it’s also an opportunity to work with new people and build rapport.',
  //   renderType: 'paragraph'
  // },
  // {
  //   data: 'Hack Week 2019',
  //   renderType: 'title'
  // },
  // {
  //   x: 'fin',
  //   y: 'vehic',
  //   xOptions: ['fin', 'vehic'],
  //   yOptions: ['lloan6', 'lloan7', 'vehic'],
  //   renderType: 'scatter'
  // },
  // {
  //   data: 'Why We Hack',
  //   renderType: 'subtitle'
  // },
  // {
  //   data:
  //     'While last year’s Hack Week was our first, it helped us start the year with a fresh perspective, stretch our thinking and pull the company together in a fun, collaborative way. A week dedicated to data-driven projects outside the scope of our normal work, Hack Week is not only a chance for us to flex our creative muscles and get our hands dirty with code, it’s also an opportunity to work with new people and build rapport.',
  //   renderType: 'paragraph'
  // },
  [
    {
      data: 'Hack Week 2019',
      renderType: 'title'
    },
    {
      x: 'fin',
      y: 'networth',
      r: 'networth',
      color: 'lloan7',
      xOptions: ['fin', 'vehic'],
      yOptions: ['lloan6', 'lloan7', 'vehic', 'networth'],
      rOptions: ['networth', 'lloan7', 'vehic'],
      colorOptions: ['lloan7', 'fin', 'networth', 'vehic'],
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
  ],
  [
    {
      data: 'Hack Week 2019',
      renderType: 'title'
    },
    {
      x: 'vehic',
      xOptions: ['fin', 'vehic'],
      renderType: 'histogram',
      bins: 20
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
  ]
];

class App extends Component {
  componentDidMount() {
    this.props.actions.getData();
  }
  render() {
    const { data } = this.props;
    return (
      <div className='app-container'>
        {groups.map((group, i) => {
          return <Chart data={data} group={group} key={i} />;
        })}
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
