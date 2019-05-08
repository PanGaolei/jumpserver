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


class ApplicationCreateUpdateForm(OrgModelForm):

    # chrome
    chrome_path = forms.CharField(
        label=_('App path'), max_length=100, required=False
    )
    chrome_target = forms.CharField(
        label=_('Target url'), max_length=100, required=False
    )
    chrome_username = forms.CharField(
        label=_('Login username'), max_length=100, required=False
    )
    chrome_password = forms.CharField(
        label=_('Login password'), max_length=100, required=False
    )

    # db client
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

    # vmware client
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

    # other
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

    class Meta:
        model = Application
        fields = [
            'name', 'asset', 'system_user', 'app_type', 'comment'
        ]

        widgets = {
            'asset': forms.Select(attrs={
                'class': 'select2', 'data-placeholder': _('Asset')
            }),
            'system_user': forms.Select(attrs={
                'class': 'select2', 'data-placeholder': _('System user')
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asset'].queryset = Asset.objects.filter(
            protocol=Asset.PROTOCOL_RDP
        )
        self.fields['system_user'].queryset = SystemUser.objects.filter(
            protocol=SystemUser.PROTOCOL_RDP
        )

    @property
    def app_type(self):
        return self.data.get('app_type')

    # 处理校验参数

    def clean_chrome_path(self):
        if self.app_type != const.APP_TYPE_CHROME:
            return None
        chrome_path = self.data.get('chrome_path')
        if not chrome_path:
            msg = _("* Please enter the application path")
            raise forms.ValidationError(msg)
        return chrome_path

    def clean_chrome_target(self):
        if self.app_type != const.APP_TYPE_CHROME:
            return None
        chrome_target = self.data.get('chrome_target')
        if not chrome_target:
            msg = _("* Please enter the Target url")
            raise forms.ValidationError(msg)
        return chrome_target

    def clean_db_path(self):
        if self.app_type not in const.DB_APP_TYPE:
            return None
        db_path = self.data.get('db_path')
        if not db_path:
            msg = _("* Please enter the application path")
            raise forms.ValidationError(msg)
        return db_path

    def clean_vmware_path(self):
        if self.app_type != const.APP_TYPE_VMWARE_CLIENT:
            return None
        vmware_path = self.data.get('vmware_path')
        if not vmware_path:
            msg = _("* Please enter the application path")
            raise forms.ValidationError(msg)
        return vmware_path

    def clean_other_path(self):
        if self.app_type != const.APP_TYPE_OTHER:
            return None
        other_path = self.data.get('other_path')
        if not other_path:
            msg = _("* Please enter the application path")
            raise forms.ValidationError(msg)
        return other_path

    # 处理保存逻辑

    chrome_fields = [
        'chrome_path', 'chrome_target', 'chrome_username', 'chrome_password'
    ]
    db_fields = [
        'db_path', 'db_ip', 'db_name', 'db_username', 'db_password'
    ]
    vmware_fields = [
        'vmware_path', 'vmware_target', 'vmware_username', 'vmware_password'
    ]
    other_fields = [
        'other_path', 'other_cmdline', 'other_target', 'other_username',
        'other_password'
    ]
    app_fields_map = {
        const.APP_TYPE_CHROME: chrome_fields,
        const.APP_TYPE_PLSQL: db_fields,
        const.APP_TYPE_MSSQL: db_fields,
        const.APP_TYPE_MYSQL_WORKBENCH: db_fields,
        const.APP_TYPE_VMWARE_CLIENT: vmware_fields,
        const.APP_TYPE_OTHER: other_fields
    }

    def get_params(self):
        params = {
            field: self.cleaned_data[field]
            for field in self.app_fields_map[self.app_type]
        }
        return params

    def save(self, commit=True):
        instance = super().save(commit=commit)
        instance.params = self.get_params()
        instance.save()
        return instance
