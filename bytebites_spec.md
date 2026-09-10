## Client Feature Request

We need to build the backend logic for the ByteBites app. The system needs to manage our customers, tracking their names and their past purchase history so the system can verify they are real users.

These customers need to browse specific food items (like a "Spicy Burger" or "Large Soda"), so we must track the name, price, category, and popularity rating for every item we sell.

We also need a way to manage the full collection of items — a digital list that holds all items and lets us filter by category such as "Drinks" or "Desserts".

Finally, when a user picks items, we need to group them into a single transaction. This transaction object should store the selected items and compute the total cost.

## Candidate Classes

1. **Customer** – Represents a user of the app. Stores their name and past purchase history, used to verify they are a real/returning user.
2. **FoodItem** – Represents a single item sold by ByteBites (e.g., "Spicy Burger"). Stores its name, price, category, and popularity rating.
3. **Menu** – Represents the full collection of available FoodItems. Allows filtering by category (e.g., "Drinks", "Desserts").
4. **Order** – Represents a single transaction. Stores the FoodItems a customer selected and computes the total cost.