const loginForm = document.querySelector("#loginForm");
const registerForm = document.querySelector("#registerForm");
const newUserForm = document.querySelector("#newUserForm");
const editUserForm = document.querySelector("#editUserForm");
const messageForm = document.querySelector("#messageForm");
const commentForm = document.querySelector("#commentForm");
const statusMessage = document.querySelector("#statusMessage");

function showMessage(text) {
    if (statusMessage) {
        statusMessage.textContent = text;
    }
}

function passwordsMatch(form, passwordName, confirmPasswordName) {
    const formData = new FormData(form);
    return formData.get(passwordName) === formData.get(confirmPasswordName);
}

if (loginForm) {
    loginForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const formData = new FormData(loginForm);
        const email = String(formData.get("loginEmail")).trim().toLowerCase();
        const target = email === "patricia@codingdojo.com" || email.includes("admin")
            ? "pages/dashboard-admin.html"
            : "pages/dashboard.html";

        showMessage("Inicio de sesion enviado.");
        loginForm.reset();
        window.location.href = target;
    });
}

if (registerForm) {
    registerForm.addEventListener("submit", (event) => {
        event.preventDefault();

        if (!passwordsMatch(registerForm, "password", "confirmPassword")) {
            showMessage("Las contrasenas no coinciden.");
            return;
        }

        showMessage("Registro enviado correctamente.");
        registerForm.reset();
    });
}

if (newUserForm) {
    newUserForm.addEventListener("submit", (event) => {
        event.preventDefault();

        if (!passwordsMatch(newUserForm, "newPassword", "newConfirmPassword")) {
            showMessage("Las contrasenas no coinciden.");
            return;
        }

        window.location.href = "dashboard-admin.html";
    });
}

if (editUserForm) {
    editUserForm.addEventListener("submit", (event) => {
        event.preventDefault();

        if (!passwordsMatch(editUserForm, "editPassword", "editConfirmPassword")) {
            showMessage("Las contrasenas no coinciden.");
            return;
        }

        window.location.href = "dashboard-admin.html";
    });
}

if (messageForm) {
    messageForm.addEventListener("submit", (event) => {
        event.preventDefault();
        showMessage("Mensaje enviado.");
        messageForm.reset();
    });
}

if (commentForm) {
    commentForm.addEventListener("submit", (event) => {
        event.preventDefault();
        showMessage("Comentario enviado.");
        commentForm.reset();
    });
}
