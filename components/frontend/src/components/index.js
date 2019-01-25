import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import axios from 'axios';
import { mapDispatchToProps } from './util/withActions';
import Chart from './chart/container';

class App extends Component {
  state = {
    pages: []
  };
  componentDidMount() {
    const pageId = this.props.match.params.pageId;
    if (pageId) {
      this.props.actions.getData(pageId);
    } else {
      axios.get('api/pages/').then((res) => {
        this.setState({ pages: res.data.map((d) => d.id) });
      });
    }
  }
  render() {
    const { data } = this.props;
    const { pages } = this.state;
    const pageId = this.props.match.params.pageId;
    return (
      <div className='app-container'>
        <Link to='/'>
          <img src='/img/logo.svg' height='60px' />
        </Link>
        {pageId ? <Chart group={data} /> : null}
        {!pageId ? (
          <div className='content-container'>
            {pages.map((page) => {
              return (
                <div className='link-row' key={page}>
                  <Link to={`/${page}`}>{page}</Link>
                </div>
              );
            })}
          </div>
        ) : null}
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
