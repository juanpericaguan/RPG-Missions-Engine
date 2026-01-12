🧩 Sistema de Misiones RPG en Python
Arquitectura basada en State y Mediator


📌 Descripción

Este proyecto implementa un sistema de misiones secuenciales inspirado en videojuegos RPG, desarrollado en Python y enfocado en arquitectura de software y patrones de diseño.

El objetivo principal no es el juego en sí, sino demostrar cómo organizar un sistema donde:

El flujo de ejecución depende del estado actual

Los componentes no se comunican entre sí directamente

La lógica es extensible, mantenible y desacoplada

Las misiones se definen de forma declarativa mediante un archivo JSON y se ejecutan automáticamente respetando el orden lógico de los pasos.





🧠 Patrones de diseño aplicados
🔹 State Pattern

Cada etapa de la misión se modela como un estado independiente:

Combate

Interacción

Recompensa

Cada estado define:

Qué acciones están permitidas

Qué resultado produce cada acción

Esto permite cambiar el comportamiento del sistema sin condicionales complejos y sin modificar el resto del código.

🔹 Mediator Pattern

Toda la comunicación entre los componentes pasa por un mediador central:

Jugador

Enemigo

NPC

Cofre

Estados de la misión

Los componentes no se conocen entre sí, lo que:

Reduce el acoplamiento

Simplifica el flujo

Facilita futuras extensiones




📂 Estructura del proyecto

├── main.py            # Punto de entrada
├── mediator.py        # Lógica central y flujo de la misión
├── states.py          # Estados de la misión (State Pattern)
├── components.py      # Entidades del sistema
├── json_loader.py     # Carga y validación de misiones
├── misiones.json      # Definición declarativa de misiones
└── README.md




📜 Definición de misiones (JSON)

Las misiones se definen externamente en JSON, lo que permite modificar el flujo sin tocar el código:

{
  "tipo": "combatir",
  "objetivo": "Derrotar al lobo alfa"
}

El sistema interpreta automáticamente cada paso y ejecuta la acción correspondiente según el estado actual.




▶️ Cómo ejecutar el proyecto

Asegurarse de tener Python 3.10+

Ejecutar:   python main.py





⚙️ Flujo de ejecución

Se cargan las misiones desde JSON

El mediador valida los pasos

Se crea el estado inicial

Cada paso se ejecuta según su tipo

El estado devuelve un resultado

El mediador decide cómo avanzar

La lógica de control está centralizada y desacoplada de los componentes.




✅ Características técnicas destacadas

Separación clara de responsabilidades

Uso de mapas en lugar de if/elif

Validación de datos de entrada

Arquitectura orientada a escalabilidad

Código modular y fácil de mantener

Pensado para crecimiento futuro






🚀 Posibles mejoras

Ejecución interactiva (elecciones del jugador)

Soporte para múltiples misiones

Persistencia de progreso

Integración con interfaz gráfica

Generación dinámica de misiones





🎯 Objetivo del proyecto

Este proyecto fue desarrollado como práctica avanzada para:

Consolidar el uso de patrones de diseño

Mejorar la organización del código

Pensar en sistemas escalables más allá de scripts simples




🧑‍💻 Autor
Juan Pericaguan
Correo: juanmiguel018@gmail.com

Proyecto desarrollado en Python como parte de un proceso de crecimiento hacia un perfil Junior sólido / Semi-Senior, con foco en arquitectura y buenas prácticas.