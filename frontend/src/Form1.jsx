import { Link } from 'react-router-dom';
import image from './assets/form.jpeg';
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';

export default function Form1() {
    const navigate = useNavigate();
  const [selected, setSelected] = useState({
    fiction: false,
    fantasy: false,
    selfHelp: false
  });

  const toggleGenre = (genre) => {
    setSelected((prev) => ({ ...prev, [genre]: !prev[genre] }));
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

            <div className=' w-96 h-96 ml-0 flex-col flex'>
              <div className='flex flex-row items-center justify-center space-x-4 mb-6 left-0'>
                <div className='h-1 w-32 bg-blue-500 rounded-full'></div>
                <div className='h-1 w-32 bg-gray-200 rounded-full'></div>
                <div className='h-1 w-32 bg-gray-200 rounded-full'></div>
              </div>
              <p>Step 1/3</p>
              <p className='mb-6'>What Genres do you enjoy?</p>
              <button
              onClick={() => toggleGenre('fiction')}
              className={`w-56 h-8 border flex items-center justify-center rounded-2xl cursor-pointer mb-6 border-[#546F9D] transition duration-300
                ${selected.fiction ? "bg-[#546F9D] text-white" : "hover:bg-[#546F9D] hover:text-white"}
              `}>
              Fiction
            </button>

            <button
              onClick={() => toggleGenre('fantasy')}
              className={`w-56 h-8 border flex items-center justify-center rounded-2xl cursor-pointer mb-6 border-[#546F9D] transition duration-300
                ${selected.fantasy ? "bg-[#546F9D] text-white" : "hover:bg-[#546F9D] hover:text-white"}
              `}>
              Fantasy
            </button>

            <button
              onClick={() => toggleGenre('selfHelp')}
              className={`w-56 h-8 border flex items-center justify-center rounded-2xl cursor-pointer mb-6 border-[#546F9D] transition duration-300
                ${selected.selfHelp ? "bg-[#546F9D] text-white" : "hover:bg-[#546F9D] hover:text-white"}
              `}>
              Self-help
            </button>


              <button className='w-32 h-8 border flex items-center justify-center rounded-2xl bg-[#546F9D] hover:bg-[#546F9D] text-white cursor-pointer mt-6 border-[#546F9D]'
              onClick={() => navigate('/Form2')}>Next step</button>
            </div>
          </div>
        </div>
        </>
                     
    )
}