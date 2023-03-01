name = input("name: ")
filename = input("filename: ")

with open(filename, "w")as file:
    file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")
