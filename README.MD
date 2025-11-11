# Microservicio de Cálculo de Factorial y Paridad

## Descripción del Proyecto

Este microservicio recibe un número por URL y devuelve una respuesta JSON con:
- El número recibido
- Su factorial
- Una etiqueta "par" o "impar" según corresponda

## Uso del Microservicio

### Ejemplo de Petición
- Si ingresamos a la URL base del local host podemos ingresar un numero en el campo habilitado para esto y al darle enter seremos redirigos a la pagina que nos entrega el json, si no queremos podemos hacer la peticion a la URL directamente así ->

```bash
curl http://localhost:5000/numero/5
```

### Ejemplo de Respuesta
```json
{
  "numero_recibido": 5,
  "factorial": 120,
  "paridad": "impar"
}
```

## Instalación y Ejecución
- Clonar el repositorio y entrar en el directorio.

1. Instalar dependencias:
```bash
pip install flask
```

2. Ejecutar el microservicio:
```bash
python app.py
```
El servicio estará disponible en `http://localhost:5000`

## Pregunta: Comunicación con Servicio de Historial de Cálculos

### ¿Cómo modificar el diseño si este microservicio tuviera que comunicarse con otro servicio que almacena el historial de cálculos en una base de datos externa?

### Respuesta:

- Una solcución para manejar el historial de los numeros calculados puede ser generar una comunicación mediante HTTP REST, es decir, el microservicio realiza llamadas HTTP directas al servicio de historial y este le entrega los resultados que pidamos, esta es una solucion facil y obtenemos una respuesta inmedianta, ademas, con esta opcion no sería necesario una infraestructura extra (carita feliz), pero si el historial falla puede llegar a afectar directamente a la aplicacion principal por dicha conexion directa y en caso de que el historial se vuelva muy grande las peticiones a la base de datos pueden hacerse mas lenta (carita triste). Es decir depende del tamaño de datos que vayamos a manejar y la cantidad de peticiones que vayamos a hacer, pues esta es una solución sencilla.

- En caso de que se quiera implementar un sistema diferente podriamos pensar en usar algo como una aplicacion externa (terceros) a la cual hagamos un llamado mediante el consumo de una API y cada que hagamos un calculo se almacene luego de completar la petición inicial a nuestro microservicio
