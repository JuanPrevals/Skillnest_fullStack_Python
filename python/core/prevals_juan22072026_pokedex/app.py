from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

pokedex = [
   {"id": 1, "nombre": "Bulbasaur", "tipo": "Planta/Veneno", "imagen": "bulbasaur.png", "poder": 45, "altura": "0.7m", "peso": "6.9kg"},
   {"id": 4, "nombre": "Charmander", "tipo": "Fuego", "imagen": "charmander.png", "poder": 39, "altura": "0.6m", "peso": "8.5kg"},
   {"id": 7, "nombre": "Squirtle", "tipo": "Agua", "imagen": "squirtle.png", "poder": 44, "altura": "0.5m", "peso": "9.0kg"},
   {"id": 25, "nombre": "Pikachu", "tipo": "Eléctrico", "imagen": "pikachu.png", "poder": 35, "altura": "0.4m", "peso": "6.0kg"},
   {"id": 39, "nombre": "Jigglypuff", "tipo": "Normal/Hada", "imagen": "jigglypuff.png", "poder": 115, "altura": "0.5m", "peso": "5.5kg"},
   {"id": 52, "nombre": "Meowth", "tipo": "Normal", "imagen": "meowth.png", "poder": 40, "altura": "0.4m", "peso": "4.2kg"},
   {"id": 54, "nombre": "Psyduck", "tipo": "Agua", "imagen": "psyduck.png", "poder": 50, "altura": "0.8m", "peso": "19.6kg"},
   {"id": 94, "nombre": "Gengar", "tipo": "Fantasma/Veneno", "imagen": "gengar.png", "poder": 60, "altura": "1.5m", "peso": "40.5kg"},
   {"id": 95, "nombre": "Onix", "tipo": "Roca/Tierra", "imagen": "onix.png", "poder": 35, "altura": "8.8m", "peso": "210.0kg"},
   {"id": 143, "nombre": "Snorlax", "tipo": "Normal", "imagen": "snorlax.png", "poder": 160, "altura": "2.1m", "peso": "460.0kg"}
]


@app.route("/")
def inicio():
   return redirect(url_for("mostrar_pokemon"))


@app.route("/pokemon")
def mostrar_pokemon():
   return render_template("pokemon.html", pokemones=pokedex)


@app.route("/pokemon/buscar")
def buscar_pokemon():
   consulta = request.args.get("q", "").strip()
   if not consulta:
      return redirect(url_for("mostrar_pokemon"))
   return redirect(url_for("mostrar_pokemon_por_identificador", identificador=consulta))


@app.route("/pokemon/cantidad/<int:cantidad>")
def mostrar_cantidad(cantidad):
   if cantidad < 1:
      return pokemon_no_encontrado("La cantidad debe ser mayor que cero.")
   return render_template("pokemon.html", pokemones=pokedex[:cantidad])


@app.route("/pokemon/<identificador>")
def mostrar_pokemon_por_identificador(identificador):
   pokemon = next(
      (
         item for item in pokedex
         if item["nombre"].casefold() == identificador.casefold()
         or str(item["id"]) == identificador
      ),
      None,
   )
   if pokemon is None:
      return pokemon_no_encontrado(
         f'No pudimos encontrar información sobre "{identificador}" en nuestra Pokédex.'
      )
   return render_template("pokemon.html", pokemones=[pokemon])


@app.route("/404")
def pagina_no_encontrada():
   return pokemon_no_encontrado("No pudimos encontrar ese Pokémon en nuestra Pokédex.")

def pokemon_no_encontrado(mensaje):
   return render_template("404.html", mensaje=mensaje), 404


@app.errorhandler(404)
def ruta_no_encontrada(_error):
   return pokemon_no_encontrado("La página que buscas no existe.")

if __name__ == "__main__":
   app.run(debug=True)
