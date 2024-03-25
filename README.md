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
### Logistic Regression Model Summary

The logistic regression model was developed to predict the binary happiness indicator derived from the World Happiness Report data. The model's performance was robust, with an accuracy score of approximately 98.9%. Precision, recall, and F1-scores were consistently high for both the 'happy' (1) and 'not happy' (0) classes, signifying the model's proficient classification capabilities.
<img width="466" alt="Screenshot 2024-03-25 at 7 33 26 PM" src="https://github.com/NidaB-C/happiness_project/assets/147389952/58ada587-c8ce-4fec-930c-01a8ab113778">
#### Performance Metrics:
- **Accuracy**: Approximately 98.9%, indicating a high overall rate of correct predictions.
- **Precision**: High for both classes (0.98 for class 0 and 1.00 for class 1), implying a low false-positive rate.
- **Recall**: Perfect (1.00) for class 0 and nearly perfect (0.98) for class 1, reflecting the model's effectiveness in identifying true positives.
- **F1-Score**: Close to 1 for both classes, denoting a balanced precision-recall relationship.
<img width="524" alt="Screenshot 2024-03-24 at 1 11 22 PM" src="https://github.com/NidaB-C/happiness_project/assets/147389952/90ae6a69-dc42-49c9-b837-2d6a24bcf357">

The confusion matrix provided additional insights:

- Correctly predicted "not happy" instances: 131
- Correctly predicted "happy" instances: 140
- False negatives: 3
- False positives: 0

## Random Forest Model Summary

In the development of our Random Forest model, we have achieved a remarkable level of accuracy, reaching the pinnacle of 100%. The precision, recall, and F1-scores achieved by the model are consistently perfect across both the "happy" and "not happy" classes, according to the classification report. This suggests an exceptional ability of the model to classify individuals accurately based on their happiness indicators. Detailed metrics from the evaluation are as follows:
<img width="455" alt="Screenshot 2024-03-25 at 7 40 57 PM" src="https://github.com/NidaB-C/happiness_project/assets/147389952/1b0f8ac2-2c12-4833-ad8b-9901929ee0b2">

- **Precision**: A perfect score of 1.00 for both classes, suggesting an absence of false positives.
- **Recall**: Flawless recall of 1.00 for both "not happy" and "happy" classes, indicating no misclassifications in the form of false negatives.
- **F1-Score**: At 1.00 for both classes, the model shows an ideal balance between precision and recall.
- **Support**: The support values show an even distribution of observations across the classes in the test dataset.
<img width="513" alt="Screenshot 2024-03-25 at 7 41 14 PM" src="https://github.com/NidaB-C/happiness_project/assets/147389952/622f385f-caa3-41e0-bde2-295bae018f25">

The confusion matrix corroborates these findings, demonstrating the model's accuracy:

- **131 instances** of class "not happy" were correctly classified.
- **143 instances** of class "happy" were correctly classified.
- There were **no instances** of false negatives or false positives.

### Interpretation and Recommendations

While the Random Forest model's performance is commendable, a 100% accuracy rate raises considerations regarding the potential for overfitting, especially if the model has not been subjected to a robust cross-validation procedure or tested on an independent dataset.

## Decision Tree Model Summary

The Decision Tree model was meticulously crafted and assessed, yielding an exemplary performance with an accuracy score of 100%. The precision, recall, and F1-score for both classes — "happy" and "not happy" — achieved the highest possible mark, demonstrating the model's remarkable classification precision. Below are the salient details from the model's evaluation:
<img width="441" alt="Screenshot 2024-03-25 at 7 44 04 PM" src="https://github.com/NidaB-C/happiness_project/assets/147389952/88ade3a4-31ac-49f6-af29-d46aa7a30503">

- **Precision**: Attained a perfect score of 1.00 for both classes, indicating no instance of a false positive.
- **Recall**: Achieved a score of 1.00 for both classes, reflecting the model's precision in correctly identifying all true positives without any false negatives.
- **F1-Score**: Obtained a score of 1.00 for each class, suggesting an optimal balance between precision and recall.
- **Support**: The support numbers indicate an evenly distributed number of observations across both classes in the test data.

The confusion matrix solidifies the exemplary metrics, showing a flawless classification by the model:

- Total correct classifications for "not happy": 131
- Total correct classifications for "happy": 143
- Zero instances of false negatives and false positives.
<img width="536" alt="Screenshot 2024-03-25 at 7 44 22 PM" src="https://github.com/NidaB-C/happiness_project/assets/147389952/288dd0f7-df2e-4f59-aa41-836d573545af">

