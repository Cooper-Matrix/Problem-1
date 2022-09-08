"Calculate"

#Given two integer numbers return their product only if the product is equal to or lower than 1000,
# else return their sum

num1 = input("enter a number: ")
num2 = input("enter a number: ")

variable = 1000
result_1 = float(num1) * float(num2)
result_2 = float(num1) + float(num2)

def problem_solver():
    if result_1 < variable:
        return result_1 , print(result_1, "result_1")
    elif result_1 > variable:
        return result_2 , print(result_2, "result_2")
result = problem_solver()


