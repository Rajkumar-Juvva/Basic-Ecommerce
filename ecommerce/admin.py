from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

class MyAdminSite(admin.AdminSite):
    site_title = 'My Site Admin'
    site_header = 'My Site Administration'

    def get_app_list(self, request):
        app_dict = self._build_app_dict(request)
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
        # print(app_list,app_dict)
        for app in app_list:
            app['models'].sort(key=lambda x: x['name'])
            for model in app['models']:
                model['admin_url'] = reverse('admin:%s_%s_changelist' % (model['app_label'], model['model_name']))
                model['add_url'] = reverse('admin:%s_%s_add' % (model['app_label'], model['model_name']))
                model['view_link'] = format_html('<a href="{}">View</a>', model['admin_url'])
                model['add_link'] = format_html('<a href="{}">Add</a>', model['add_url'])
        return app_list
    def has_module_permission(self,request):
        return True

admin_site = MyAdminSite(name='myadmin')