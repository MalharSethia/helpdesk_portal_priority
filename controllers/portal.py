import logging
from odoo import http
from odoo.http import request
from odoo.addons.helpdesk_mgmt.controllers.main import HelpdeskTicketController

_logger = logging.getLogger(__name__)

class HelpdeskPortalPriority(HelpdeskTicketController):
    
    def _prepare_submit_ticket_vals(self, **kw):
        """Override to add priority field handling"""
        _logger.debug("Preparing ticket submission values with kwargs: %s", kw)
        
        vals = super()._prepare_submit_ticket_vals(**kw)
        
        # Add priority field if provided
        priority = kw.get('priority')
        _logger.debug("Received priority value: %s", priority)
        
        if priority:
            vals['priority'] = priority
            _logger.debug("Priority set to: %s", priority)
        else:
            # Default to Normal priority if not specified
            vals['priority'] = '1'
            _logger.debug("Defaulting priority to Normal (1)")
            
        _logger.debug("Final ticket values: %s", vals)
        return vals
