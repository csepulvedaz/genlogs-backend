import logging
from typing import List

# Schemas
from api.schemas.carrier_schemas import Carrier

logger = logging.getLogger("api")

carriers_data = {
    ("New York", "Washington DC"): [
        {"name": "Knight-Swift Transport Services", "trucks_per_day": 10},
        {"name": "J.B. Hunt Transport Services Inc", "trucks_per_day": 7},
        {"name": "YRC Worldwide", "trucks_per_day": 5},
    ],
    ("San Francisco", "Los Angeles"): [
        {"name": "XPO Logistics", "trucks_per_day": 9},
        {"name": "Schneider", "trucks_per_day": 6},
        {"name": "Landstar Systems", "trucks_per_day": 2},
    ],
    "default": [
        {"name": "UPS Inc.", "trucks_per_day": 11},
        {"name": "FedEx Corp", "trucks_per_day": 9},
    ],
}


def get_top_carriers_by_direction(from_city: str, to_city: str) -> List[Carrier]:
    logger.info(f"Getting top carriers from {from_city} to {to_city}")
    key = (from_city, to_city)
    carriers = carriers_data.get(key, carriers_data["default"])
    return [Carrier(**carrier) for carrier in carriers]