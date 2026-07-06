# Devon Dowdy
 # Date 07/05/2026
 # P4HW2
 #Caclulates employee pay

#START PROGRAM
#Intialize tracking variables
#SET total_employees = 0
#SET total_gross_pay = 0.0
#CREATE empty list employees_data
#main loop for employee data entry
#WHILE True DO
#OUTPUT "Enter employee name (or 'done' to finish): "
#INPUT employee_name
#check termination condition
#IF employee_name.lower() == 'done' THEN
#   BREAK out of loop
#ENDIF
#OUTPUT"what is the hours worked for employee_name: "
#INPUT hours_worked
#OUTPUT "What is the hourly pay rate for employee_name: "
#INPUT hourly_rate
#calculate regular and overtime pay
#IF hours_worked > 40 THEN
#   SET reg_hours = 40
#   SET overtime_hours = hours_worked - 40
#ELSE
#   SET reg_hours = hours_worked
#   SET overtime_hours = 0
#ENDIF
#cacluate individual pay
#SET reg_pay = reg_hours * hourly_rate
#SET overtime_pay = overtime_hours * hourly_rate * 1.5
#SET gross_pay = reg_pay + overtime_pay
#track global totals
#SET total_employees += 1
#SET total_gross_pay += gross_pay
#store employee data in dictionary and append to list
#save employee data in dictionary
#END WHILE
#Display summary report
#IF total_employees > 0 THEN
#OUTPUT table header columns (Name, Hours Worked, Hourly Rate, Regular Pay, Overtime Pay, Gross Pay)
#FOR each employee in employees_data DO
#   OUTPUT employee data in formatted table row
#END FOR
#OUTPUT total employees and total gross pay
#ELSE
#   OUTPUT "No employee data entered."
#ENDIF
#END PROGRAM

def main():
    total_employees = 0
    total_gross_pay = 0.0
    employees_data = []

    print("--- Employee Pay Calculator ---")

    while True:
        name = input("Enter employee name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        try:
            hours = float(input(f"Enter hours worked for {name}: "))
            rate = float(input(f"Enter hourly pay rate for {name}: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if hours > 40:
            reg_hours = 40
            overtime_hours = hours - 40
        else:
            reg_hours = hours
            overtime_hours = 0

        reg_pay = reg_hours * rate
        overtime_pay = overtime_hours * rate * 1.5
        gross_pay = reg_pay + overtime_pay

        total_employees += 1
        total_gross_pay += gross_pay

        employees_data.append({
            "name": name,
            "hours": hours,
            "rate": rate,
            "reg_hours": reg_hours,
            "overtime_hours": overtime_hours,
            "reg_pay": reg_pay,
            "overtime_pay": overtime_pay,
            "gross_pay": gross_pay
        })
        print()

    if total_employees > 0:
        print("\n" + "="*80)
        print(f"{'Employee Name':<20}{'Hours Worked':<15}{'Hourly Rate':<15}{'Regular Pay':<15}{'Overtime Pay':<15}{'Gross Pay':<15}")
        print("="*80)

        for emp in employees_data:
            print(f"{emp['name']:<20}{emp['hours']:<15.2f}{emp['rate']:<15.2f}{emp['reg_pay']:<15.2f}{emp['overtime_pay']:<15.2f}{emp['gross_pay']:<15.2f}")
            print("_" * 80)
        print(f"{'Total Employees:':<20}{total_employees:<15}")
        print(f"{'Total Gross Pay:':<20}${total_gross_pay:<15.2f}")
        print("="*80)
    else:
        print("No employee data entered.")

if __name__ == "__main__":
    main()