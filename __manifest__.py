# -*- coding: utf-8 -*-
{
    'name': "FieldService GMaps Routes",

    'summary': """
                The idea of the module is to add the funtionality to create a dinamic route with the locations of the tasks selected in the field service module
                """,

    'description': """
        The idea of the module is to add the funtionality to create a dinamic route with the locations of the tasks selected in the field service module
    """,

    'author': "Samuel",
    'website': "http://www.zitycard.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ["base_territory", "base_geolocalize", "resource", "contacts","field_service"],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
