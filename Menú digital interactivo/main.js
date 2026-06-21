// VARIABLES

let cantidadProductos =
    Number(localStorage.getItem("cantidadProductos")) || 0;
let total =
    Number(localStorage.getItem("total")) || 0;
let detalle =
    localStorage.getItem("detalle") || "";

// ELEMENTOS HTML

const contadorNavbar =
    document.getElementById("cart-count");

const detalleCarrito =
    document.getElementById("detalle-carrito");

const totalCarrito =
    document.getElementById("total-carrito");

if (contadorNavbar) {
    contadorNavbar.innerText = cantidadProductos;
}

if (detalleCarrito) {
    detalleCarrito.innerText = detalle;
}

if (totalCarrito) {
    totalCarrito.innerText = "$" + total;
}

// FUNCION AGREGAR PRODUCTO

function agregarProducto(nombre, precio) { 

    cantidadProductos++; //es lo mismo que cantidadProductos = cantidadProductos + 1, se incrementa la cantidad de productos cada vez que se llama a esta función.

    // suma total
    total += precio;

    // se guarda el detalle del producto agregado, se concatena el nombre del producto y su precio al detalle, separado por un guion y un salto de línea para que cada producto aparezca en una nueva línea en el detalle.
    detalle += nombre + " - $" + precio + "\n";

    //guardo en localStorage la cantidad de productos, el total y el detalle para que se mantengan al navegar entre páginas o al recargar la página. Se utiliza localStorage.setItem para guardar cada valor con una clave específica.
    localStorage.setItem(
        "cantidadProductos",
        cantidadProductos
    );

    localStorage.setItem(
        "total",
        total
    );

    localStorage.setItem(
        "detalle",
        detalle
    );

    // actualizar navbar
    contadorNavbar.innerText = cantidadProductos;

    // se muestra en consola el detalle
    console.log(detalle);
    console.log("TOTAL: $" + total);
}

function vaciarCarrito() {

    cantidadProductos = 0;
    total = 0;
    detalle = "";

    localStorage.removeItem("cantidadProductos");
    localStorage.removeItem("total");
    localStorage.removeItem("detalle");

    contadorNavbar.innerText = 0;

    if (detalleCarrito) {
        detalleCarrito.innerText = "";
    }

    if (totalCarrito) {
        totalCarrito.innerText = "$0";
    }

}