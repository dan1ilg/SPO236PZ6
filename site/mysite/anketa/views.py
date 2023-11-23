from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, CreateView, DetailView, UpdateView, ListView
from mysite.anketa.models import Proffessia, Naviki, Myuser, Vopros, PystoiSertificat, Model_prof

item_for_page =15

###Proffessia
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProffessiaView(ListView):
  model = Proffessia
  context_object_name = 'proffessia_list'
  success_url = reverse_lazy('anketa: Proffessia')

  paginate_by = item_for_page
  def get_context_data(self, *, object_list=None, **kwargs):
    context = super(ProffessiaView,self).get_context_data(**kwargs)
    context['sometry'] = self.model._meta.verbose_name_plural
    context['col1name'] = self.model._meta.get_field("title").verbose_name
    context['collastname'] = 'Cервисы'
    return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProffessiaUpdate(UpdateView):
	model = Proffessia
	template_name_suffix = '_update_form'
	fields = '__all__'
	success_url = '/anketa/proffessia/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(ProffessiaUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProffessiaDetail(DetailView):
	model = Proffessia
	context_object_name = 'proffessia_one'
	success_url = '/anketa/proffessia/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(ProffessiaDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProffessiaCreate(CreateView):
	model = Proffessia
	context_object_name = 'proffessia_one'
	success_url = '/anketa/proffessia/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(ProffessiaCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProffessiaDelete(DeleteView):
	model = Proffessia
	success_url = '/anketa/proffessia/'

###Naviki
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NavikiView(ListView):
  model = Naviki
  context_object_name = 'naviki_list'
  success_url = reverse_lazy('anketa: Naviki')

  paginate_by = item_for_page
  def get_context_data(self, *, object_list=None, **kwargs):
    context = super(NavikiView,self).get_context_data(**kwargs)
    context['sometry'] = self.model._meta.verbose_name_plural
    context['col1name'] = self.model._meta.get_field("title").verbose_name
    context['collastname'] = 'Cервисы'
    return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NavikiUpdate(UpdateView):
	model = Naviki
	template_name_suffix = '_update_form'
	fields = '__all__'
	success_url = '/anketa/naviki/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(NavikiUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NavikiDetail(DetailView):
	model = Naviki
	context_object_name = 'naviki_one'
	success_url = '/anketa/naviki/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(NavikiDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NavikiCreate(CreateView):
	model = Naviki
	context_object_name = 'naviki_one'
	success_url = '/anketa/naviki/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(NavikiCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NavikiDelete(DeleteView):
	model = Naviki
	success_url = '/anketa/naviki/'


###Vopros
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class VoprosView(ListView):
  model = Vopros
  context_object_name = 'vopros_list'
  success_url = reverse_lazy('anketa: Vopros')

  paginate_by = item_for_page
  def get_context_data(self, *, object_list=None, **kwargs):
    context = super(VoprosView,self).get_context_data(**kwargs)
    context['sometry'] = self.model._meta.verbose_name_plural
    context['col1name'] = self.model._meta.get_field("title").verbose_name
    context['col2name'] = self.model._meta.get_field("naviki").verbose_name
    context['col3name'] = self.model._meta.get_field("ball").verbose_name
    context['collastname'] = 'Cервисы'
    return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class VoprosUpdate(UpdateView):
	model = Vopros
	template_name_suffix = '_update_form'
	fields = '__all__'
	success_url = '/anketa/vopros/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(VoprosUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title','naviki','ball'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class VoprosDetail(DetailView):
	model = Vopros
	context_object_name = 'vopros_one'
	success_url = '/anketa/vopros/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(VoprosDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title','naviki','ball'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class VoprosCreate(CreateView):
	model = Vopros
	context_object_name = 'vopros_one'
	success_url = '/anketa/vopros/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(VoprosCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title','naviki','ball'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class VoprosDelete(DeleteView):
	model = Vopros
	success_url = '/anketa/vopros/'


###PystoiSertificat
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class PystoiSertificatView(ListView):
  model = PystoiSertificat
  context_object_name = 'pystoisertificat_list'
  success_url = reverse_lazy('anketa: PystoiSertificat')

  paginate_by = item_for_page
  def get_context_data(self, *, object_list=None, **kwargs):
    context = super(PystoiSertificatView,self).get_context_data(**kwargs)
    context['sometry'] = self.model._meta.verbose_name_plural
    context['col1name'] = self.model._meta.get_field("title").verbose_name
    context['col2name'] = self.model._meta.get_field("full").verbose_name
    context['col3name'] = self.model._meta.get_field("one").verbose_name
    context['collastname'] = 'Cервисы'
    return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class PystoiSertificatUpdate(UpdateView):
	model = PystoiSertificat
	template_name_suffix = '_update_form'
	fields = '__all__'
	success_url = '/anketa/pystoisertificat/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(PystoiSertificatUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title','full','one'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class PystoiSertificatDetail(DetailView):
	model = PystoiSertificat
	context_object_name = 'pystoisertificat_one'
	success_url = '/anketa/pystoisertificat/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(PystoiSertificatDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title','full','one'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class PystoiSertificatCreate(CreateView):
	model = PystoiSertificat
	context_object_name = 'pystoisertificat_one'
	success_url = '/anketa/pystoisertificat/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(PystoiSertificatCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title','full','one'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class PystoiSertificatDelete(DeleteView):
	model = PystoiSertificat
	success_url = '/anketa/pystoisertificat/'


###Model_prof
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Model_profView(ListView):
  model = Model_prof
  context_object_name = 'model_prof_list'
  success_url = reverse_lazy('anketa: Model_prof')

  paginate_by = item_for_page
  def get_context_data(self, *, object_list=None, **kwargs):
    context = super(PModel_profView,self).get_context_data(**kwargs)
    context['sometry'] = self.model._meta.verbose_name_plural
    context['col1name'] = self.model._meta.get_field("title").verbose_name
    context['col2name'] = self.model._meta.get_field("Proffessia").verbose_name
    context['col3name'] = self.model._meta.get_field("Naviki").verbose_name
    context['col4name'] = self.model._meta.get_field("ball").verbose_name
    context['collastname'] = 'Cервисы'
    return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Model_profUpdate(UpdateView):
	model = Model_prof
	template_name_suffix = '_update_form'
	fields = '__all__'
	success_url = '/anketa/model_prof/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(Model_profUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title','Proffessia','Naviki','ball'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Model_profDetail(DetailView):
	model = Model_prof
	context_object_name = 'model_prof_one'
	success_url = '/anketa/model_prof/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(Model_profDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title','Proffessia','Naviki','ball'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Model_profCreate(CreateView):
	model = Model_prof
	context_object_name = 'model_prof_one'
	success_url = '/anketa/model_prof/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(Model_profCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'title','Proffessia','Naviki','ball'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Model_profDelete(DeleteView):
	model = Model_prof
	success_url = '/anketa/model_prof/'