from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm, DepositForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User 
from django.db import IntegrityError
from django.http import HttpResponse 
from .models import Deposit,Balance
from django.db.models import Sum
from django.contrib.auth import logout as django_logout

from django.db import transaction 

#home page
def home(request):
    return render(request, 'base.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage', user=user.username)
    else:
        form = AuthenticationForm()
    return render(request, 'customerlogin.html', {'form': form})

#signup page
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            form = User.objects.create_user(username, email, password)
            return redirect('login')
        except IntegrityError as e:
            return render(request, 'customersignup.html', {'error': 'username already exists'})
    else:
        form = SignupForm()
    return render(request, 'customersignup.html', {'form': form})

#account details home page
def homepage(request, user):
    return render(request, 'homepage.html', {'user': user})


#deposit page
def deposit(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            form.save()
            # Fetch the last deposit from the database
            total = Deposit.objects.aggregate(total=Sum('amount'))['total'] 
            return render(request,'depositform.html',{'total':total})
    else:
        form = DepositForm()
    return render(request, 'depositform.html', {'form': form})



#withdrawal page
def withdrawal(request):
    # Calculate the sum of deposit amounts
    sum_of_deposits = Deposit.objects.aggregate(total=Sum('amount'))['total']

    # Retrieve or create the Balance object (assuming there's only one)
    balance_instance, _ = Balance.objects.get_or_create(id=1)

    # Update the balance field with the sum of deposits
    balance_instance.balance = sum_of_deposits

    # Save the changes to the Balance object
    balance_instance.save()


    if request.method == 'POST':
        amount = float(request.POST.get('amount', 0))  
        user_balance = Balance.objects.get(user=request.user)
        balance = user_balance.balance - amount
        if amount <= 0:
            return render(request, 'withdrawalform.html', {'error': 'Amount must be greater than 0'})
        elif balance < 0:
            return render(request, 'withdrawalform.html', {'error': 'Insufficient balance'})

        # Update balance
        with transaction.atomic():
            user_balance.balance = balance
            user_balance.save()

        return render(request, 'withdrawalform.html', {'error1': 'Withdrawal success'})  # Render a success page or redirect as needed
    else:
        return render(request, 'withdrawalform.html')


def checkbalance(request):
        data =Balance.objects.aggregate(total=Sum('balance'))['total']
        return render(request,'checkbalance.html',{'data':data})



#logout page
def logout(request):
    if request.method == 'POST':
        django_logout(request)
        return redirect('login')

    context = {
        'user': request.user
    }

    return render(request, 'logout.html', context)