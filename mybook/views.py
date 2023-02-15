from django.shortcuts import render,redirect

# Create your views here.
from mybook.models import books,Books
from mybook.forms import BookForm,BookModelForm,RegistrationForm,LoginForm
from django.contrib import messages
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

def signin_required(fn):
    def wrapper(request,*args,**kw):
        if not request.user.is_authenticated:
            messages.error(request,"u must login to perform this action")
            return redirect("signin")
        else:
            return fn(request,*args,**kw)
    return wrapper

@method_decorator(signin_required,name="dispatch")
class Bookview(CreateView):
    model=Books
    form_class=BookModelForm
    template_name="addbook.html"
    success_url=reverse_lazy("book-list")

    def form_valid(self, form):
        
        messages.success(self.request,"book created")
        return super().form_valid(form)

    # def get(self,request,*args,**kwargs):
    #     form=BookModelForm()
    #     return render(request,"addbook.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     form=BookModelForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,"book created")
            # ----------------------wout mf-----------------
            # bname=form.cleaned_data.get("bookname")
            # auth=form.cleaned_data.get("author")
            # pr=form.cleaned_data.get("price")
            # Books.objects.create(bookname=bname,author=auth,price=pr)
            # ---------------------------------------------------------------
            # last_bookid=books[-1].get("id")
            # id=last_bookid+1
            # form.cleaned_data["id"]=id
            # books.append(form.cleaned_data)
            # print(books)
        #     return redirect("book-list")
        # else:
        #     messages.error(request,"cant create")
        #     return render(request,"addbook.html",{"form":form})

@method_decorator(signin_required,name="dispatch")
class BooklistView(ListView):
    model=Books
    template_name="book-list.html"
    context_object_name="books"

   

    # def get(self,request,*args,**kwargs):
    #     all_books=Books.objects.all()
    #     return render(request,"book-list.html",{"books":all_books})

@method_decorator(signin_required,name="dispatch")
class BookdetailView(DetailView):
    model=Books
    template_name="book-detail.html"
    context_object_name="book"
    pk_url_kwarg:str="id"
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     book=Books.objects.filter(id=id)[0]
    #     # book=[book for book in books if book.get("id")==id].pop()
    #     return render(request,"book-detail.html",{"book":book})

@method_decorator(signin_required,name="dispatch")
class BookdeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        dlt=Books.objects.filter(id=id).delete()
        # book=[book for book in books if book.get("id")==id].pop()
        # books.remove(book)
        messages.success(request,"removed successfully")
        return redirect("book-list")

@method_decorator(signin_required,name="dispatch")
class BookeditView(UpdateView):
    model=Books
    form_class=BookModelForm
    template_name="book-update.html"
    pk_url_kwarg: str="id"
    success_url=reverse_lazy("book-list")


    def form_valid(self, form):
        messages.success(self.request,"book updated")
        return super().form_valid(form)
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     books=Books.objects.get(id=id)
    #     # book=[book for book in books if book.get("id")==id].pop()
    #     form=BookModelForm(instance=books)
    #     return render(request,"book-update.html",{"form":form})

    # def post(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     books=Books.objects.get(id=id)
    #     form=BookModelForm(request.POST,instance=books)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,"book updated")
    #         return redirect("book-list")
    #     else:
    #         messages.error(request,"cant update")
    #         return render(request,"book-update.html",{"form":form})


class RegistrationView(View):

    def get(self,request,*args,**kw):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})


    def post(self,request,*args,**kw):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"registerd successfully")
            return redirect("signin")
        else:
            messages.error(request,"registration failed")
            return render("registration.html",{"form":form})



class LoginView(View):
    def get(self,request,*args,**kw):
        form=LoginForm()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kw):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                # print("login success")
                # messages.success(request,"login successfully")
                return redirect("book-list")
            else:
                # print("login failed")
                messages.error(request,"login failed")
                return render(request,"login.html",{"form":form})   

@signin_required
def signout(request,*args,**kw):
    logout(request) 
    return redirect("signin")       