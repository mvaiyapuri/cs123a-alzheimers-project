# NAME: ad-chi-sq-test.py
"""
 Team Members: Manimegalai Vaiyapuri, Manasa Gadepalli, Skyla Dennis

 This program builds contingency tables with the frequencies of SNP and patient group 
 classification (Control, MCI, or AD) and performs Chi-square tests on the contingency 
 tables.

"""

# IMPORTS
import pandas as pd
import numpy as np 
from scipy.stats import chi2_contingency

# MAIN FUNCTION
def main():
    # Load the csv file into a DataFrame
    df = pd.read_csv('Patient_total_sheet.csv')

    print()
    print("Performing Chi-square test for CN:")

    # Convert the data into a contingency table with frequencies for CN and print it
    contingency1 = pd.crosstab(df['SNP Name'], df['Group'] == 'CN')
    print(contingency1)

    # Perform Chi-Square test and print p-value for CN
    c1, p1, dof1, expected1 = chi2_contingency(contingency1)
    print("p-value:", p1)
    print()

    print("Performing Chi-square test for MCI:")

    # Convert the data into a contingency table with frequencies for MCI and print it
    contingency2 = pd.crosstab(df['SNP Name'], df['Group'] == 'MCI')
    print(contingency2)

    # Perform Chi-Square test and print p-value for MCI
    c2, p2, dof2, expected2 = chi2_contingency(contingency2)
    print("p-value:", p2)
    print()

    print("Performing Chi-square test for AD:")

    # Convert the data into a contingency table with frequencies for AD and print it
    contingency3 = pd.crosstab(df['SNP Name'], df['Group'] == 'AD')
    print(contingency3)

    # Perform Chi-Square test and print p-value for AD
    c3, p3, dof3, expected3 = chi2_contingency(contingency3)
    print("p-value:", p3)
    print()

#####################################################################################
if __name__ == "__main__":
    main() 
else:
    print("ad-chi-sq-test.py: Is intended to be executed and not imported.")
