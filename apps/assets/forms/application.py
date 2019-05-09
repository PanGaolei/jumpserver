# -*- coding: utf-8 -*-
#

from django.utils.translation import ugettext as _
from django import forms

from orgs.mixins import OrgModelForm
from ..models import Application, Asset, SystemUser
from .. import const

__all__ = [
    'ApplicationCreateUpdateForm',
]


class ApplicationBrowserParamsForm(forms.ModelForm):

    browser_path = forms.CharField(
        label=_('App path'), max_length=100, required=False
    )
    browser_target = forms.CharField(
        label=_('Target url'), max_length=100, required=False
    )
    browser_username = forms.CharField(
        label=_('Login username'), max_length=100, required=False
    )
    browser_password = forms.CharField(
        label=_('Login password'), max_length=100, required=False
    )

    def clean_browser_path(self):
        return self.clean_app_field_or_raise(
            'browser_path', const.APP_TYPE_BROWSER_LIST
        )

    def clean_browser_target(self):
        return self.clean_app_field_or_raise(
            'browser_target', const.APP_TYPE_BROWSER_LIST
        )


class ApplicationDBParamsForm(forms.ModelForm):

    db_path = forms.CharField(
        label=_('App path'), max_length=100, required=False
    )
    db_ip = forms.CharField(
        label=_('Database IP'), max_length=100, required=False
    )
    db_name = forms.CharField(
        label=_('Database name'), max_length=100, required=False
    )
    db_username = forms.CharField(
        label=_('Database username'), max_length=100, required=False
    )
    db_password = forms.CharField(
        label=_('Database password'), max_length=100, required=False
    )

    def clean_db_path(self):
        return self.clean_app_field_or_raise('db_path', const.APP_TYPE_DB_LIST)


class ApplicationVMwareParamsForm(forms.ModelForm):

    vmware_path = forms.CharField(
        label=_('App path'), max_length=100, required=False
    )
    vmware_target = forms.CharField(
        label=_('Target address'), max_length=100, required=False
    )
    vmware_username = forms.CharField(
        label=_('Login username'), max_length=100, required=False
    )
    vmware_password = forms.CharField(
        label=_('Login password'), max_length=100, required=False
    )

    def clean_vmware_path(self):
        app_type_list = [const.APP_TYPE_VMWARE]
        return self.clean_app_field_or_raise('vmware_path', app_type_list)


class ApplicationOtherParamsForm(forms.ModelForm):

    other_path = forms.CharField(
        label=_('App path'), max_length=100, required=False
    )
    other_cmdline = forms.CharField(
        label=_('Operating parameter'), max_length=100, required=False
    )
    other_target = forms.CharField(
        label=_('Target address'), max_length=100, required=False
    )
    other_username = forms.CharField(
        label=_('Login username'), max_length=100, required=False
    )
    other_password = forms.CharField(
        label=_('Login password'), max_length=100, required=False
    )

    def clean_other_path(self):
        app_type_list = [const.APP_TYPE_OTHER]
        return self.clean_app_field_or_raise('other_path', app_type_list)

# 所有应用的参数form


class ApplicationParamsForm(
    ApplicationBrowserParamsForm,
    ApplicationDBParamsForm,
    ApplicationVMwareParamsForm,
    ApplicationOtherParamsForm,
):
    pass


class ApplicationCreateUpdateForm(ApplicationParamsForm, OrgModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter protocols for RDP assets and system users
        field_asset = self.fields['asset']
        field_system_user = self.fields['system_user']
        field_asset.queryset = field_asset.queryset.filter(
            protocol=Asset.PROTOCOL_RDP
        )
        field_system_user.queryset = field_system_user.queryset.filter(
            protocol=SystemUser.PROTOCOL_RDP
        )

    class Meta:
        model = Application
        fields = ['name', 'asset', 'system_user', 'app_type', 'comment']
        widgets = {
            'asset': forms.Select(attrs={
                'class': 'select2', 'data-placeholder': _('Asset')
            }),
            'system_user': forms.Select(attrs={
                'class': 'select2', 'data-placeholder': _('System user')
            })
        }

    def clean_app_field_or_raise(self, field, app_type_list):
        if self.data.get('app_type') not in app_type_list:
            return None
        value = self.data.get(field)
        if not value:
            raise forms.ValidationError(_('* Please fill in this field'))
        return value

    # 处理保存逻辑
    def save_params(self, instance):
        app_type = self.data.get('app_type')
        fields = const.APP_TYPE_FIELDS_MAP.get(app_type, [])
        params = {}
        for field in fields:
            value = self.cleaned_data[field]
            params.update({field: value})
        instance.params = params
        instance.save()
        return instance

    def save(self, commit=True):
        instance = super().save(commit=commit)
        instance = self.save_params(instance)
        return instance
