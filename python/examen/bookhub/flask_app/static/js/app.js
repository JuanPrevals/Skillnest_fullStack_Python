document.querySelectorAll(".password-toggle").forEach((button) => {
    button.addEventListener("click", () => {
        const input = document.getElementById(button.dataset.target);
        const visible = input.type === "text";
        input.type = visible ? "password" : "text";
        button.textContent = visible ? "Mostrar" : "Ocultar";
        button.setAttribute("aria-label", visible ? "Mostrar contraseña" : "Ocultar contraseña");
    });
});

document.querySelectorAll("form[data-confirm-delete]").forEach((form) => {
    form.addEventListener("submit", (event) => {
        const titulo = form.dataset.confirmDelete;
        if (!window.confirm(`¿Eliminar “${titulo}”? Esta acción no se puede deshacer.`)) {
            event.preventDefault();
        }
    });
});

const errorSummary = document.querySelector("[data-error-summary]");
if (errorSummary) {
    errorSummary.focus();
}
