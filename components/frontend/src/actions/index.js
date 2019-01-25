import { push } from 'connected-react-router';
import axios from 'axios';
import * as constants from '../config/constants';
import * as d3 from 'd3';
export { push } from 'connected-react-router';

const api = axios.create({
  baseURL: 'api/'
});

export const getData = (id) => {
  let content;
  return (dispatch) => {
    api
      .get(`pages/${id}`)
      .then((res) => {
        if (res.data) {
          content = JSON.parse(res.data.content);
          const promises = content.map((d) =>
            d.data ? d.data : d3.csv(d.dataframe.url)
          );
          return Promise.all(promises);
        }
      })
      .then((res) => {
        const data = content.map((c, i) => ({ ...c, data: res[i] }));
        dispatch({
          type: constants.GET_DATA,
          data
        });
      });
  };
};
