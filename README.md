# dracosecure.com

Web estática de **DracoSecure**, especialistas en mantenimiento y seguridad de WordPress.

## Estructura

| Archivo | Uso |
| --- | --- |
| `gen.py` | Generador de las cuatro páginas. **Editar aquí**, no en los HTML. |
| `index.html`, `services.html`, `pricing.html`, `contact.html` | Páginas generadas (no editar a mano). |
| `styles.css` | Sistema visual, componentes y responsive. |
| `script.js` | Menú móvil, selector mensual/anual y formulario de contacto. |
| `assets/` | Logotipo y favicon. |
| `sitemap.xml`, `robots.txt` | SEO técnico. |
| `CNAME` | Dominio personalizado de GitHub Pages (`www.dracosecure.com`). |

## Desarrollo local

```bash
python3 gen.py
python3 -m http.server 8000
```

Abre `http://localhost:8000`. Tras cualquier cambio en textos, precios o marca, vuelve a ejecutar `python3 gen.py`: los HTML se sobrescriben desde el generador.

## Configuración

En la cabecera de `gen.py` están los valores centralizados:

- `BRAND`: nombre comercial.
- `DOMAIN` / `BASE`: dominio canónico, URLs de Open Graph, JSON-LD, sitemap y robots.
- `EMAIL`: correo de contacto y destinatario del formulario.

Los precios y sus características están en las listas `COMPARE`, `VALUE_ITEMS`, `FAQ` y en las llamadas a `plan()` dentro de `gen.py`.

## Formulario de contacto

No hay backend: al enviar, `script.js` abre el cliente de correo del visitante con el mensaje pre rellenado hacia `EMAIL`. No se almacenan datos en el sitio. Si más adelante quieres un formulario con envío automático, cambia el listener de `#f` para usar tu proveedor (Formspree, Netlify Forms, etc.) y actualiza el texto de privacidad del formulario.

## Publicación

Es un sitio puramente estático: sube la carpeta tal cual a GitHub Pages. El fichero `CNAME` ya apunta a `www.dracosecure.com`; el dominio apex (`dracosecure.com`) debe redirigir a `www` desde tu proveedor DNS.
