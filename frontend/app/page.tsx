"use client"
import { logoutUser, getUserInfo, refreshToken } from "../utils/auth"
import { useState, useEffect } from "react";

export default function Home() {
  type User = {
    username: string,
    email: string,
    password: string
  }

  const [user, setUser] = useState<User>();
  useEffect(() => {
    const getUser = async () => {
      const userDetails = await getUserInfo()
      if (userDetails) {
        setUser(userDetails)
      }
    }
    getUser()
  }, [])

  const handleLogout = async () => {
    await logoutUser();
  }

  const handleRefresh = async () => {
    await refreshToken();
  }

  return (
    <div>
      <div>
        {user ? <h1> Hi, {user.username}</h1> : <h1>Welcome stranger!</h1>}
        <button onClick={handleLogout}>Logout</button>
        <button onClick={handleRefresh}>Refresh Token</button>
      </div>
      
    </div>
  );
}
