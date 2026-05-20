"use client"
import { useState, ChangeEvent } from "react";
import { matchingFoods } from "@/utils/searchbar"

interface iDefault {
    defaultValue: string | null
}

export default function Searchbar({ defaultValue }: iDefault) {

    // We need to grab the current search parameters and use it as default value for the search input

    const [inputValue, setValue] = useState(defaultValue)

    const handleChange = (event: ChangeEvent<HTMLInputElement>) =>{
        const inputValue = event.target.value;

        setValue(inputValue);
    }



    // If the user clicks enter on the keyboard, the input value should be submitted for search 

    // We are now routing the search results to another page but still on the same page


    const handleSearch = async () => {
        if (inputValue) return await matchingFoods(inputValue)
    }


    const handleKeyPress = async (event: { key: any; }) => {
        if (event.key === "Enter") return handleSearch()
    }



    return (
        <>
            <div className="search__input border-2px border-solid border-slate-500 flex flex-row items-center gap-5 p-1 rounded-[15px]">
                <label htmlFor="input_box">Food Search</label>
                <input type="text"
                    id="input_box"
                    placeholder="Enter your keywords"
                    value={inputValue ?? ""} onChange={handleChange}
                    onKeyDown={handleKeyPress}
                    className="bg-transparent outline-none border-none w-full py-3 pl-2 pr-3"/>
            </div>
        </>
  );
};