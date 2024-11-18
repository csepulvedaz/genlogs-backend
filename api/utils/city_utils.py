def extract_city_name(full_location: str) -> str:
    return full_location.split(",")[0].strip()