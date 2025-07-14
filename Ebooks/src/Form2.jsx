import { Link } from 'react-router-dom';
import image from './assets/form.jpeg';
import { useNavigate } from 'react-router-dom';

export default function Form1() {
     const navigate = useNavigate();
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
                <div className='h-1 w-32 bg-blue-500 rounded-full'></div>
                <div className='h-1 w-32 bg-gray-200 rounded-full'></div>
              </div>
              <p>Step 2/3</p>
              <p className='mb-6'>What's your reading goal?</p>
              <button className='w-56 h-8 border flex items-center justify-center rounded-2xl hover:bg-[#546F9D] hover:text-white cursor-pointer mb-6'>Learn something</button>
              <button className='w-56 h-8 border flex items-center justify-center rounded-2xl hover:bg-[#546F9D] hover:text-white cursor-pointer mb-6'>Entertainment</button>
              <button className='w-56 h-8 border flex items-center justify-center rounded-2xl hover:bg-[#546F9D] hover:text-white cursor-pointer mb-6'>Productivity</button>
              <button className='w-56 h-8 border flex items-center justify-center rounded-2xl hover:bg-[#546F9D] hover:text-white cursor-pointer mb-6'>Relaxation</button>

            <div className='flex justify-between mt-6'>
                <button className='w-32 h-8 border flex items-center justify-center rounded-2xl hover:bg-[#546F9D] hover:text-white cursor-pointer mb-6'
                onClick={() => navigate('/Form1')}>Previous step</button>
                <button className='w-32 h-8 border flex items-center justify-center rounded-2xl bg-[#546F9D] hover:bg-[#546F9D] hover:text-white cursor-pointer mb-6'
                onClick={() => navigate('/Form3')}>Next step</button>
                
            </div>
              </div>
          </div>
        </div>
        </>
                     
    )
}