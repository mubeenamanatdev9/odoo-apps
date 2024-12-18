from odoo import fields, api, models


class AccountMoveExt(models.Model):

    _inherit = 'account.move'

    analytic_distribution_for_all = fields.Json('Analytic Distribution Template')

    analytic_precision = fields.Integer(
        store=False ,
        default=lambda self: self.env['decimal.precision'].precision_get("Percentage Analytic"),
    )
    def action_analytic_account_set(self):
        for record in self:
            if record.analytic_distribution_for_all:
                record.invoice_line_ids.write({
                    "analytic_distribution": record.analytic_distribution_for_all
                })

