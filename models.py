from __future__ import annotations


class FoodItem:
    """A single sellable item (e.g. "Spicy Burger", "Large Soda")."""

    def __init__(self, name: str, price: float, category: str, popularity_rating: float) -> None:
        self._name = name
        self._price = price
        self._category = category
        self._popularity_rating = popularity_rating


class Menu:
    """The digital collection of all available FoodItems."""

    def __init__(self) -> None:
        self._items: list[FoodItem] = []


class Customer:
    """A user of the app; tracks their name and past purchase history."""

    def __init__(self, name: str) -> None:
        self._name = name
        self._purchase_history: list[Order] = []


class Order:
    """A single transaction grouping the FoodItems a Customer selected."""

    def __init__(self, customer: Customer) -> None:
        self._customer = customer
        self._selected_items: list[FoodItem] = []
