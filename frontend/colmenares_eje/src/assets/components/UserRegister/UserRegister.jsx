import React, { useState } from 'react';
import './UserRegister.css';
import { Navigate } from 'react-router-dom'; // Asegúrate de que Navigate esté importado

function UserRegister() {
  const [formData, setFormData] = useState({
    nombre: '',
    identificacion: '',
    correo: '',
    telefono: '',
    fecha_nacimiento: '',
    contacto_emergencia: '',
    password: '',
    confirmPassword: '',
  });
  const [redirectToLogin, setRedirectToLogin] = useState(false);

  const handleInputChange = (e) => {
    const { id, value } = e.target;
    setFormData({ ...formData, [id]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Validación para asegurarse de que todos los campos estén llenos
    for (let key in formData) {
      if (formData[key] === '') {
        alert(`El campo ${key} es obligatorio.`);
        return;
      }
    }

    if (formData.password !== formData.confirmPassword) {
      alert('Las contraseñas no coinciden');
      return;
    }

    // Guardamos los datos en el localStorage
    localStorage.setItem('userData', JSON.stringify(formData));

    // Actualizamos el estado para redirigir
    setRedirectToLogin(true);
  };

  // Redirigir a la página de inicio de sesión si el estado es true
  if (redirectToLogin) {
    return <Navigate to="/" />;
  }

  return (
    <>
      <header className="header">
        <img src="#" alt="logo" className="logo" />
        <h1 className="header-title">Colmenares del Eje</h1>
      </header>

      <main className="main-register">
        <div className="register-container">
          <h2 className="form-title">Regístrate</h2>
          <form className="form-register" onSubmit={handleSubmit}>
            <label htmlFor="nombre" className="label">Nombre</label>
            <input
              type="text"
              id="nombre"
              placeholder="Ingrese su nombre completo"
              className="input"
              value={formData.nombre}
              onChange={handleInputChange}
            />

            <label htmlFor="identificacion" className="label">Identificación</label>
            <input
              type="text"
              id="identificacion"
              placeholder="Ingrese su identificación"
              className="input"
              value={formData.identificacion}
              onChange={handleInputChange}
              required
            />

            <label htmlFor="correo" className="label">Correo</label>
            <input
              type="email"
              id="correo"
              placeholder="Ingrese su correo"
              className="input"
              value={formData.correo}
              onChange={handleInputChange}
              required
            />

            <label htmlFor="telefono" className="label">Teléfono</label>
            <input
              type="text"
              id="telefono"
              placeholder="Ingrese su teléfono"
              className="input"
              value={formData.telefono}
              onChange={handleInputChange}
              required
            />

            <label htmlFor="fecha_nacimiento" className="label">Fecha de nacimiento</label>
            <input
              type="date"
              id="fecha_nacimiento"
              className="input"
              value={formData.fecha_nacimiento}
              onChange={handleInputChange}
              required
            />

            <label htmlFor="contacto_emergencia" className="label">Contacto de emergencia</label>
            <input
              type="text"
              id="contacto_emergencia"
              placeholder="Ingrese su contacto de emergencia"
              className="input"
              value={formData.contacto_emergencia}
              onChange={handleInputChange}
              required
            />

            <label htmlFor="password" className="label">Contraseña</label>
            <input
              type="password"
              id="password"
              placeholder="Ingrese su contraseña"
              className="input"
              value={formData.password}
              onChange={handleInputChange}
              required
              minLength={8}
            />

            <label htmlFor="confirmPassword" className="label">Confirmar Contraseña</label>
            <input
              type="password"
              id="confirmPassword"
              placeholder="Confirme su contraseña"
              className="input"
              value={formData.confirmPassword}
              onChange={handleInputChange}
              required
            />

            <button type="submit" className="button">
              Registrarse
            </button>
          </form>
        </div>
      </main>

      <footer className="footer">
        <h2>Colmenares del Eje</h2>
        <p>© Todos los derechos reservados</p>
      </footer>
    </>
  );
}

export default UserRegister;
