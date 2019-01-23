import React, { Component } from 'react';
import { connect } from 'react-redux';
import { mapDispatchToProps } from './util/withActions';
import Chart from './chart/container';

class App extends Component {
  componentDidMount() {
    this.props.actions.getData();
  }
  render() {
    const { data } = this.props;
    return (
      <div className='app-container'>
        <Chart data={data} />
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
