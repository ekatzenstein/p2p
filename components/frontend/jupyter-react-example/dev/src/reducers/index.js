import { combineReducers } from 'redux';
import { connectRouter } from 'connected-react-router';

import data from './data';

const Reducers = (history) =>
  combineReducers({
    router: connectRouter(history),
    data
  });

export default Reducers;
