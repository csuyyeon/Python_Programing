def print_str(string, num_times):
    for _ in range(num_times):
        print(string)

string = input("Enter a string: ")
num_times = int(input("Enter the number of times: "))
print_str(string, num_times)
