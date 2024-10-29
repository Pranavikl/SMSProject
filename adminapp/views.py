import matplotlib
from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'adminapp/index.html')


def printpagecall(request):
    return render(request, 'adminapp/printer.html')


def printpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
    a1 = {'user_input': user_input}
    return render(request, 'adminapp/printer.html', a1)


def exceptionpagecall(request):
    return render(request, 'adminapp/ExceptionExample.html')


def exceptionpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        result = None
        error_message = None
        try:
            num = int(user_input)
            result = 10 / num

        except Exception as e:
            error_message = str(e)
        return render(request, 'adminapp/ExceptionExample.html', {'result': result, 'error': error_message})
    return render(request, 'adminapp/ExceptionExample.html')


import string
import random


def randompagecall(request):
    return render(request, 'adminapp/RandomExample.html')


def randomlogic(request):
    if request.method == "POST":
        number1 = int(request.POST['number1'])
        ran = ''.join(random.sample(string.ascii_uppercase + string.digits, k=number1))
    a1 = {'ran': ran}
    return render(request, 'adminapp/RandomExample.html', a1)


def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminapp/calculator.html', {'result': result})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')

    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'adminapp/add_task.html', {'form': form, 'tasks': tasks})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')


def register(request):
    return render(request, 'adminapp/register.html')


def login(request):
    return render(request, 'adminapp/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

from datetime import datetime, timedelta
from django.shortcuts import render


def daytimepagecall(request):
    return render(request, 'adminapp/daytime.html')


def daytimepagelogic(request):
    if request.method == 'POST':
        number1 = int(request.POST['date1'])
        x = datetime.now()
        ran = x + timedelta(days=number1)
        a1 = {'ran': ran}
        return render(request, 'adminapp/daytime.html', a1)
    else:
        return render(request, 'adminapp/daytime.html')  # Handle non-POST requests


from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render


def UserRegisterPageCall(request):
    return render(request, 'adminapp/register.html')


def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created successfully!')
                return redirect('index')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/register.html')
    else:
        return render(request, 'adminapp/register.html')


def UserLoginPageCall(request):
    return render(request, 'adminapp/login.html')


def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check the length of the username
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/login.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/login.html')
    else:
        return render(request, 'adminapp/login.html')



from .forms import StudentForm
from .models import StudentList


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})


def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student_list.html', {'students': students})

#  ============== CSV TASK ===============

import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from django.shortcuts import render
matplotlib.use('Agg')


def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        # Read the CSV file
        df = pd.read_csv(file, parse_dates=['Date'], dayfirst=True)

        # Calculate total and average sales
        total_sales = df['Sales'].sum()
        average_sales = df['Sales'].mean()

        # Add a 'Month' column and calculate monthly sales
        df['Month'] = df['Date'].dt.month
        monthly_sales = df.groupby('Month')['Sales'].sum()

        # Month names for labels
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        monthly_sales.index = monthly_sales.index.map(lambda x: month_names[x - 1])

        # Plot the pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(monthly_sales, labels=monthly_sales.index, autopct='%1.1f%%', startangle=90)
        plt.title('Sales Distribution Per Month')

        # Save the plot to a buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        # Convert to base64 to send to the template
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        plt.close()

        # Pass data to the template
        context = {
            'total_sales': total_sales,
            'average_sales': average_sales,
            'monthly_sales': monthly_sales.to_dict(),
            'chart': image_data,
        }
        return render(request, 'adminapp/chart.html', context)

    return render(request, 'adminapp/chart.html')


from django.shortcuts import render, redirect
from .forms import FeedbackForm


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save feedback to the database
            return redirect('feedback_thanks')  # Redirect after successful submission
    else:
        form = FeedbackForm()

    return render(request, 'adminapp/feedback_form.html', {'form': form})


def feedback_thanks(request):
    return render(request, 'adminapp/feedback_thanks.html')
