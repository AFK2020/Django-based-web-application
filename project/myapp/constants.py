from enum import Enum

class UserRole(Enum):
    GOLD = "gold",
    SILVER= "silver",
    BRONZE = "bronze"

    @classmethod
    def get_roles(cls):
        return [
            (cls.GOLD, cls.GOLD.value),
            (cls.SILVER, cls.SILVER.value),
            (cls.BRONZE, cls.BRONZE.value),
        ]