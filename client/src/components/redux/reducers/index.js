import { combineReducers } from "redux";
import messageReducer from "./messageReducer";

const rootReducer = combineReducers({
  messages: messageReducer,
});

export default rootReducer;
