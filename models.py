from __future__ import annotations


class FoodItem:
    """A single sellable item (e.g. "Spicy Burger", "Large Soda")."""

    def __init__(self, name: str, price: float, category: str, popularity_rating: float) -> None:
        self._name = name
        self._price = price
        self._category = category
        self._popularity_rating = popularity_rating

    def get_name(self) -> str:
        """Return this item's name."""
        return self._name

    def get_price(self) -> float:
        """Return this item's price."""
        return self._price

    def get_category(self) -> str:
        """Return this item's category (e.g. "Drinks", "Desserts")."""
        return self._category

    def get_popularity_rating(self) -> float:
        """Return this item's popularity rating."""
        return self._popularity_rating


class Menu:
    """The digital collection of all available FoodItems."""

    def __init__(self) -> None:
        self._items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Add a FoodItem to the menu."""
        self._items.append(item)

    def remove_item(self, item: FoodItem) -> None:
        """Remove a FoodItem from the menu, if it is present."""
        if item in self._items:
            self._items.remove(item)

    def filter_by_category(self, category: str) -> list[FoodItem]:
        """Return every menu item whose category matches the given category."""
        return [item for item in self._items if item.get_category() == category]

    def get_all_items(self) -> list[FoodItem]:
        """Return every item currently on the menu."""
        return self._items


class Customer:
    """A user of the app; tracks their name and past purchase history."""

    def __init__(self, name: str) -> None:
        self._name = name
        self._purchase_history: list[Order] = []

    def get_name(self) -> str:
        """Return this customer's name."""
        return self._name

    def get_purchase_history(self) -> list[Order]:
        """Return this customer's past orders."""
        return self._purchase_history

    def add_to_purchase_history(self, order: Order) -> None:
        """Record a completed order in this customer's purchase history."""
        self._purchase_history.append(order)


class Order:
    """A single transaction grouping the FoodItems a Customer selected."""

    def __init__(self, customer: Customer) -> None:
        self._customer = customer
        self._selected_items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Add a FoodItem to this order's selected items."""
        self._selected_items.append(item)

    def get_selected_items(self) -> list[FoodItem]:
        """Return the FoodItems selected for this order."""
        return self._selected_items

    def compute_total_cost(self) -> float:
        """Return the sum of the prices of every selected item."""
        return sum(item.get_price() for item in self._selected_items)
