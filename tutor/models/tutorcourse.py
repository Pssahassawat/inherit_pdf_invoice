# -*- coding: utf-8 -*-

from odoo import models, fields


class TutorCourse(models.Model):
     _name = 'tutor.course'
     _description = 'course that tutor has'

     name = fields.Char(string="Course")
     partner_id = fields.Many2one("res.partner", string="Student name")
     user_id = fields.Many2one("res.users", string="Salesperson")
     cost = fields.Float()
     grade = fields.Selection(
            string='Grade of course',
            selection=[('high', 'High'), ('middle', 'Middle'), ('primary', 'Primary')],
            help="To indicate hierarchy of course")
     description = fields.Text()
