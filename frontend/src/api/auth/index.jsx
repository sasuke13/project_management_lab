import Endpoints from "../endpoints";
import { axiosInstance } from "../instance";

export const login = (params) => 
    axiosInstance.post(Endpoints.AUTH.LOGIN, params);

export const logout = () =>  axiosInstance.get(Endpoints.AUTH.LOGOUT);


export const getProfile = () => axiosInstance.get(Endpoints.AUTH.PROFILE);

export const refreshToken = () => axiosInstance.get(Endpoints.AUTH.REFRESH);