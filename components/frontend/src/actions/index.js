import { push } from 'connected-react-router';
import axios from 'axios';
import * as constants from '../config/constants';
import * as d3 from 'd3';
export { push } from 'connected-react-router';

export const fetchRisks = () => {
  return (dispatch, getState) => {
    setTimeout(() => {
      dispatch({
        type: constants.FETCH_RISKS,
        data: ['risk1']
      });
    }, 800);
  };
};

export const getData = () => {
  return (dispatch) => {
    Promise.all([d3.csv('/data/data.csv'), d3.csv('/data/truncated.csv')]).then(
      (data, err) => {
        // axios.get('/pages').then((res) => {
        //   console.log(res);
        // });
        dispatch({
          type: constants.GET_DATA,
          data: {
            df1: data[0],
            df2: data[1]
          }
        });
      }
    );
  };
};
