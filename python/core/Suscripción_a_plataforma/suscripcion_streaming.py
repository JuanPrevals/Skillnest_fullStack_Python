# Las plataformas de streaming utilizan modelos de suscripción que determinan el acceso a contenido, calidad de reproducción y beneficios adicionales. Poder modelar estas reglas usando clases en Python es clave para entender cómo funcionan los sistemas de pago y control de acceso en aplicaciones reales como Netflix, Spotify o YouTube Premium.

# 📝 Instrucciones
# 📄 Crea un archivo de Python llamado suscripcion_streaming.py.

# 📦 Define la clase SuscripcionStreaming, que debe incluir:

# Atributos:
# usuario (nombre del usuario asociado a la suscripción)
# tipo_suscripcion (Gratis, Estándar, Premium)
# costo_mensual (según el tipo de suscripción)
# saldo_pendiente (monto acumulado que debe pagar el usuario)
# Métodos:
# realizar_pago(self, monto) reduce el saldo pendiente según el monto pagado.
# cambiar_suscripcion(self, nuevo_tipo) cambia el tipo de suscripción y ajusta el costo mensual.
# ver_contenido_exclusivo(self) permite el acceso a contenido según el tipo de suscripción. La suscripción “Gratis” no tiene acceso a contenido exclusivo.
# mostrar_info_suscripcion(self) muestra el estado actual de la suscripción del usuario.

# 🧪 Realizar las siguientes pruebas con instancias:

# Crea 3 usuarios con diferentes tipos de suscripción.
# Haz que el primer usuario intente ver contenido exclusivo, mejore su suscripción y pague su saldo.
# Haz que el segundo usuario vea contenido exclusivo, cambie su suscripción a Premium y pague dos veces.
# Haz que el tercer usuario intente pagar una cantidad menor a su saldo pendiente y vea contenido exclusivo.

# 🏁 Resultado esperado 
# Al finalizar esta práctica, habrás implementado una clase en Python que simula la gestión de suscripciones en una plataforma de streaming, permitiendo cambiar el tipo de suscripción, realizar pagos y ver contenido exclusivo. Esto te ayudará a entender cómo funcionan los modelos de suscripción en aplicaciones reales y cómo estructurar código reutilizable y escalable con POO.

# 💻 Código base


class SuscripcionStreaming:
   costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

   def __init__(self, usuario, tipo_suscripcion="Gratis"):
         if tipo_suscripcion not in SuscripcionStreaming.costos_suscripcion:
              print("Tipo de suscripción no válido. Se asignará la suscripción Gratis.")
              tipo_suscripcion = "Gratis"

         self.usuario = usuario
         self.tipo_suscripcion = tipo_suscripcion
         self.costo_mensual = SuscripcionStreaming.costos_suscripcion[tipo_suscripcion]
         self.saldo_pendiente = self.costo_mensual

   def realizar_pago(self, monto):
         """Realiza un pago y reduce el saldo pendiente."""
         if monto <= 0:
              print("El monto debe ser mayor a cero.")
              return
         
         self.saldo_pendiente -= monto
         if self.saldo_pendiente < 0:
              self.saldo_pendiente = 0
         print(f"Pago realizado: ${monto:.2f}. Saldo pendiente: ${self.saldo_pendiente:.2f}")

   def cambiar_suscripcion(self, nuevo_tipo):
         """Cambia el tipo de suscripción y ajusta el costo mensual."""
         if nuevo_tipo not in SuscripcionStreaming.costos_suscripcion:
              print("Tipo de suscripción no válido.")
              return
         
         self.tipo_suscripcion = nuevo_tipo
         self.costo_mensual = SuscripcionStreaming.costos_suscripcion[nuevo_tipo]
         self.saldo_pendiente += self.costo_mensual  # Agrega el nuevo costo al saldo pendiente
         print(f"Suscripción cambiada a {nuevo_tipo}. Nuevo costo mensual: ${self.costo_mensual:.2f}")

   def ver_contenido_exclusivo(self):
            """Permite el acceso a contenido exclusivo según el tipo de suscripción."""
            if self.tipo_suscripcion == "Gratis":
                print("Acceso denegado. Actualiza tu suscripción para ver contenido exclusivo.")
            else:
                print(f"Acceso concedido. Disfruta del contenido exclusivo con tu suscripción {self.tipo_suscripcion}.")

   def mostrar_info_suscripcion(self):
            """Muestra el estado actual de la suscripción del usuario."""
            print(f"Usuario: {self.usuario}")
            print(f"Tipo de Suscripción: {self.tipo_suscripcion}")
            print(f"Costo Mensual: ${self.costo_mensual:.2f}")
            print(f"Saldo Pendiente: ${self.saldo_pendiente:.2f}")
   
# Pruebas
if __name__ == "__main__":
    # Crear usuarios con diferentes tipos de suscripción
    usuario1 = SuscripcionStreaming("Alice", "Gratis")
    usuario2 = SuscripcionStreaming("Bob", "Estándar")
    usuario3 = SuscripcionStreaming("Charlie", "Premium")
    
    # Usuario 1 intenta ver contenido exclusivo, mejora su suscripción y paga su saldo
    print("Usuario 1:")
    usuario1.ver_contenido_exclusivo()
    usuario1.cambiar_suscripcion("Estándar")
    usuario1.realizar_pago(5.99)
    usuario1.mostrar_info_suscripcion()
    
    # Usuario 2 ve contenido exclusivo, cambia a Premium y paga dos veces
    print("\nUsuario 2:")
    usuario2.ver_contenido_exclusivo()
    usuario2.cambiar_suscripcion("Premium")
    usuario2.realizar_pago(10.99)
    usuario2.realizar_pago(10.99)
    usuario2.mostrar_info_suscripcion()
    
    # Usuario 3 intenta pagar una cantidad menor a su saldo pendiente y ve contenido exclusivo
    print("\nUsuario 3:")
    usuario3.realizar_pago(5)  # Pago insuficiente
    usuario3.ver_contenido_exclusivo()
    usuario3.mostrar_info_suscripcion()

    
    
    
