import './App.css'
import SignUp from './SignUp.jsx'
import Login from './Login.jsx'
import { Routes, Route } from 'react-router-dom'

function App() {

  return (
    <>
      <Routes>
      <Route path="/Login" element={<Login />} />
      <Route path="/SignUp" element={<SignUp />} />
    </Routes>
    </>
  )
}

export default App
