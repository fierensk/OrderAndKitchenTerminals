from flask import Flask, render_template, url_for, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from order_model import Base, Order

app = Flask(__name__)

engine = create_engine("sqlite:///orders.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

@app.route("/<int:tableNum>")
def main_menu(tableNum):
    return render_template("main_menu.html", order_summary_reference=url_for("order", table_number=tableNum))

@app.route('/order/<int:table_number>', methods=['POST'])
def order(table_number):
    order_items_in_String_format = request.form["order_summary"].strip()
    order_items_in_array_format = [
        item.replace("\r", "").strip() for item in order_items_in_String_format.split("\n") if item.strip()
    ]
    customer_name = request.form["customer_name"]
    # creating an Order object to be saved into the database
    new_order = Order(customer_name=customer_name, 
                      orders=order_items_in_String_format, 
                      order_number=table_number)
    current_order = { 
        "customer" : customer_name, 
        "order_items" : order_items_in_array_format, 
        "order_number" : table_number}
    
    try:
        session.add(new_order)
        session.commit()
        return render_template("order_summary.html", order=current_order)
    except:
        return 'There was an issue adding your task'

if __name__ == "__main__":
    app.run(debug=True)