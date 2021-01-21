#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""HTTP route definitions"""

from flask import request, render_template
from app import app
from app.database import create, read, update, delete, scan
from datetime import datetime
from app.forms.product import ProductForm

@app.route("/")
def index():
    serv_time = datetime.now().strftime("%F %H:%M:%S")
    return {
        "ok": True,
        "version": "1.0.0",
        "server_time": serv_time
    }


@app.route("/product_form", methods=["GET", "POST"])
def product_form():
    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        category = request.form.get("category")
        description = request.form.get("description")
        create(name, price, category, description)
    form = ProductForm()
    return render_template("form_example.html", form=form)


@app.route("/products")
def get_all_products():
    out = scan()
    # out["ok"] = True
    # out["message"] = "Success"
    # return out
    return render_template("products.html", products=out["body"])


# @app.route("/products/<pid>")
# def get_one_product(pid):
#     out = read(int(pid))
#     out["ok"] = True
#     out["message"] = "Success"
#     return out


@app.route("/products", methods=["POST"])
def create_product():
    product_data = request.json
    new_id = create(
        product_data.get("name"),
        product_data.get("price"),
        product_data.get("category"),
        product_data.get("description"),
        product_data.get("quantity")
    )

    return {"ok": True, "message": "Success", "new_id": new_id}


@app.route("/products/<pid>", methods=["GET", "PUT"])
def update_product(pid):
    # product_data = request.json
    if request.method == "PUT":
        update(pid, request.form)
        return {"ok": "True", "message": "Updated"}
    out = read(int(pid))
    update_form = ProductForm()
    if out["body"]:
        return render_template("single_product.html", product=out["body"][0], form=update_form)
    else:
        return render_template("404.html"), 404


@app.route("/user/<name>")
def show_user(name):
    last_name="GPL"
    hobbies="DIY stuff"
    return render_template("user.html", first_name=name, last_name=last_name, hobbies=hobbies)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
