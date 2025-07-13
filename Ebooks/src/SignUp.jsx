import { Link } from 'react-router-dom';

export default function SignUp() {
  return (
    <div className="flex"> 
      <div className="w-1/2 h-screen items-center justify-center flex">
        <div className="w-[350px] h-[538px] relative">
          <h1 className="text-3xl font-medium  mb-14">Get Started Now</h1>
          <p className="font-medium">Name</p>
          <input type="text" className="w-full border border-gray-400 px-2 py-1 placeholder:text-xs text-sm rounded-lg mb-5" placeholder="Enter your name" />
          <p className="font-medium">Email</p>
          <input type="email" className="w-full border border-gray-400 px-2 py-1 placeholder:text-xs text-sm rounded-lg mb-5" placeholder="Enter your email" />
          <p className="font-medium">Password</p>
          <input type="password" className="w-full border border-gray-400 px-2 py-1 placeholder:text-xs text-sm rounded-lg mb-5" placeholder="Enter your password" />

          <div className="flex "><input type="checkbox" className="cursor-pointer"/> <p className="ml-2 text-sm">I agree to the <a href="" className="underline">terms & policy</a></p></div>
          
          <button className="w-full bg-[#3A5B22] text-white p-1 rounded-xl mt-10 font-medium cursor-pointer">Sign Up</button>

          <p className="absolute bottom-0 left-1/2 -translate-x-1/2 text-center font-medium text-sm w-full">have an account? <Link to="/LogIn" className="text-[#0F3DDE]">Sign In</Link></p>

        </div>
      </div>
      <div className="w-1/2 h-screen ">
        <img className="h-screen w-auto object-cover object-left rounded-l-4xl" src=".\src\assets\c46d84d5deb30ef828b49462ec3e3daf7da40194.jpg" alt="" />
      </div>
    </div>
  )
}