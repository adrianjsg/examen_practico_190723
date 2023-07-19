from employee import Employee

if __name__ == '__main__':
    employee = Employee("John Doe", 5000)
    current_salary = employee.get_salary()
    print(f"Salario actual: {current_salary}")

    new_salary = 6000
    employee.change_salary(new_salary)
    updated_salary = employee.get_salary()
    print(f"Salario actualizado: {updated_salary}")

from employee import Employee

if __name__ == '__main__':
    # Instanciar la clase Employee
    employee = Employee("Juan Garcia", 5000)

    # Obtener el salario del empleado
    current_salary = employee.get_salary()
    print(f"Salario actual: {current_salary}")

    # Cambiar el salario del empleado
    new_salary = 6000
    employee.change_salary(new_salary)

    # Obtener el nuevo salario del empleado
    updated_salary = employee.get_salary()
    print(f"Salario actualizado: {updated_salary}")

