# ============================================================
# OptiCrop: Smart Agricultural Production Optimization Engine
# Import Required Libraries
# ============================================================

# ----------------------------
# Data Manipulation Libraries
# ----------------------------
import pandas as pd
import numpy as np

# ----------------------------
# Visualization Libraries
# ----------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# Jupyter Notebook Configuration
# ----------------------------
from IPython.core.interactiveshell import InteractiveShell
from ipywidgets import interact

# ----------------------------
# Machine Learning Libraries
# ----------------------------
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    confusion_matrix,
    classification_report
)

# ============================================================
# Display Settings
# ============================================================

# Display all columns and up to 50 rows
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 50)
pd.set_option("display.max_colwidth", 20)

# Configure plot size
plt.rcParams["figure.figsize"] = (12, 8)

# Display all outputs in Jupyter Notebook cells
InteractiveShell.ast_node_interactivity = "all"

# Enable inline plotting (for Jupyter Notebook)
%matplotlib inline

# Set visualization theme
plt.style.use("fivethirtyeight")
sns.set_style("whitegrid")
