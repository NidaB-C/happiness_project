# Global Happiness Predictor

The Global Happiness Predictor is an innovative project designed to utilize machine learning techniques to predict an individual's happiness level based on input data reflective of the factors identified in the World Happiness Report. This project abstracts global data to a personal level, providing users with a unique tool for self-assessment.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Technical Stack](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Collaborators](#collaborators)

## <a id="introduction"></a>Introduction

This project aims to analyze, understand, and predict happiness levels by exploring the data provided in the World Happiness Report. It involves data preprocessing, exploratory data analysis, machine learning model development, and creating an interactive web application for users to input their data and receive happiness predictions.

### Data Source

The project utilizes the World Happiness Report dataset available on [Kaggle](https://www.kaggle.com/datasets/unsdsn/world-happiness), which compiles global happiness metrics across several years. This dataset forms the foundation for our analysis and model development, providing a robust framework for understanding the intricacies of happiness on a global scale.

## <a id="project-structure"></a>Project Structure

The repository is organized as follows to ensure ease of navigation and collaboration:

- **`data/`**: Contains all datasets used in the project.
  - `processed/`: Cleaned and processed data ready for modelling.
  - `raw/`: Original datasets.
- **`docs/`**: Documentation related to the project.
- **`models/`**: Machine learning models and training scripts.
- **`notebooks/`**: Jupyter notebooks for exploratory data analysis.
- **`src/`**: Source code for the application.
- **`tests/`**: Automated tests for the application.
- **`.gitignore`**: Specifies untracked files to ignore.
- **`requirements.txt`**: Lists dependencies for the project.

## <a id="dependencies"></a>Technical Stack

The project relies on several Python libraries, including but not limited to:
- Pandas
- Scikit-learn
- Flask
- PySpark

## <a id="installation"></a>Installation

To set up your environment to run the project, follow these steps:

1. **Clone the Repository**:  
   `git clone https://github.com/NidaB-C/happiness_project.git`
   
2. **Create a Virtual Environment** (optional, but recommended):  
   `python -m venv venv`  
   `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
   
3. **Install Dependencies**:  
   `pip install -r requirements.txt`

## <a id="usage"></a>Usage

To use the application and interact with the happiness prediction model:

1. Navigate to the `src/` directory:  
   `cd src/`
   
2. Run the Flask application:  
   `python app.py`
   
3. Open a web browser and go to `http://127.0.0.1:5000/` to interact with the application.


## <a id="collaborators"></a>Collaborators 

- [Sunil Malhi](https://github.com/SunilMalhi)
- [Tafadzwa Fararira](https://github.com/BootcampCoderTF)
- [Yuk Hang Hui](https://github.com/alexyhHui)
- [Nida Ballinger-Chaudhary](https://github.com/NidaB-C)

