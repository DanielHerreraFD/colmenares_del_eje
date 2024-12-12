function Colmena(){
   const lista_colmenas=[
      {
         "numero_colmena" : 6547,
         "nombre_finca" : "Finca Los Alpes"
      },
      {
          "numero_colmena" : 6424,
         "nombre_finca" : "Finca Los Moras"
      },
      {
         "numero_colmena": 4454,
         "nombre_finca": "Finca la Graciela"
      },
      {
         "numero_colmena": 7636,
         "nombre_finca": "Finca de Dayana"
      }
   ]

   const options = [
    { value: 'Editar', label: 'Editar' },
    { value: 'Monitoreo', Monitoreo: '' },
    { value: 'Colmena', label: 'Colmena' }]
    
     return (
    <div>
      <h1>Lista de Colmenas </h1>
      <ul>
        {lista_colmenas.map((colmena, index) => (
          <li key={index}>
            <strong>Colmena #{colmena.numero_colmena}</strong> - {colmena.nombre_finca}
          </li>
        ))}
      </ul>
      <select>
      {options.map((option, index) => (
        <option key={index} value={option.value}>
          {option.label || 'Monitoreo'}
        </option>
      ))}
    </select>
    </div>
  );
   
};

export default Colmena;