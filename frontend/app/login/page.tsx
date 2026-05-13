"use client"
import React from 'react';
import { useState } from "react";
import { loginUser } from '../../utils/auth';

export default function loginPage() {
    const [password, setPassword] = useState("")
    const [email, setEmail] = useState("")

    const handleSubmit = async (e: any) => {
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
        <div>
            <form onSubmit={handleSubmit}>
                <label>Email</label>
                <input type="email" value={email} required
                onChange={(e)=>{setEmail(e.target.value)}}/>
                <br />

                <label>Password</label>
                <input type="password" value={password} required
                onChange={(e)=>{setPassword(e.target.value)}}/>
                <br />

                <button
                type="submit">Login</button>
            </form>
        </div>
    )
}