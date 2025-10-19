# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from users_db import find_user_by_email, add_user, update_user_password
from db_setup import SessionLocal
from emails import send_reset_email
from models.Payment import Payment
from models.Order import Order
from models.OrderItem import OrderItem
from models.User import Customer, Administrator
from models.Book import Book
from models.Author import Author
from models.BookAuthor import BookAuthor
from models.User import Administrator
from cart_json import load_cart, save_cart
from cart_db import SessionLocal as CartSession, CartItem
from db_json import load_users  # use your correct JSON loader
from datetime import datetime, timedelta
from models.Coupon import Coupon
from models.OrderCoupon import OrderCoupon
from coupon_json import get_user_coupon, load_coupons, save_coupons
import re
import os
import json
import urllib.parse
from order_json import save_order_to_json, load_orders_by_user
from order_db import save_order_to_db
from cart_json import remove_cart_by_email
from cart_db import delete_cart_by_email

app = Flask(__name__)
app.secret_key = "bookie_secret_key"

@app.route('/')
def home():
    return redirect(url_for('catalog'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = SessionLocal()
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        user = find_user_by_email(email, db)
        db.close()

        if not user:
            flash("User not found.", "danger")
        elif user["password"] != password:
            flash("Incorrect password.", "danger")
        else:
            session['user'] = {"name": user['name'], "email": user['email'], "role": user['role']}
            flash(f"Welcome back, {user['name']}!", "success")
            if user['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('catalog'))

    return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been signed out.", "info")
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name'].strip()
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        confirm_password = request.form['confirm_password'].strip()

        # Validate password constraints
        if password != confirm_password:
            flash("Passwords do not match.", "danger")
        elif not re.match(r'^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{5,}$', password):
            flash("Password must be at least 5 characters long, contain at least one letter and one number, and no punctuation.", "danger")
        else:
            db = SessionLocal()
            if find_user_by_email(email, db):
                flash("Email already registered.", "danger")
            else:
                role = "admin" if email.endswith("@bookie.com") else "customer"
                add_user({
                    "name": name,
                    "email": email,
                    "password": password,
                    "role": role
                }, db)
                flash("Registration successful!", "success")
                db.close()
                return redirect(url_for('login'))
            db.close()

    return render_template("register.html")

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email'].strip()
        db = SessionLocal()
        user = find_user_by_email(email, db)
        db.close()

        if user:
            reset_link = url_for('reset_password', email=email, _external=True)
            send_reset_email(email, reset_link)
            flash("A reset link has been sent to your email.", "success")
        else:
            flash("Email not found in the system.", "danger")

        return redirect(url_for('forgot_password'))

    return render_template("forgot_password.html")

@app.route('/reset-password/<email>', methods=['GET', 'POST'])
def reset_password(email):
    db = SessionLocal()
    user = find_user_by_email(email, db)

    if not user:
        db.close()
        flash("Invalid reset link.", "danger")
        return redirect(url_for('login'))

    if request.method == 'POST':
        new_password = request.form['new_password']
        update_user_password(email, new_password, db)
        db.close()
        flash("Password updated. Please log in.", "success")
        return redirect(url_for('login'))

    db.close()
    return render_template("reset_password.html")

@app.route('/catalog')
def catalog():
    user = session.get('user')
    is_logged_in = user is not None
    return render_template("catalog.html", user=user, is_logged_in=is_logged_in)

@app.route('/profile')
def profile():
    user_data = session.get('user')
    if not user_data:
        flash("Please log in to view your profile.", "warning")
        return redirect(url_for('login'))
    db = SessionLocal()
    db_user = find_user_by_email(user_data['email'], db)
    db.close()
    if not db_user:
        flash("User not found.", "danger")
        return redirect(url_for('login'))
    # Only instantiate Customer if user is a customer
    if db_user['role'] == 'customer':
        customer = Customer(db_user['name'], db_user['email'], db_user['password'])
        profile_info = {
            "name": customer.name,
            "email": customer.email,
            "role": db_user['role'],
            "user_id": customer.userId
        }
    else:
        # fallback for admin or other roles
        profile_info = {
            "name": db_user['name'],
            "email": db_user['email'],
            "role": db_user['role'],
            "user_id": "N/A"
        }
    return render_template("profile.html", user=profile_info)

@app.route('/admin-dashboard')
def admin_dashboard():
    user = session.get('user')
    if not user or user['role'] != 'admin':
        flash("Access denied: Admins only.", "danger")
        return redirect(url_for('login'))

    return render_template("admin.html", user=user, features=[
        {"name": "Upload Book", "endpoint": "upload_book"},
        {"name": "Delete Book", "endpoint": "delete_book"},
        {"name": "Manage Inventory", "endpoint": "manage_inventory"},
        {"name": "Manage Categories & Authors", "endpoint": "manage_categories"},
        {"name": "View Reports & Analytics", "endpoint": "view_reports"},
        {"name": "Manage Users", "endpoint": "manage_users"},
        {"name": "Moderate Reviews", "endpoint": "moderate_reviews"}
    ])

# Placeholder admin features (routes to be implemented)
@app.route('/upload-book')
def upload_book():
    return "Upload Book Page (Under Construction)"

@app.route('/delete-book')
def delete_book():
    return "Delete Book Page (Under Construction)"

@app.route('/manage-inventory')
def manage_inventory():
    return "Manage Inventory Page (Under Construction)"

@app.route('/manage-categories')
def manage_categories():
    return "Manage Categories & Authors Page (Under Construction)"

@app.route('/view-reports')
def view_reports():
    return "Reports & Analytics Page (Under Construction)"

@app.route('/manage-users')
def manage_users():
    return "Manage Users Page (Under Construction)"

@app.route('/moderate-reviews')
def moderate_reviews():
    return "Moderate Reviews Page (Under Construction)"


@app.route('/cart')
def cart():
    user = session.get('user')
    if not user:
        flash("Please log in to view your cart.", "warning")
        return redirect(url_for('login'))

    cart_items = session.get('cart', [])

    total = 0
    for item in cart_items:
        # Convert "$12.99" to 12.99 safely
        price_str = item.get("price", "$0").replace("$", "")
        try:
            item["price_float"] = round(float(price_str), 2)
        except:
            item["price_float"] = 0.0
        item["subtotal"] = item["price_float"] * item.get("quantity", 1)
        total += item["subtotal"]

    return render_template("cart.html", user=user, cart_items=cart_items, total=total)




@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    if 'user' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    book = request.json
    if not book or 'title' not in book:
        return jsonify({'success': False, 'message': 'Invalid book data'}), 400

    cart = session.get('cart', [])
    found = False
    for item in cart:
        if item['title'] == book['title']:
            item['quantity'] = item.get('quantity', 1) + 1
            found = True
            break

    if not found:
        book['quantity'] = 1
        cart.append(book)

    session['cart'] = cart
    return jsonify({'success': True, 'message': f"Added '{book['title']}' to cart!", 'cart_count': len(cart)})

@app.route('/book/<title>')
def book_preview(title):
    decoded_title = urllib.parse.unquote(title)
    with open("templates/books_data.json") as f:
        books = json.load(f)

    book_data = next((b for b in books if b['title'].lower() == decoded_title.lower()), None)
    if not book_data:
        flash("Book not found.", "danger")
        return redirect(url_for('catalog'))

    # Create Book, Author, BookAuthor objects
    admins = load_users()
    book_admin = next((a for a in admins if a["role"] == "admin"), None)
    admin_obj = Administrator(book_admin["name"], book_admin["email"],
                              book_admin["password"]) if book_admin else None

    book_obj = Book(
        title=book_data["title"],
        category=book_data.get("category", "General"),
        price=float(book_data["price"].replace("$", "")),
        stock=10,
        description=book_data.get("description", ""),
        is_free=book_data["price"] == "$0.00",
        admin=admin_obj
    )

    author_obj = Author(book_data.get("author", "Unknown"), bio="Bio not provided.")
    book_author_obj = BookAuthor(book=book_obj, author=author_obj, role="Author", contribution="Full")

    return render_template("preview.html", book=book_obj,
                           author=author_obj, book_author=book_author_obj, user=session.get("user"))


@app.route('/increase-quantity', methods=['POST'])
def increase_quantity():
    title = request.form.get('book_title')
    for item in session.get('cart', []):
        if item['title'] == title:
            item['quantity'] = item.get('quantity', 1) + 1
            break
    session.modified = True
    return redirect(url_for('cart'))


@app.route('/decrease-quantity', methods=['POST'])
def decrease_quantity():
    title = request.form.get('book_title')
    cart = session.get('cart', [])
    for item in cart:
        if item['title'] == title:
            if item['quantity'] > 1:
                item['quantity'] -= 1
            else:
                cart.remove(item)
            break
    session['cart'] = cart
    return redirect(url_for('cart'))


@app.route('/remove-from-cart', methods=['POST'])
def remove_from_cart():
    title = request.form.get('book_title')
    session['cart'] = [item for item in session.get('cart', []) if item['title'] != title]
    return redirect(url_for('cart'))


# --- FINALIZE ORDER ---
@app.route('/finalize-order', methods=['POST'])
def finalize_order():
    user = session.get('user')
    if not user:
        flash("Please log in to finalize order.", "warning")
        return redirect(url_for('login'))

    cart = session.get('cart', [])
    if not cart:
        flash("Your cart is empty.", "warning")
        return redirect(url_for('catalog'))

    db = SessionLocal()
    user_data = find_user_by_email(user["email"], db)
    db.close()
    if not user_data:
        flash("User not found.", "danger")
        return redirect(url_for('cart'))

    customer = Customer(user_data["name"], user_data["email"], user_data["password"])
    order = Order(customer, payment_status="Pending", delivery_address="123 Main Street")

    for item in cart:
        book = Book(
            title=item["title"],
            category=item.get("category", "General"),
            price=float(item["price"].replace("$", "").strip()),
            stock=10,
            description=item.get("description", ""),
            is_free=item.get("is_free", False),
            admin=None
        )
        order.add_item(book, item.get("quantity", 1))

    coupon_data = session.get("order_coupon")
    coupon = None
    if coupon_data:
        coupon = Coupon(
            code=coupon_data["code"],
            discount_percent=coupon_data["discount"],
            expiry_date=datetime(2099, 1, 1)  # Placeholder
        )
        order_coupon = OrderCoupon(order, coupon)
        if order_coupon.verify_coupon():
            order.add_coupon(order_coupon)
        else:
            session.pop("order_coupon", None)
            flash("Invalid or expired coupon removed.", "warning")

    session["order_preview"] = {
        "id": order.id,
        "customer": user["email"],
        "items": [
            {"title": item.book.title, "quantity": item.quantity, "price": item.book.price}
            for item in order.order_items
        ],
        "total": order.total_amount,
        "coupon": {
            "code": coupon.get_code(),
            "discount": coupon.discount
        } if coupon else None
    }

    return redirect(url_for("review_order"))


# --- REVIEW ORDER PAGE ---
@app.route('/review_order', methods=['GET', 'POST'])
def review_order():
    user = session.get("user")
    if not user:
        flash("Please log in to review your order.", "danger")
        return redirect(url_for("login"))

    db = SessionLocal()
    user_data = find_user_by_email(user["email"], db)
    db.close()

    if not user_data:
        flash("User not found.", "danger")
        return redirect(url_for("login"))

    cart = session.get("cart", [])
    customer = Customer(user_data["name"], user_data["email"], user_data["password"])
    order = Order(customer, payment_status="Pending", delivery_address="123 Main Street")

    for item in cart:
        book = Book(
            title=item["title"],
            category=item.get("category", "General"),
            price=float(item["price"].replace("$", "")),
            stock=10,
            description=item.get("description", ""),
            is_free=item.get("is_free", False),
            admin=None
        )
        order.add_item(book, item.get("quantity", 1))

    coupon_data = session.get("order_coupon")
    coupon = None
    if coupon_data:
        coupon = Coupon(
            code=coupon_data["code"],
            discount_percent=coupon_data["discount"],
            expiry_date=datetime(2099, 1, 1)
        )
        order_coupon = OrderCoupon(order, coupon)
        if order_coupon.verify_coupon():
            order.add_coupon(order_coupon)
        else:
            session.pop("order_coupon", None)

    if request.method == "POST":
        # Payment + Final Confirmation
        payment_method = request.form.get("payment_method", "Unknown")
        payment = Payment(order, method=payment_method)
        payment.process()
        payment.confirm()
        order.set_payment(payment)
        order.update_status("Confirmed")

        # Save to JSON and DB
        save_order_to_json(order)
        save_order_to_db(order)

        # Clear cart
        remove_cart_by_email(user["email"])
        delete_cart_by_email(user["email"])
        session['cart'] = []
        session.pop('order_coupon', None)

        flash("Order confirmed successfully!", "success")
        return redirect(url_for("view_orders"))

    # Otherwise just show preview
    return render_template("review_order.html", order={
        "id": order.id,
        "items": [
            {"title": item.book.title, "quantity": item.quantity, "price": item.book.price}
            for item in order.order_items
        ],
        "total": order.total_amount,
        "coupon": {
            "code": coupon.get_code(),
            "discount": coupon.discount
        } if coupon else None
    })


@app.route('/confirm_order')
def confirm_order():
    user = session.get("user")
    if not user:
        flash("Please log in to confirm your order.", "warning")
        return redirect(url_for('login'))

    cart_items = session.get('cart', [])
    if not cart_items:
        flash("Your cart is empty.", "warning")
        return redirect(url_for('cart'))

    db = SessionLocal()
    db_user = find_user_by_email(user['email'], db)
    db.close()

    if not db_user:
        flash("User not found.", "danger")
        return redirect(url_for('login'))

    # Build display data from session cart
    total = sum(float(item['price'].replace('$', '')) * item['quantity'] for item in cart_items)

    coupon_data = session.get("order_coupon")
    if coupon_data:
        discount = coupon_data["discount"]
        discounted_total = total * (1 - discount / 100)
    else:
        discounted_total = total

    # Add per-item subtotal
    cart_display = []
    for item in cart_items:
        cart_display.append({
            "title": item["title"],
            "price_float": float(item["price"].replace("$", "")),
            "quantity": item["quantity"],
            "subtotal": float(item["price"].replace("$", "")) * item["quantity"]
        })

    return render_template("cart.html",
        cart_items=cart_display,
        total=discounted_total,
        user=user,
        coupon={
            "code": coupon_data["code"],
            "discount": coupon_data["discount"],
            "original_total": total
        } if coupon_data else None
    )




# --- APPLY COUPON ---
@app.route("/apply_coupon", methods=["POST"])
def apply_coupon():
    email = session.get("user", {}).get("email")
    if not email:
        flash("Please log in to apply a coupon.", "danger")
        return redirect(url_for("login"))

    code = request.form.get("coupon_code", "").strip().upper()
    coupon_data = get_user_coupon(email, code)
    if not coupon_data:
        flash("Invalid coupon code or not linked to your account.", "danger")
        return redirect(url_for("cart"))

    coupon_obj = Coupon(
        code=coupon_data["code"],
        discount_percent=coupon_data["discount_percent"],
        expiry_date=datetime.strptime(coupon_data["expiry_date"], "%Y-%m-%d")
    )

    if not coupon_obj.is_valid():
        flash("This coupon has expired.", "warning")
        return redirect(url_for("cart"))

    session["order_coupon"] = {
        "code": coupon_obj.get_code(),
        "discount": coupon_obj.discount
    }

    flash("Coupon applied successfully!", "success")
    return redirect(url_for("cart"))


# --- VIEW COUPONS ---
@app.route('/view_coupon')
def view_coupon():
    user = session.get('user')
    if not user:
        flash("Please log in to view coupons.", "warning")
        return redirect(url_for('login'))

    with open('templates/coupon.json', 'r') as f:
        all_coupons = json.load(f)

    user_coupons = []
    for c in all_coupons:
        if c['user_email'] == user['email']:
            try:
                c['expiry_date'] = datetime.strptime(c['expiry_date'], '%Y-%m-%d')
            except ValueError:
                continue
            user_coupons.append(c)

    return render_template('view_coupon.html', coupons=user_coupons, user=user, current_time=datetime.now())


# --- ADD COUPON SUBMISSION ---
@app.route('/add_coupon', methods=['POST'])
def add_coupon():
    user = session.get('user')
    if not user:
        flash("Please log in first.", "warning")
        return redirect(url_for('login'))

    coupon_code = request.form.get('code', '').strip().upper()
    discount = request.form.get('discount', '').strip()
    expiry = request.form.get('expiry', '').strip()

    if not coupon_code or not discount or not expiry:
        flash("All fields are required.", "danger")
        return redirect(url_for('view_coupon'))

    try:
        discount = int(discount)
        expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
    except ValueError:
        flash("Invalid discount or expiry date.", "danger")
        return redirect(url_for('view_coupon'))

    # Check if coupon already exists for this user
    if get_user_coupon(user['email'], coupon_code):
        flash("You already have this coupon.", "warning")
        return redirect(url_for('view_coupon'))

    coupons = load_coupons()

    new_coupon = {
        "code": coupon_code,
        "discount_percent": discount,
        "expiry_date": expiry_date.strftime("%Y-%m-%d"),
        "user_email": user["email"]
    }

    coupons.append(new_coupon)
    save_coupons(coupons)

    flash(f"Coupon '{coupon_code}' added successfully.", "success")
    return redirect(url_for('view_coupon'))


@app.route('/your_orders')
def view_orders():
    user = session.get("user")
    if not user:
        flash("Please log in to view your order history.", "warning")
        return redirect(url_for("login"))

    from order_json import load_orders_by_user
    orders = load_orders_by_user(user["email"])
    return render_template("view_orders.html", orders=orders)




if __name__ == '__main__':
    app.run(debug=True)
