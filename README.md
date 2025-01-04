
```shell
spotfolio/
│
├── spotfolio/                 # Carpeta principal del framework
│   ├── __init__.py            # Inicializador del módulo
│   ├── core.py                # Clase principal (SpotFolio)
│   ├── blog.py                # Módulo para manejar blogs
│   ├── portfolio.py           # Módulo para manejar portafolios
│   ├── templates/             # Plantillas HTML por defecto
│   └── static/                # Archivos estáticos (CSS, JS)
│
├── tests/                     # Pruebas unitarias
│   └── test_core.py           # Pruebas para el core del framework
│
├── examples/                  # Ejemplos de uso
│   ├── basic_blog/            # Ejemplo básico de blog
│   └── portfolio_site/        # Ejemplo básico de portafolio
│
├── setup.py                   # Configuración para PyPI
├── README.md                  # Documentación inicial
└── requirements.txt           # Dependencias
```

### To run an example first export the module
```shell
export PYTHONPATH=$PYTHONPATH:./portfolio
# Then run
uv run examples/basic_blog/app.py
```
