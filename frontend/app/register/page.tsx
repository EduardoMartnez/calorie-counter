"use client"
import React from 'react';
import { useState } from "react";
import { registerUser } from '../../utils/auth';
import Navbar from '../components/navbar/Navbar';

export default function registerPage() {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [email, setEmail] = useState("")

    const handleSubmit = async (e: any) => {
        e.preventDefault()
        if (username === "" || password === "" || email === "") {
            return
        }
        try {
            await registerUser(email, username, password)
            alert("User created")
        } catch (e) {
            alert("User creation failed")
        }
    }
    return (
        <>
            <Navbar/>
            <div className='min-h-screen bg-gray-100 items-center flex flex-col justify-center'>
                <form onSubmit={handleSubmit} className='bg-gray-600 p-8 flex flex-col rounded-lg'>
                    <label>Username</label>
                    <input className='bg-white text-gray-900 p-2 rounded border' type="text" value={username} required 
                    onChange={(e)=>{setUsername(e.target.value)}}/>
                    <br />

                    <label>Email</label>
                    <input className='bg-white text-gray-900 p-2 rounded border' type="email" value={email} required
                    onChange={(e)=>{setEmail(e.target.value)}}/>
                    <br />

                    <label>Password</label>
                    <input className='bg-white text-gray-900 p-2 rounded border' type="password" value={password} required
                    onChange={(e)=>{setPassword(e.target.value)}}/>
                    <br />

                    <button
                    className='bg-blue-400 p-2 rounded text-white'
                    type="submit">Register</button>
                </form>
            </div>
        </>
    )
}