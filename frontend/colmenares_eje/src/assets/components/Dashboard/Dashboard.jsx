import Colmena from "../Colmena/Colmena";
import "./Dashboard.css"
function Dashboard() {
  function Header() {
    return (
      <header className="header">
        <img src="#" alt="loguito" className="logo" />
        <ul>
          <li>Crear Colmena</li>
          <li>Visualizar Colmena</li>
          <li>Escanear QR</li>
        </ul>
      </header>
    );
  }

  function MainDashboard() {
    return (
      <main className="main_dashboard">
        {/* Aquí inyectamos el componente Colmena */}
        <Colmena />
      </main>
    );
  }

  function Aside() {
    return (
      <aside>
        <h2>Apicultor</h2>
        <img src="#" alt="imagen_perfil" className="imagen_perfil" />
        <h3>Giovanny Molina</h3>
        <select name="relacion" id="colmenas_relacionadas">
          <option value="">Colmenas Relacionadas</option>
          <ul>
            <li></li>
          </ul>
        </select>
      </aside>
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

  return (
    <>
      <Header />
      <MainDashboard />
      <Aside />
      <Footer />
    </>
  );
}

export default Dashboard;
