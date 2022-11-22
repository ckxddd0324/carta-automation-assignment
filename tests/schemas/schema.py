current_weather_data_api_schema = {
    "type": "object",
    "properties": {
        "coord": {
            "type": "object",
            "properties": {"lon": {"type": "number"}, "lat": {"type": "number"}},
        },
        "weather": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "number"},
                    "main": {"type": "string"},
                    "description": {"type": "string"},
                    "icon": {"type": "string"},
                },
            },
            "minItems": 1,
        },
        "base": {"type": "string"},
        "main": {
            "type": "object",
            "properties": {
                "temp": {"type": "number"},
                "feels_like": {"type": "number"},
                "temp_min": {"type": "number"},
                "temp_max": {"type": "number"},
                "pressure": {"type": "number"},
                "humidity": {"type": "number"},
            },
        },
        "visibility": {"type": "number"},
        "wind": {
            "type": "object",
            "properties": {
                "speed": {"type": "number"},
                "deg": {"type": "number"},
                "gust": {"type": "number"},
            },
        },
        "clouds": {
            "type": "object",
            "properties": {
                "all": {"type": "number"},
            },
        },
        "dt": {"type": "number"},
        "sys": {
            "type": "object",
            "properties": {
                "type": {"type": "number"},
                "id": {"type": "number"},
                "country": {"type": "string"},
                "sunrise": {"type": "number"},
                "sunset": {"type": "number"},
            },
        },
        "timezone": {"type": "number"},
        "id": {"type": "number"},
        "name": {"type": "string"},
        "cod": {"type": "number"},
    },
    "required": ["coord", "base", "id", "name", "cod", "weather"],
    "additionalProperties": False,
}

geo_coding_api_schema = {
    "type": "object",
    "properties": {
        "zip": {"type": "string"},
        "name": {"type": "string"},
        "lat": {"type": "number"},
        "lon": {"type": "number"},
        "country": {"type": "string"},
    },
    "required": ["zip", "name", "country"],
    "additionalProperties": False,
}
