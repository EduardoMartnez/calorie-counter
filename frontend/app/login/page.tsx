"use client"
import { ChangeEvent, useState } from 'react';
import { loginUser } from '../../utils/auth';
import Navbar from '../components/navbar/Navbar';

export default function loginPage() {
    const [password, setPassword] = useState("")
    const [email, setEmail] = useState("")

    const handleSubmit = async (e: ChangeEvent) => {
        e.preventDefault()
        if (password === "" || email === "") {
            return
        }
        try {
            await loginUser(email, password)
            alert("User logged in")
        } catch (e) {
            alert("User login failed")
        }
    }
    return (
        <>
            <Navbar/>
            <div className='min-h-screen bg-gray-100 flex flex-col items-center justify-center'>
                <form
                    onSubmit={handleSubmit}
                    className='bg-gray-600 p-8 flex flex-col gap-4 rounded-lg'
                >
                    <label className='text-white'>Email</label>

                    <input
                    className='bg-white text-gray-900 p-2 rounded border'
                    type="email"
                    value={email}
                    required
                    onChange={(e) => setEmail(e.target.value)}
                    />

                    <label className='text-white'>Password</label>

                    <input
                    className='bg-white text-gray-900 p-2 rounded border'
                    type="password"
                    value={password}
                    required
                    onChange={(e) => setPassword(e.target.value)}
                    />

                    <button
                    className='bg-blue-400 p-2 rounded text-white'
                    type="submit"
                    >
                    Login
                    </button>
                </form>
            </div>
        </>
        
    )
}