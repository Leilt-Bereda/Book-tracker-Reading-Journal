import { Link } from 'react-router-dom';
import image from './assets/home.jpeg';
import { useState } from "react";
import { login } from "./auth";

// ...existing imports...
import { useNavigate } from "react-router-dom"; // Add this if you want to redirect after login

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate(); // Add this if you want to redirect

  const handleSubmit = async (e) => {
  e.preventDefault();
  setError("");
  const data = await login({ email, password });
  if (data.access_token) {
    localStorage.setItem("token", data.access_token);
    navigate("/Form1"); // <-- Redirect to home or dashboard after login
  } else {
    setError(data.error || "Login failed");
  }
};

  return (
    <div className="flex flex-col md:flex-row h-screen m-15 md:m-0 ">
      <div className="w-full md:w-1/2 h-auto md:h-screen flex items-center justify-center">
        <div className="w-[350px] h-[538px] relative">
          <h1 className="text-3xl font-medium mb-5">Welcome Back!</h1>
          <p className="mb-14">Enter your Credentials to access your account</p>
          <form onSubmit={handleSubmit}>
            <p className="font-medium">Email</p>
            <input
              type="email"
              className="w-full border border-gray-400 px-2 py-1 placeholder:text-xs text-sm rounded-lg mb-5"
              placeholder="Enter your email"
              value={email}
              onChange={e => setEmail(e.target.value)}
              required
            />
            <p className="font-medium">Password</p>
            <input
              type="password"
              className="w-full border border-gray-400 px-2 py-1 placeholder:text-xs text-sm rounded-lg mb-5"
              placeholder="Enter your password"
              value={password}
              onChange={e => setPassword(e.target.value)}
              required
            />

            <a href="" className="text-[#0C2A92] text-xs">
              forgot password?
            </a>

            <button className="w-full bg-[#546F9D] text-white p-1 rounded-xl mt-10 font-medium cursor-pointer" type="submit">
              Login
            </button>
            {error && <div className="text-red-500 mt-2">{error}</div>}
          </form>
          <p className="absolute bottom-0 left-1/2 -translate-x-1/2 text-center font-medium text-sm w-full">
            Don't have an account?{' '}
            <Link to="/SignUp" className="text-[#0F3DDE]">
              Sign Up
            </Link>
          </p>
        </div>
      </div>

      <div className="hidden md:block w-full md:w-1/2 h-64 md:h-screen">
        <img
          className="h-full w-full md:w-auto object-cover object-left rounded-l-4xl"
          src={image}
          alt=""
        />
      </div>
    </div>
  );
}