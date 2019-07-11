# Copyright (C) 2019 - TODAY, Brian McMaster, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import timedelta

from odoo import models, fields


class FSMOrder(models.Model):
    _inherit = 'fsm.order'

    fsm_recurring_id = fields.Many2one(
        'fsm.recurring', 'Recurring Order', readonly=True)

    def _compute_request_late(self):
        if not self.fsm_recurring_id:
            return super(FSMOrder, self)._compute_request_late()
        else:
            days_late = self.fsm_recurring_id.fsm_frequency_set_id.buffer_late
            self.request_late = \
                self.scheduled_date_start + timedelta(days=days_late)
