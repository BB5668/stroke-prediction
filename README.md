FOLDER STRUCTURE
================

```
/project-folder
│── /executive_summary         # Contains PDF of Stroke Prediction using Patient Data
│── /ppt                       # Contains presentation
│── /code                      # Contains Python notebooks and HTML files
│── README.txt                 # This document

The code folder contains 2 notebooks : Stroke_Predict_Model_Comparison and Stroke_Predict_Random_Forest

This file will help the user to navigate and run the notebooks for the Stroke Prediction outputs

*****************************************************************************************************************
1st Notebook : Stroke_Predict_Model_Comparison

*****************************************************************************************************************
REQUIREMENTS:

Make sure you have the following installed:
- Python 3.7 or higher
- Jupyter Notebook or JupyterLab
- Required Python libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn

RUNNING THE APPLICATION :

1. Create a folder 'Project' in the current working directory and Copy the dataset 'healthcare-dataset-stroke-data.csv'
or update the file path accordingly in the notebook
1. **Open Terminal or Anaconda Prompt**
2. **Launch Jupyter Notebook**
Command:
jupyter notebook
3. **Navigate to the notebook location**  
In the Jupyter interface, browse to and open `Stroke_Predict_Model_Comparison.ipynb`.
4. **Run the Notebook Cells**  
Run each cell in sequence using `Shift + Enter` to execute and proceed.


📌 Notes
- Make sure the dataset used in the notebook is available in the same directory or update the file path accordingly.
- Check kernel and restart if you face any dependency issues.

*****************************************************************************************************************
2nd Notebook : Stroke_Predict_Model_Comparison

*****************************************************************************************************************

RUNNING THE APPLICATION :

1. **Open Terminal or Anaconda Prompt**
2. **Launch Jupyter Notebook**
Command:
jupyter notebook
3. **Navigate to the notebook location**  
In the Jupyter interface, browse to and open `Stroke_Predict_Random_Forest.ipynb`.
4. **Run the Notebook Cells**  
Run each cell in sequence using `Shift + Enter` to execute and proceed.
5. Verify whether the current working directory contains the file model-new.pkl created at the current timestamp

Python app has to be run from the root directory of the app (code that holds the starting point of the app). 
- The folder that contains this README file also contains the Python file/s to start the app/s. 
- From the root directory, open the Command Prompt (or Terminal). To do that in Windows OS, you can click on the address bar at the root directory, type "cmd" and hit Enter. 
- Another way to do the same as above would be to open Command Prompt (or Terminal), and navigate to the root directory via typing command/s to change diretory.

1.
To Run (in terminal / command prompt):-
python stroke_prediction_dash.py

2.
To See Output:- (in any web browser):- 
http://127.0.0.1:8050/

3. Enter values for all the stroke parameters on the screen and click 'Submit' to verify the result.

4.
To Exit (in terminal / command prompt):-
Press Ctrl+C
