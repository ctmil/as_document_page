# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.osv import osv
from openerp.exceptions import except_orm, ValidationError
from StringIO import StringIO
import urllib2, httplib, urlparse, gzip, requests, json
import openerp.addons.decimal_precision as dp
import logging
import datetime
from openerp.fields import Date as newdate

#Get the logger
_logger = logging.getLogger(__name__)


class DocumentPage(models.Model):
	_inherit = 'document.page'


	@api.model
	def create(self, vals):
		user = self.env['res.users'].browse(self.env.context['uid'])
		vals['company_id'] = user.company_id.id
	        return super(DocumentPage, self).create(vals)

	company_id = fields.Many2one('res.company',string='Empresa')

