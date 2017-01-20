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


class AssetAsset(models.Model):
	_inherit = 'asset.asset'


	@api.model
	def create(self, vals):
		user = self.env['res.users'].browse(self.env.context['uid'])
		vals['company_id'] = user.company_id.id
	        return super(AssetAsset, self).create(vals)

	company_id = fields.Many2one('res.company',string='Empresa')

class MroRequest(models.Model):
	_inherit = 'mro.request'


	@api.model
	def create(self, vals):
		user = self.env['res.users'].browse(self.env.context['uid'])
		vals['company_id'] = user.company_id.id
	        return super(MroRequest, self).create(vals)

	company_id = fields.Many2one('res.company',string='Empresa')

