# Breast Cancer Diagnosis with an ANN

## Project Description

This academic project aims to develop a breast cancer diagnosis system using an artificial neural network (ANN) with regression. The system is based on the Wisconsin breast cancer dataset (diagnosis) and provides a graphical user interface (GUI) to visualize the analysis results.  
If you want to contact me, you can do so via my email: andres.montes-zuluaga@laplateforme.io

## Table of Contents

- [Project Description](#project-description)
- [Table of Contents](#table-of-contents)
- [Screenshot](#screenshot)
- [Main Features](#main-features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)
- [Authors](#authors)

## Screenshot

![Project Screenshot](path/to/screenshot.png)

## Main Features

- Breast cancer diagnosis using an artificial neural network.
- Graphical user interface (GUI) to visualize the analysis results.
- Based on the Wisconsin breast cancer dataset (diagnosis).
- Easy installation and usage with clear instructions.

## Requirements

To run this project, you will need the following Python libraries:

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

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/breast-cancer-diagnosis-nna-regresion.git
   cd breast-cancer-diagnosis-nna-regresion
   ```

2. Install the dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the project, simply execute the `main.py` script:

```bash
python main.py
```

This will open a graphical user interface where you can see the model analysis results.

## Project Structure

```
breast-cancer-diagnosis-nna-regresion/
│
├── src/
│   ├── __init__.py               # Initializes the package and performs necessary imports
│   ├── build_ann.py              # Builds and compiles the artificial neural network
│   ├── DatasetInfo.py            # Displays information about the dataset
│   ├── HelpButton.py             # Creates a help button that shows an informative message
│   ├── load_and_prepare_data.py  # Loads and prepares the breast cancer dataset
│   └── ResultsWindow.py          # Displays the analysis results in a graphical window
│
├── main.py                       # Main script that runs the complete project workflow
├── requirements.txt              # List of dependencies required for the project
├── README.md                     # Project description and usage guide
└── LICENSE.txt                   # Project license information
```

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License. For more details, see the LICENSE.txt file.

## Authors

Andrés MONTES ZULUAGA - Lead Developer - https://github.com/andres-montes-zuluaga/  
If you have any questions or suggestions, feel free to contact me.

Thank you for using this project! I hope it is very helpful in your studies and academic projects.