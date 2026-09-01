# College Admission Management System

class Applicant:
    def __init__(self, applicant_name, application_id, entrance_score):
        self.applicant_name = applicant_name
        self.application_id = application_id
        self.entrance_score = entrance_score

    def categorize(self):
        if self.entrance_score >= 80:
            return "Merit List"
        elif self.entrance_score >= 50:
            return "Waiting List"
        else:
            return "Not Eligible"

    def display(self):
        print("Applicant Name      :", self.applicant_name)
        print("Application ID      :", self.application_id)
        print("Entrance Score      :", self.entrance_score)
        print("Admission Category  :", self.categorize())

    def __str__(self):
        return (f"Applicant(Name={self.applicant_name}, "
                f"ID={self.application_id}, "
                f"Score={self.entrance_score}, "
                f"Category={self.categorize()})")


class College:
    def __init__(self):
        self.applicants = []

    def add_applicant(self, applicant):
        self.applicants.append(applicant)

    def display_all_records(self):
        if not self.applicants:
            print("No applicant records available.")
        else:
            print("\n--- Admission Records ---")
            for applicant in self.applicants:
                applicant.display()
                print()


# Main Program
college = College()

n = int(input("Enter number of applicants: "))

for i in range(n):
    print(f"\nEnter details of Applicant {i + 1}")
    name = input("Enter applicant name: ")
    app_id = input("Enter application ID: ")
    score = float(input("Enter entrance examination score: "))

    applicant = Applicant(name, app_id, score)
    college.add_applicant(applicant)

college.display_all_records()


# Longest Common Subsequence using Dynamic Programming

def lcs_length(string1, string2):
    m = len(string1)
    n = len(string2)

    # Create DP table
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


string1 = input("\nEnter first string: ")
string2 = input("Enter second string: ")

result = lcs_length(string1, string2)

print("Length of Longest Common Subsequence:", result)