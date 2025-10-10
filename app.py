from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'devops_2025'
# TAX Function
def tax(Annual_Salary, Passive_Income, Age):
    Total_Income = Annual_Salary + Passive_Income

    if Age < 60:
        if Total_Income < 250000:
            return "The Candidate does not need to pay any tax as his/her Income is not under Taxation slab"
        elif 250000 < Total_Income < 500000:
            Excess = Total_Income - 250000
            IT = (Excess / 100) * 5
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {IT}"
        elif 500000 < Total_Income < 1000000:
            Excess = Total_Income - 500000
            IT = ((Excess / 100) * 20) + 12500
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {IT}"
        elif 1000000 < Total_Income < 5000000:
            Excess = Total_Income - 1000000
            IT = ((Excess / 100) * 30) + 112500
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {IT}"
        elif 5000000 < Total_Income < 10000000:
            Excess = Total_Income - 1000000
            IT = ((Excess / 100) * 30) + 112500
            Surcharge = (IT / 100) * 10
            Tax = IT + Surcharge
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {Tax}"
        elif 10000000 < Total_Income < 20000000:
            Excess = Total_Income - 1000000
            IT = ((Excess / 100) * 30) + 112500
            Surcharge = (IT / 100) * 15
            Tax = IT + Surcharge
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {Tax}"
        elif 20000000 < Total_Income < 50000000:
            Excess = Total_Income - 1000000
            IT = ((Excess / 100) * 30) + 112500
            Surcharge = (IT / 100) * 25
            Tax = IT + Surcharge
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {Tax}"
        else:
            Excess = Total_Income - 1000000
            IT = ((Excess / 100) * 30) + 112500
            Surcharge = (IT / 100) * 37
            Tax = IT + Surcharge
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {Tax}"

    elif 60 <= Age < 80:
        if Total_Income < 300000:
            return "The Candidate does not need to pay any tax as his/her Income is not under Taxation slab"
        elif 300000 < Total_Income < 500000:
            Excess = Total_Income - 300000
            IT = (Excess / 100) * 5
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {IT}"
        elif 500000 < Total_Income < 1000000:
            Excess = Total_Income - 500000
            IT = ((Excess / 100) * 20) + 10000
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {IT}"
        elif 1000000 < Total_Income < 5000000:
            Excess = Total_Income - 1000000
            IT = ((Excess / 100) * 30) + 110000
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {IT}"
        elif 5000000 < Total_Income < 10000000:
            Excess = Total_Income - 1000000
            IT = ((Excess / 100) * 30) + 110000
            Surcharge = (IT / 100) * 10
            Tax = IT + Surcharge
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {Tax}"
        elif 10000000 < Total_Income < 20000000:
            Excess = Total_Income - 1000000
            IT = ((Excess / 100) * 30) + 110000
            Surcharge = (IT / 100) * 15
            Tax = IT + Surcharge
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {Tax}"
        elif 20000000 < Total_Income < 50000000:
            Excess = Total_Income - 1000000
            IT = ((Excess / 100) * 30) + 110000
            Surcharge = (IT / 100) * 25
            Tax = IT + Surcharge
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {Tax}"
        else:
            Excess = Total_Income - 1000000
            IT = ((Excess / 100) * 30) + 110000
            Surcharge = (IT / 100) * 37
            Tax = IT + Surcharge
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {Tax}"

    else:  # Age >= 80
        if Total_Income < 500000:
            return "The Candidate does not need to pay any tax as his/her Income is not under Taxation slab"
        elif 500000 < Total_Income < 1000000:
            Excess = Total_Income - 500000
            IT = ((Excess / 100) * 20)
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {IT}"
        elif 1000000 < Total_Income < 5000000:
            Excess = Total_Income - 1000000
            IT = ((Excess / 100) * 30) + 110000
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {IT}"
        elif 5000000 < Total_Income < 10000000:
            Excess = Total_Income - 1000000
            IT = ((Excess / 100) * 30) + 100000
            Surcharge = (IT / 100) * 10
            Tax = IT + Surcharge
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {Tax}"
        elif 10000000 < Total_Income < 20000000:
            Excess = Total_Income - 1000000
            IT = ((Excess / 100) * 30) + 100000
            Surcharge = (IT / 100) * 15
            Tax = IT + Surcharge
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {Tax}"
        elif 20000000 < Total_Income < 50000000:
            Excess = Total_Income - 1000000
            IT = ((Excess / 100) * 30) + 100000
            Surcharge = (IT / 100) * 25
            Tax = IT + Surcharge
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {Tax}"
        else:
            Excess = Total_Income - 1000000
            IT = ((Excess / 100) * 30) + 100000
            Surcharge = (IT / 100) * 37
            Tax = IT + Surcharge
            return f"The Income Tax that has to be paid by the candidate for the respective Financial Year is {Tax}"

@app.route('/')
def index():
    return render_template('index.html', tax_amt=session.pop('tax_amt', None))
@app.route('/Calculate_Tax', methods=['POST'])
@app.route('/Calculate_Tax', methods=['POST'])
def calculate_tax():
    try:
        active_income = int(request.form.get('num1', 0))
        passive_income = int(request.form.get('num2', 0))
        age = int(request.form.get('num3', 0))
        
        app.logger.info(f"Received request: Active Income={active_income}, Passive Income={passive_income}, Age={age}")

        tax_amt = tax(active_income, passive_income, age)
        if tax_amt is not None:
            session['tax_amt'] = tax_amt
            app.logger.info(f"Calculated tax amount: {tax_amt}")
            return jsonify({'result': 'success', 'message': f'{tax_amt} Rupees'})
        else:
            app.logger.error("Failed to calculate tax: tax_amt is None")
            return jsonify({'result': 'error', 'message': 'Failed to calculate tax'})
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return jsonify({'result': 'error', 'message': f'An error occurred: {e}'})




if __name__ == '__main__':
    app.run(debug=True)
    print("Trying web hook")
    print("changes made")
    print("added trigger")
