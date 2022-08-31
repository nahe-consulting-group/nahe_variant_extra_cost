# -*- coding: utf-8 -*-
{
    'name': "Costos extra para variantes",

    'summary': """
        Costos extra para cada variante cuando la formula delista de precios se basa en costo.""",

    'description': """
        Costos extra para cada variante cuando la formula de lista de precios se basa en costo.
        De ese modo se puede usar en ventas, ecommerce y pos. 
        En cada template se setean variantes y luego en las variantes se agrega data en el campo standard_price_extra. 
    """,

    'author': "Nähe Consulting Group",
    'website': "http://www.nahe.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets': {
    "point_of_sale.assets": [
        '/nahe_variant_extra_cost/static/src/js/models.js',
    ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
