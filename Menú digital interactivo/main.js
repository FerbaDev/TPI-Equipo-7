// VARIABLES

let cantidadProductos = 0;
let total = 0;
let detalle = "";

// ELEMENTOS HTML

const contadorNavbar = document.getElementById("cart-count");
//cart-count es el id del span que muestra la cantidad de productos en el carrito en la navbar. Se obtiene con getElementById para poder actualizarlo dinámicamente cada vez que se agrega un producto al carrito.



// FUNCION

const agregarProducto = (nombre, precio) => {

    cantidadProductos++; //es lo mismo que cantidadProductos = cantidadProductos + 1, se incrementa la cantidad de productos cada vez que se llama a esta función.

    // suma total
    total += precio;

    // se guarda el detalle del producto agregado, se concatena el nombre del producto y su precio al detalle, separado por un guion y un salto de línea para que cada producto aparezca en una nueva línea en el detalle.
    detalle += nombre + " - $" + precio + "\n";

    // actualizar navbar
    contadorNavbar.innerText = cantidadProductos;

    // se muestra en consola el detalle
    console.log(detalle);
    console.log("TOTAL: $" + total);
}