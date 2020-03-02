from django.views import generic
from .models import Post, Department, STAGE


class PostList(generic.ListView):
    #template name
    
    template_name = 'index.html'
    queryset = Post.objects.filter(status=1).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs) 
        list_of_case_studies = Post.objects.filter(status=1,type='featured').order_by('-created_on')
        context['list_of_case_studies'] = list_of_case_studies[:5]
        return context


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class DepartmentDetail(generic.DetailView):
    model = Department
    template_name = 'department_details.html'

    def get_context_data(self, **kwargs):
        context = super(DepartmentDetail, self).get_context_data(**kwargs)
        return context


class DepartmentList(generic.ListView):
    model = Department
    template_name = 'departments.html'
    

    def get_context_data(self, *args, **kwargs):
        context = super(DepartmentList, self).get_context_data(**kwargs)
        post_list = Post.objects.filter(status=1).order_by('-created_on')[:3]
        context['post_list'] = post_list
        return context
