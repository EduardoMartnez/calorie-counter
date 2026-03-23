import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/users/";

export const registerUser = async (email, username, password) => {
    try {
        const response = await axios.post(`${API_URL}register/`, {email, username, password},
            {withCredentials: True}
        )
        return response.data
    }
    catch (e) {
        throw new Error("Registration failed.");
    }
}

export const loginUser = async (email, password) => {
    try {
        const response = await axios.post(`${API_URL}login/`, {email, password},
            {withCredentials: True}
        )
        return response.data
    }
    catch (e) {
        throw new Error("Login failed.");
    }
}

export const logoutUser = async () => {
    try {
        const response = await axios.post(`${API_URL}logout/`, null,
            {withCredentials: True}
        )
        return response.data
    }
    catch (e) {
        throw new Error("Logout failed.");
    }
}

export const getUserInfo = async () => {
    try {
        const response = await axios.post(`${API_URL}user-info/`, null,
            {withCredentials: True}
        )
        return response.data
    }
    catch (e) {
        throw new Error("User retrieval failed.");
    }
}

export const refreshToken = async () => {
    try {
        const response = await axios.post(`${API_URL}refresh/`, null,
            {withCredentials: True}
        )
        return response.data
    }
    catch (e) {
        throw new Error("Refreshing token failed.");
    }
}