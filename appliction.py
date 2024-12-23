from dataclasses import dataclass, field
from typing import List
from copy import deepcopy
from datetime import date

@dataclass(frozen=True)
class Address:
    street: str
    city: str
    zip_code: str

@dataclass(frozen=True)
class ImmutableEmployee:
    name: str
    id: str
    date_of_joining: date
    addresses: List[Address] = field(default_factory=list)

    def __post_init__(self):
        object.__setattr__(self, "addresses", deepcopy(self.addresses))

if __name__ == "__main__":
    address1 = Address(street="123 Main road", city="hyderabad", zip_code="500002")
    address2 = Address(street="14567 main road", city="kdd", zip_code="5000003")

    employee = ImmutableEmployee(
        name="ram",
        id="12345",
        date_of_joining=date(2025, 5, 15),
        addresses=[address1, address2]
    )

    print(employee)
