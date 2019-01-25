import React from 'react';

export default class Tooltip extends React.Component {
  render() {
    const { x, y, content } = this.props;
    return (
      <div
        className='tooltip'
        style={{
          left: x + 'px',
          top: y + 'px',
          transformOrigin: 'bottom center',
          display: y === 0 ? 'none' : null,
          ...this.props.style
        }}
      >
        <div className='tooltip-wrap'>{content}</div>
      </div>
    );
  }
}
