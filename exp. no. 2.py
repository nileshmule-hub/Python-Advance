def report_decorator(func):
    def wrapper(*args, **kwargs):
        print("=" * 60)
        print("DYNAMIC REPORT GENERATOR")
        print("=" * 60)
        
        func(*args, **kwargs)
        print("=" * 60)
        print("END OF REPORT")
        print("=" * 60)
        
        return wrapper



class Report:
    company_name = "Nil Technologies Pvt. Ltd."
def __init__(self, title, author):
    self.title = title
    self.author = author
    self.contents = []
    
    
def add_content(self, text):
    self.contents.append(text)
    
    
@classmethod
def change_company(cls, new_company):
    cls.company_name = new_company
    
@staticmethod
def line():
        print("-" * 60)
        
def __str__(self):
 return (
            f"Report Title : {self.title}\n"
            f"Author       : {self.author}"
        )
 
def __len__(self):
    return len(self.contents)

@report_decorator
def display_report(self):
    print("Company :", Report.company_name)
    print(self)
    Report.line()
    
    print("Report Contents:")
    
    
    Report.line()
    
    print("Total Sections :", len(self))
    
r1 = Report(
    "Advanced Python Practical Report",
    "Nilesh Mule"
)

r1.add_content("Completed Experiment No. 2 successfully.")

r1.add_content("Implemented Decorators, Class Methods, Static Methods and Magic Methods.")

r1.add_content("Learned Object-Oriented Programming concepts.")

r1.add_content("Report prepared by Nilesh Mule.")

r1.display_report()

print("\nChanging Company Name...\n")

Report.change_company("MIT ADT University")

r2 = Report("Faculty Practical Demonstration","Nilesh")

r2.add_content("Practical demonstrated successfully.")

r2.add_content("Students understood decorators.")

r2.add_content("Students understood class methods.")

r2.add_content("Students understood magic methods.")

r2.add_content("Students performed the practical successfully.")

r2.display_report()