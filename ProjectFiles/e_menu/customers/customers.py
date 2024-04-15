from flask import render_template, request, url_for, redirect, session, flash, jsonify

from . import customers  # Import the blueprint from the package
from ProjectFiles.e_menu.models.customers_model import *
from ProjectFiles.e_menu.models.menuItems_model import *
from ProjectFiles.e_menu.models.tables_model import *
from ProjectFiles.e_menu.models.payment_methods_model import *


@customers.route('/', methods=['POST', 'GET'])
def home_page():
    if 'table' in session:
        session.pop('table', None)

    if 'customer' in session:
        session.pop('customer', None)

    if 'cart' in session:
        session.pop('cart', None)

    if request.method == 'POST':
        table_code = request.form['tbl_code']

        table = Table.get(code=table_code)

        if table is not None:
            session["table"] = table.to_dict()
            session.modified = True
            return redirect(url_for('customers.sign_page'))

        else:
            flash("Table Code is Incorrect!", "danger")

    return render_template("customers/home_page.html")


@customers.route('/sign')
def sign_page():
    if 'table' in session and session['table'] is not None:
        return render_template("customers/sign_page.html")

    else:
        flash("Please Enter table code first", "danger")
        return redirect(url_for('customers.home_page'))


@customers.route('/sign/sign_up', methods=['POST', 'GET'])
def sign_up():
    if 'table' not in session or session['table'] is None:
        flash("Please Enter table code first", "danger")
        return redirect(url_for('customers.home_page'))

    if request.method == 'POST':
        customer_name = request.form['name']
        customer_phone = request.form['phone']

        print(customer_name, customer_phone)

        check = Customer.insert(Customer(customer_name, customer_phone))

        # check insert_customer(customer_name, customer_phone)
        if check:
            flash("Added Successfully", "success")
            return redirect(url_for('customers.log_in'))

        else:
            flash("Cannot be Added! already registered!", "danger")

    return render_template("customers/sign_up.html")


@customers.route('/sign/log_in', methods=['POST', 'GET'])
def log_in():
    if 'table' not in session or session['table'] is None:
        flash("Please Enter table code first", "danger")
        return redirect(url_for('customers.home_page'))

    if request.method == 'POST':

        if 'customer' in session:
            session.pop('customer', None)

        user_phone = request.form['phone']

        print(user_phone)
        customer = Customer.get_by_phone(phone_number=user_phone)

        if customer is not None:
            print('not non')
            session["customer"] = customer.to_dict()

            session.modified = True

            return redirect(url_for('customers.categories'))

        else:
            flash("Sorry, phone number does not exists", "danger")

    return render_template("customers/log_in.html")


@customers.route('/categories')
def categories():
    if 'table' not in session or session['table'] is None:
        flash("Please Enter table code first", "danger")
        return redirect(url_for('customers.home_page'))

    if 'customer' not in session or session['customer'] is None:
        flash("Please Login first", "danger")
        return redirect(url_for('customers.sign_page'))

    items_categories = MenuItems.get_categories()
    customer = Customer.from_dict(session['customer'])
    return render_template("customers/categories.html", items_categories=items_categories, user_name=customer.name)


@customers.route('/categories/<category>')
def category_items(category):
    if 'table' not in session or session['table'] is None:
        flash("Please Enter table code first", "danger")
        return redirect(url_for('customers.home_page'))

    if 'customer' not in session or session['customer'] is None:
        flash("Please Login first", "danger")
        return redirect(url_for('customers.sign_page'))

    menuItems = MenuItems.get_by_category(category)

    return render_template("customers/menuItems.html", category=category, menuItems=menuItems)


@customers.route('/categories/<category>/<menu_item>')
def item_details(category, menu_item):
    if 'table' not in session or session['table'] is None:
        flash("Please Enter table code first", "danger")
        return redirect(url_for('customers.home_page'))

    if 'customer' not in session or session['customer'] is None:
        flash("Please Login first", "danger")
        return redirect(url_for('customers.sign_page'))

    item = MenuItems.get(menu_item)

    return render_template("customers/item_details.html", category=category, menuItem=item)


