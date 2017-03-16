from django.urls import reverse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView, TemplateView
from .models import Message, Comment
from .forms import MessageForm, CommentForm
from .utils import MessageList
from django.views.decorators.http import require_http_methods


class IndexView(TemplateView):
    template_name = 'app_wall/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()

        messages_dict = MessageList.get_list()

        context['form_message'] = MessageForm()
        context['form_comment'] = CommentForm()
        context['messages_list'] = messages_dict

        return render(request, self.template_name, context)


class MessageAddView(CreateView):
    model = Message
    form_class = MessageForm
    http_method_names = ['post']

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(MessageAddView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MessageAddView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('app_wall:index')


@require_http_methods(['POST'])
def add_comment(request):
    form = CommentForm(request.POST)

    if form.is_valid():
        try:
            comment = Comment()
            comment.user = request.user
            comment.message_id = request.POST['message_id']
            comment.parent_id = request.POST['parent_id']
            comment.text = request.POST['text']
            comment.save()
        except:
            return JsonResponse({'error': 'error add comment'})

        return JsonResponse({'result': 'success'})
    else:
        return JsonResponse({'error': 'form is invalid'})

def get_content(request):
    rendered = render_to_string('app_wall/message_list.html',
                                {'messages_list': MessageList.get_list(),
                                 'request': request})
    return HttpResponse(rendered)
