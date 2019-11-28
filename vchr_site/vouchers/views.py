'''Module to render the html template with form for entering voucher code'''
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from vouchers.forms import VchrForm
from vouchers.models import Voucher

# render the code form
def render_form(request):
    '''
    This function renders the form inside the html template.
    When a GET request is sent, it will render the voucher status page if the voucher code is valid

    '''

    # init form
    form = VchrForm()

    # For when form is submitted
    submit_form = VchrForm(request.GET)

    # If the form is valid, return the voucher status page
    if submit_form.is_valid():

        # Retrieve code input from form
        vchr_code = submit_form.cleaned_data['code_input']

        # Check if code exist in model, if exist: return voucher status page,
        # if not: voucher not found page
        if Voucher.objects.filter(code_field=vchr_code).exists():

            # create dictionary for voucher information to be displayed in
            # voucher status page
            context = {
                'code': vchr_code,
                'status': Voucher.objects.get(code_field=vchr_code).validate(),
                'discount': Voucher.objects.get(code_field=vchr_code).discount_rate(),
                'acceptance': Voucher.objects.get(code_field=vchr_code).accept()
            }

            # load html for voucher status page
            template_stat = loader.get_template('vouchers/voucher_status.html')

            return HttpResponse(template_stat.render(context, request))

        # load html for voucher not found
        template_not_found = loader.get_template('vouchers/voucher_not_found.html')

        return HttpResponse(template_not_found.render())

    return render(request, 'vouchers/vouchers.html', {'form':form})
