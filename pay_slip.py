import os


# payrolldataa.csv
def get_date(prompt):
    invalid = 1

    while invalid == 1:

        date = raw_input(prompt)

        if "end" in prompt and date == '':
            return date

        if date.count("/") != 2:
            print  "Invalid format must have 2 //"
            continue
        if len(date) > 10:
            print "Invalid length"
            continue
        if date.split('/')[0] == '00' or date.split('/')[1] == '00' or date.split('/')[2] == '0000':
            print "Invalid date values..."
            continue

        new = date.split('/')
        dd, mm, yyyy = new
        m = int(dd)
        d = int(mm)
        y = int(yyyy)

        if y <= 1910 or y >= 2100:
            print "Invalid year"
            continue

        if m > 12 or m < 1:
            print "Invalid month"

            continue

        if (m == 4 or m == 6 or m == 9 or m == 11) and (d > 30 or d < 1):
            print "Invalid day as per month"
            continue
        elif m == 2 and (d > 28 or d < 1):
            print "Invalid day"
            continue
        else:
            if d > 31 or d < 1:
                invalid = 1
                print "Invalid day"
                continue
        invalid = 0

    return date


import csv
import datetime


def main(get_date, output_file):
    is_first_line = True
    temp_sum = 0

    if output_file == '':
        output_file = 'CA1-Payroll-Output.txt'

    infile = open("payrolldataa.csv", "r")
    reader = csv.reader(infile)
    outfile = open(output_file, "w")

    startdate = get_date("Enter start date (dd/mm/yyyy): ")
    enddate = get_date("Enter end date (dd/mm/yyyy): ")

    if enddate == '':
        enddate = startdate

    for line in reader:
        if is_first_line:
            is_first_line = False
            continue
        if line[0] <= startdate:
            first_name = line[2]
            surname = line[1]
            employee_num = line[3]
            normal = line[4]
            rate1 = line[5]
            rate2 = line[6]
            tax_rate = line[8]

            fullname = first_name + ' ' + surname

            hours_normal = float(37.50) * float(normal)
            hours1 = float(5.00) * float(rate1)
            hours2 = float(1.00) * float(rate2)

            grand_total = round(hours1 + hours2 + hours_normal, 1)
            tax_amount = round((grand_total * float(tax_rate)) / 100, 1)
            net_pay = round(grand_total - tax_amount, 1)

            outfile.write("%44s" % ("P A Y S L I P"))
            outfile.write("\n")
            outfile.write("%38s %s" % ("WEEK ENDING", enddate))
            outfile.write("\n")
            outfile.write
            outfile.write("\n")
            outfile.write("Employee: %.20s %.15s" % (first_name, surname))
            outfile.write("\n")
            outfile.write("Number: %.10s" % (employee_num))
            outfile.write("\n\n")
            outfile.write("Earnings %43s" % ("Deductions"))
            outfile.write("\n")
            outfile.write("-------- %43s" % ("----------"))
            outfile.write("\n")
            outfile.write("%22s %8s %8s" % ("Hours", "Rate", "Total"))
            outfile.write("\n")
            outfile.write("Hours(Normal) %8s %8s %6d %13s %15s" % (
            "37.50", normal, hours_normal, "Tax @ {}%".format(tax_rate), tax_amount))
            outfile.write("\n")
            outfile.write("Hours (1.5) %9s %9s %6d" % ("5.00", rate1, hours1))
            outfile.write("\n")
            outfile.write("Hours (2.0) %9s %9s %6d" % ("1.00", rate2, hours2))
            outfile.write("\n\n\n")
            outfile.write("%58s %10s" % ("Total Deductions", tax_amount))
            outfile.write("\n")
            outfile.write("%39s %29s" % ("------", "------"))
            outfile.write("\n")
            outfile.write("Total Pay: %28s %9s %19s" % (grand_total, "Net Pay", net_pay))
            outfile.write("\n\n\n")
            print('{} having employee number {} is completed.'.format(fullname, employee_num))


def check_file(input_file):
    if input_file == '':
        input_file = 'CA1-Payroll-Data.csv'

    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path) + '\\'
    return os.path.exists(dir_path.replace("\\", "\\\\") + input_file)


if __name__ == '__main__':

    invalid = 1

    while invalid == 1:
        input_file = raw_input('Enter input file name : ')
        isFolderExist = check_file(input_file)
        if isFolderExist:
            invalid = 0
        else:
            print 'Enter correct file name or left blank.'

    if isFolderExist:
        output_file = raw_input('Enter output file name : ')
        main(get_date, output_file)
    else:
        print "Given file does not exists"

