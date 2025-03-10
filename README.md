# Extractor de Productos de HTML a CSV

Este proyecto es un script en Python que extrae información de un archivo HTML y la exporta a un archivo CSV. El script identifica bloques de productos en el HTML, extrae el nombre de cada producto y la URL de la imagen asociada, y guarda estos datos en un CSV.

## Características

- **Extracción de datos:** Utiliza expresiones regulares para localizar y extraer los bloques de productos, el nombre del producto y la URL de la imagen.
- **Exportación a CSV:** Los datos extraídos se guardan en un archivo CSV con dos columnas: "Nombre del Producto" y "URL de la Imagen".
- **Fácil personalización:** Las expresiones regulares se pueden ajustar para adaptarse a diferentes estructuras de HTML.

## Estructura del HTML de Entrada

El script está diseñado para trabajar con un HTML que contenga productos definidos dentro de un bloque `<div class="item">`. Dentro de cada bloque se espera encontrar:
- El nombre del producto, dentro de una etiqueta `<h2>`.
- La imagen del producto, en una etiqueta `<img>` que incluya el atributo `alt="producto"`.

Ejemplo de bloque de producto:
```html
<div class="item">
  <h2>Nombre del Producto</h2>
  <img src="url_de_la_imagen.jpg" alt="producto" />
</div>

```

## Video

Link: https://youtu.be/5RI85g1Kf4I