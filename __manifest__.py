{
    'name': 'Estoque',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Módulo para gerenciamento de estoque',
    'description': 'Este módulo permite gerenciar o estoque de produtos, incluindo quantidade, localização e estado do estoque.',
    'author': 'Marcos Gabriel',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estoque_view.xml',
        'views/produto_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}