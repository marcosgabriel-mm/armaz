from odoo import models, fields, api

class Estoque(models.Model):
    _name = 'estoque'
    _description = 'Gestão de Estoque'
    _rec_name = 'produto_id'

    produto_id = fields.Many2one(
        'estoque.produto',
        string='Produto',
        required=True,
        ondelete='restrict',
        domain=[('active', '=', True)],
        help='Produto associado ao registro de estoque.',
    )

    quantity = fields.Integer(
        string='Quantidade em Estoque',
        default=0,
        help='Quantidade disponível do produto em estoque.',
        required=True
    )

    location = fields.Char(
        string='Localização',
        help='Localização física do estoque do produto.',
        required=True
    )

    date = fields.Datetime(
        string='Data',
        default=fields.Datetime.now,
        help='Data e hora do registro de estoque.',
    )

    state = fields.Selection([
        ('available', 'Disponível'),
        ('out_of_stock', 'Fora de Estoque')],

        string='Estado do Estoque',
        default='available',
        help='Estado atual do estoque do produto.',
        required=True        
    )


    total_value = fields.Float(
        string='Valor Total do Estoque',
        compute='_compute_total_value',
        store=True,
        help='Valor total do estoque baseado na quantidade e preço do produto.',
    )

    @api.depends('quantity', 'produto_id.standard_price')
    def _compute_total_value(self):
        for record in self:
            if record.produto_id and record.produto_id.standard_price:
                record.total_value = record.quantity * record.produto_id.standard_price
            else:
                record.total_value = 0.0

    @api.constrains('quantity')
    def _check_quantity(self):
        for record in self:
            if record.quantity < 0:
                raise models.ValidationError('A quantidade não pode ser negativa!')
    
    def action_set_available(self):
        for record in self:
            record.state = 'available'

    def action_set_out_of_stock(self):
        for record in self:
            record.state = 'out_of_stock'
    

    