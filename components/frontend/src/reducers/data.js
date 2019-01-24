import { GET_DATA } from '../config/constants';

const initialState = {
  data: []
};

const reducer = (state = initialState, action) => {
  const { data } = action;
  switch (action.type) {
    case GET_DATA:
      return {
        ...state,
        data
      };
    default:
      return state;
  }
};

export default reducer;
