
def monthly_cost():
    print('Gotta couple of questions for you...')
    p = float(input('Enter loan amount '))
    r = float(input('Enter interest rate (%)'))
    n = int(input('Enter loan period (in months)'))
    # convert r to a decimal and divide by interest per year
    r = (r / 100) / 12
    # breaks formula down into 3 parts to reduce error
    # numerator
    top = r * (1 + r)**n
    # denominator
    bottom = ((1 + r)**n) - 1
    # putting it all together
    a = round(p * (top / bottom))
    # use simple interest formula
    # I = Prt
    # In this case, I = Prn
    total_interest = round(p * r * n, 3)
    print(f'Monthly costs = ${a}. Total interest = ${total_interest} ')


if __name__ == '__main__':
    monthly_cost()