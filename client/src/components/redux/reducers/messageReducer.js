import * as type from "../actions/types";

const initialState = {
  messages: [],
};

export default function (state = initialState, action) {
  switch (action.type) {
    case type.ADD_USER_MESSAGE:
      return {
        ...state,
        messages: [...state.messages, action.payload],
      };
    case type.GET_BOT_MESSAGE:
      return {
        ...state,
        messages: [
          ...state.messages,
          action.payload,
          // { person: "Mr Health Quotation", message: action.payload },
        ],
      };
    default:
      return state;
  }
}
