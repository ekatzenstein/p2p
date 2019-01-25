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
        this.setState({ pages: res.data });
      });
    }
  }
  render() {
    const { data } = this.props;
    const { pages } = this.state;
    const pageId = this.props.match.params.pageId;
    console.log(pages);
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
                <div className='link-row' key={page.id}>
                  <Link to={`/${page.id}`}>{page.title || page.id}</Link>
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
