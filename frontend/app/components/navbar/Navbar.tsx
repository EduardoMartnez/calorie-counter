"use client"
import { useState, useEffect } from "react";
import Link from "next/link";
import { logoutUser, getUserInfo, refreshToken } from "@/utils/auth"

export default function Navbar() {
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
    <>
      <nav className="w-full h-20 bg-emerald-800 sticky top-0">
        <div className="container mx-auto px-4 h-full">
          <div className="flex justify-between items-center h-full">
            
            {/* Title and Home button */}
            <Link
              href="/"
              className="text-white"
            >
              Calorie Counter
            </Link>

            {/* Navigation Buttons */}
            <ul className="hidden md:flex gap-x-6 text-white">

              {/* Login Or Register / Meal Plan or Logout */}
              {!user ? (
                <>
                  <li>
                    <Link
                      href="/login"
                    >
                      Login
                    </Link>
                  </li>
                  <li>
                    <Link
                      href="/register"
                    >
                      Register
                    </Link>
                  </li>
                </>
              ) : (
                <>
                  <li>
                    <Link
                      href="/mealplan"
                    >
                      Meal Plan
                    </Link>
                  </li>
                  <li>
                    <button
                      onClick={handleLogout}
                    >
                      Logout
                    </button>
                  </li>
                </>
              )}
            </ul>
          </div>
        </div>
      </nav>
    </>
  );
};