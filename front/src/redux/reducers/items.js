import axios from "axios";
const GET_ITEMS = "GET_ITEMS";
const GET_PRODUCT = "GET_PRODUCT";
const initState = {
  items: [],
  product: {},
};
export default (state = initState, action) => {
  switch (action.type) {
    case GET_ITEMS: {
      return {
        ...state,
        items: action.items,
      };
    }
    case GET_PRODUCT: {
      return {
        ...state,
        product: action.product,
      };
    }
    default:
      return state;
  }
};
export const getItems = () => {
  return (dispatch) => {
    axios
      .get("http://127.0.0.1:8000//api/v1/servicelist/")
      .then(({ data }) => {
        return dispatch({ type: GET_ITEMS, items: data });
      });
  };
};
export const getProduct = (idx) => {
  return (dispatch) => {
    axios
      .get("http://127.0.0.1:8000//api/v1/servicelist/")
      .then(({ data }) => {
        return dispatch({ type: GET_PRODUCT, product: data[idx] });
      });
  };
};
