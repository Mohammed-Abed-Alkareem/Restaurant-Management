# E-Menu for Restaurants

E-Menu is a web-based application designed to enhance the dining experience at restaurants. It offers two interfaces: one for customers and another for restaurant management.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
  - [Customer Interface](#customer-interface)
  - [Restaurant Management Interface](#restaurant-management-interface)
- [File Structure](#file-structure)
- [ER Diagram](#er-diagram)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Customer Interface:**
  - Scan QR code to access the menu.
  - Enter table code and sign in.
  - View and order from the menu.
  - Choose payment options: VISA or cash.
  - Rate the order.

- **Restaurant Management Interface:**
  - Log in with a username and password.
  - Managing the menu
  - Tables
  - Employees
  - View order
  - Statistics.

## Usage

### Customer Interface

1. **Access Home Page:**
   - Scan the QR code provided at the restaurant table.
   - Enter the table code.

2. **Sign Up / Log In:**
   - New users can sign up.
   - Existing users can log in using their phone number.

3. **Browse Menu:**
   - View categories and items.
   - Add items to the cart.

4. **Checkout:**
   - Choose payment method (VISA or cash).
   - Confirm the order.

5. **Rate the Order:**
   - Provide feedback on the food and service.

### Restaurant Management Interface

1. **Log In:**
   - Access the management interface with a username and password.

2. **Modify Menu:**
   - Add, update, or delete menu items.
  
3. **Modify Tables:**
   - Add, update, or delete tables.
  
4. **Modify Employees Info:**
   - Add, update, or delete employees info.

5. **View Statistics:**
   - Analyze order data and performance.

## File Structure
```plaintext
.
└── ProjectFiles/
    └── e_menu/
        ├── __init__.py
        ├── e_menu_app.py
        ├── customers/
        │   ├── __init__.py
        │   ├── customers.py
        │── models/
        ├── employees/
        │   ├── __init__.py
        │   └── employees.py
        ├── static/
        │   ├── css/
        │   ├── img/
        │   └── js/
        ├── templates/
        │   ├── customers/
        │   ├── employees/
        │   ├── 404.html
        │   ├── home_page.html
        │   └── base.html
        └── utils/
            ├── csvFiles/
            ├── queries/
            ├── __init__.py
            ├── db.py
            └── read_initial_data.py

```

## ER Diagram
![ER Diagram](ER_diagram.png)

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.

## License

This project is licensed under a custom proprietary license. Permission is required from the repository owner to use this software. For more details, see the [LICENSE](./LICENSE.txt) file.




