import numpy as np 
import pandas as pd
import pickle
import streamlit as st

st.write("""
# Used Car Price Recommendation 

List of Recommender car
""")


st.sidebar.header("User Input Parameters")

df= pd.read_csv('df_model.csv') 

df['year'] = df['year'].astype(str).str.replace(".0","",regex=False)

def rec_user_input():
    manufacturer = st.sidebar.selectbox('Brands Alphabetically',('Acura', 'Alfa-Romeo', 
       'Aston-Martin', 'Audi', 'BMW', 'Buick',
       'Cadillac', 'Chevrolet', 'Chrysler', 'Datsun', 'Dodge', 'Ferrari',
       'Fiat', 'Ford', 'Gmc', 'Harley-Davidson', 'Honda', 'Hyundai',
       'Infiniti', 'Jaguar', 'Jeep', 'Kia', 'Land Rover', 'Lexus',
       'Lincoln', 'Mazda', 'Mercedes-Benz', 'Mercury', 'Mini',
       'Mitsubishi', 'Morgan', 'Nissan', 'Pontiac', 'Porsche', 'Ram',
       'Saturn', 'Subaru', 'Tesla', 'Toyota', 'Volkswagen',
       'Volvo'))
    year = st.sidebar.selectbox('Year', list(reversed(range(1900,2022))))
    types = st.sidebar.selectbox('Type of Car',('SUV', 'sedan', 'truck', 'van', 'mini-van',
                                                'convertible', 'coupe', 'hatchback', 'offroad', 
                                                'bus','pickup', 'wagon', 'other'))
    st.sidebar.write("Insert range of price")
    min_price = st.sidebar.number_input('Minimum of Price')
    max_price = st.sidebar.number_input('Maximum of Price')
    number_result = st.sidebar.selectbox("Number of Car", list(reversed(range(5,20))))

    data = {'manufacturer': manufacturer.title(),
            'year': year,
            "car_type": types,
            "min_price": min_price,
            "max_price": max_price,
            "number_result": number_result}

    
    return data
    

input_feature = rec_user_input()


# st.write(input_feature['manufacturer'],input_feature['year'],input_feature['car_type'],
#         input_feature['min_price'], input_feature['max_price'])

# #st.write

# #recommender = brand_recommender(input_feature['manufacturer'], input_feature['year'],input_feature['car_type'],
#                                 #input_feature['min_price'], input_feature['max_price'])

# #recommender = brand_recommender('acura',input_feature['year'] , input_feature['car_type'] ,input_feature['min_price'], input_feature['max_price'])
# #st.write(recommender)

# recommender = brand_recommender(input_feature['manufacturer'],input_feature['year'] , input_feature['car_type'],
#                                 input_feature['min_price'], input_feature['max_price'] )
# st.write(recommender)
# #st.balloons()


def price_recommender(car_type, min_price, max_price, number_result):
    data = df.loc[(df['type']==car_type) & (df['price']>=min_price) & (df['price']<=max_price)]
    data.reset_index(level =0, inplace = True)
   
    # Top 6 car recommendations
    car_recommend = data[['price','manufacturer','type','year','condition','fuel','title_status',
                'transmission','paint_color']].iloc[:number_result,:]

    return car_recommend

st.write(price_recommender(input_feature['car_type'], input_feature['min_price'], 
                           input_feature['max_price'], input_feature['number_result']))

