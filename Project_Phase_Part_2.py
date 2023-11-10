#Suraya Malek
#CIS 261
#Date: 11/10/2023
#Project:Course Project Phase part 2

def getEmpName():
    empname = input("Enter employee name: ")
    return empname
def getDateWorked():
    fromdate = input("Enter start Date (mm/dd/yyyy): ")
    todate = input("Enter end Date(mm/dd/yyyy): ")
    return fromdate,todate
def getHoursWorked():
    hours = float(input("Enter amount of hours worked: "))
    return hours
def getHourlyRate():
    hourlyrate = float(input("Enter hours rate: "))
    return hourlyrate
def getTaxRate():
    taxrate = float(input("Enter tax rate: "))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay
def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrosspay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]
        grosspay, incometax, netpay = CalcTaxAndNetPay( hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}",f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")
        TotEmployees += 1
        TotHours += hours
        TotGrosspay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        EmpTotals["TotEmp"] = TotEmployees
        EmpTotals["TotHours"] = TotHours
        EmpTotals["TotGrosspay"] = TotGrosspay
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TotNetPay"] = TotNetPay

def printTotals(EmpTotals):
    print()
    print(f'Total number of employees: {EmpTotals["TotEmp"]}')
    print(f'Total hours of employees: {EmpTotals["TotHours"]}')
    print(f'Total grosspay of employees: {EmpTotals["TotGrosspay"]}')
    print(f'Total tax of employees: {EmpTotals["TotTax"]}')
    print(f'Total net pay of employees: {EmpTotals["TotNetPay"]}')

if __name__ == "__main__":
    EmpDetailList = []
    EmpTotals = {}
    while True:
        empname = getEmpName()
        if(empname.lower() == "end"):
            break
        fromdate, todate = getDateWorked()
        hours = getHoursWorked()
        hourlyrate = getHourlyRate()
        taxrate = getTaxRate()
        EmpDetail =[fromdate, todate, empname, hours, hourlyrate, taxrate]
        EmpDetailList.append(EmpDetail)
    printinfo(EmpDetailList)
    printTotals(EmpTotals)
    
        

    