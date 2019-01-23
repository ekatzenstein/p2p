import { push } from 'connected-react-router';
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
    d3.csv('/data/data.csv').then((data, err) => {
      dispatch({
        type: constants.GET_DATA,
        data
      });
    });
  };
};
