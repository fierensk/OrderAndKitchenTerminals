from flask import Flask, render_template, url_for, request

app = Flask(__name__)

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
    current_order = { 
        "customer" : customer_name, 
        "order_items" : order_items_in_array_format, 
        "table_number" : table_number}

    return render_template("order_summary.html", order = current_order)

if __name__ == "__main__":
    app.run(debug=True)