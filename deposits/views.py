from django.shortcuts import render
from django.views.generic import ListView, DetailView
from deposits.models import Deposit



def add_deposit(request):

    if request.method == 'POST':


        add_deposit = Deposit(
            deposit=request.POST['deposit'],
            term=request.POST['term'],
            rate=request.POST['rate'],
            interest=2,
        )

        add_deposit.save()

        interest = (int(add_deposit.deposit) * (float(add_deposit.rate) + 1)) - int(add_deposit.deposit)

        context = {
            'deposit': add_deposit.deposit,
            'term': add_deposit.term,
            'rate': add_deposit.rate,
            'interest': interest,
        }

        return render(
            template_name='add_deposit.html',
            request=request,
            context=context,
        )


    return render(
        template_name='new_deposit.html',
        request=request,
        context={},
    )

class DepositsListView(ListView):
    model = Deposit
    template_name = 'deposit_list.html'



class DepositDetailView(DetailView):
    model = Deposit
    template_name = 'deposit_show.html'


