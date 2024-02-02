from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from .forms import FormFacturaForm
from django.contrib import messages
 
# Create your views here.
 
 #formulario
def form_factura(request):
    form = FormFacturaForm(request.POST or None)
    if form.is_valid():
        form.save()		
        messages.success(request, 'Factura insertada correctamente.')
        form = FormFacturaForm()
    else:
        messages.error(request, 'Error al insertar factura. Revise los datos.')
    context = {'form': form }      
    return render(request, 'contact.html', context)