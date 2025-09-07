# 🏀 SuperManager ACB 21/22

Proyecto en Python para **crear la mejor plantilla posible** del SuperManager ACB de la temporada 21/22.  

La idea es usar datos reales y un algoritmo para conseguir la mejor valoración con el presupuesto y las restricciones disponibles.

## Cómo funciona

1. **Scrapea la web de ACB** para obtener la valoración de cada jugador de la temporada pasada.  
2. **Scrapea la web de SuperManager** para saber el precio actual de cada jugador.  
3. Resuelve el **problema de la mochila** con **algoritmos genéticos**: Se combina valoración y precio (además de restricciones como máximo de jugadores) para elegir la mejor plantilla dentro del presupuesto disponible.

*Disclaimer: Este proyecto fue creado durante la temporada 2021-2022. Si no cambia la web y se puede scrapear igual debería funcionar en cualquier temporada.*

*Disclaimer: Es un proyecto de prueba para jugar con algoritmos genéticos y no tiene en cuenta muchos otros factores. Por ejemplo, jugadores sin valoraciones en ACB en años anteriores no se tendrán en cuenta.*
