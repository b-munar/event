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

## 1. Get Sessions 

Retorna sesiones deportivas del usuarip.

<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6950/sport-session</strong> </td>
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
    "id": "16d83bc2-1d61-4ea3-ae36-e937c52f8a9a",
    "trainingDayId": "86559da0-6100-45e1-84e7-85a304a6be21",
    "endDate": "2022-06-14 13:00:00",
    "startDate": "2022-06-14 13:00:00"
}
```
</td>
</tr>
</tbody>
</table>

## 2. Post session 

Permite realizar el almacenamiento de información de una sesion deportiva.

<table>
<tr>
<td> Método </td>
<td> POST </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6950/sport-session</strong> </td>
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
 "trainingDayId": "86559da0-6100-45e1-84e7-85a304a6be21",
 "startDate": "2022-06-14T13:00:00-07:00",
 "endDate": "2022-06-14T13:00:00-07:00"
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
    "sessions": [
        {
            "id": "16d83bc2-1d61-4ea3-ae36-e937c52f8a9a",
            "trainingDayId": "86559da0-6100-45e1-84e7-85a304a6be21",
            "endDate": "2022-06-14 13:00:00",
            "startDate": "2022-06-14 13:00:00"
        }
    ]
}
```
</td>
</tr>
</tbody>
</table>