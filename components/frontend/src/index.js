import React, { Fragment } from 'react';
import ReactDOM from 'react-dom';
import { connectRouter } from 'connected-react-router';
import createHistory from 'history/createBrowserHistory';
import App from './components';
import * as serviceWorker from './serviceWorker';
import { Provider } from 'react-redux';
import { Route, Router } from 'react-router-dom';
import { applyMiddleware, createStore, compose } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './reducers';
import { routerMiddleware, ConnectedRouter } from 'connected-react-router';

import './style.css';

const history = createHistory();
const historyMiddleware = routerMiddleware(history);
const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

export const store = createStore(
  rootReducer(history),
  {},
  composeEnhancers(applyMiddleware(thunk, historyMiddleware))
);

ReactDOM.render(
  <Provider store={store}>
    <ConnectedRouter history={history}>
      <div>
        <Route exact path={`/`} component={App} />
        <Route exact path={`/:pageId`} component={App} />
      </div>
    </ConnectedRouter>
  </Provider>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls. Learn
// more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
