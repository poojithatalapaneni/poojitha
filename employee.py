class employee:
    def __init__(emp,name,id,sal,dept):
        emp.name = name
        emp.id = id
        emp.sal = sal
        emp.dept = dept

    def display(emp):
        print(emp.name)

e = employee("kamala",'3456','345','cm')
e.display()