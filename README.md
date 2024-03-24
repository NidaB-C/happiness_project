# Global Happiness Predictor

The Global Happiness Predictor aims to leverage machine learning techniques to predict an individual's happiness level based on global happiness metrics. By abstracting data from the World Happiness Report to a personal level, this tool offers a unique perspective for self-assessment and understanding happiness determinants.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Technical Stack](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Model Development](#model-development)
- [Collaborators](#collaborators)

## <a id="introduction"></a>Introduction

This project synthesizes data from the World Happiness Report to predict happiness levels on an individual basis. Through exploratory data analysis, model development, and an interactive web interface, users can gain insights into their happiness determinants and see how they compare on a global scale.

### Data Source

The project utilizes the World Happiness Report dataset available on [Kaggle](https://www.kaggle.com/datasets/carlosmorenohernndez/world-happiness-report-2015-2023), which compiles global happiness metrics across several years. This dataset forms the foundation for our analysis and model development, providing a robust framework for understanding the intricacies of happiness on a global scale.

## <a id="project-structure"></a>Project Structure

The repository is organized as follows to ensure ease of navigation and collaboration:

- **`data/`**: Contains all datasets used in the project.
  - `processed/`: Cleaned and processed data ready for modelling.
  - `raw/`: Original datasets.
- **`docs/`**: Documentation related to the project.
- **`models/`**: Machine learning models including training and evaluation scripts.
- **`notebooks/`**: Jupyter notebooks for exploratory data analysis and model prototyping.
- **`src/`**: Source code for the application, including Flask backend and frontend assets.
- **`tests/`**: Automated tests for application functionality.
- **`.gitignore`**: Configuration file for ignored files and directories in git.
- **`requirements.txt`**: Required Python libraries for the project.

## <a id="dependencies"></a>Technical Stack

- **Data Analysis and Modeling:** Pandas, Scikit-learn
- **Backend Framework:** Flask
- **Data Processing:** PySpark (for handling large datasets, if necessary)
- **Frontend:** HTML, CSS (Bootstrap for styling), JavaScript (for dynamic content)
- **Visualization:** Matplotlib/Plotly for generating insightful charts
- **Database:** SQL Database (for storing user inputs and predictions, if applicable)

## <a id="installation"></a>Installation

To set up your environment to run the project, follow these steps:

1. **Clone the Repository**:  
   `git clone https://github.com/NidaB-C/happiness_project.git`
   
2. **Create a Virtual Environment** (optional, but recommended):  
   `python -m venv venv`  
   `source venv/bin/activate` (Linux/Mac)
   `venv\Scripts\activate` (Windows)
   
4. **Install Dependencies**:  
   `pip install -r requirements.txt`

## <a id="usage"></a>Usage

To use the application and interact with the happiness prediction model:

1. Navigate to the `src/` directory:  
   `cd src/`
   
2. Run the Flask application:  
   `python app.py`
   
3. Open a web browser and go to `http://127.0.0.1:5000/` to interact with the application.

## <a id="model-development"></a>Model Development
Detail the process of model selection, training, evaluation, and optimization here. Include any specific metrics (e.g., accuracy, R-squared) achieved during the development.

## <a id="collaborators"></a>Collaborators 

- [Sunil Malhi](https://github.com/SunilMalhi)
- [Tafadzwa Fararira](https://github.com/BootcampCoderTF)
- [Yuk Hang Hui](https://github.com/alexyhHui)
- [Nida Ballinger-Chaudhary](https://github.com/NidaB-C)

