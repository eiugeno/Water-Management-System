import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from datetime import datetime, timedelta
import ee  # Ensure you have authenticated GEE
import statsmodels.api as sm
from google.oauth2 import service_account

# Path to your service account JSON key file
service_account_key = r'C:\Users\serafino\Desktop\Water Management System\ee-eugenioserafino01-dca7dda5348b.json'

# Define the required OAuth scope for Earth Engine
scopes = ['https://www.googleapis.com/auth/earthengine']

# Create credentials with the specified scope
credentials = service_account.Credentials.from_service_account_file(
    service_account_key, scopes=scopes
)

# Initialize Google Earth Engine
ee.Initialize(credentials=credentials)
# Helper function to retrieve soil moisture data in quarterly chunks

def get_soil_moisture_data(lat, lon, days_before_today, collection_id='NASA/SMAP/SPL4SMGP/007', band_name='sm_rootzone'):
    """
    Retrieve soil moisture data in quarterly intervals for a specified number of days before today.
    
    Parameters:
    lat (float): Latitude of the location.
    lon (float): Longitude of the location.
    days_before_today (int): Number of days before today for which to retrieve data.
    collection_id (str): Earth Engine Collection ID for soil moisture data.
    band_name (str): Band name for soil moisture data.
    
    Returns:
    pd.DataFrame: DataFrame containing dates and soil moisture values.
    """
    # Define the point geometry
    point = ee.Geometry.Point([lon, lat])
    
    # Calculate start and end dates
    end_date = ee.Date(datetime.datetime.now().strftime('%Y-%m-%d'))
    start_date = end_date.advance(-days_before_today, 'day')

    results = []

    # Iterate over each quarter in the specified range
    current_date = start_date
    while current_date.difference(end_date, 'month').getInfo() < 0:
        next_date = current_date.advance(3, 'month')  # Advance by a quarter (3 months)

        # Filter dataset for the current quarter
        dataset = ee.ImageCollection(collection_id) \
                    .filterDate(current_date, next_date) \
                    .select(band_name)

        # Calculate mean soil moisture over each quarter
        quarterly_data = dataset.map(lambda image: ee.Feature(
            point,
            {
                'date': image.date().format('YYYY-MM-dd'),
                'soil_moisture': image.reduceRegion(
                    reducer=ee.Reducer.mean(),
                    geometry=point,
                    scale=1000
                ).get(band_name)
            }
        ))

        # Fetch data and handle missing values
        try:
            quarterly_data_list = quarterly_data.getInfo()['features']
            results.extend([{
                'date': feature['properties']['date'],
                'soil_moisture': feature['properties'].get('soil_moisture', None)
            } for feature in quarterly_data_list])
        except Exception as e:
            print(f"An error occurred while retrieving data for {current_date.format('YYYY-MM').getInfo()}: {e}")

        # Move to the next quarter
        current_date = next_date

    # Convert to DataFrame for consistency
    soil_moisture_df = pd.DataFrame(results)
    soil_moisture_df['date'] = pd.to_datetime(soil_moisture_df['date'])
    soil_moisture_df.set_index('date', inplace=True)

    return soil_moisture_df

def get_weather_data(lat, lon, days_before_today):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days_before_today)
    start_date_str = start_date.strftime('%Y%m%d')
    end_date_str = end_date.strftime('%Y%m%d')

    parameters = "T2M,PRECTOTCORR,ALLSKY_SFC_SW_DWN,RH2M,WS10M,PS"
    nasa_power_url = (
        f"https://power.larc.nasa.gov/api/temporal/daily/point?parameters={parameters}"
        f"&community=AG&longitude={lon}&latitude={lat}"
        f"&start={start_date_str}&end={end_date_str}&format=JSON"
    )

    response = requests.get(nasa_power_url)
    weather_data = response.json()["properties"]["parameter"]

    dates = list(weather_data["T2M"].keys())
    temperature = list(weather_data["T2M"].values())
    precipitation = list(weather_data["PRECTOTCORR"].values())
    irradiation = list(weather_data["ALLSKY_SFC_SW_DWN"].values())
    humidity = list(weather_data["RH2M"].values())
    wind_speed = list(weather_data["WS10M"].values())
    pressure = list(weather_data["PS"].values())

    weather_df = pd.DataFrame({
        'date': pd.to_datetime(dates, format='%Y%m%d'),
        'temperature': temperature,
        'precipitation': precipitation,
        'irradiation': irradiation,
        'humidity': humidity,
        'wind_speed': wind_speed,
        'pressure': pressure
    })
    return weather_df

def get_ndvi_data(lat, lon, days_before_today):
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=days_before_today)).strftime('%Y-%m-%d')
    point = ee.Geometry.Point([lon, lat])

    ndvi_collection = ee.ImageCollection('MODIS/061/MOD13A1').filter(ee.Filter.date(start_date, end_date)).select('NDVI')
    def extract_ndvi(image):
        mean_ndvi = image.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=point,
            scale=500
        ).get('NDVI')
        return ee.Feature(None, {
            'date': image.date().format('YYYY-MM-dd'),
            'NDVI': mean_ndvi
        })
    ndvi_data = ndvi_collection.map(extract_ndvi)
    ndvi_list = ndvi_data.getInfo()['features']

    ndvi_dates = [feature['properties']['date'] for feature in ndvi_list]
    ndvi_values = [feature['properties']['NDVI'] for feature in ndvi_list]

    return pd.DataFrame({
        'date': pd.to_datetime(ndvi_dates),
        'ndvi': ndvi_values
    })

def get_lst_data(lat, lon, days_before_today):
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=days_before_today)).strftime('%Y-%m-%d')
    point = ee.Geometry.Point([lon, lat])

    lst_collection = ee.ImageCollection('MODIS/061/MOD11A1').filter(ee.Filter.date(start_date, end_date)).select('LST_Day_1km')
    def extract_lst(image):
        mean_lst = image.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=point,
            scale=500
        ).get('LST_Day_1km')
        return ee.Feature(None, {
            'date': image.date().format('YYYY-MM-dd'),
            'LST_Day_1km': mean_lst
        })
    lst_data = lst_collection.map(extract_lst)
    lst_list = lst_data.getInfo()['features']

    lst_dates = [feature['properties']['date'] for feature in lst_list]
    lst_values = [feature['properties'].get('LST_Day_1km', None) for feature in lst_list]

    lst_df = pd.DataFrame({
        'date': pd.to_datetime(lst_dates),
        'lst': lst_values
    })
    lst_df['lst'] = lst_df['lst'].interpolate(method='linear', limit_direction='both')
    return lst_df

