import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  color: "",
};
export const themeSlice = createSlice({
  name: "theme",
  initialState,
  reducers: {
    setColorDark: (state) => {
      state.color = " dark";
    },
    setColorLight: (state) => {
      state.color = "";
    },
  },
});

export const themeReducer = themeSlice.reducer;
export const { setColorDark, setColorLight } = themeSlice.actions;
export const selectThemeColor = (state) => state.theme.color;