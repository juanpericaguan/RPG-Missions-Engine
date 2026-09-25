🧩Sistema de Misiones RPG en Python
Arquitectura basada en State y Mediator


📌 Descripción

Este proyecto implementa un sistema de misiones secuenciales inspirado en videojuegos RPG, desarrollado en Python y enfocado en arquitectura de software, programación orientada a objetos y patrones de diseño.

El objetivo principal no es el juego en sí, sino demostrar cómo organizar un sistema donde:

- El comportamiento depende del estado actual de la misión.
- Las acciones del jugador determinan el flujo de ejecución.
- Los componentes no se comunican entre sí directamente.
- La lógica se encuentra desacoplada y distribuida entre responsabilidades claras.
- Las misiones se definen de forma declarativa mediante un archivo JSON.

El sistema permite iniciar una misión, interactuar con sus diferentes etapas, realizar acciones inválidas sin avanzar de estado, abandonar una misión y retomarla posteriormente, completar la misión y volver a ejecutarla desde el principio.



🧠 Patrones de diseño aplicados
🔹 State Pattern

Cada etapa de la misión se modela como un estado independiente:

- NivelCombate
- NivelInteraccion
- NivelRecompensa

Cada estado define:

- Qué acciones están permitidas.
- Qué resultado produce cada acción.
- Cuándo una acción debe ser rechazada.

Por ejemplo, durante el estado de combate:

Combatir      → Acción válida
Interactuar   → Acción inválida
Abrir cofre   → Acción inválida

Mientras que durante la etapa de recompensa:

Combatir      → Acción inválida
Interactuar   → Acción inválida
Abrir cofre   → Acción válida

Esto permite modificar el comportamiento de cada etapa sin recurrir a grandes bloques de if/elif y sin modificar los componentes del sistema.



🔹 Mediator Pattern

Toda la comunicación entre los componentes principales pasa por un mediador central:

- Jugador
- Enemigo
- NPC
- Cofre
- Estados de la misión

Los componentes no necesitan conocerse entre sí.

Por ejemplo:

Jugador
Enemigo
NPC
Cofre
   │
   ▼
MediatorMision
   │
   ▼
State actual


El MediatorMision coordina las acciones, recibe los resultados del estado actual y determina cómo debe continuar la misión.

Esto permite:

- Reducir el acoplamiento entre componentes.
- Centralizar la coordinación del flujo.
- Facilitar futuras extensiones.
- Mantener las responsabilidades de cada componente más claras.



📂 Estructura del proyecto
├── main.py            # Punto de entrada e interfaz de terminal
├── mediator.py        # Mediador y coordinación del flujo de misión
├── states.py          # Estados de la misión (State Pattern)
├── components.py      # Componentes del sistema
├── json_loader.py     # Carga de misiones desde JSON
├── misiones.json      # Definición declarativa de las misiones
└── README.md


📜 Definición de misiones (JSON)

Las misiones se definen externamente mediante JSON, permitiendo modificar sus pasos sin modificar directamente la lógica del programa.

Ejemplo de un paso:

{
  "tipo": "combatir",
  "objetivo": "Derrotar al lobo alfa"
}

Una misión puede estar compuesta por diferentes tipos de pasos:

- combatir
- interaccion
- recompensa

El sistema utiliza esta información para determinar el estado correspondiente y validar las acciones disponibles para el jugador.



🎮 Ejecución interactiva

A diferencia de una ejecución automática, el sistema permite que el jugador controle el desarrollo de la misión desde la terminal.

Durante cada etapa se muestra el objetivo actual y las acciones disponibles:

Objetivo actual:
    - Derrotar al lobo alfa

¿Qué desea hacer?

1. Combate
2. Interactuar con aldeano
3. Abrir cofre
0. Salir

La opción seleccionada por el usuario es traducida por la interfaz a una acción del dominio y enviada al MediatorMision.

El estado actual determina si dicha acción es válida.

Ejemplo

Si la misión se encuentra en estado de combate:

Jugador → Combate
           ↓
        válido
           ↓
     avanzar al siguiente estado

Si el jugador intenta abrir el cofre antes de tiempo:

Jugador → Abrir cofre
           ↓
        inválido
           ↓
      permanecer en
      estado actual
🔄 Control del progreso


El MediatorMision mantiene el estado actual de la misión mediante:

- indice: indica el paso actual.
- state: representa el estado correspondiente al paso.
- terminada: indica si la misión fue completada.

Esto permite que el jugador pueda abandonar una misión durante la sesión y retomarla posteriormente desde el mismo punto.

Una misión completada también puede reiniciarse mediante el método:

mediator.reiniciar_mision()

El reinicio restaura el índice, reconstruye el estado inicial y marca nuevamente la misión como no terminada.

⚙️ Flujo de ejecución

El flujo general del sistema es:

Usuario
   │
   ▼
Interfaz de terminal
   │
   │ elección del jugador
   ▼
MediatorMision
   │
   ├── determina la acción
   │
   ├── comunica con el componente correspondiente
   │
   └── consulta al State actual
              │
              ▼
        ¿Acción válida?
          │         │
         Sí        No
          │         │
          ▼         ▼
       avanzar   permanecer
          │       en el estado
          ▼
    nuevo State

El mediador también utiliza mapas de correspondencia para evitar condicionales innecesarios:

Tipo de paso → Estado
Tipo de acción → Componente
Resultado → Acción del Mediator



▶️ Cómo ejecutar el proyecto

Requisitos:

- Python 3.10 o superior.

Ejecutar desde la carpeta del proyecto:

python main.py

El programa iniciará la interfaz de terminal y permitirá interactuar con la misión.



✅ Características técnicas destacadas
- Programación Orientada a Objetos.
- Implementación del patrón State.
- Implementación del patrón Mediator.
- Misiones configurables mediante JSON.
- Ejecución interactiva desde terminal.
- Validación de tipos de pasos.
- Validación de acciones según el estado actual.
- Control del progreso mediante un índice de misión.
- Posibilidad de abandonar y retomar una misión.
- Posibilidad de reiniciar misiones completadas.
- Uso de mapas/diccionarios para despachar acciones.
- Separación entre interfaz, coordinación y comportamiento de estados.
- Código modular y preparado para futuras extensiones.




🚀 Posibles mejoras

Algunas extensiones que podrían incorporarse en futuras versiones:

- Soporte para múltiples misiones y selección de misiones.
- Sistema de progreso persistente entre ejecuciones.
- Sistema de experiencia, niveles y estadísticas del jugador.
- Sistema de recompensas configurable desde JSON.
- Más tipos de estados y acciones.
- Sistema de diálogos para NPCs.
- Interfaz gráfica.
- Generación dinámica de misiones.




🎯 Objetivo del proyecto

Este proyecto fue desarrollado para:

- Consolidar el uso de programación orientada a objetos.
- Comprender y aplicar patrones de diseño.
- Mejorar la separación de responsabilidades.
- Trabajar con sistemas configurables mediante archivos externos.
- Practicar arquitecturas desacopladas.
- Pensar en la evolución de un sistema más allá de un script lineal.

El proyecto también representa una evolución desde una ejecución automática de misiones hacia un sistema interactivo donde las decisiones del usuario determinan el flujo de la misión.





🧑‍💻 Autor

Juan Pericaguan

Correo: juanmiguel018@gmail.com

Proyecto desarrollado en Python como parte de un proceso de crecimiento hacia un perfil profesional de desarrollo de software, con especial interés en programación orientada a objetos, arquitectura, automatización y buenas prácticas.