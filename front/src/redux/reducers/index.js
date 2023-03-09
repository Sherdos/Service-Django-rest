import {combineReducers} from "redux";
import items from "./items";
import { configureStore } from "@reduxjs/toolkit";
import { themeReducer } from "./theme";
const rootReducer = () => combineReducers({
items,
reducer: {
    theme: themeReducer,
},
});

export default rootReducer;