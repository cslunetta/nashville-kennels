from animals import request


CUSTOMERS = [
    {
        "id": 1,
        "name": "Emily"
    },
    {
        "id": 2,
        "name": "Deanna"
    }
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer