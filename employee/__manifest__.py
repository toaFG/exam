{
    "name": "Employee Management",
    "version": "1.0",
    "author": "Odoo S.A.",
    "website": "https://www.odoo.com",
    "description": """
    Employee Management Modules to show available properties and manage them.
    """,
    "category": "Services",
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/set_experience_year.xml",
        "views/employee_views.xml",
        "views/menu_items.xml",
    ],
    "depends": [
        "base", "hr", "mail"
    ],
    "application": True,
    "installable": True,
    "license": "LGPL-3",
}
