import requests
import schemas.schema as schema
from dotenv import dotenv_values
from jsonschema import validate

# CONSTANT for the test variables
NEW_YORK_COORD = {"lon": -74.006, "lat": 40.7143}
BROOKLYN_COORD = {"lon": -73.9496, "lat": 40.6501}
MOUNTAIN_VIEW_COORD = {"lon": -122.0832, "lat": 37.3894}
COUNTRY = "US"
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
GEOCODING_API_URL = "http://api.openweathermap.org/geo/1.0/zip"


def query_builder_with_api_key(input_dict):
    config = dotenv_values(".env")
    return {"appid": config["API_KEY"], **input_dict}


# Query the URL by the city name
def test_query_by_city_name():
    city = "New York"
    params = query_builder_with_api_key({"q": city})
    response = requests.get(url=WEATHER_API_URL, params=params)
    r_json = response.json()

    validate(instance=r_json, schema=schema.current_weather_data_api_schema)
    assert response.status_code == 200
    assert r_json["coord"] == NEW_YORK_COORD
    assert r_json["sys"]["country"] == COUNTRY
    assert r_json["name"] == city
    assert r_json["base"] == "stations"
    assert r_json["cod"] == 200
    assert r_json["timezone"] == -18000


def test_query_by_lat_and_long():
    city = "Brooklyn"
    params = query_builder_with_api_key(BROOKLYN_COORD)
    response = requests.get(url=WEATHER_API_URL, params=params)
    r_json = response.json()

    validate(instance=r_json, schema=schema.current_weather_data_api_schema)
    assert response.status_code == 200
    assert r_json["coord"] == BROOKLYN_COORD
    assert r_json["sys"]["country"] == COUNTRY
    assert r_json["name"] == city
    assert r_json["base"] == "stations"
    assert r_json["cod"] == 200
    assert r_json["timezone"] == -18000


def test_query_by_zip_code():
    city = "Mountain View"
    zipcode = 94040

    # get geocoding to verify city name
    zip_code_to_state_req_params = query_builder_with_api_key({"zip": zipcode})
    zip_code_to_state_response = requests.get(
        url=GEOCODING_API_URL, params=zip_code_to_state_req_params
    )
    zip_code_to_state_r_json = zip_code_to_state_response.json()
    validate(instance=zip_code_to_state_r_json, schema=schema.geo_coding_api_schema)
    assert zip_code_to_state_response.status_code == 200
    assert zip_code_to_state_r_json["zip"] == str(zipcode)
    assert zip_code_to_state_r_json["name"] == city

    # get current weather request/response
    current_weather_params = query_builder_with_api_key({"q": zipcode})
    current_weather_response = requests.get(
        url=WEATHER_API_URL, params=current_weather_params
    )
    current_weather_r_json = current_weather_response.json()
    validate(
        instance=current_weather_r_json, schema=schema.current_weather_data_api_schema
    )
    assert current_weather_response.status_code == 200
    assert current_weather_r_json["coord"] == MOUNTAIN_VIEW_COORD
    assert current_weather_r_json["sys"]["country"] == COUNTRY
    # validate if the name from current weather response match with geo coding match with zip
    assert current_weather_r_json["name"] == zip_code_to_state_r_json["name"]
    assert current_weather_r_json["base"] == "stations"
    assert current_weather_r_json["cod"] == 200
    assert current_weather_r_json["timezone"] == -28800
