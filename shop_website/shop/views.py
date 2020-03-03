from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Product
from .forms import ProductCreationForm,CollectionCreationForm
from django.shortcuts import redirect
from django import forms





class ProductListView(ListView):
	model = Product
	template_name = 'shop/home.html'
	context_object_name = 'products'
	paginate_by = 12	

class ProductCreateView(CreateView):
	model = Product
	fields = ['name', 'price','description', 'photo']

	def form_valid(self, form):
		return super().form_valid(form)

def about(request):
	return render(request, 'shop/about.html')



def collection(request):
	if request.method == 'POST':
		form = CollectionCreationForm()
		if form.is_valid():
			form = CollectionCreationForm(request.POST, instance=request.collection)
			form.save()
	else:
		form = CollectionCreationForm()
	context = {'form': form}
	return render(request, 'shop/collection.html', context)








# def product_creation_view(request):

# 	if request.method == 'POST':
# 		form = ProductCreationForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('product-list')

# 	else:
# 		form = ProductCreationForm()
# 	return render(request, 'shop/product_form.html', {'form': form})