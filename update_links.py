import os
import re
from datetime import datetime

def replace_links_and_texts(file_path):
    print(f"📂 Procesando el archivo: {file_path}")

    # Expresión regular para `href`, `src` o `content`
    link_pattern = re.compile(r'(href|src|content)=(["\'])([^"\']+\.(svg|jpg|png|js|css))\2')
    # Expresión regular especial para `use xlink:href`
    sprite_pattern = re.compile(r'(<use xlink:href=["\'][^"\'>]+\#([^"\'>]+)["\'].*?</use>)')

    # Leer el archivo HTML
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"❌ El archivo '{file_path}' no existe.")
        return
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return

    print("✅ Archivo leído correctamente. Realizando Tarea 1: Reemplazo de enlaces...\n")

    # Tarea 1: Reemplazo de enlaces
    replacements = []

    # Buscar y procesar enlaces generales
    matches = link_pattern.findall(content)
    if matches:
        for match in matches:
            attr = match[0]  # 'href', 'src', o 'content'
            quote = match[1]  # Tipo de comillas: simples o dobles
            full_path = match[2]  # Ruta completa del enlace
            file_name = full_path.split('/')[-1]  # Nombre del archivo
            new_value = f'{{{{ url_for(\'static\', filename=\'img/{file_name}\') }}}}'
            # Siempre usar doble comilla
            original = f'{attr}={quote}{full_path}{quote}'
            new_link = f'{attr}="{new_value}"'
            print(f"🔗 Original encontrado: {original}")
            print(f"   ➡️ Nuevo generado: {new_link}\n")
            # Agregar al listado de reemplazos
            replacements.append((original, new_link))

    # Buscar y procesar enlaces `use xlink:href`
    sprite_matches = sprite_pattern.findall(content)
    if sprite_matches:
        for match in sprite_matches:
            original = match[0]  # Línea completa del <use ...></use>
            fragment = match[1]  # Fragmento después del `#`
            file_name = f"{fragment}.svg"  # Nombre del archivo basado en el fragmento
            new_link = f'<image src="{{{{ url_for(\'static\', filename=\'img/{file_name}\') }}}}" alt="{fragment}" />'
            print(f"🔗 Original encontrado: {original}")
            print(f"   ➡️ Nuevo generado: {new_link}\n")
            # Agregar al listado de reemplazos
            replacements.append((original, new_link))

    # Aplicar los reemplazos de enlaces al contenido
    for original, new in replacements:
        content = content.replace(original, new)

    # Guardar contenido después de la Tarea 1
    now = datetime.now().strftime('%H%M%S')
    temp_file_path = os.path.splitext(file_path)[0] + f"_tarea1_{now}.html"
    try:
        with open(temp_file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"✅ Tarea 1 completada. Archivo temporal guardado como: {temp_file_path}")
    except Exception as e:
        print(f"❌ Error al guardar el archivo de Tarea 1: {e}")
        return

    # Tarea 2: Reemplazo de textos adicionales
    print("\n✅ Realizando Tarea 2: Reemplazo de textos adicionales...\n")
    replacements_texts = [
        ("hawk-style.com/en", "tecnomata.com"),
        ("hawk-style.com", "tecnomata.com"),
        ("Hawk Style Design", "Tecnomata Desarrollo Web"),
        ("en_US", "es_MX"),
    ]

    for original_text, new_text in replacements_texts:
        print(f"🔄 Reemplazando: {original_text} ➡️ {new_text}")
        content = content.replace(original_text, new_text)

    # Guardar contenido final después de la Tarea 2
    final_file_path = os.path.splitext(file_path)[0] + f"_final_{now}.html"
    try:
        with open(final_file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"✅ Tarea 2 completada. Archivo final guardado como: {final_file_path}")
    except Exception as e:
        print(f"❌ Error al guardar el archivo final: {e}")

if __name__ == "__main__":
    file_path = input("Introduce la ruta completa del archivo HTML que deseas modificar: ").strip()
    if os.path.isfile(file_path):
        replace_links_and_texts(file_path)
    else:
        print(f"❌ La ruta '{file_path}' no corresponde a un archivo válido.")







