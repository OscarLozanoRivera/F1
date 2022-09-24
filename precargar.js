const jsondata = null
  fetch("./auto.json")
  .then(response => {
    return response.json();
  })
  .then(jsondata => {
    const carrera = jsondata.carreras
    const botonesDiv = document.querySelector(".botones");
    
    for (let index = 0; index < carrera.length; index++) {
        const boton = document.createElement("button");
        boton.type = "button" 
        boton.classList.add("btn","btn-info","btn-sm","ml-1")
        boton.id = (parseInt(index)+1)
        boton.setAttribute("onclick","cargar(this.id)") 
        boton.textContent = (parseInt(index)+1).toString()
        botonesDiv.appendChild(boton)    
    }

    const boton = document.createElement("button");
    boton.type = "button" 
    boton.classList.add("btn","btn-danger","btn-sm","ml-1")
    boton.setAttribute("onclick","cargar(0)") 
    boton.textContent = "Reiniciar"
    botonesDiv.appendChild(boton) 

    cargar(0)
    





    });
