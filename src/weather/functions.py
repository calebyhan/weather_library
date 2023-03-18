import requests

from weather import weather_api_key

def __check_api_key():
    if weather_api_key == "":
        raise ValueError("Empty API Key.")


def current(q, aqi="no", lang=-1):
    __check_api_key()
    params = {
        "key": weather_api_key,
        "q": q,
        "aqi": aqi
    }
    if lang != -1:
        params.update({"lang": lang})
    return requests.get("https://api.weatherapi.com/v1/current.json?", params=params).json()


def forecast(q, days=3, alerts="no", aqi="no", lang=-1):
    __check_api_key()
    params = {
        "key": weather_api_key,
        "q": q,
        "days": days,
        "alerts": alerts,
        "aqi": aqi
    }
    if lang != -1:
        params.update({"lang": lang})
    return requests.get("https://api.weatherapi.com/v1/forecast.json?", params=params).json()


def history(q, dt=-1, lang=-1):
    __check_api_key()
    params = {
        "key": weather_api_key,
        "q": q,
    }
    if dt != -1:
        params.update({"dt": dt})
    if lang != -1:
        params.update({"lang": lang})
    return requests.get("https://api.weatherapi.com/v1/history.json?", params=params).json()


def future(q, dt=-1, lang=-1):
    __check_api_key()
    params = {
        "key": weather_api_key,
        "q": q,
    }
    if dt != -1:
        params.update({"dt": dt})
    if lang != -1:
        params.update({"lang": lang})
    return requests.get("https://api.weatherapi.com/v1/future.json?", params=params).json()


def search(q, lang=-1):
    __check_api_key()
    params = {
        "key": weather_api_key,
        "q": q,
    }
    if lang != -1:
        params.update({"lang": lang})
    return requests.get("https://api.weatherapi.com/v1/search.json?", params=params).json()


def ip(q, lang=-1):
    __check_api_key()
    params = {
        "key": weather_api_key,
        "q": q,
    }
    if lang != -1:
        params.update({"lang": lang})
    return requests.get("https://api.weatherapi.com/v1/ip.json?", params=params).json()


def astro(q, dt=-1, lang=-1):
    __check_api_key()
    params = {
        "key": weather_api_key,
        "q": q,
    }
    if dt != -1:
        params.update({"dt": dt})
    if lang != -1:
        params.update({"lang": lang})
    return requests.get("https://api.weatherapi.com/v1/astronomy.json?", params=params).json()


def sports(q, lang=-1):
    __check_api_key()
    params = {
        "key": weather_api_key,
        "q": q,
    }
    if lang != -1:
        params.update({"lang": lang})
    return requests.get("https://api.weatherapi.com/v1/sports.json?", params=params).json()


def timezone(q, lang=-1):
    __check_api_key()
    params = {
        "key": weather_api_key,
        "q": q,
    }
    if lang != -1:
        params.update({"lang": lang})
    return requests.get("https://api.weatherapi.com/v1/timezone.json?", params=params).json()