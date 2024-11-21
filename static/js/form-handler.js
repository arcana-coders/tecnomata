document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("formSend"); // Asegúrate de usar el selector correcto para tu formulario

    if (form) {
        form.addEventListener("submit", async (event) => {
            event.preventDefault(); // Evita el comportamiento predeterminado de envío

            const formData = new FormData(form);

            try {
                const response = await fetch("/send_form", {
                    method: "POST",
                    body: formData,
                });

                if (response.ok) {
                    // Si la respuesta es exitosa, redirige o muestra un mensaje
                    window.location.href = "/gracias"; // Ruta de redirección en el backend
                } else {
                    // Manejar errores del servidor
                    const errorData = await response.json();
                    alert(errorData.error || "Ocurrió un error al enviar el formulario.");
                }
            } catch (error) {
                // Manejo de errores de red o del cliente
                alert("Error de conexión. Inténtalo de nuevo.");
                console.error("Error al enviar el formulario:", error);
            }
        });
    } else {
        console.warn("Formulario no encontrado. Revisa el selector del formulario.");
    }
});
