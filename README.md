# 📊 Proyecto FBX: Análisis de Server Access Logs con Pandas

Trabajo 1 (Pandas) · 2º de ASIR

Análisis de los logs de acceso de un servidor web con Pandas, documentado en un informe de Quarto y publicado como página web con GitHub Pages.
Desde el punto de vista de un administrador de sistemas: limpieza y exploración de los datos, combinación de tablas (`merge`), agrupaciones (`groupby`), tabla dinámica (`pivot_table`), selección avanzada (`loc` e `iloc`) y visualización con gráficos estáticos e interactivos. El informe está escrito en Quarto y publicado como web.


## 👥 Integrantes del Equipo

- Fred Ruiz Guerrero
- Bryan Fabricio Paucar Alvarado
- Xiomara Isabella Valenzuela Maza
- 
## Enlaces

- **Informe publicado:** (URL de GitHub Pages, por ejemplo https://TU_USUARIO.github.io/Proyecto_FBX/)
- **Repositorio:** https://github.com/frg-skbd/Proyecto_FBX

## Objetivo

Aplicar Pandas a un caso de administración de sistemas: partiendo del log de acceso de una tienda online, limpiar y explorar los datos, responder preguntas propias de un SysAdmin (carga por horas, errores HTTP, IPs abusivas, tráfico de robots) y proponer acciones correctoras a partir de los resultados.

## Dataset

- **Nombre:** Web Server Access Logs
- **Fuente:** [Kaggle (eliasdabbas)](https://www.kaggle.com/datasets/eliasdabbas/web-server-access-logs)
- **Contenido:** 3,5 GB de logs de acceso en formato Nginx de una tienda online iraní
- **Archivos:** `access.log` (3,5 GB) y `client_hostname.csv` (13 MB)
- **Licencia de los datos:** CC0 (dominio público)
- **Cita:** Zaker, Farzin (2019), «Online Shopping Store - Web Server Logs», Harvard Dataverse, V1, https://doi.org/10.7910/DVN/3QBYB5

El log completo no cabe en GitHub (límite de 100 MB por archivo), así que el repositorio incluye una **muestra sistemática**: una de cada N líneas del original (N = 100; *sustituir por el valor real usado*). El script que la genera está en `scripts/crear_muestra.py`.

## Contenido del análisis

1. Carga y parseo del log con expresiones regulares
2. Exploración inicial y limpieza (EDA) con tres resúmenes estadísticos
3. Combinación de datos con `merge`: log + `client_hostname.csv` y log + tabla de códigos HTTP
4. Análisis avanzado: `groupby`, `pivot_table` y filtrado con `loc` / `iloc`
5. Visualización: dos gráficos estáticos, un gráfico interactivo y uno animado (Plotly)
6. Conclusiones técnicas y acciones correctoras

## Estructura del repositorio

```
Proyecto_FBX/
├── index.qmd               # Informe en Quarto (código + explicaciones)
├── _quarto.yml             # Configuración del sitio web
├── requirements.txt        # Librerías de Python
├── README.md
├── .gitignore
├── scripts/
│   └── crear_muestra.py    # Genera data/muestra.log a partir de access.log
└── data/
    ├── muestra.log         # Muestra del log (1 de cada N líneas)
    ├── client_hostname.csv # IP y hostname de los clientes
    └── codigos_http.csv    # Tabla auxiliar de códigos HTTP
```

El archivo original `data/access.log` (3,5 GB) no se sube al repositorio.

## Cómo reproducirlo

Requisitos: Python 3, [Quarto](https://quarto.org/docs/get-started/) y Git.

```powershell
git clone https://github.com/frg-skbd/Proyecto_FBX.git
cd Proyecto_FBX
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
quarto preview
```

Con eso se puede regenerar el informe, porque la muestra ya está incluida en `data/`.

Para volver a crear la muestra desde el log original:

1. Descargar `access.log` y `client_hostname.csv` desde Kaggle y copiarlos en `data/`.
2. Ejecutar `python scripts\crear_muestra.py`.

Para publicar la web:

```powershell
quarto publish gh-pages
```

## Tecnologías

Python · Pandas · Matplotlib · Seaborn · Plotly · Quarto · Git y GitHub Pages

