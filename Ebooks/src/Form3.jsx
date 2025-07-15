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

            <div className=' w-96 h-[450px] ml-0 flex-col flex'>
              <div className='flex flex-row items-center justify-center space-x-4 mb-6 left-0'>
                <div className='h-1 w-32 bg-blue-500 rounded-full'></div>
                <div className='h-1 w-32 bg-blue-500 rounded-full'></div>
                <div className='h-1 w-32 bg-blue-500 rounded-full'></div>
              </div>
              <p>Step 3/3</p>
              <p className='mb-6'>How much time do you want to spend?</p>
              <button className='w-56 h-8 border flex items-center justify-center rounded-2xl hover:bg-[#546F9D] hover:text-white cursor-pointer mb-6 border-[#546F9D]'>Short reads(&lt;15 mins)</button>
              <button className='w-56 h-8 border flex items-center justify-center rounded-2xl hover:bg-[#546F9D] hover:text-white cursor-pointer mb-6 border-[#546F9D]'>Medium(~ 30 mins)</button>
              <button className='w-56 h-8 border flex items-center justify-center rounded-2xl hover:bg-[#546F9D] hover:text-white cursor-pointer mb-6 border-[#546F9D]'>Long(1hr+)</button>
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