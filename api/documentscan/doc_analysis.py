from documentscan.models import IncomeStatement
import pdf2image
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pandas as pd
import csv


# helper functions
def back_step(str, target_str):
    try:
        i = str.index(target_str)
        count = -1
        while str[i] != " ":
            i -= 1
            count += 1
        val = int(str[i+1:i+count])
    except ValueError:
        val = 0
    return val

# this removes bad characters and spaces (except for spaces that precede the numbers at end of line)
def clean_image_string(image_str):
    bad_chars = "!#$%&'()*+,-./:;<=>?@[]^_~}`{°£§|» \"\'"
    clean_image_str = ""
    for i in range(1, len(image_str)-1):
        if image_str[i] == " " and image_str[i+1].isnumeric():
            j = i+1
            while image_str[j] != "\n" and image_str[j].isnumeric():
                j += 1
            if image_str[j] == "\n":
                clean_image_str += image_str[i]
        elif image_str[i] not in bad_chars:
            clean_image_str += image_str[i]
    return clean_image_str

def save_doc_type_and_doc_string(file_name):
    images = pdf2image.convert_from_path(file_name)
    image_str = pytesseract.image_to_string(images[0])
    if image_str.count("1120-S") >= 1:
        return ("1120-S", image_str)
    elif image_str.count("1120") >= 1:
        return ("1120", image_str)
    return ("Unknown", image_str)

def save_tax_form_data(document, ocr_string):
    str = clean_image_string(ocr_string)
    df = pd.read_csv(r'/mnt/c/Users/tmcgl/Desktop/Coding/boilerplate-angular-django-jwt-login/api/documentscan/mapping/document_mapping.csv')
    df['value'] = df.apply(lambda x: back_step(str, x['next_line']), axis=1)
    for index, row in df.iterrows():
        setattr(document, row['line_item'], row['value'])
    return document

def make_income_statement(document):
    income_statement = IncomeStatement()
    for key, value in document.__dict__.items():
        if key in income_statement.__dict__.keys():
            setattr(income_statement, key, value)
        
    
    # in the future this will be based off of the income statement templates but this will work for now
    income_statement.salaries_and_wages_expense = document.salaries_and_wages_expense + \
                                                  document.pension_expense + \
                                                  document.employee_benefits_expense + \
                                                  document.officer_compensation_expense
    income_statement.other_income = document.dividend_revenue + \
                                    document.interest_revenue + \
                                    document.rent_revenue + \
                                    document.royalty_revenue + \
                                    document.capital_gain_revenue + \
                                    document.net_gain_or_loss_revenue + \
                                    document.other_income_revenue
    income_statement.total_operating_expense = income_statement.salaries_and_wages_expense + \
                                               document.repairs_and_maintenence_expense + \
                                               document.bad_debt_expense + \
                                               document.rent_expense + \
                                               document.taxes_and_licenses_expense + \
                                               document.interest_expense + \
                                               document.charitable_contributions_expense + \
                                               document.depreciation_expense + \
                                               document.depletion_expense + \
                                               document.advertising_expense 
    income_statement.gross_profit = document.net_sales - document.cogs
    income_statement.operating_profit = income_statement.gross_profit - income_statement.total_operating_expense
    income_statement.taxable_income = income_statement.operating_profit + income_statement.other_income
    income_statement.net_income = income_statement.taxable_income - income_statement.income_tax_expense
    return income_statement