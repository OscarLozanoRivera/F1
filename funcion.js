async function cargar(id){

{/* <div class="progress mb-2">
                    <div class="progress-bar bg-primary" role="progressbar" style="width: 50%;"
                       aria-valuemin="0" aria-valuemax="100">Description</div>
</div> */}
  
  const jsondata = null
  fetch("./auto.json")
  .then(response => {
    return response.json();
  })
  .then(jsondata => {
    const carrera = jsondata.carreras[id-1]
    const posiciones = carrera.posiciones
    var pos = 1
    var pil 
    posiciones.forEach(posicion => {
      var porcentaje
      const barras = document.querySelector(".barras");
      const divProgress = document.createElement("div");
      const divBar = document.createElement("div");
      divBar.classList.add("progress-bar","bg-primary") 
      divBar.ariaValueMin = "0"
      divBar.ariaValueMax = "100"
      divProgress.classList.add("progress", "mb-2") 
      console.log(Object.keys(posicion))                      //Posicion
      console.log(posicion[Object.keys(posicion)[0]][0])      //Piloto
      console.log(posicion[Object.keys(posicion)[0]][1])      //Puntos
      porcentaje = posicion[Object.keys(posicion)[0]][1]/25 *100
      divBar.style = "width: "+ porcentaje +"%;"
      divProgress.appendChild(divBar)
      barras.appendChild(divProgress)
      //pos.push()
    });

    }
    
    );


}
