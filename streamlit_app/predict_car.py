import numpy as np 
import pandas as pd
import pickle
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

st.write("""
# Used Car Price Prediction App

This app only predicts the price of used car

Data obtained from Kaggle
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
    odometer = st.sidebar.number_input('Insert a number', min_value=0, max_value=1000000)
    title_status = st.sidebar.selectbox('Current Title Status of Car',('clean', 'lien', 
                                                                       'missing', 'parts only', 
                                                                       'rebuilt', 'salvage'))
    transmission = st.sidebar.selectbox('Type of Transmission',('automatic', 'manual', 'other'))
    drive = st.sidebar.selectbox('Type of car drive',('4WD','FWD','RWD'))
    #drive = '4wd'
    size = st.sidebar.selectbox('Car Size',('Compact', 'Full-size', 'Mid-size', 'Sub-compact'))
    types = st.sidebar.selectbox('Type of Car',('SUV', 'Sedan', 'Truck', 'Van', 'Mini-van',
                                                'Convertible', 'Coupe', 'Hatchback', 'Offroad', 
                                                'Bus','Pickup', 'Wagon', 'Other'))
    paint_color = st.sidebar.selectbox('Car Color', ('Black', 'Blue', 'Brown','Custom'
                                                     ,'Green','Grey', 'Orange','Purple', 
                                                     'Red', 'Silver', 'White', 'Yellow'))
    state = st.sidebar.selectbox('State', ('AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
       'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
       'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
       'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
       'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'))

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
            'type': types.lower(),
            'paint_color': paint_color.lower(),
            'state': state.lower()}
    features = pd.DataFrame(data, index=[0])
    return features
input_df = user_input_features()


with open('etr_pipe.pkl',"rb") as f:
    model = pickle.load(f)
    
predicttion = model.predict(input_df)
st.subheader("Predicted Used Car Value")
st.write(f"${predicttion}")

# Recommendation system

st.write('What used car is ')

df = pd.read_csv('df_model.csv')
df.head()

def brand_recommender(manufacturer,year,car_type,price_range):
    data = df.loc[(df['year']==year) & (df['type']==car_type)
                 & ((df['price']>=price_range[0]) & (df['price']<=price_range[1]))]
    data.reset_index(level =0, inplace = True)
    
    indices = pd.Series(data.index, index=data['manufacturer'])
    
    # Converting the car manufacturer into vectors unigrams and bigrams
    cvec = CountVectorizer(ngram_range=(1, 2), stop_words='english')
    cvec_matrix = cvec.fit_transform(data['manufacturer'])
    
    # Apply Cosine Similarity
    cs = cosine_similarity(cvec_matrix)
    
    # Sort by manufacturer and get the top 6 car with highest similiraty score
    score = sorted(list(enumerate(cs[indices[manufacturer]])), reverse=True)[0:6]

    # car indicies
    car_indices = [i[0] for i in score]
   
    # Top 6 car recommendations
    car_recommend = data[['price','manufacturer','type','year','condition','fuel','title_status',
                'transmission','paint_color']].iloc[car_indices]
    return car_recommend

def user_input():
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


# st.write(rec)

# import streamlit as st

# # Create a Streamlit app
# st.title("Range of Numbers Input")

# # Define the input range
# min_value = st.number_input("Min Value", value=0)
# max_value = st.number_input("Max Value", value=100)

# # Display the selected range
# st.write(f"You selected a range from {min_value} to {max_value}")

st.balloons()