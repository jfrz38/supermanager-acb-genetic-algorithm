# Scraping de la Valoración

Scrapear la página de la ACB para obtener la valoración de todos los jugadores el año pasado.

Esta información se guardará en un fichero .csv que posteriormente será leído por el programa de predicción.

## Pasos a seguir

Cogiendo como base la página de la [ACB](https://www.acb.com/):

1. Se itera sobre el div `contenedor_logos_equipos`.
2. Obtener información para los jugadores de la plantilla:
    - Coger el nombre del equipo de `datos.roboto_condensed_bold mayusculas`.
    - Coger enlaces para las estadísticas del valor href de `grid_plantilla principal.caja_miembro_plantilla caja_jugador_medio_cuerpo.datos.nombre roboto_condensed_bold`. Y el nombre de este mismo sitio pero con el valor.
    - Coger el permiso del jugador de `info_personal roboto.span`. Es el último `span` y el valor será de 3 letras siempre.
    - Coger la posición de `info_basica.posicion roboto_condensed`
3. Obtener la valoración del último año:
    - Coger el antepenúltimo `tr` del body la tabla `table-estadisticas-jugador`. (si no hay mínimo 3 es que el año pasado no jugó en ACB)
    - La valoración es el valor del penúltimo `td`. Pero hay que mirar el valor del primer `td` que tiene la clase "temporada", para ver si es 21-22.

## Fichero generado

Con todos los datos de todos los equipos scrapeados debe quedar un fichero similar al que se muestra a continuación:

```bash
equipo,jugador,posicion,valoracion,permiso
Barça,Oriol Paulí,A,11,JFL
```

## SuperManager

Con estos datos se debe scrapear la web del supermanager para obtener el precio que tiene cada jugador y así añadirlo al CSV.

1. Iniciar sesión en: <https://supermanager.acb.com/#/session/signin-email> con los datos:
    - email: YOUR_EMAIL
    - contraseña: YOUR_PASSWORD

2. Acceder al mercado para ver los valores:
    - Bases: <https://supermanager.acb.com/#/market?position=1>
    - Aleros: <https://supermanager.acb.com/#/market?position=3>
    - Pivots: <https://supermanager.acb.com/#/market?position=5>

3. Para cada una de las posiciones:
    1. Acceder a la tabla de `table table-borderless.tbody`.
    2. Para cada `tr`:
        - 1er `td`: Foto de perfil.
        - 2º `td`: Nombre (1er `div`) y posición.
        - 3er `td`: Licencia `div.img.src`(el valor puede no existir o acabar en "eu.png" o "spain.png")
        - 4º `td`: Equipo `div.img.title`
        - 5º `td`: Precio `div.span`
