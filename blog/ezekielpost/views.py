from django.views import generic
from .models import Post, Department, STAGE


class PostList(generic.ListView):

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

    # def get_context_data(self, **kwargs):
    #     context = super(PostDetail, self).get_context_data(**kwargs)
    #
    #     # related_post = Post.objects.filter(stage__iexact=context['object'].stage).filter(
    #     #     department__name__iexact=context['object'].department.name).exclude(id=context['object'].id)[:5]
    #     related_post = Post.objects.filter(
    #         department__name__iexact=context['object'].department.name).exclude(id=context['object'].id)[:5]
    #
    #     context['related_post'] = related_post
    #     return context


class DepartmentDetail(generic.DetailView):
    model = Department
    template_name = 'department_details.html'

    def get_context_data(self, **kwargs):
        context = super(DepartmentDetail, self).get_context_data(**kwargs)

        # related_post = Post.objects.filter(stage__iexact=context['object'].stage).filter(
        #     department__name__iexact=context['object'].department.name).exclude(id=context['object'].id)[:5]
        # related_post = Post.objects.filter(
        #     department__name__iexact=context['object'].department.name).exclude(id=context['object'].id)[:5]
        #
        # context['related_post'] = related_post
        return context


class DepartmentList(generic.ListView):
    model = Department
    template_name = 'departments.html'
