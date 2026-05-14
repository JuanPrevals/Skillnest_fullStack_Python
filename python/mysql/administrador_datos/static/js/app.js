const loginForm = document.querySelector("#loginForm");
const registerForm = document.querySelector("#registerForm");
const statusMessage = document.querySelector("#statusMessage");

function showMessage(text) {
    statusMessage.textContent = text;
}

loginForm.addEventListener("submit", (event) => {
    event.preventDefault();
    showMessage("Inicio de sesion enviado.");
    loginForm.reset();
});

registerForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const formData = new FormData(registerForm);
    const password = formData.get("password");
    const confirmPassword = formData.get("confirmPassword");

    if (password !== confirmPassword) {
        showMessage("Las contrasenas no coinciden.");
        return;
    }

    showMessage("Registro enviado correctamente.");
    registerForm.reset();
});
