import React from 'react'
import './estilos.css';

const Paises = ({ paises }) => {
  return (
    <div>
      <center><h1>Lista de paises</h1></center>
      {paises.map((pais) => (
        <div class="contenedor">
          <div class="cuerpo-contenedor">
            <center><img src="./bandera2.svg" alt="img"></img></center>
            <center><h5 class="card-title">{pais.name}</h5></center>
            <h6 class="card-subtitle mb-2 text-muted">Región: {pais.region}</h6>
            <p class="card-text">Subregión: {pais.subregion}</p>
          </div>
        </div>
      ))}
    </div>
  )
};

export default Paises