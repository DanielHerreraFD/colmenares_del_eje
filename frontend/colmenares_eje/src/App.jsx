import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './assets/components/Login/Login';
import UserRegister from './assets/components/UserRegister/UserRegister';
import Dashboard from './assets/components/Dashboard/Dashboard';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Ruta para el Login */}
        <Route path="/" element={<Login />} />
        {/* Ruta para el Registro */}
        <Route path="/UserRegister" element={<UserRegister />} />
        {/* Ruta para el Dashboard */}
        <Route path="/Dashboard" element={<Dashboard />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
