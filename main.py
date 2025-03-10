import re
import csv

def cargar_html(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return f.read()

def extraer_productos(html):
    pattern_item = re.compile(r'<div class="item">(.*?)</div>', re.IGNORECASE | re.DOTALL)
    pattern_name = re.compile(r'<h2[^>]*>(.*?)</h2>', re.IGNORECASE | re.DOTALL)
    pattern_img  = re.compile(r'<img[^>]*src="([^"]+)"[^>]*alt="producto"[^>]*>', re.IGNORECASE | re.DOTALL)

    items = pattern_item.findall(html)
    productos = []

    for bloque in items:
        name_match = pattern_name.search(bloque)
        img_match  = pattern_img.search(bloque)
        if name_match and img_match:
            name = name_match.group(1).strip()
            url  = img_match.group(1).strip()
            productos.append((name, url))

    return productos

def exportar_csv(productos, archivo_salida):
    with open(archivo_salida, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nombre del Producto", "URL de la Imagen"])
        writer.writerows(productos)

if __name__ == "__main__":
    archivo_html = "tienda.html"
    archivo_csv = "productos.csv"

    html_content = cargar_html(archivo_html)
    productos_extraidos = extraer_productos(html_content)
    exportar_csv(productos_extraidos, archivo_csv)
    print(f"Datos exportados correctamente a '{archivo_csv}'")
