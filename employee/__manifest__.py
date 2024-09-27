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
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/data.xml",
        "views/set_experience_year.xml",
        "views/employee_certificate_views.xml",
        "views/employee_views.xml",
        "views/employee_skills_views.xml",
        "views/menu_items.xml",
    ],
    "depends": [
        "base", "hr", "mail",
    ],
    "application": True,
    "installable": True,
    "license": "LGPL-3",
}
