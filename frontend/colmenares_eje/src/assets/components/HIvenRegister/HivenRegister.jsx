import React, { useState } from 'react';
import "./HivenRegister.css";

function Header() {
    return (
        <header className="header">
            <img src="#" alt="logo" className="logo" />
            <h1 className="header-title">Colmenares del Eje</h1>
        </header>
    );
}

function Main() {
    const [formData, setFormData] = useState({
        cantidadCriasAbierta: '',
        cantidadCriasOperculada: '',
        presenciaReina: '',
        colorReina: '',
        origenReina: '',
        reportesGenerales: '',
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(formData);
        // Aquí puedes agregar la lógica para guardar los datos o enviarlos al backend
    };

    return (
        <main className="main-hiven-register">
            <h2>Crear Colmena</h2>
            <form className="hiven-form" onSubmit={handleSubmit}>
                <label htmlFor="cantidad-crias-abierta">Cantidad de cuadros de cria abierta</label>
                <input
                    type="text"
                    id="cantidad-crias-abierta"
                    name="cantidadCriasAbierta"
                    placeholder="Ingrese la cantidad de crias abierta"
                    required
                    value={formData.cantidadCriasAbierta}
                    onChange={handleChange}
                />
                <label htmlFor="cantidad-crias-operculada">Cantidad de cuadros de cria operculada</label>
                <input
                    type="text"
                    id="cantidad-crias-operculada"
                    name="cantidadCriasOperculada"
                    placeholder="Ingrese la cantidad de cria operculada"
                    required
                    value={formData.cantidadCriasOperculada}
                    onChange={handleChange}
                />
                <label htmlFor="presencia-reina">Presencia de la reina</label>
                <select
                    id="presencia-reina"
                    name="presenciaReina"
                    required
                    value={formData.presenciaReina}
                    onChange={handleChange}
                >
                    <option value="">Seleccione presencia de la reina</option>
                    <option value="1">Si</option>
                    <option value="2">No</option>
                </select>
                <label htmlFor="color-reina">Color de la reina</label>
                <select
                    id="color-reina"
                    name="colorReina"
                    required
                    value={formData.colorReina}
                    onChange={handleChange}
                >
                    <option value="Negra">Negra</option>
                    <option value="Amarilla">Amarilla</option>
                </select>
                <label htmlFor="origen-reina">Origen de la reina</label>
                <select
                    id="origen-reina"
                    name="origenReina"
                    required
                    value={formData.origenReina}
                    onChange={handleChange}
                >
                    <option value="1">Europea</option>
                    <option value="2">Angelita</option>
                    <option value="3">Africanita</option>
                </select>
                <label htmlFor="reportes-generales">Reportes generales</label>
                <input
                    type="text"
                    id="reportes-generales"
                    name="reportesGenerales"
                    placeholder="Ingrese los reportes generales"
                    required
                    value={formData.reportesGenerales}
                    onChange={handleChange}
                />
                <button type="submit">Guardar</button>
            </form>
        </main>
    );
}

function Footer() {
    return (
        <footer className="footer">
            <h2>Copyright</h2>
            <h2>Todos los derechos reservados</h2>
        </footer>
    );
}

function HivenRegister() {
    return (
        <div>
            <Header />
            <Main />
            <Footer />
        </div>
    );
}

export default HivenRegister;
