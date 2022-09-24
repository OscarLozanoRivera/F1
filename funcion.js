async function cargar(id){
  const jsondata = null
  fetch("./auto.json")
  .then(response => {
    return response.json();
  })
  .then(jsondata => {
    const pilotos = jsondata.pilotos

      if (id==0){   //Reiniciar
                    //Borrar e imprimir
        Object.values(pilotos).forEach(piloto => {
          
          if (parseInt(piloto['numCarreras']) > 0 ){
            const divPiloto = document.getElementById(piloto['nom'])
            if (divPiloto==null){
              const barras = document.querySelector(".barras");
              const divProgress = document.createElement("div");
              divProgress.id= piloto['nom']
              const divBar = document.createElement("div");
              const divImg = document.createElement("div");
              divImg.classList.add("progress-bar","bg-warning") 
              const imagen = document.createElement("img");
              imagen.src= 'Imagenes/f1-car-vectors.jpg'
              divImg.style = "width: 5%;margin-left: 2rem !important;"
              divBar.classList.add("progress-bar","bg-primary") 
              divBar.ariaValueMin = "0"
              divProgress.classList.add("progress", "mb-2","bg-warning") 
              divBar.textContent = piloto['nom']
              divBar.style = "width: 0%;"
              divProgress.appendChild(divBar)
              divImg.appendChild(imagen)
              divProgress.appendChild(divImg)
              barras.appendChild(divProgress)
            }
            else{
              divPiloto.childNodes[0].style = "width : 0%;"
              divPiloto.childNodes[0].ariaValueMax = 100
              divPiloto.childNodes[0].ariaValueNow = 0
            }
          }
          
        });
    
      }
      else{
        const carrera = jsondata.carreras[id-1]
        const posiciones = carrera.posiciones
        maxPuntos= carrera.lider[1]
        maxPuntosInt = parseInt(carrera.lider[1])
        const barras = document.querySelector(".barras");
        var porcentaje = 0
        const pilotosOrden = []
        posiciones.forEach(posicion => {
          //console.log(posicion[Object.keys(posicion)[0]][0])
          const divPiloto = document.getElementById(posicion[Object.keys(posicion)[0]][0])//Piloto
          const divProgress = divPiloto.childNodes
          //console.log(divProgress)
          porcentaje = posicion[Object.keys(posicion)[0]][1]/maxPuntosInt *90     //Puntos/25*100
          divProgress[0].setAttribute("style","width: "+ porcentaje +"%;")
          divProgress[0].ariaValueMax = maxPuntos
          let index = 0 
          for ( index = 0; index < pilotosOrden.length; index++) {
            if (parseInt(posicion[Object.keys(posicion)[0]][1]) > parseInt(pilotosOrden[index][1]) ){
              break
            }
          }
          pilotosOrden.splice(index,0,posicion[Object.keys(posicion)[0]])
        });
        const divs = document.getElementsByClassName('progress')
        for (let index = 0; index < pilotosOrden.length -1; index++) {
          const arriba = $('#'+pilotosOrden[index][0])
          let abajo = pilotosOrden[index][0]
          if (index!=0){
            abajo = $('#'+pilotosOrden[index-1][0])
          }
          console.log( arriba[0] , divs[index])
          arriba.animate({
            
            top : -arriba[0].offsetTop + divs[index].offsetTop
          },1000,function(){
            arriba[0].setAttribute('style','top:0;')
            if (index!=0){
              $('#'+pilotosOrden[index][0]).insertAfter('#'+pilotosOrden[index-1][0]);
            }
            else{
              $('#'+pilotosOrden[index][0]).insertBefore('#'+pilotosOrden[index+1][0]);
            }
            
          })          
        }
      }
    }
  )
  
;}





//$('#div1').insertAfter('#div3');      //Mover Divs