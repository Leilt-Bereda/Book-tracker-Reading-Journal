import { Link } from 'react-router-dom';
import image from './assets/home.jpeg';
import { useNavigate } from 'react-router-dom';
import { useState } from "react";
import { register } from "./auth";


export default function SignUp() {
  
    const navigate = useNavigate();
    const [form, setForm] = useState({ name: "", email: "", password: "" });
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(""); setSuccess("");
    const data = await register(form);
    if (data.message) {
      setSuccess("Registration successful! You can now log in.");
    } else if (data.validation_errors) {
      setError(data.validation_errors.map(e => Object.values(e)[0]).join(", "));
    } else {
      setError(data.error || "Registration failed");
    }
  };

  return (
    <div className="flex flex-col md:flex-row h-screen m-15 md:m-0"> 
      <div className="w-full md:w-1/2 h-auto md:h-screen flex items-center justify-center">
        <div className="w-[350px] h-[538px] relative">
          <h1 className="text-3xl font-medium mb-14">Get Started Now</h1>
<form onSubmit={handleSubmit}>
  <p className="font-medium">Name</p>
  <input
    type="text"
    name="name"
    value={form.name}
    onChange={handleChange}
    className="w-full border border-gray-400 px-2 py-1 placeholder:text-xs text-sm rounded-lg mb-5"
    placeholder="Enter your name"
    required
  />
  <p className="font-medium">Email</p>
  <input
    type="email"
    name="email"
    value={form.email}
    onChange={handleChange}
    className="w-full border border-gray-400 px-2 py-1 placeholder:text-xs text-sm rounded-lg mb-5"
    placeholder="Enter your email"
    required
  />
  <p className="font-medium">Password</p>
  <input
    type="password"
    name="password"
    value={form.password}
    onChange={handleChange}
    className="w-full border border-gray-400 px-2 py-1 placeholder:text-xs text-sm rounded-lg mb-5"
    placeholder="Enter your password"
    required
  />

  <div className="flex">
    <input type="checkbox" className="cursor-pointer" required />
    <p className="ml-2 text-sm">
      I agree to the <a href="" className="underline">terms & policy</a>
    </p>
  </div>

  <button
    className="w-full bg-[#546F9D] text-white p-1 rounded-xl mt-10 font-medium cursor-pointer"
    type="submit"
  >
    Sign Up
  </button>
  {error && <div className="text-red-500 mt-2">{error}</div>}
  {success && <div className="text-green-600 mt-2">{success}</div>}

  <p className="absolute bottom-0 left-1/2 -translate-x-1/2 text-center font-medium text-sm w-full">
    have an account? <Link to="/LogIn" className="text-[#0F3DDE]">Sign In</Link>
  </p>
</form>
        </div>
      </div>

      <div className="w-full md:w-1/2 h-64 hidden md:block md:h-screen">
        <img
          className="h-full w-full md:w-auto object-cover object-left rounded-l-4xl"
          src={image}
          alt=""
        />
      </div>
    </div>
  )
}
