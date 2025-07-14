import './App.css'
import SignUp from './SignUp.jsx'
import Login from './Login.jsx'
import { Routes, Route } from 'react-router-dom'
import Form1 from './Form1.jsx'
import Form2 from './Form2.jsx'
import Form3 from './Form3.jsx'
import Home from './Home.jsx'

function App() {

  return (
    <>
      <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/Login" element={<Login />} />
      <Route path="/SignUp" element={<SignUp />} />
      <Route path="/Form1" element={<Form1 />} />
      <Route path="/Form2" element={<Form2 />} />
      <Route path="/Form3" element={<Form3 />} />
      <Route path="/Home" element={<Home />} />

    </Routes>
    </>
  )
}

export default App
