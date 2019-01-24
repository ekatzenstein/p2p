import { bindActionCreators } from 'redux';
import * as Actions from '../../../actions'

export const mapDispatchToProps = (dispatch) => {
  return {
    actions: bindActionCreators(Actions, dispatch)
  };
}