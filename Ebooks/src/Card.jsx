import { useState } from "react";

export default function Card() { 
      const [toggled, setToggled] = useState(true);

    return (
        <div className='flex flex-col items-center justify-center'>
                        <div className='bg-gray-500 h-60 w-36 mb-4'>
                            <img src="" alt="" />
                            <button></button>
                        </div>
                        <button className="cursor-pointer transition duration-500 ease-in-out transform scale-100 opacity-100 relative w-6 h-6"
                        onClick={() => setToggled(!toggled)}>
                            
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" 
                            className={`absolute inset-0 transition-all duration-500 ease-in-out ${
                            toggled ? 'opacity-100 scale-100' : 'opacity-0 scale-75'
                                        }`}>
                        <path strokeLinecap="round" strokeLinejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                        </svg>
                            
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="blue" 
                            className={`absolute inset-0 transition-all duration-500 ease-in-out ${
                                        toggled ? 'opacity-0 scale-75' : 'opacity-100 scale-100'
                                        }`}>
                            <path fillRule="evenodd" d="M2.25 12c0-5.385 4.365-9.75 9.75-9.75s9.75 4.365 9.75 9.75-4.365 9.75-9.75 9.75S2.25 17.385 2.25 12Zm13.36-1.814a.75.75 0 1 0-1.22-.872l-3.236 4.53L9.53 12.22a.75.75 0 0 0-1.06 1.06l2.25 2.25a.75.75 0 0 0 1.14-.094l3.75-5.25Z" clipRule="evenodd" />
                            </svg>

        </button> 
                    </div>
    );
}   