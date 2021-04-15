# demonstrate template string functions
from string import Template

def main():
    # Usual string formatting with format()
    str1 = "Das ist der Kurs '{0}' von {1}".format("Fortgeschrittene Python-Techniken", "Joe Marini und Ralph Steyer")
    print(str1)
    
    # TODO: create a template with placeholders
    templ = Template("Das ist der Kurs '${title}' von ${authors}")
    
    # TODO: use the substitute method with keyword arguments
    str2 = templ.substitute(title="Fortgeschrittene Python-Techniken", authors="Joe Marini und Ralph Steyer")
    print(str2)
    
    # TODO: use the substitute method with a dictionary
    data = {
        "authors":"Joe Marini und Ralph Steyer",
        "title":"Fortgeschrittene Python-Techniken"

    }
    str3 = templ.substitute(data)
    print(str3)

    
if __name__ == "__main__":
    main()
    