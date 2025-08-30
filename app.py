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

