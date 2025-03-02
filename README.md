# Breast Cancer Diagnosis with an ANN

## Descripción del Proyecto

Este proyecto académico tiene como objetivo desarrollar un sistema de diagnóstico de cáncer de mama utilizando una red neuronal artificial (ANN) con regresión. El sistema se basa en el conjunto de datos de cáncer de mama de Wisconsin (diagnóstico) y proporciona una interfaz gráfica de usuario (GUI) para visualizar los resultados del análisis.  
Si quieres contactarme puedes hacerlo a través de mi correo electrónico: andres.montes-zuluaga@laplateforme.io

## Contenido

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Contenido](#contenido)
- [Visualización](#screenshot)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Licencia](#licencia)
- [Autores](#autores)

## Screenshot

![Screenshot del Proyecto](ruta/al/screenshot.png)

## Requisitos

Para ejecutar este proyecto, necesitarás las siguientes bibliotecas de Python:

```pip-requirements
# Machine learning and data processing libraries
scikit-learn==1.2.2  # Tools for data mining and data analysis
pandas==1.5.3        # Data manipulation and analysis
numpy==1.24.2        # Fundamental package for scientific computing

# Deep learning library
keras==2.11.0        # High-level neural networks API

# Visualization libraries
matplotlib==3.7.1    # Plotting and visualization
seaborn==0.12.2      # Statistical data visualization

# PyQt5 for the graphical user interface
PyQt5==5.15.9        # Set of Python bindings for Qt libraries
```

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tu-usuario/breast-cancer-diagnosis-nna-regresion.git
   cd breast-cancer-diagnosis-nna-regresion
   ```

2. Instala las dependencias utilizando pip:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para ejecutar el proyecto, simplemente ejecuta el script `main.py`:

```bash
python main.py
```

Esto abrirá una interfaz gráfica de usuario donde podrás ver los resultados del análisis del modelo.

## Estructura del Proyecto

```
breast-cancer-diagnosis-nna-regresion/
│
├── src/
│   ├── __init__.py               # Inicializa el paquete y realiza las importaciones necesarias
│   ├── build_ann.py              # Construye y compila la red neuronal artificial
│   ├── DatasetInfo.py            # Muestra la información del conjunto de datos
│   ├── HelpButton.py             # Crea un botón de ayuda que muestra un mensaje informativo
│   ├── load_and_prepare_data.py  # Carga y prepara el conjunto de datos de cáncer de mama
│   └── ResultsWindow.py          # Muestra los resultados del análisis en una ventana gráfica
│
├── main.py                       # Script principal que ejecuta el flujo completo del proyecto
├── requirements.txt              # Lista de dependencias necesarias para el proyecto
├── README.md                     # Descripción del proyecto y guía de uso
└── LICENSE.txt                   # Información sobre la licencia del proyecto
```

## Licencia

Este proyecto está licenciado bajo la Licencia Creative Commons Attribution-NonCommercial 4.0 International. Para más detalles, consulta el fichero LICENSE.txt.

## Autores

Andrés MONTES ZULUAGA - Desarrollador Principal - https://github.com/andres-montes-zuluaga/  
Si tienes alguna pregunta o sugerencia, no dudes en contactarme.

¡Gracias por utilizar este proyecto! Espero que te sea de gran ayuda en tus estudios y proyectos académicos.