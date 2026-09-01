# Visitas

Aplicación Flask que utiliza la sesión del navegador para contar visitas y reinicios.

## Instalación y ejecución

```powershell
cd python/core/visitas
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Abre `http://127.0.0.1:5000/` en el navegador.

## Funcionalidades

- Cuenta cada visita directa a la ruta principal.
- Aumenta el contador en dos.
- Agrega una cantidad personalizada mediante un formulario.
- Reinicia las visitas a cero y registra la cantidad de reinicios.
- Elimina toda la sesión desde `/destruir_sesion`.
