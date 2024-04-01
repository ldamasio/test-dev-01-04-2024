def discount(consumption, tax_type, distributor_tax):

    if len(consumption) != 3:
        raise KeyError('Não foram fornecidos 3 valores de consumo de energia!')

    for x in consumption:
        if not isinstance(x, (int, float)):
            raise KeyError('O valor do consumo não é inteiro nem decimal!')

    if not tax_type:
        raise KeyError('Não foi fornecido o tipo de tarifa!')

    if not isinstance(distributor_tax, (int, float)):
        raise KeyError('O valor do consumo não é inteiro nem decimal!')

    average_consumption = sum(consumption) / 3

    if tax_type == "RESIDENCIAL":
        if average_consumption < 10000:
            applied_discount = 0.18
        elif average_consumption > 20000:
            applied_discount = 0.25
        else:
            applied_discount = 0.22
    elif tax_type == "COMERCIAL":
        if average_consumption < 10000:
            applied_discount = 0.16
        elif average_consumption > 20000:
            applied_discount = 0.22
        else:
            applied_discount = 0.18
    elif tax_type == "INDUSTRIAL":
        if average_consumption < 10000:
            applied_discount = 0.12
        elif average_consumption > 20000:
            applied_discount = 0.18
        else:
            applied_discount = 0.15
    else:
        raise KeyError('Tipo de tarifa não categorizado!')

    if average_consumption < 10000:
        coverage = 0.9
    elif average_consumption > 20000:
        coverage = 0.99
    else:
        coverage = 0.95

    print ('8888888888888888888888888')
    print ('avg cons', average_consumption)

    # annual_cost = (average_consumption * 12) * (distributor_tax * applied_discount)
    # print('an cost', annual_cost)

    annual_savings = (average_consumption * coverage * 12) * (distributor_tax * applied_discount)
    print('an sav', annual_savings)

    print ('8888888888888888888888888')

    print 

    return (applied_discount, coverage, annual_savings)

def calculator(consumption: list, distributor_tax: float, tax_type: str) -> tuple:
    """
    returns a tuple of floats contained anual savings, monthly savings, applied_discount and coverage
    """
    annual_savings = 0
    monthly_savings = 0
    applied_discount = 0
    coverage = 0

    # your code here #

    applied_discount, coverage, annual_savings = discount(consumption, tax_type.upper(), distributor_tax)
    annual_savings = round (annual_savings, 2)
    monthly_savings = round((annual_savings / 12), 2)


    return (
        round(annual_savings, 2),
        round(monthly_savings, 2),
        applied_discount,
        coverage,
    )

if __name__ == "__main__":
    print("Testing...")

    assert calculator([1518, 1071, 968], 0.95871974, "Industrial") == (
        1473.19,
        122.77,
        0.12,
        0.9,
    )

    assert calculator([1000, 1054, 1100], 1.12307169, "Residencial") == (
        2295.32,
        191.28,
        0.18,
        0.9,
    )

    assert calculator([973, 629, 726], 1.04820025, "Comercial") == (
        1405.56,
        117.13,
        0.16,
        0.9,
    )

    assert calculator([15000, 14000, 16000], 0.95871974, "Industrial") == (
        24591.16,
        2049.26,
        0.15,
        0.95,
    )

    assert calculator([12000, 11000, 11400], 1.12307169, "Residencial") == (
        32297.74,
        2691.48,
        0.22,
        0.95,
    )

    assert calculator([17500, 16000, 16400], 1.04820025, "Comercial") == (
        35776.75,
        2981.40,
        0.18,
        0.95,
    )

    assert calculator([30000, 29000, 29500], 0.95871974, "Industrial") == (
        60478.73,
        5039.89,
        0.18,
        0.99,
    )

    assert calculator([22000, 21000, 21400], 1.12307169, "Residencial") == (
        71602.56,
        5966.88,
        0.25,
        0.99,
    )

    assert calculator([25500, 23000, 21400], 1.04820025, "Comercial") == (
        63832.12,
        5319.34,
        0.22,
        0.99,
    )

    print("Everything passed")
