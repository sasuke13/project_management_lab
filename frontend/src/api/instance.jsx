import axios from "axios";
import Endpoints from "./endpoints";
//import { config } from "webpack";
import store from "../store";
import { getAccessToken, logoutUser } from '../store/auth/actionCreators';

export const axiosInstance = axios.create({})

const urlsSkipAuth = [Endpoints.AUTH.LOGIN, Endpoints.AUTH.REFRESH, Endpoints.AUTH.LOGOUT ]

axiosInstance.interceptors.request.use(async (config) => {
    if (config.url && urlsSkipAuth.includes(config.url)){
        return config
    }

    const accessToken = await store.dispatch(getAccessToken())

    if (accessToken) {
        const authorization = `Bearer ${accessToken}`

        config.headers = {
            ...config.headers,
            authorization: authorization
        }
    }
    return config
});

axiosInstance.interceptors.response.use(
   (response) => response, (error) => {
    const isLoggedIn =!!store.getState().auth.authData.accessToken;

    if ((error.response?.status === 401) && isLoggedIn && error.request.url !== Endpoints.AUTH.LOGOUT) {
        store.dispatch(logoutUser())
    }
   throw error;
});