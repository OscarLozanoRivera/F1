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
        boton.classList.add("btn","btn-info","btn-xxl","ml-1")
        boton.id = (parseInt(index)+1)
        boton.setAttribute("onclick","cargar(this.id)") 
        boton.textContent = (parseInt(index)+1).toString()
        boton.addEventListener('click',toogle,false)
        botonesDiv.appendChild(boton)    
    }

    const boton = document.createElement("button");
    boton.type = "button" 
    boton.classList.add("btn","btn-danger","btn-xxl","ml-1")
    boton.setAttribute("onclick","cargar(0)") 
    boton.textContent = "Reiniciar"
    botonesDiv.appendChild(boton) 

    cargar(0)
    





    });


function toogle(){
  //console.log(this.id)
 const botones = document.getElementsByClassName('btn')
 Object.values(botones).forEach(boton => {
    if(boton.classList.contains('bg-success')){
      boton.classList.remove('bg-success')
      boton.classList.add('bg-info')
    }
 });
 this.classList.add('bg-success')
 this.classList.remove('bg-info')
}