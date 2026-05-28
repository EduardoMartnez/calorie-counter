'use client'

import { useState, useEffect } from "react"
import { useSearchParams } from 'next/navigation'
import { iFood, iNutrient, matchingFoods, retrieveFood } from "@/utils/foods"
import Link from "next/link";
import Navbar from "../components/navbar/Navbar";

export default function Food() {
    const [food, setFood] = useState<iFood>()
    const searchParams = useSearchParams()
    const searchQuery = searchParams.get("id")
    const fetchFoods = async () => {
        try {
            const response = await retrieveFood(Number(searchQuery))
            setFood(response)
        } catch (error) {
            console.error(error)
        }
    }
    
    useEffect(() => {
        fetchFoods()
    }, [searchQuery])

    return (
        <>
            <Navbar/>
            <section className="h-100vh w-screen px-2rem md:px-6rem mt-100px">
                {!food ? (
                    <p>Invalid food ID</p>
                ) : (
                    <>
                        <p>{food.description}</p>
                        <p>Category: {food.food_category.description}</p>
                        <div className="mt-8">
                            <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
                                {food.nutrients.map(nutrient =>
                                    <div
                                        key={nutrient.id}
                                        className="border rounded-xl p-4"
                                    >
                                        {typeof nutrient.nutrient !== "number" && (
                                                <>
                                                    <h2>{nutrient.nutrient.name}</h2>
                                                    <p>Amount: {nutrient.amount} {nutrient.nutrient.unit_name}</p>
                                                </>
                                            )
                                        }
                                    </div>
                                )}
                            </div>
                        </div>
                    </>
                )}
            </section>
        </>
    )
}