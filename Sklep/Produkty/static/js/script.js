'use strict'

if(admin1 !== 'None'){
    if(admin1 !== JSON.parse(localStorage.getItem("koszyk"))?.admin){
        localStorage.removeItem("koszyk");
    
    }
}
let koszyk = localStorage.getItem("koszyk");
koszyk = JSON.parse(koszyk);
let btnAdd = document.getElementById("btnAdd");

if(btnAdd){
    let id = btnAdd.getAttribute("idProd");
    let nazwa = btnAdd.getAttribute("nazwaProd");
    if(koszyk){
        if(koszyk.lista.find(x => x.id === id)){    
            btnAdd.disabled = true;
            btnAdd.textContent = "Roślina dodana";
        }
    }
    btnAdd.addEventListener('click', ()=>{
        btnAdd.disabled =true;
        btnAdd.textContent = "Roślina dodana";
        if(koszyk){
           let produkt = {id: id, nazwa: nazwa};
           koszyk.lista.push(produkt);
           localStorage.setItem("koszyk", JSON.stringify(koszyk));
        }
        else{
            let lista = [{id: id, nazwa: nazwa}];
            let obj = {
                admin: admin1,
                lista: lista,
            }
            localStorage.setItem("koszyk", JSON.stringify(obj));
        }
        generowanie();
    });
}


function generowanie(){
    let koszyk2 = localStorage.getItem("koszyk");
    koszyk2 = JSON.parse(koszyk2);
    let unik = document.getElementById("listProd");
    if(unik){
        unik.innerHTML = "<li>Brak roślin</li>";
        if(koszyk2){
            unik.innerHTML="";
            for(let element of koszyk2.lista){
                unik.innerHTML += `<li><a class="dropdown-item" href="/produkt/${element.id}">${element.nazwa}</a></li>`
            
            }

        }
        else{
            unik.innerHTML = "<li>Brak roślin</li>";

        }
    }  
}

generowanie();