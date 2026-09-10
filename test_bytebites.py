from models import Customer, FoodItem, Menu, Order


def test_order_total_cost_sums_selected_items():
    """An order's total cost is the sum of the prices of its selected items."""
    burger = FoodItem("Spicy Burger", 8.99, "Entrees", 4.5)
    soda = FoodItem("Large Soda", 2.49, "Drinks", 3.8)
    order = Order(Customer("Dakarri"))

    order.add_item(burger)
    order.add_item(soda)

    assert order.compute_total_cost() == 8.99 + 2.49


def test_order_total_cost_is_zero_with_no_items():
    """An order with no selected items has a total cost of zero."""
    order = Order(Customer("Dakarri"))

    assert order.compute_total_cost() == 0


def test_menu_filter_by_category_returns_only_matching_items():
    """filter_by_category returns only the items in the requested category."""
    burger = FoodItem("Spicy Burger", 8.99, "Entrees", 4.5)
    soda = FoodItem("Large Soda", 2.49, "Drinks", 3.8)
    cake = FoodItem("Chocolate Cake", 5.25, "Desserts", 4.9)
    menu = Menu()
    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(cake)

    desserts = menu.filter_by_category("Desserts")

    assert desserts == [cake]


def test_menu_filter_by_category_returns_empty_list_when_no_matches():
    """filter_by_category returns an empty list when no items match the category."""
    menu = Menu()
    menu.add_item(FoodItem("Spicy Burger", 8.99, "Entrees", 4.5))

    assert menu.filter_by_category("Desserts") == []
