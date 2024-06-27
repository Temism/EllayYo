var carrito = JSON.parse(localStorage.getItem("carrito")) || [];
var cartContainer = document.getElementById("cart-container");
var carritoVacio = document.getElementById("carrito-vacio");
var btnComprar = document.getElementById("comprar");
var btnReiniciar = document.getElementById("reiniciar");
var totalUnidadesElement = document.getElementById("cantidad");
var totalPrecioElement = document.getElementById("precio");

function mostrarCarrito() {
  if (carrito.length > 0) {
    actualizarTablaCarrito();

    carritoVacio.style.display = "none";

    btnComprar.disabled = false;
  } else {
    carritoVacio.style.display = "block";

    btnComprar.disabled = true;
  }

  actualizarTotales();
}

function actualizarTablaCarrito() {
  var listaOrdenada = document.createElement("ol");

  carrito.forEach(function (producto) {
    var fila = document.createElement("li");

    fila.innerHTML =
      `<img src="${producto.imagen}" alt="${producto.nombre}" style="max-width: 50px;">` +
      producto.nombre +
      " - Precio: $" +
      producto.precio +
      '<button class="btnEliminarDelCarrito" style="margin-left: 10px;"> Eliminar </button>';

    listaOrdenada.appendChild(fila);

    var btnEliminar = fila.querySelector(".btnEliminarDelCarrito");
    btnEliminar.addEventListener("click", function () {
      var index = Array.from(listaOrdenada.children).indexOf(fila);
      eliminarProductoDelCarrito(index);
    });
  });

  cartContainer.innerHTML = "";
  cartContainer.appendChild(listaOrdenada);
}

function eliminarProductoDelCarrito(index) {
  carrito.splice(index, 1);

  localStorage.setItem("carrito", JSON.stringify(carrito));

  var filaAEliminar = cartContainer.querySelector(
    ":nth-child(" + (index + 1) + ")"
  );
  if (filaAEliminar) {
    filaAEliminar.remove();
  }

  mostrarCarrito();
}

function actualizarTotales() {
  var totalUnidades = carrito.length;

  totalUnidadesElement.textContent = totalUnidades;

  var precioTotal = carrito.reduce(function (total, producto) {
    return total + parseFloat(producto.precio);
  }, 0);

  var precioTotalFormateado = precioTotal.toLocaleString("es-CL", {
    style: "currency",
    currency: "CLP",
  });

  totalPrecioElement.textContent = precioTotalFormateado;
}

function vaciarCarrito() {
  localStorage.removeItem("carrito");

  cartContainer.innerHTML = "";

  carritoVacio.style.display = "block";

  btnComprar.disabled = true;

  totalUnidadesElement.textContent = "0";
  totalPrecioElement.textContent = "0";
}

function pagar() {
  alert("Pago realizado correctamente");

  vaciarCarrito();
}

btnReiniciar.addEventListener("click", vaciarCarrito);
btnComprar.addEventListener("click", pagar);

mostrarCarrito();
