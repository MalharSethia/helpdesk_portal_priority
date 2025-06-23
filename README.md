Helpdesk Priority Portal
Overview
This module extends the OCA Helpdesk Management portal functionality by adding priority field support to the portal interface. Portal users can now set ticket priority when creating new tickets and view priority information in the ticket detail view.
Features

Priority Selection: Add priority dropdown to ticket creation form in portal
Priority Display: Show priority with colored badges in ticket detail view
Portal Integration: Seamlessly integrates with existing OCA Helpdesk Management portal
User-Friendly: Clean, intuitive interface following Odoo portal design patterns

Priority Levels
The module supports four priority levels:
PriorityValueBadge ColorDescriptionLow0GrayLow priority issuesNormal1BlueStandard priority (default)High2OrangeHigh priority issuesUrgent3RedCritical/urgent issues
Dependencies

helpdesk_mgmt - OCA Helpdesk Management base module
portal - Odoo Portal base module
website - Odoo Website base module

Installation

Ensure you have the OCA Helpdesk Management module installed and configured
Copy this module to your Odoo addons directory
Update the apps list in Odoo
Install the "Helpdesk Priority Portal" module

Configuration
No additional configuration is required. The module automatically:

Adds priority field to the ticket creation form at /new/ticket
Displays priority in ticket detail views at /my/ticket/<id>
Sets "Normal" as the default priority for new tickets

Usage
For Portal Users
Creating a Ticket:

Navigate to "My Tickets" in the portal
Click "Create Ticket"
Fill in the required fields
Select the appropriate priority from the dropdown
Submit the ticket

Viewing Ticket Priority:

Open any ticket detail page
Priority is displayed with a colored badge near the category information

For Internal Users
Internal users can still manage ticket priorities through the backend interface as usual. Portal-created tickets will have the priority set by the portal user.
Technical Details
Files Structure
helpdesk_priority_portal/
├── __init__.py
├── __manifest__.py
├── controllers/
│   ├── __init__.py
│   └── portal.py
├── views/
│   └── portal_templates.xml
└── models/
    └── __init__.py
Template Inheritance

Creation Form: Inherits helpdesk_mgmt.portal_create_ticket
Detail View: Inherits helpdesk_mgmt.portal_helpdesk_ticket_page

Controller Extension
Extends HelpdeskTicketController from helpdesk_mgmt.controllers.main to handle priority field processing during ticket creation.
Customization
Changing Priority Options
To modify priority levels, update both:

The template select options in views/portal_templates.xml
The badge display logic in the detail view template

Styling
The module uses standard Bootstrap classes for styling. To customize:

Modify the CSS classes in the template files
Add custom CSS through your theme or website builder

Troubleshooting
Common Issues
Priority not saving:

Verify the helpdesk.ticket model has a priority field
Check that portal users have write access to the priority field
Ensure the priority field accepts the values (0, 1, 2, 3)

Template not found errors:

Verify OCA Helpdesk Management module is properly installed
Check that template IDs match your version of the helpdesk module

XPath errors:

The module assumes specific template structures
You may need to adjust XPath expressions based on your helpdesk module version
Inspect the actual template HTML to verify field locations

Debugging
To debug template issues:

Enable developer mode
Go to Settings > Technical > User Interface > Views
Search for the template names to inspect their structure
Adjust XPath expressions as needed

Compatibility

Odoo Version: 17.0
OCA Helpdesk: Compatible with helpdesk_mgmt module
Browser Support: All modern browsers supported by Odoo

Known Limitations

Priority field is required in the creation form
No JavaScript-based visual enhancements (intentionally kept simple)
Assumes standard Bootstrap styling
XPath expressions may need adjustment for different helpdesk module versions

Support
For issues related to:

This module: Create an issue in the module repository
OCA Helpdesk: Refer to OCA Helpdesk Management documentation
Odoo Portal: Refer to official Odoo documentation

License
LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)
