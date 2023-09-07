# Function to compute gross salary
def compute_gross_salary(basic, grade):
    # Constants
    HRA_PERCENT = 0.20
    DA_PERCENT = 0.50
    ALLOWANCES = {'A': 1700, 'B': 1500, 'C': 1300}
    PF_PERCENT = 0.11

    # Calculate HRA, DA, Allowance, and PF
    hra = basic * HRA_PERCENT
    da = basic * DA_PERCENT
    allowance = ALLOWANCES.get(grade, 0)
    pf = basic * PF_PERCENT

    # Calculate gross salary
    gross_salary = basic + hra + da + allowance - pf
    return gross_salary

# Example A
basic_A = 10000
grade_A = 'A'
gross_salary_A = compute_gross_salary(basic_A, grade_A)
print(f"Gross Salary for Grade {grade_A}: {gross_salary_A}")

# Example B
basic_B = 4567
grade_B = 'B'
gross_salary_B = compute_gross_salary(basic_B, grade_B)
print(f"Gross Salary for Grade {grade_B}: {gross_salary_B}")

# Saving this code to GitHub is done manually by creating a repository and pushing this code to it.
