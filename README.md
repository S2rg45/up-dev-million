# Prueba 

Este repositorio se crean tres servicios en FastAPI, para poder validar informacion de propiedades en USA

## Infraestructura

Se implementa una infra de microservicio, implementado con programacion orientada a objetos.

## Contexto del trabajo

| **Cargo**						 | **Nombre**		     |  
|--------------------------------|-----------------------|
| **Caso de Uso**  				 | Get properties        |   
| **Servicios**                  | /million/image        |
|                                | /million/create_property |
|                                | /million/update_price |
|                                | /singup               |
|                                | /login                |
| **Arquitectura**               | Servicios             |
| **Database**                   | MongoDB               |


## Security

Se crea una capa de seguridad para que se puedan crear usuarios que solamente puedan utilizar ellos los servicios creados, la contrasena esta encriptada por "bcrypt", y se guarda de esta manera en Base de datos.

Se genera un login que genera un token con codifica "JsonWeb token", por el usuario e email, para generar la validacion al momento de querer utilizar cualquier servicio.

## Documentacion de servicios

URL_Server/docs#

## URL del repositorio

https://github.com/S2rg45/up-dev-million

## Versiones

0.0.1

## Body de pruebas

| **api**						            | **Nombre**		                        |     
|-------------------------------------------|-------------------------------------------|
| **localhost:8000/million/change_price**   | {"property_owner":                        |
|                                           |    {"name": "luis Hamilton",              |
|                                           |    "address": "Carere"},                  |
|                                           |  "change_price_property":                 |
|                                           |    {"name": "aranjuez",                   |
|                                           |    "address": "carrera 71 --2s",          |
|                                           |    "price": "124"}                        |
|                                           |  }                                        |   
| **localhost:8000/million/update_image**   | {"property_owner":                        |
|                                           |    {"name": "luis Hamilton",              |
|                                           |    "address": "Carere"},                  |
|                                           |  "change_price_property":                 |
|                                           |    {"name": "aranjuez",                   |
|                                           |    "address": "carrera 71 --2s",          |
|                                           |     }                                     |
|                                           |  }                                        | 
| **localhost:8000/million/create_property**| {                                         | 
|                                           |       "owner": {                          | 
|                                           |           "name": "1434534222",           | 
|                                           |           "address":  "132432",           | 
|                                           |           "photo": "",                    | 
|                                           |           "birthday": "2001/01/01"        | 
|                                           |       },                                  | 
|                                           |       "property": {                       | 
|                                           |           "name": "231325",               | 
|                                           |           "address": "carrera 71 --2s",   | 
|                                           |           "price": "1525",                | 
|                                           |           "codeInternal": "1",            | 
|                                           |           "year": "2020/01/02"            | 
|                                           |       },                                  | 
|                                           |       "property_image": {                 | 
|                                           |           "file": "/jpg",                 | 
|                                           |           "enabled": false                | 
|                                           |       },                                  | 
|                                           |      "property_trace": {                  | 
|                                           |           "dateSale": "2021/01/01",       | 
|                                           |           "name": "JUAN camilo",          | 
|                                           |           "value": "300000000",           | 
|                                           |           "tax": "10"                     | 
|                                           |            }                              | 
|                                           |       }                                   |   
| **localhost:8000/million/singup**         | {                                         |
|                                           |    "username": "luis Hamilton",           |
|                                           |    "email": "Juan@gmail.com",             |
|                                           |    "password": "sdfsda"                   |
|                                           | }                                         |
| **localhost:8000/million/login**          |                                           |
|                                           | {                                         |
|                                           |    "email": "Juan@gmail.com",             |
|                                           |    "password": "sdfsda"                   |
|                                           | }                                         |
|                                           |                                           |