### Interpretation and Strategic Enhancements

While the Decision Tree model's results are outstanding, a 100% accuracy may raise questions regarding the model's generalizability, prompting us to consider the potential of overfitting. To validate the model's robustness and prepare it for real-world applications, the following strategies are recommended:

1. **Cross-Validation**: Utilise cross-validation to ascertain consistent performance and to mitigate overfitting risks.
2. **Feature Importance Assessment**: Conduct an in-depth analysis of the influence each feature has on the model's decision-making process.
3. **Model Complexity Review**: Compare the Decision Tree model against other models to evaluate whether simpler or more intricate models offer improved or comparable performance.
4. **Pruning Techniques**: Implement pruning methods available for Decision Trees to refine the model and prevent it from overfitting to the training data.
5. **Dataset Expansion**: If limited by data constraints, consider enhancing the dataset to bolster the model's ability to generalise.
6. **Anomaly Investigation**: Inspect the data for anomalies or outliers that might unduly sway the model's predictions and address them as needed.
7. **Expert Domain Review**: Consult with domain experts to verify that the model's predictions align with real-world expectations and knowledge.
8. **External Dataset Validation**: Evaluate the model against an independent dataset to confirm its generalisation capabilities.

In essence, the Decision Tree model exhibits exceptional accuracy in predicting individual happiness levels. Nonetheless, due diligence in the form of further validation and refinement is imperative to ensure its readiness for deployment and use in practical settings.

## Model Selection Rationale

When selecting the most appropriate model for predicting individual happiness levels, we were presented with two exceptionally performing models: the Logistic Regression model and the Decision Tree model. Both models achieved high accuracy scores, with the Decision Tree model reaching a perfect score of 100% and the Logistic Regression model close behind with an accuracy of approximately 98.9%. Despite these impressive metrics, our choice of the model was contingent upon a broader set of criteria, which included the following considerations:

### Model Interpretability
- **Decision Tree**: Provides a highly interpretable structure that can be visualized and easily understood, even by individuals with a non-technical background. The decision-making process is transparent, showing clear paths from features to the outcome.
- **Logistic Regression**: Also interpretable as it provides coefficients for each feature, reflecting the impact on the prediction. However, it is not as intuitive to understand as the tree structure of a Decision Tree.

### Model Complexity
- **Decision Tree**: Potentially more complex, especially if deep trees are developed. This complexity can lead to overfitting, where the model performs exceptionally well on training data but fails to generalize to new data.
- **Logistic Regression**: Simpler and less prone to overfitting compared to complex Decision Trees. It has fewer parameters and is less likely to capture noise in the data.

### Model Generalizability
- **Decision Tree**: While the perfect accuracy score suggests excellent training data performance, there is a risk that this may not translate to new, unseen data due to overfitting.
- **Logistic Regression**: The slightly lower, yet still high, accuracy score may indicate a model that generalizes better. The logistic function used in this model smooths out predictions and can handle noise in the data better.

### Model Robustness
- **Decision Tree**: Can be sensitive to small changes in the data, leading to different splits that can drastically change the structure of the tree.
- **Logistic Regression**: More robust to slight variations in the data and typically provides a stable model structure.

### Final Recommendation for Model Deployment

After careful consideration of the above factors, we recommend the **Logistic Regression** model for deployment in the Global Happiness Predictor application. This recommendation is grounded in the model's balance of high accuracy with the benefits of simplicity, interpretability, robustness, and, most critically, generalizability to new data. While the Decision Tree model's perfect accuracy is notable, it raises concerns about overfitting, which could limit its performance on unseen data. 

In contrast, the Logistic Regression model's performance indicates a strong predictive power while suggesting it may be more adaptable to a broader context, which is essential for a tool designed for a diverse global user base.

As we progress, we will continue to monitor the Logistic Regression model's performance and will remain open to incorporating more complex models, such as ensemble methods, should they provide substantive improvements in performance without compromising the model's generalizability and interpretability.


## <a id="collaborators"></a>Collaborators 

- [Sunil Malhi](https://github.com/SunilMalhi)
- [Tafadzwa Fararira](https://github.com/BootcampCoderTF)
- [Yuk Hang Hui](https://github.com/alexyhHui)
- [Nida Ballinger-Chaudhary](https://github.com/NidaB-C)

