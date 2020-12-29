from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt['username'] = 'りつ'
        return ctxt

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt['num_services'] = 1145141919
        ctxt['skills'] = [
            'python',
            'java',
            'ruby',
        ]
        return ctxt
