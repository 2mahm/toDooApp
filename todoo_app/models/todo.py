from odoo import fields,models


class Todo(models.Model):
    _name='todo.todo'
    _description='dodo'


    name=fields.Char()
    number=fields.Integer()
    tag=fields.Char()
    state = fields.Selection([
        ('new', 'New'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    ])
    file = fields.Binary()
    description = fields.Text()
    