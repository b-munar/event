# Instalacion

1. Clonar repositorio

```bash
git clone https://github.com/b-munar/event

2. 

```bash
docker compose build
docker compose up
```


El servicio de Servicios de terceros.

## 1. Get events 

Retorna eventos.

<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6950/events</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>N/A</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>

```json
{
    "events": [
        {
            "id": "416cd4c3-044c-407c-a0aa-abd58ec49de6",
            "titulo": "evente",
            "fecha": "2019-05-05",
            "hora": "17:00",
            "description": "Test event",
            "location": "Mall"
        }
    ]
}
```
</td>
</tr>
</tbody>
</table>

## 2. Post events 

Permite realizar creación de eventos.

<table>
<tr>
<td> Método </td>
<td> POST </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6950/events</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>

```json
  {
 "titulo": "evente",
 "fecha":"2019-05-05",
 "description":"Test event",
 "hora": "17:00",
 "location":"Mall"
}
  ```
</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>

```json
{
    "id": "416cd4c3-044c-407c-a0aa-abd58ec49de6",
    "titulo": "evente",
    "fecha": "2019-05-05",
    "hora": "17:00",
    "description": "Test event",
    "location": "Mall"
}
```
</td>
</tr>
</tbody>
</table>

## 3. Get events as user registrated to an event

Retorna eventos.

<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6950/events/sportmen</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>N/A</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>

```json
{
    "events": [
        {
            "id": "95b43bdc-023a-4903-be2c-47108e7190ab",
            "event_id": "3ebb7955-7c2b-479f-8d8f-1fb02700b5b7",
            "event": {
                "id": "3ebb7955-7c2b-479f-8d8f-1fb02700b5b7",
                "titulo": "evente",
                "fecha": "2019-05-05",
                "hora": "17:00",
                "description": "Test event",
                "location": "Mall"
            }
        }
    ]
}
```
</td>
</tr>
</tbody>
</table>

## 4. Registrarme a un evento 

Permite realizar de registro de eventos.

<table>
<tr>
<td> Método </td>
<td> POST </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6950/events/sportmen</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>

```json
  {
"event_id": "3ebb7955-7c2b-479f-8d8f-1fb02700b5b7"
}
  ```
</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>

```json
{
    "id": "95b43bdc-023a-4903-be2c-47108e7190ab",
    "event_id": "3ebb7955-7c2b-479f-8d8f-1fb02700b5b7",
    "event": {
        "id": "3ebb7955-7c2b-479f-8d8f-1fb02700b5b7",
        "titulo": "evente",
        "fecha": "2019-05-05",
        "hora": "17:00",
        "description": "Test event",
        "location": "Mall"
    }
}
```
</td>
</tr>
</tbody>
</table>

## 5. Get events as a partner who create those events

Retorna eventos.

<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6950/events/partner</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>N/A</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>

```json
{
    "events": [
        {
            "id": "00917c5a-a6d9-49bc-9e0a-e6977e7458b1",
            "titulo": "evente",
            "fecha": "2019-05-05",
            "hora": "17:00",
            "description": "Test event",
            "location": "Mall"
        },
        {
            "id": "3ebb7955-7c2b-479f-8d8f-1fb02700b5b7",
            "titulo": "evente",
            "fecha": "2019-05-05",
            "hora": "17:00",
            "description": "Test event",
            "location": "Mall"
        }
    ]
}
```
</td>
</tr>
</tbody>
</table>

## 6. Cancel register to an event as user 

Permite realizar de cancelacion de registro de eventos.

<table>
<tr>
<td> Método </td>
<td> DELETE </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6950/events/sportmen</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>

```json
  {
"event_id": "3ebb7955-7c2b-479f-8d8f-1fb02700b5b7"
}
  ```
</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>
N/A
</td>
</tr>
</tbody>
</table>
