from django.shortcuts import render
from .models import TodoModel
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView,FormView
from django.urls import reverse_lazy,reverse
from django.db.models import Max
from django.http import HttpResponseRedirect

class HomeView(ListView):
    model=TodoModel
    template_name='home.html'
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['lists']=TodoModel.objects.order_by('category','id')
        context['detail']=TodoModel.objects.all()[0]
        
        return context

class HomeUpdate(UpdateView):
    model=TodoModel
    template_name='home.html'
    fields=['content']
    
    def get_success_url(self):
        todo_id=self.kwargs['pk']
        return reverse('homeupdate',kwargs={'pk':todo_id})
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['lists']=TodoModel.objects.order_by('category','id')
        context['detail']=TodoModel.objects.get(id=self.kwargs['pk'])
        return context
    
class TodoView(ListView):
    model=TodoModel
    template_name='list.html'

class Detail(DetailView):
    model=TodoModel
    template_name='detail.html'
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        todo_id=self.kwargs['pk']
        context['todo_id']=todo_id
        return context
    
class TodoCreateView(CreateView):#adminフォームに似た要領で作成
    model=TodoModel
    template_name='create.html'
    fields=['title','content','pic']
   
    def get_success_url(self):
        #idの最高値を取得することで直接詳細ページにリダイレクト
        todo_id=TodoModel.objects.all().aggregate(Max('id'))
        return reverse('detail',kwargs={'pk':todo_id['id__max']})
    
class TodoDelete(DeleteView):
    model=TodoModel
    template_name='delete.html'
    success_url=reverse_lazy('list')
    
class TodoUpdateView(UpdateView):
    model=TodoModel
    template_name='update.html'
    fields=['title','content','pic']
   
    def get_success_url(self):
        todo_id=self.kwargs['pk']
        return reverse('detail',kwargs={'pk':todo_id})
        
        
