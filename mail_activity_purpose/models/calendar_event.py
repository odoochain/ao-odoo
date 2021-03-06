# Copyright 2018 Eficent <http://www.eficent.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class CalendarEvent(models.Model):
    _inherit = "calendar.event"

    purpose_id = fields.Many2one(
        'mail.activity.purpose', 'Purpose',
        index=True, ondelete='restrict',
        domain="[('activity_type_ids.category', '=', 'meeting')]")

    def _sync_activities(self, values):
        res = super(CalendarEvent, self)._sync_activities(values)
        if self.mapped('activity_ids'):
            activity_values = {}
            if values.get('purpose_id'):
                activity_values['purpose_id'] = values['purpose_id']
            if activity_values.keys():
                self.mapped('activity_ids').write(activity_values)
        return res
