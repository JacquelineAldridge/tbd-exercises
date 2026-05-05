

Implementar el modelo `Cliente` y  `Orden` en SQLAlchemy, sus schemas Pydantic, y los 5 endpoints CRUD en FastAPI.

---

## Paso 1 — Modelos SQLAlchemy (`models.py`)

Crea el modelo `Cliente` con las siguientes columnas:

- `id` — entero, primary key
- `nombre` — string de máximo 100 caracteres
- `email` — string de máximo 150 caracteres, debe ser único
- `telefono` — string de máximo 20 caracteres, **opcional** (puede ser null)
- `activo` — booleano, por defecto `True`
- `creado_en` — datetime, por defecto la fecha/hora actual


Crea el modelo `Orden` con las siguientes columnas:

- `id` — UUID, primary key, generado automáticamente con `uuid.uuid4`
- `cantidad` — entero
- `estado` — string, por defecto `"pendiente"`
- `creado_en` — datetime, por defecto la fecha/hora actual

## Paso 2 — Schemas Pydantic (`schemas.py`)

Creá los siguientes schemas:

- **`ClienteRead`** — `nombre`,`email`, `telefono`, `activo`  agrega `id` y `creado_en`. Configuralo para que pueda leer datos desde objetos SQLAlchemy.
- **`ClienteCreate`** — todos los campos excepto el  `id`.
- **`ClienteUpdate`** — todos los campos opcionales.
- **`OrdenCreate`** — todos los campos excepto el id 
- **`OrdenUpdate`** — `cantidad` y `estado`, ambos opcionales.
- **`OrdenRead`** — mismos campos que `OrdenCreate` más `id`

Puedes validar el email utilizando el tipo de Pydantic `EmailStr`

## Paso 3 — Endpoints (`routers/clientes.py`)

Creá un router con prefijo `/clientes`. Implementá estos 5 endpoints:

- **GET `/`** — devuelve la lista de todos los clientes.
- **GET `/{cliente_id}`** — devuelve un cliente por su id. Si no existe, retorná 404.
- **POST `/`** — recibe un `ClienteCreate`, crea el cliente y lo retorna. Status code 201.
- **PATCH `/{cliente_id}`** — recibe un `ClienteUpdate` y actualiza solo los campos que llegaron. Si no existe, retorná 404.
- **DELETE `/{cliente_id}`** — elimina el cliente. Si no existe, retorná 404. Status code 204, sin body.

Creá un router con prefijo `/ordenes`. Implementá estos 5 endpoints:
- **GET `/`** — devuelve la lista de todas las órdenes.
- **GET `/{orden_id}`** — devuelve una orden por su UUID. Si no existe, retorná 404.
- **POST `/`** — recibe un `OrdenCreate`, crea la orden y la retorna. Status code 201.
- **PATCH `/{orden_id}`** — recibe un `OrdenUpdate` y actualiza solo los campos que llegaron. Si no existe, retorná 404.
- **DELETE `/{orden_id}`** — elimina la orden. Si no existe, retorná 404. Status code 204, sin body.



## Paso 4 — Registrar el router

Incluye los router en `main.py` para que los endpoints queden disponibles.

