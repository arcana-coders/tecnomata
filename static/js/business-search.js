document.addEventListener("DOMContentLoaded", () => {
    const apiKey = "TU_CLAVE_API"; // Reemplaza con tu clave de Google Maps
    const form = document.getElementById("searchForm");
    const resultsContainer = document.getElementById("results");

    form.addEventListener("submit", async (event) => {
        event.preventDefault(); // Prevenir recarga de la página

        const query = document.getElementById("query").value;
        const url = `https://maps.googleapis.com/maps/api/place/textsearch/json?query=${encodeURIComponent(query)}&key=${apiKey}`;

        try {
            const response = await fetch(url);
            if (!response.ok) throw new Error("Error al obtener resultados");

            const data = await response.json();
            displayResults(data.results);
        } catch (error) {
            console.error("Error al buscar negocios:", error);
            resultsContainer.innerHTML = "<p>Hubo un error al realizar la búsqueda.</p>";
        }
    });

    function displayResults(results) {
        resultsContainer.innerHTML = results.map(result => `
            <div class="result-item">
                <h2>${result.name}</h2>
                <p>${result.formatted_address}</p>
                <a href="https://www.google.com/maps/place/?q=place_id:${result.place_id}" target="_blank">
                    Ver en Google Maps
                </a>
            </div>
        `).join("");
    }
});
