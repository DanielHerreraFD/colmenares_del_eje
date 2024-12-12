import "./Login.css";
import { Link, useNavigate } from "react-router-dom";
import React, { useState } from 'react';

const LoginForm = () => {
    const [identificacion, setIdentificacion] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const navigate = useNavigate();  // Para redirigir a otras páginas

    const handleLogin = (e) => {
        e.preventDefault();

        const storedUser = JSON.parse(localStorage.getItem("userData"));

        if (storedUser) {
            if (storedUser.identificacion === identificacion && storedUser.password === password) {
                setError(""); // Limpiamos cualquier mensaje de error
                alert("Inicio de sesión exitoso");
                navigate("/Dashboard"); // Redirigir al Dashboard
            } else {
                setError("Identificación o contraseña incorrectos");
            }
        } else {
            setError("No se encuentran datos de registro");
        }
    };

    return (
        <>
            <header className="header">
                <img src="#" alt="loguito" className="logo" />
                <h1 className="header-title">Colmenares del Eje</h1>
            </header>

            <main className="main">
                <div className="login-container">
                    <form className="form-login" onSubmit={handleLogin}>
                        <label htmlFor="usuario" className="label">Usuario</label>
                        <input 
                            type="text" 
                            id="usuario" 
                            name="usuario"
                            placeholder="Ingrese su usuario"
                            value={identificacion}
                            onChange={(e) => setIdentificacion(e.target.value)} 
                            className="input" 
                        />

                        <label htmlFor="password" className="label">Contraseña</label>
                        <input 
                            type="password" 
                            id="password" 
                            name="password" 
                            placeholder="Ingrese su contraseña" 
                            value={password}
                            onChange={(e) => setPassword(e.target.value)} 
                            className="input" 
                        />
                        
                        {error && <p className="error-message">{error}</p>}

                        <div className="button-container">
                            <button type="button" className="button">
                                <Link to="/UserRegister">Registrarse</Link>
                            </button>
                            <button type="submit" className="button">
                                Iniciar Sesion
                            </button>
                        </div>
                    </form>
                </div>
            </main>

            <footer className="footer">
                <h2>Colmenares del Eje</h2>
                <p>© Todos los derechos reservados</p>
            </footer>
        </>
    );
};

export default LoginForm;
