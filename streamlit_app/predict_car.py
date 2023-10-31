import numpy as np 
import pandas as pd
import pickle
import streamlit as st


st.write("""
# Used Car Price Prediction App

This app only predicts the price of used car

Data obtained from 
""")

st.sidebar.header("User Input Parameters")

def user_input_features():
    year = st.sidebar.selectbox('Year', list(reversed(range(1900,2022))))
    manufacturer = st.sidebar.selectbox('Brands Alphabetically',('Acura', 'Alfa-Romeo', 
       'Aston-Martin', 'Audi', 'BMW', 'Buick',
       'Cadillac', 'Chevrolet', 'Chrysler', 'Datsun', 'Dodge', 'Ferrari',
       'Fiat', 'Ford', 'Gmc', 'Harley-Davidson', 'Honda', 'Hyundai',
       'Infiniti', 'Jaguar', 'Jeep', 'Kia', 'Land Rover', 'Lexus',
       'Lincoln', 'Mazda', 'Mercedes-Benz', 'Mercury', 'Mini',
       'Mitsubishi', 'Morgan', 'Nissan', 'Pontiac', 'Porsche', 'Ram',
       'Saturn', 'Subaru', 'Tesla', 'Toyota', 'Volkswagen',
       'Volvo'))
    condition = st.sidebar.selectbox('Condition',('Excellent', 'Fair', 'Good', 'Like New', 
                                                  'New', 'Salvage'))
    cylinders = st.sidebar.selectbox('Cylinders',('10 cylinders', '12 cylinders', '3 cylinders', 
                                                  '4 cylinders','5 cylinders', '6 cylinders', 
                                                  '8 cylinders', 'other'))
    fuel = st.sidebar.selectbox('Type of Fuel',('diesel', 'electric', 'gas', 'hybrid', 'other'))
    odometer = st.sidebar.slider('Odometer Number', 0, 10000000, 50000)
    title_status = st.sidebar.selectbox('Current Title Status of Car',('clean', 'lien', 
                                                                       'missing', 'parts only', 
                                                                       'rebuilt', 'salvage'))
    transmission = st.sidebar.selectbox('Type of Transmission',('automatic', 'manual', 'other'))
    drive = st.sidebar.selectbox('Type of car drive',('4wd','fwd','rwd'))
    size = st.sidebar.selectbox('Car Size',('Compact', 'Full-size', 'Mid-size', 'Sub-compact'))
    types = st.sidebar.selectbox('Type of Car',('SUV', 'sedan', 'truck', 'van', 'mini-van',
                                                'convertible', 'coupe', 'hatchback', 'offroad', 
                                                'bus','pickup', 'wagon', 'other'))
    paint_color = st.sidebar.selectbox('Car Color', ('black', 'blue', 'brown','custom'
                                                     ,'green','grey', 'orange','purple', 
                                                     'red', 'silver', 'white', 'yellow'))

    data = {'year': year,
            'manufacturer': manufacturer.lower(),
            'condition': condition.lower(),
            'cylinders': cylinders.lower(),
            'fuel': fuel.lower(),
            'odometer': odometer,
            'title_status': title_status.lower(),
            'transmission': transmission.lower(),
            'drive': drive.lower(),
            'size': size.lower(),
            'type': types,
            'paint_color': paint_color.lower()}
    features = pd.DataFrame(data, index=[0])
    return features
input_df = user_input_features()

car_df = pd.read_csv('df_model.csv')
car = car_df.drop(columns=['price'])
df = pd.concat([input_df,car],axis=0)

# encode = ['manufacturer','condition','cylinders','fuel','title_status',
#             'transmission','drive','size','type','paint_color','state']
# for col in encode:
#     dummy = pd.get_dummies(df[col], prefix=col)
#     df = pd.concat([df,dummy], axis=1)
#     del df[col]
# df = df[:1]
df_dummy = pd.get_dummies(df, columns=['manufacturer','condition','cylinders','fuel','title_status',
                                 'transmission','drive','size','type','paint_color','state'], 
                    dtype=float, drop_first=True)

df = df_dummy[:1]

with open('car_rf.pkl',"rb") as f:
    model = pickle.load(f)
    

# st.subheader("User Input features")
# st.write(df)
# st.write(pd.DataFrame(input_features, columns=['year','manufacturer','condition','cylinder',
#                                                'fuel','odometer','title_status','transmission',
#                                                'drive,size', 'types', 'paint_color']))
predicttion = model.predict(df)
st.subheader("Predicted Used Car Value")
st.write(f"${predicttion}")