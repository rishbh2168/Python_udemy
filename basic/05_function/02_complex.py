def fetch_report():
    print("report fetch")

def filter_data():
    print("data is filter")

def sumarrize_data():
    print("data is summarize")

def generate_report():    # main function
    fetch_report()             # caling sub function
    filter_data()
    sumarrize_data()
    print("report is generated")

generate_report()   # caling main function