@customers.route('categories/<menu_item>/add', methods=['GET', 'POST'])
def item_add(menu_item):
    if 'table' not in session or session['table'] is None:
        flash("Please Enter table code first", "danger")
        return redirect(url_for('customers.home_page'))

    if 'customer' not in session or session['customer'] is None:
        flash("Please Login first", "danger")
        return redirect(url_for('customers.sign_page'))

    if 'cart' not in session:
        session['cart'] = {}

    if request.method == 'GET':
        flash("Please select the quantity", "danger")
        return redirect(url_for('customers.categories'))

    # Get the quantity of the item from the form data
    quantity = int(request.form['quantity'])

    # Update the cart dictionary with the new item and its quantity
    if menu_item in session['cart']:
        # If the item already exists in the cart, add the new quantity to the existing quantity
        session['cart'][menu_item] += quantity
    else:
        # If the item is not already in the cart, set its quantity
        session['cart'][menu_item] = quantity

    session.modified = True

    print(session)

    print(quantity)

    flash("Item added to cart", "success")
    return redirect(url_for("customers.categories"))


@customers.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'table' not in session or session['table'] is None:
        flash("Please Enter table code first", "danger")
        return redirect(url_for('customers.home_page'))

    if 'customer' not in session or session['customer'] is None:
        flash("Please Login first", "danger")
        return redirect(url_for('customers.sign_page'))

    if 'cart' not in session or len(session['cart']) == 0:
        flash("Your cart is empty", "danger")
        return redirect(url_for('customers.categories'))

    return render_template("customers/cart_management.html")


@customers.route('/checkout/payment', methods=['GET', 'POST'])
def payment():
    if 'table' not in session or session['table'] is None:
        flash("Please Enter table code first", "danger")
        return redirect(url_for('customers.home_page'))

    if 'customer' not in session or session['customer'] is None:
        flash("Please Login first", "danger")
        return redirect(url_for('customers.sign_page'))

    if 'cart' not in session or len(session['cart']) == 0:
        flash("Your cart is empty", "danger")
        return redirect(url_for('customers.categories'))

    payment_methods = PaymentMethod.get_all()

    for payment in payment_methods:
        print(payment.id, payment.description)

    return render_template("customers/payment.html", payment_methods=payment_methods)


# @customers.route('/checkout/payment/confirm', methods=['POST'])
# def confirm_payment():
#     if 'table' not in session or session['table'] is None:
#         flash("Please Enter table code first", "danger")
#         return redirect(url_for('customers.home_page'))
#
#     if 'customer' not in session or session['customer'] is None:
#         flash("Please Login first", "danger")
#         return redirect(url_for('customers.sign_page'))
#
#     if 'cart' not in session or len(session['cart']) == 0:
#         flash("Your cart is empty", "danger")
#         return redirect(url_for('customers.categories'))
#
#     data = request.json
#     payment_method = data['paymentMethod']
#
#     print(payment_method)
#
#     table = Table.from_dict(session['table'])
#     customer = Customer.from_dict(session['customer'])
#
#     order = Orders.insert(Order(table.id, customer.id, payment_method))
#
#     if order:
#         for item_id, quantity in session['cart'].items():
#             order_item = OrderItems.insert(OrderItem(order.id, item_id, quantity))
#
#         session.pop('cart', None)
#         session.modified = True
#
#         flash("Order Placed Successfully", "success")
#         return jsonify({'success': True})
#
#     else:
#         flash("Order cannot be placed", "danger")
#         return jsonify({'success': False})

#-------------------------------------------------
@customers.route('/rate_order')
def rate_order():
    return render_template("customers/rating.html")


@customers.route('/update_quantity', methods=['POST'])
def update_quantity():
    data = request.json
    item_id = data.get('itemId')
    new_quantity = data.get('newQuantity')

    if item_id is None or new_quantity is None:
        return jsonify({'error': 'Missing item ID or new quantity'}), 400

    session['cart'][item_id] = new_quantity
    session.modified = True
    return jsonify({'success': True})


@customers.route('/delete_item', methods=['POST'])
def delete_item():
    data = request.json
    item_id = data['itemId']

    if item_id in session['cart']:
        session['cart'].pop(item_id)
        session.modified = True

    return jsonify({'success': True})


@customers.route('/get_cart_items')
def get_cart_items():
    items = []
    print("view")
    print(
        session.get('cart', {})
    )
    for item_id, quantity in session.get('cart', {}).items():
        item = MenuItems.get(item_id)

        items.append({'id': item.id, 'name': item.name,
                      'description': item.description,
                      'price': item.price * quantity,
                      'quantity': quantity})

    session_data = {
        'items': items,
    }
    return jsonify(session_data)

