import axios from "axios";

const API_URL = "/api/foods/";

export const matchingFoods = async (pattern: string | null) => {
    try {
        const response = await axios.get(`${API_URL}matching-foods/`, {params: pattern})
        return response.data
    }
    catch (e) {
        throw new Error("Food retrieval failed.");
    }
}