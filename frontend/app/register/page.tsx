"use client"
import React from 'react';
import { useState } from "react";
import { registerUser } from '../../utils/auth';

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
        <div>
            <form onSubmit={handleSubmit}>
                <label>Username</label>
                <input value={username} required 
                onChange={(e)=>{setUsername(e.target.value)}}/>
                <br />

                <label>Email</label>
                <input value={email} required
                onChange={(e)=>{setEmail(e.target.value)}}/>
                <br />

                <label>Password</label>
                <input type="password" value={password} required
                onChange={(e)=>{setPassword(e.target.value)}}/>
                <br />

                <button
                type="submit">Register</button>
            </form>
        </div>
    )
}