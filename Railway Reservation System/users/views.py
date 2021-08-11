from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
import random 

train_data = ''
def register(request):
    if request.method == 'POST':
 
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            messages.success(request,f'your account has been created, You are now able to login')
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance= request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"Your Profile has been Updated")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance= request.user)
        p_form = ProfileUpdateForm(instance= request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)
    
def ticketbook(request):
    if request.method == 'POST':
 
        form = TicketBookingForm(request.POST)
        
        if form.is_valid():
            day = form.cleaned_data['date'].weekday()
            train_source =  form.cleaned_data['source']
            train_source = train_source.upper()
            train_destination = form.cleaned_data['destination']
            train_destination = train_destination.upper()
            selected_class = form.cleaned_data['select_class']
            request.session['class'] = selected_class
            request.session['date'] = str(form.cleaned_data['date']) 
            source_data = Train.objects.filter(source = train_source, destination = train_destination,running_days__contains = day).values()
            data = []
            for train in source_data:
                if train[selected_class] >= 1:
                    print(train[selected_class])
                    train['booked_class']=train[selected_class]
                    data.append(train)
                    print(data)
            return render(request, 'users/select_train.html', {'trains' : data}) 
    else:
        form = TicketBookingForm()
    context = {
                'form' : form
            }
    return render(request, 'users/ticket_booking.html', context)

def train(request):
    context = {
        'train' : train_data
    }
    print('in the train',context)
    return render(request, 'users/select_train.html', context)
    
def cancel(request):
    reservations = Booking.objects.filter(user = request.user.profile,status = True).values('pnr','date','train_number','train_name','source','destination','number_of_seats').distinct()
    return render(request,'users/cancel_ticket.html',  {'reservations':reservations})

def cancel_reservation(request,pnr):
    cancel = Booking.objects.filter(user= request.user.profile,pnr = pnr,status = True).first()
    cancel.status = False
    cancel.save()
    messages.success(request,f"Your booking of PNR Number {pnr} is cancelled")
    return redirect('cancel')

def booking_history(request):
    reservations = Booking.objects.filter(user = request.user.profile).values('pnr','date','train_number','train_name','source','destination','number_of_seats','status').distinct()
    return render(request,'users/booking_history.html',  {'reservations':reservations})

def passenger(request,train_number):
    if request.method == "POST":
        train = get_object_or_404(Train, train_number=train_number)
        print("train num is :",train)
        form = PassengerDetailsForm(request.POST)
		
        if form.is_valid():
            passenger_name = form.cleaned_data['name']
            passenger_age = form.cleaned_data['age']
            passenger_gender = form.cleaned_data['gender']
            passenger_total = form.cleaned_data['total_passengers']
            passenger_class = request.session['class']
            total_price = 0
            booking_date = request.session['date']
            train_data = Train.objects.filter(train_number = train_number).values()[0]
            if train_data[passenger_class] <=passenger_total:
                return redirect('home')
            if passenger_class == 'ac_class':
                passenger_class = 'AC'
                total_price = passenger_total * 50 
            elif passenger_class == 'sleeper_class':
                passenger_class = 'SL'
                total_price = passenger_total * 100
            elif passenger_class == 'second_sitting_class':
                passenger_class = '2S'
                total_price = passenger_total * 150
            elif passenger_class == 'first_class':
                 passenger_class = 'FC'
                 total_price = passenger_total * 200
            else :
                passenger_class = 'EC' 
                total_price = passenger_total * 250

            
            print ('session is',request.session['class'])
            context = {
                'train_number' : train_number,
                'passenger_name' : passenger_name,
                'age' : passenger_age,
                'passenger_gender' : passenger_gender,
                'passenger_seats' : passenger_total,
                'train_data' : train_data,
                'passenger_class' : passenger_class,
                'date' : booking_date,
                'total_price' : total_price
            }
            print(train_data)
            return render(request, 'users/payment.html', context)
            
            
    else:       
        form = PassengerDetailsForm()
     
    return render(request, 'users/passenger_details.html', {'form' : form})

def payment(request):
    if(request.method=='POST'):
        dt=request.POST['date']
        src=request.POST['src']
        des=request.POST['des']
        tno=request.POST['bk']
        cls = request.POST['cls'+str(tno)]
        nos=request.POST['nos'+str(tno)]
        pr=request.POST['price'+str(tno)]
        tname=Train.objects.get(tno=tno).tname
        price = int(pr) * int(nos)
        return render(request,'users/payment.html',{'price': price,'dt':dt,'cls':cls,'tno':tno,'nos':nos,'tname':tname,'src':src,'des':des,'payment' : payment})

    return render(request, 'users/payment.html')

def booking_confirm(request):
    if request.method=='POST':
        a = request.POST
        print(a)
        nos=int(request.POST['nos'])
        tno=request.POST['tno']
        dt=request.POST['date']
        cls=request.POST['cls']
        tname=request.POST['tname']
        src=request.POST['src'] 
        des=request.POST['des']
        price=str(request.POST['price'])
        print(tno)
        print(src)
        pnr = random.randint(0,999999)
        booking_data = Booking.objects.create(pnr = pnr,date = dt, train_number = tno, user = request.user.profile, train_name = tname, source = src, destination = des, number_of_seats = nos, booking_class = cls, status = True )
        seats_remain= Train.objects.filter(train_number = tno).values().first()
        seat_class = cls
        print(seats_remain['ac_class'])
        if seat_class == 'AC':
            seat_class = 'ac_class'
            seat = seats_remain['ac_class'] - nos
            Train.objects.filter(train_number = tno).update(ac_class =seat)
        elif seat_class == 'SL':
            seat_class = 'sleeper_class'
            seat = seats_remain['sleeper_class'] - nos
            Train.objects.filter(train_number = tno).update(sleeper_class = seat)   
        elif seat_class == '2S':
            seat_class = 'second_sitting_class'
            seat = seats_remain['second_sitting_class'] - nos
            Train.objects.filter(train_number = tno).update(second_sitting_class = seat)    
        elif seat_class == 'FC':
            seat_class = 'first_class'
            seat = seats_remain['first_class'] - nos
            Train.objects.filter(train_number = tno).update(first_class = seat)    
        else :
            seat_class = 'executive_chair_class'
            seat = seats_remain['executive_chair_class'] - nos
            Train.objects.filter(train_number = tno).update(executive_chair_class = seat)
        print(seats_remain,seat_class)
        return render(request,"users/booking_confirm.html",{'tname':tname,'date':dt,'tno':tno,'date':dt,'src':src,'des':des,'cls':cls,'pnr':pnr,'nos':nos,'dt':dt})
    return render(request, 'users/booking_confirm.html')