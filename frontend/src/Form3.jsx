import { Link } from 'react-router-dom';
import image from './assets/form.jpeg';
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';

export default function Form1() {
    const navigate = useNavigate();
    const [selected, setSelected] = useState({
            short: false,
            medium: false,
            long: false,
          });
    
          const toggleTime = (time) => {
        setSelected((prev) => ({ ...prev, [time]: !prev[time] }));
      };
    
    return (
      <>
      <div className="relative h-screen w-screen overflow-hidden">
        <div
          className="absolute inset-0 bg-no-repeat bg-center opacity-60 z-0"
          style={{ backgroundImage: `url(${image})` }}
        >
        </div>

          <div className='w-full h-full flex items-center justify-center flex-col z-10 relative'>
            <h1 className='text-5xl font-medium mb-10'>Find your next favorite read</h1>

            <div className=' w-96 h-[450px] ml-0 flex-col flex'>
              <div className='flex flex-row items-center justify-center space-x-4 mb-6 left-0'>
                <div className='h-1 w-32 bg-blue-500 rounded-full'></div>
                <div className='h-1 w-32 bg-blue-500 rounded-full'></div>
                <div className='h-1 w-32 bg-blue-500 rounded-full'></div>
              </div>
              <p>Step 3/3</p>
              <p className='mb-6'>How much time do you want to spend?</p>
               <button
              onClick={() => toggleTime('short')}
              className={`w-56 h-8 border flex items-center justify-center rounded-2xl cursor-pointer mb-6 border-[#546F9D] transition duration-300
                ${selected.short ? "bg-[#546F9D] text-white" : "hover:bg-[#546F9D] hover:text-white"}
              `}>
              Short reads(&lt;15 mins)
            </button>

             <button
              onClick={() => toggleTime('medium')}
              className={`w-56 h-8 border flex items-center justify-center rounded-2xl cursor-pointer mb-6 border-[#546F9D] transition duration-300
                ${selected.medium ? "bg-[#546F9D] text-white" : "hover:bg-[#546F9D] hover:text-white"}
              `}>
              Medium(~ 30 mins)
            </button>

             <button
              onClick={() => toggleTime('long')}
              className={`w-56 h-8 border flex items-center justify-center rounded-2xl cursor-pointer mb-6 border-[#546F9D] transition duration-300
                ${selected.long ? "bg-[#546F9D] text-white" : "hover:bg-[#546F9D] hover:text-white"}
              `}>
              Long(1hr+)
            </button>

              <button className='w-32 h-8 border flex items-center justify-center rounded-2xl  hover:bg-[#546F9D] hover:text-white cursor-pointer mt-6 border-[#546F9D]'
              onClick={() => navigate('/Form2')}>Previous step</button>
              <button className='w-full h-10 border flex items-center justify-center rounded-full bg-[#546F9D] text-white cursor-pointer mt-20'
              onClick={() => navigate('/Home')}>See suggestions</button>
            </div>
          </div>
        </div>
        </>
                     
    )
}