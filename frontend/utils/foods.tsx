import axios from "axios";

const API_URL = "/api/foods/";

export interface iFoodCategory {
    id: number;
    description: string;
}

export interface iNutrient {
    id: number;
    name: string,
    unit_name: string,
    rank: number
}

export interface iNutrients {
    id: number,
    food: number,
    nutrient: number | iNutrient,
    amount: number
}

export interface iFood {
    id: number;
    description: string;
    food_category: iFoodCategory;
    nutrients: iNutrients[];
}

export const matchingFoods = async (pattern: string | null) => {
    try {
        const response = await axios.get(`${API_URL}matching-foods/`, {params: {pattern: pattern}})
        return response.data
    }
    catch (e) {
        throw new Error("Food retrieval failed.");
    }
}

export const retrieveFood = async (id: number | null) => {
    try {
        const response = await axios.get(`${API_URL}retrieve-food/${id}`)
        return response.data
    }
    catch (e) {
        throw new Error("Food retrieval failed.");
    }
}