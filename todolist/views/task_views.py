from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q, Case, When, Value, IntegerField

from ..models import Task
from ..forms import TaskForm


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_queryset(self):
        queryset = Task.objects.all()
        
        priority = self.request.GET.get('priority')
        if priority:
            queryset = queryset.filter(priority=priority)
        
        status = self.request.GET.get('status')
        if status == 'completed':
            queryset = queryset.filter(completed=True)
        elif status == 'pending':
            queryset = queryset.filter(completed=False)
        
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            )
        
        priority_order = Case(
            When(priority='HIGH', then=Value(4)),
            When(priority='MEDIUM', then=Value(3)),
            When(priority='LOW', then=Value(2)),
            When(priority='NONE', then=Value(1)),
            output_field=IntegerField(),
        )
        
        return queryset.annotate(priority_order=priority_order).order_by('due_data', '-priority_order')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_priority'] = self.request.GET.get('priority', '')
        context['current_status'] = self.request.GET.get('status', '')
        context['current_search'] = self.request.GET.get('search', '')
        return context


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_create.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_update.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')
    

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')
