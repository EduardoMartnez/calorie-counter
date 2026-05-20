interface iFood {
    id: BigInteger;
    description: string;
    food_category: string;
    calories: Int32Array;
}

export const iItem = ({ id, description, food_category, calories }: iFood) => {
    return (
        <div className="profile__card rounded-15px border border-solid">
            <div className="bg-slate-300 p-3">
                <h2 className="">Description: {description}</h2>
                <p>Category: {food_category}</p>
                <p>Calories: {calories}</p>
            </div>
        </div>
    )
}