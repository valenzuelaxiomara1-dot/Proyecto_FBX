# 📊 Análisis de Server Access Logs con Pandas

Este proyecto analiza y procesa un archivo de registros de acceso (*access logs*) de un servidor web Nginx/Apache utilizando **Python** y la librería **Pandas**. Forma parte del trabajo práctico para la asignatura de **2º de ASIR**.

---

## 👥 Integrantes del Equipo

- Fred Ruiz Guerrero
- Bryan Fabricio Paucar Alvarado
- Xiomara Isabella Valenzuela Maza

## Descripción

Análisis de los logs de acceso de una tienda online con Pandas, desde el punto de vista de un administrador de sistemas: limpieza y exploración de los datos, combinación de tablas (`merge`), agrupaciones (`groupby`), tabla dinámica (`pivot_table`), selección avanzada (`loc` e `iloc`) y visualización con gráficos estáticos e interactivos. El informe está escrito en Quarto y publicado como web.

## Enlaces

- **Informe publicado:** (URL de GitHub Pages, por ejemplo https://TU_USUARIO.github.io/Proyecto_FBX/)
- **Repositorio:** https://github.com/frg-skbd/Proyecto_FBX

## Dataset

- **Nombre:** Web Server Access Logs
- **Fuente:** [Kaggle](https://www.kaggle.com/datasets/eliasdabbas/web-server-access-logs)
- **Cita:** Zaker, Farzin (2019), «Online Shopping Store - Web Server Logs», Harvard Dataverse, V1, https://doi.org/10.7910/DVN/3QBYB5
- **Licencia:** CC0 (dominio público)
- **Contenido:** log de acceso de 3,5 GB en formato Nginx (`access.log`) y un archivo con información de los clientes (`client_hostname.csv`).

El log original no está en el repositorio por su tamaño. En `data/muestra.log` se incluye una muestra sistemática (una de cada N líneas, con N = (valor usado)), generada con `scripts/crear_muestra.py`.

## Estructura del repositorio

```
Proyecto_FBX/
├── index.qmd              # Informe en Quarto (código y explicaciones)
├── _quarto.yml            # Configuración de la web
├── requirements.txt       # Librerías de Python necesarias
├── scripts/
│   └── crear_muestra.py   # Crea la muestra a partir del log completo
└── data/
    ├── muestra.log        # Muestra del log de acceso
    ├── client_hostname.csv
    └── codigos_http.csv   # Tabla auxiliar de códigos HTTP
```

## Cómo reproducir el análisis

Requisitos: Python 3, Quarto y Git.

```powershell
git clone https://github.com/frg-skbd/Proyecto_FBX.git
cd Proyecto_FBX
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
quarto preview
```

Para publicar la web en GitHub Pages:

```powershell
quarto publish gh-pages
```

## Herramientas

Python, Pandas, Matplotlib, Seaborn, Plotly, Quarto, Git y GitHub Pages.
