tariff_to_estimator = {"TARIFF_11" : 0.244618, "TARIFF_31" : 0.136928}

print("Electricity bill estimator 2.0")
traiff = float(input("Which tariff? 11 or 31: "))

if traiff == 11:
    traiff = tariff_to_estimator["TARIFF_11"]
elif traiff == 31:
    traiff = tariff_to_estimator["TARIFF_31"]
else:
    print("Wrong tariff.")
daily_kwh = float(input("Enter daily use in kWh: "))
billing_day = float(input("Enter number of billing days: "))

print("Estimated bill: {:.2f}".format(traiff * daily_kwh * billing_day))