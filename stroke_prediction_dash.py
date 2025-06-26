import dash
from dash import dcc, html, Input, Output
import joblib
import numpy as np
import pandas as pd
import plotly.express as px

# Load trained model
model = joblib.load("model-new.pkl")


# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Stroke Risk Prediction", style={'textAlign': 'center'}),
    
    html.Label("Gender"),
    dcc.Input(id='gender',type='number', placeholder='Enter Gender ( 0 = Female, 1 = Male)'),
    html.Br(),
    html.Br(),
   
    html.Label("Age:  "),
    dcc.Input(id='age', type='number', placeholder='Enter age'),
    html.Br(),
    html.Br(),

    html.Label("Hypertension"),
    dcc.Input(id='hypertension', type='number', placeholder='Enter Hypertension ( 0 = No, 1 = Yes)'),
    html.Br(),
    html.Br(),
    

    html.Label("HeartDisease"),
    dcc.Input(id='heart_disease',type='number', placeholder='Enter Heart Disease ( 0 = No, 1 = Yes)'),
    html.Br(),
    html.Br(),
        

    html.Label("Ever Married ?"),
    dcc.Input(id='ever_married',type='number', placeholder='Enter Married or Not ( 0 = No, 1 = Yes)'),
    html.Br(),
    html.Br(),   

    html.Label("Work Type:"),
    dcc.Input(id='work_type',type='number', placeholder='Enter Work Type ( 2 = Private, 3 = Self Employed)'),
    html.Br(),
    html.Br(), 

    html.Label("Residence Type"),
    dcc.Input(id='Residence_type',type='number', placeholder='Enter Residence Type ( 0 = Rural, 1 = Urban)'),
    html.Br(),
    html.Br(), 

    html.Label("Glucose Level:   "),
    dcc.Input(id='avg_glucose_level', type='number', placeholder='Enter glucose level'),
    html.Br(),
    html.Br(),
    
    html.Label("BMI:   "),
    dcc.Input(id='bmi', type='number', placeholder='Enter BMI'),
    html.Br(),
    html.Br(),
    
    html.Label("Smoking Status:"),
    dcc.Input(id='smoking_status',type='number', placeholder='Enter Smoking Status ( 1 = formerly, 2 = never, 3 = smokes)'),
    html.Br(),
    html.Br(),

    
    html.Button("Predict", id='predict-button', n_clicks=0),
    
    html.Div(id='prediction-output', style={'fontSize': 20, 'marginTop': 20, 'textAlign': 'center'})
])

@app.callback(
    Output('prediction-output', 'children'),
    [Input('predict-button', 'n_clicks')],
    [dash.State('gender', 'value'),
     dash.State('age', 'value'),
     dash.State('hypertension', 'value'),
     dash.State('heart_disease', 'value'),
     dash.State('ever_married', 'value'),
     dash.State('work_type', 'value'),
     dash.State('Residence_type', 'value'),
     dash.State('avg_glucose_level', 'value'),
     dash.State('bmi', 'value'),
     dash.State('smoking_status', 'value'),]
)
def predict_stroke(n_clicks, gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status):
    if n_clicks > 0: 

        try:

            # Prepare input data
            input_data = np.array([[gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status]])

            # Print all elements
            print("All elements in input_data:")
            for i, val in enumerate(input_data[0]):
                print(f"Feature {i+1}: {val}")
        
            # Make prediction
            prediction = model.predict(input_data)[0]  # 1 = High Risk, 0 = Low Risk
            probability = model.predict_proba(input_data)[0][1]
        
            result_text = "High Stroke Risk" if prediction == 1 else "Low Stroke Risk"
            color = "red" if prediction == 1 else "green"

        
        except Exception as e:
            return html.Div(f"Error in prediction: {e}", style={'color': 'red'})
    return ""
    

if __name__ == '__main__':
    app.run_server(debug=True)
