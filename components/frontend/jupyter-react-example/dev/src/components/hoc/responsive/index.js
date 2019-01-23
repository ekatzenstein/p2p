import React from 'react';

const withSubscription = (WrappedComponent) => {
  return class extends React.Component {
    state = {
      width: 0,
      height: 0
    };

    componentDidMount() {
      window.addEventListener('resize', this.handleWindowResize, false);
      setTimeout(() => this.setState(this.getWrapperSize()), 0);
    }

    componentWillUnmount() {
      window.removeEventListener('resize', this.handleWindowResize, false);
    }

    getWrapperSize = () => {
      const parent = document.getElementById(this.props.id);
      const { clientWidth, clientHeight } = parent;

      return {
        width: clientWidth,
        height: clientHeight
      };
    };

    handleWindowResize = () => {
      this.setState(this.getWrapperSize());
    };

    render() {
      return (
        <WrappedComponent
          {...this.state}
          {...this.props}
          resize={this.handleWindowResize}
        />
      );
    }
  };
};

export default withSubscription;
