const btnsAgregarAlCarrito = document.querySelectorAll(".btnAgregarAlCarrito");
btnsAgregarAlCarrito.forEach(function (btn) {
  btn.addEventListener("click", function () {
    const producto = {
      id: this.getAttribute("data-producto-id"),
      nombre: this.getAttribute("data-producto-nombre"),
      precio: this.getAttribute("data-producto-precio"),
    };

    const carrito = JSON.parse(localStorage.getItem("carrito")) || [];

    carrito.push(producto);

    localStorage.setItem("carrito", JSON.stringify(carrito));

    document.getElementById("btnAgregarAlCarrito").style.display = "none";
    document.getElementById("btnEliminarDelCarrito").style.display =
      "inline-block";
    alert("Producto agregado al carrito");
  });
});
