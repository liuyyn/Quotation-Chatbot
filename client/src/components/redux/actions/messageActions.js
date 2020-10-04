import * as type from "./types";
import axios from "axios";

export const addUserMessage = (data) => (dispatch) => {
  dispatch({
    type: type.ADD_USER_MESSAGE,
    payload: data,
  });
};

// export const getBotMessage = () => (dispatch) => {
//   dispatch({
//     type: type.GET_BOT_MESSAGE,
//     payload: data,
//   });
// };

export const getBotMessage = () => (dispatch) => {
  axios
    .get("/")
    .then((res) => dispatch({ type: type.GET_BOT_MESSAGE, payload: res.data }));
};

// export const getBotMessage = (data) => (dispatch) => {
//   axios
//     .post("/", data)
//     .then((res) => dispatch({ type: type.GET_BOT_MESSAGE, payload: res.data }));
// };
