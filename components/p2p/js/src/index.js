import JupyterReact from 'jupyter-react-js';
import components from './components';

const TARGET_NAME = 'p2p';

function load_ipython_extension() {
  requirejs(['base/js/namespace', 'base/js/events'], function(Jupyter, events) {
    JupyterReact.init(Jupyter, events, TARGET_NAME, {
      components,
      save: false
    });
  });
}

module.exports = {
  load_ipython_extension: load_ipython_extension
};
