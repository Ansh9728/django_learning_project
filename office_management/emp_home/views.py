from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.template import loader
from .models import Employee, Department, Role, EmployeeForm
from django.contrib.auth.decorators import login_required
import datetime


# Create your views here.
@login_required(login_url='/login')
def index(request):
    return render(request, "index.html")

def add_employee(request):
    
    if request.method =='POST':
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        department_id = int(request.POST['department'])  # Get department_id from form
        role_id = int(request.POST['role'])  # Get role_id from form

        try:
            department = Department.objects.get(id=department_id)
        except Department.DoesNotExist:
            return HttpResponse("Department Not Found")
        

        try:
            role = Role.objects.get(id=role_id)

        except Role.DoesNotExist:
            return HttpResponse("Role Not Found")

        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])


        hire_date = datetime.datetime.now()

        new_emp = Employee(
            first_name=first_name,
            last_name=last_name,
            department = department,
            salary=salary,
            bonus=bonus,
            role=role,
            hire_date = hire_date
        )

        new_emp.save()

        return HttpResponse(f"Data Stored Succufully")
    
    elif request.method=="GET":
        return render(request, "html//add_employee.html")
    
    else:
        return HttpResponse("Exception occured")


def delete_emp(request, emp_id=0):

    try:
        if emp_id:
            emp_to_remove = Employee.objects.get(id=emp_id)
            emp_to_remove.delete()
            return HttpResponse("Employe Delete Succussfully")

    except:
        HttpResponse("Please Enter a Valid Employee Id")

    emps = Employee.objects.all()
    emps = {
        "emps":emps
    }
    return render(request, "html\\delete_emp.html", context=emps)


def update_emp(request, emp_id=0):
    # If emp_id is provided, we want to update that employee
    if emp_id:
        emp = get_object_or_404(Employee, id=emp_id)

        # Handle form submission
        if request.method == 'POST':
            form = EmployeeForm(request.POST, instance=emp)
            if form.is_valid():
                form.save()  # Save the updated employee data
                return HttpResponse("Data updated successfully!")
            else:
                return HttpResponse("Error in updating the data")
        else:
            form = EmployeeForm(instance=emp)  # Pre-fill the form with existing employee data

        return render(request, 'html/update_emp.html', {'form': form, 'emp_id': emp_id})

    # If emp_id is not provided, display all employees
    emps = Employee.objects.all()
    return render(request, 'html/update_emp.html', {'emps': emps})


# def read(request):
#     return render(request, "html\\delete_emp")

