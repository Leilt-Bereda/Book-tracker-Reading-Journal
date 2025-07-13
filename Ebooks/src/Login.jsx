import { Link } from 'react-router-dom';

export default function Login() {
  return (
    <div className="flex"> 
      <div className="w-1/2 h-screen items-center justify-center flex">
        <div className="w-[350px] h-[538px] relative">
          <h1 className="text-3xl font-medium  mb-5">Welcome back!</h1>
          <p className="mb-14 ">Enter your Credentials to access your account</p>
          <p className="font-medium">Email</p>
          <input type="email" className="w-full border border-gray-400 px-2 py-1 placeholder:text-xs text-sm rounded-lg mb-5" placeholder="Enter your email" />
          <p className="font-medium">Password</p>
          <input type="password" className="w-full border border-gray-400 px-2 py-1 placeholder:text-xs text-sm rounded-lg mb-5" placeholder="Enter your password" />

          <a href="" className="text-[#0C2A92] text-xs">forgot password?</a>
          
          <button className="w-full bg-[#3A5B22] text-white p-1 rounded-xl mt-10 font-medium cursor-pointer">Login</button>

          <p className="absolute bottom-0 left-1/2 -translate-x-1/2 text-center font-medium text-sm w-full">Don't have an account? <Link to="/SignUp" className="text-[#0F3DDE]">Sign Up</Link></p>

        </div>
      </div>
      <div className="w-1/2 h-screen ">
        <img className="h-screen w-auto object-cover object-left rounded-l-4xl" src=".\src\assets\c46d84d5deb30ef828b49462ec3e3daf7da40194.jpg" alt="" />
      </div>
    </div>
  )
}