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