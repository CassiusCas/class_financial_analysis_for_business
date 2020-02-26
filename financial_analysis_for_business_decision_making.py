

def implied_value():
    a=input("Value of Resources Offered for Equity:")
    b=input("Equity Stake in Exchange for Resources:")
    value_equity=float(a)
    equity_stake=float(b)
    ans_imp_value = value_equity/equity_stake
    return ans_imp_value

def return_on_assets():
    x=input("Enter Earnings amount:")
    y=input("Enter Asset amount here:")
    earnings=int(x)
    assets=int(y)
    roa_answer=earnings/assets
    return roa_answer

def internal_growth_rate():
    y=input("Enter ROA value as a decimal.\nIf you haven't yet computed it, enter \"-\":")
    if y!="-":
        roa_already=float(y)
        igr=roa_already/(1-roa_already)
    else:
        e=input("Enter Earnings Amount:")
        a=input("Enter Asset Amount:")
        earning=(float(e))
        asset=(float(a))
        roa=(earning/asset)
        igr=roa/(1-roa)
    return igr

def return_on_equity():
    x = input("What is the Net Income?:")
    y = input("What is the Total Business Worth or Equity?:")
    net_income=float(x.replace(",","").replace("$",""))
    equity=float(y.replace(",","").replace("$",""))
    roe=net_income/equity
    return roe

def net_profit_margin():
    x=input("What is the Net Income?:")
    y=input("What is the Total Sales?:")
    net_income=float(x.replace(",","").replace("$",""))
    total_sales=float(y.replace(",","").replace("$",""))
    npm=net_income/total_sales
    return npm

def total_asset_turnover():
    x=input("Enter total Sales:")
    y=input("Enter total Assets:")
    sales=float(x.replace("$","").replace(",",""))
    total_assets=float(y.replace("$","").replace(",",""))
    tat=sales/total_assets
    return tat

def equity_multiplier():
    x=input("Enter the Total Assets:")
    y=input("Enter the Total Equity:")
    total_assets=float(x.replace("$","").replace(",",""))
    total_equity=float(y.replace("$","").replace("$",""))
    equity_multiplier=total_assets/total_equity
    return equity_multiplier

def dupont_decomposition():
    print("If you don't have the variables calculated enter 'na' and you will be walked through the calculation.\nEnter all percentages as decimals.")
    a=input("Enter the Net Profit Margin:")
    if a.isalpha() or a=="":
        netpm=net_profit_margin()
    else:
        netpm=float(a.replace("$","").replace(",",""))
    b=input("Enter the the Total Asset Turnover:")
    if b.isalpha() or b=="":
        totalat=total_asset_turnover()
    else:
        totalat=float(b.replace("$","").replace(",",""))
    c=input("Enter the Equity Multiplier:")
    if c.isalpha() or c=="":
        em=equity_multiplier()
    else:
        em=float(c.replace("$","").replace(",",""))
    dupont=netpm*totalat*em
    return dupont

def discounted_payback():
    i=input("Initial Investment:")
    ri=input("Investor's required interest per year:")
    initial_investment=float(i.replace("$","").replace(",",""))
    required_interest=float(ri.replace("$","").replace(",",""))
    cf=input("Enter Cashflows for each year seperated by a comma:")
    cf2=cf.split(',')
    cash_flows=[float(i) for i in cf2]
    
    print("Investors Interest Rate Adjusted to Today's Value:")
    adjusted_interest_rate=[]
    for x in range(len(cash_flows)):
        adjusted_interest_rate.append((required_interest+1)**(x+1))
        print("year",(x+1),":",adjusted_interest_rate[x])
    
    
    print("Investors Expected Return Adjusted To Today's Value:")
    adjusted_expected_return=[]
    for x in range(len(cash_flows)):
        adjusted_expected_return.append(cash_flows[x]/adjusted_interest_rate[x])
        print("Year",(x+1),":",adjusted_expected_return[x])
    
    print("Payback to Date:")
    ptd=[]
    for x in range(len(cash_flows)):
        if x==0:
            ptd.append(adjusted_expected_return[0])
        else:
            ptd.append(adjusted_expected_return[x]+ptd[x-1])
        print("Year",(x+1),":",ptd[x])
        
    for x in range(len(cash_flows)):
        if ptd[x]>=initial_investment:
            break_even_point=((initial_investment-ptd[x-1])/adjusted_expected_return[x])+(x)
            print("The Break Even Point is at year:\n",break_even_point)
            break
    else:
        print("The break even point was never met")


def net_present_value():
    print("The net present value is the economic measure of whether or not the project is expected to create value.\nIf the net present value is positive, then the project earns above what investors need.")
    
    #initial investment
    ii=input("What is the Initial Investment:")
    initial_investment=float(ii.replace(",","").replace("$",""))
    
    #risk
    r=input("Enter all risks as a decimal point seperated by a ','")
    risk_list=r.split(",")
    risk_float=[float(i) for i in risk_list]
    total_risk= sum(risk_float)
    print("Total Risk is:",total_risk)
    
    #cash flows
    cf=input("Enter all cashflows per year seperated by a ',':")
    cf2=cf.split(",")
    cash_flows=[float(f) for f in cf2]
    print("Cash Flow Values:")
    for x in range(len(cash_flows)):
        print("Year",x+1,":",cash_flows[x])
    
    #Total Risk Per Year
    print("Total Risk Per Year:")
    trpy=[]
    for x in range(len(cash_flows)):
        if x==0:
            trpy.append(total_risk+1)
        else:
            trpy.append(trpy[0]**(x+1))
        print("Year",x+1,":",trpy[x])
    
    #Net Present Value Per Year
    npvpy=[]
    print("Net Present Value Per Year:")
    for x in range(len(cash_flows)):
        npvpy.append(cash_flows[x]/trpy[x])
        print("Year",x+1,":",npvpy[x])
    
    #total net present values
    tnpv=initial_investment+sum(npvpy)
    print("Total Net Present Value:",tnpv)


def internal_rate_of_return():
    present_value=input("Enter the Present Value aka Investment Costs Today:")
    pv=float(present_value.replace(",","").replace("$",""))
    future_value=input("Enter the Future Value aka Investment Worth Later:")
    fv=float(future_value.replace(",","").replace("$",""))
    internal_rate_of_return=(((fv-pv)/pv))
    print(internal_rate_of_return)