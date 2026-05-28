'use client'

import { useState, useEffect } from "react"
import { useSearchParams } from 'next/navigation'
import { iFood, matchingFoods } from "@/utils/foods"
import SearchInput from "./Searchinput";
import Link from "next/link";

export default function SearchBar() {
    const [foods, setFoods] = useState<iFood[]>([])
    const searchParams = useSearchParams()
    const searchQuery = searchParams.get("pattern")
    const fetchFoods = async () => {
        try {
            const response = await matchingFoods(searchQuery)
            setFoods(response)
        } catch (error) {
            console.error(error)
            setFoods([])
        }
    }
    
    useEffect(() => {
        fetchFoods()
    }, [searchQuery])

    return (

        <section className="h-100vh w-screen px-2rem md:px-6rem mt-100px">
            <p className="mb-10">
                Showing {foods.length} Foods
            </p>
            <SearchInput defaultValue={searchQuery} />
            <div className="mt-8">
                {foods.length === 0 ? (
                    <p>No results returned</p>
                ) : (
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
                        {foods.map(food =>
                            <div
                                key={food.id}
                                className="border rounded-xl p-4"
                            >
                                <Link href={`food/id?=${food.id}`}>
                                    <h2>{food.description}</h2>
                                    <p>Category: {food.food_category.description}</p>
                                    {food.nutrients && <p>Calories: {food.nutrients[0].amount}</p>}
                                </Link>
                                
                            </div>
                        )}
                    </div>
                )}
            </div>
        </section>
    )
}