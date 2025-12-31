from odoo import models, fields

class Produto(models.Model):
    _name = 'estoque.produto'
    _description = 'Produto do Estoque'    
    _rec_name = 'name'

    name = fields.Char(
        string='Nome do Produto',
        required=True,
        help='Nome do produto no estoque.',
    )

    code = fields.Char(
        string='Código do Produto',
        required=True,
        help='Código único do produto no estoque.',
    )

    description = fields.Text(
        string='Descrição do Produto',
        help='Descrição detalhada do produto no estoque.',
    )

    category = fields.Selection([
        ('eletronicos', 'Eletrônicos'),
        ('moveis', 'Móveis'),
        ('ferramentas', 'Ferramentas'),
        ('outros', 'Outros')],

        string='Categoria do Produto',
        default='outros',
    ) 

    standard_price = fields.Float(
        string='Preço Padrão',
        help='Preço padrão do produto.',
    )

    active = fields.Boolean(
        string='Ativo',
        default=True,
        help='Se desmarcado, oculta o produto sem deletá-lo.',
    )

    estoque_ids = fields.One2many(
        'estoque',
        'produto_id',
        string='Registros de Estoque',
        help='Registros de estoque associados a este produto.',
    )

    def deactivate_product(self):
        for record in self:
            record.active = False

    def activate_product(self):
        for record in self:
            record.active = True