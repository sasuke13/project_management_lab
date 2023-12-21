import { createSlice } from '@reduxjs/toolkit';

export const initialState = {
  authData: {
    accessToken: null,
    isLoading: false,
    error: null,
  },
  profileData: {
    profile: null,
    isLoading: false,
    error: null,
  },
};

export const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    loginStart: (state) => {
      state.authData.isLoading = true;
    },
    loginSuccess: (state, action) => {
      state.authData.accessToken = action.payload;
      state.authData.isLoading = false;
      state.authData.error = null;
    },
    loginFailure: (state, action) => {
      state.authData.isLoading = false;
      state.authData.error = action.payload;
    },
    loadProfileStart: (state) => {
      state.profileData.isLoading = true;
    },
    loadProfileSuccess: (state, action) => {
      state.profileData.profile = action.payload;
      state.profileData.isLoading = false;
      state.profileData.error = null;
    },
    loadProfileFailure: (state, action) => {
      state.profileData.isLoading = false;
      state.profileData.error = action.payload;
    },
    logoutSuccess: () => initialState,
  },
});

export const { 
    loginStart,
    loginSuccess, 
    loginFailure,
    loadProfileStart, 
    loadProfileSuccess, 
    loadProfileFailure,
    logoutSuccess,
} = authSlice.actions;

export default authSlice.reducer;
