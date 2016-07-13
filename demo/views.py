from ditto.core.views import HomeView as DittoHomeView


class HomeView(DittoHomeView):
    template_name = 'demo/home.html'

