function validarFormulario() {
  var nombre = document.getElementById("nombre").value;
  var telefono = document.getElementById("telefono").value;
  var correo = document.getElementById("correo").value;
  var descripcion = document.getElementById("descripcion").value;
  var mensajeError = document.getElementById("mensajeError");

  mensajeError.innerHTML = "";

  if (!/^[a-zA-Z\s]+$/.test(nombre)) {
    mensajeError.innerHTML +=
      "Por favor, ingrese un nombre válido (solo letras).<br>";
  }

  if (!/^\+?[0-9]{6,15}$/.test(telefono)) {
    mensajeError.innerHTML +=
      "Por favor, ingrese un número de teléfono válido (solo números).<br>";
  }

  if (!/\S+@\S+\.\S+/.test(correo)) {
    mensajeError.innerHTML +=
      "Por favor, ingrese un correo electrónico válido.<br>";
  }

  if (descripcion.trim() === "") {
    mensajeError.innerHTML += "Por favor, ingrese una descripción.<br>";
  }

  return mensajeError.innerHTML === "";
}

document
  .getElementById("contactForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    if (validarFormulario()) {
      this.submit();
    }
  });
