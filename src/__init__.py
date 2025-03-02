"""
This module initializes the package and performs the necessary imports for breast cancer diagnosis using an artificial neural network (ANN) with regression.

Imports:
- DatasetInfo: Class to handle dataset information.
- HelpButton: Class to create a help button in the user interface.
- load_and_prepare_data: Function to load and prepare data for the model.
- build_ann: Function to build the artificial neural network.
- ResultsWindow: Class to display results in a window.
"""

from .DatasetInfo import DatasetInfo
from .HelpButton import HelpButton
from .load_and_prepare_data import load_and_prepare_data
from .build_ann import build_ann
from .ResultsWindow import ResultsWindow