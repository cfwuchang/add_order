from odoo import api, fields, models, tools, _

class PurchasePurchase(models.Model):
    _inherit = 'purchase.order'

    x_aaa = fields.Many2many('ir.attachment', compute='_get_attachment_ids', string=u'附件')


    def _get_attachment_ids(self):
        att_model = self.env['ir.attachment'] #获取附件模型
        for obj in self:
            query = obj.order_line.information_attachment
            obj.x_aaa = query #取得附件list
