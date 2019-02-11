from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout
from .form import UserReg, UserLog, MessageForm
from .models import Person,Userinfo, Chatbox
from django.contrib.auth.models import User


class Homepage(View):
    form_class = UserLog
    template_name = 'permit/homepage.html'

    def get(self, request, person_id):
        # person = Person.objects.all()
        # for item in person:
        #     if item.username == "pankaj":
        #         current_user = item.username
        cur = str(request.user)
        context = {'current_user': cur}
        return render(request, self.template_name, context)

class UserRegView(View):
    form_class = UserReg
    template_name = 'permit/register.html'
    current_user = ''

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #cleaned (normalized) form

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            user.set_password(password)
            user.save()
            per = Person(username, email, password)
            per.save()
            current_user = per
            #return user object if credentials are correct

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    django_login(request, user)
                    return redirect('/permit/profile/' + str(current_user.username) + '/')

        return render(request, self.template_name, {'form': form})


class UserLogView(View):
    form_class = UserLog
    template_name = 'permit/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        #form = self.form_class(request.POST)

        #if form.is_valid():
            #user = form.save(commit=False)


            #cleaned (normalized) form

        username = request.POST["username"]
        password = request.POST["password"]
            #user.set_password(password)
            #user.save()

            #return user object if credentials are correct

        user = authenticate(username=username, password=password)

        if user is not None:

             if user.is_active:
                  django_login(request, user)
                  return redirect('/permit/profile/' + str(username) + '/')

        return render(request, self.template_name)


class LogoutView(View):
    template_name = 'permit/logout.html'

    def get(self, request):
        logout(request)
        return render(request, self.template_name)


class Messages(View):
    form_class = MessageForm
    template_name = "permit/message.html"

    def get(self, request, person_id):
        chatbox = Chatbox.objects.all()
        current_user = str(request.user)
        context = {'chatbox': chatbox, 'current_user': current_user}
        return render(request, self.template_name, context)

    def post(self, request, person_id):
        form = self.form_class(request.POST)
        chatbox = Chatbox.objects.all()
        current_user = str(request.user)
        context = {'chatbox': chatbox, 'current_user': current_user}


        if form.is_valid():
            msg = form.save(commit=False)

            # cleaned (normalized) form

            # sender = form.cleaned_data["sender"]
            message = form.cleaned_data["message"]
            chat = Chatbox(sender=str(request.user), receiver=str(request.user), message=message)
            chat.save()
            return render(request, self.template_name, context, {'form': form})

        return render(request, self.template_name, context, {'form': form})




