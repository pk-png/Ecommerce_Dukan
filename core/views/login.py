from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect
from core.models.customer import Customer
from django.contrib.auth.hashers import check_password

# ......... login pages .........
class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')


    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_massage = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id  # (sm code-2)   this is use when user login then take customer object and chack condition base.html  
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage',)
            else:
                error_massage = "Please Enter Valid Email or Password !!"
        else:
            error_massage = "Please Enter Valid Email or Password"
        return render(request, 'login.html', {'error':error_massage})


def logout(request):
    request.session.clear()
    return redirect('login')
