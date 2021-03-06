# Copyright 2015-18 Eficent Business and IT Consulting Services S.L.
# - Jordi Ballester Alomar
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "AO-specific customizations on stock",
    "version": "11.0.1.1.0",
    "author": "Eficent Business and IT Consulting Services S.L.",
    "website": "http://www.eficent.com",
    "category": "Warehouse Management",
    "depends": ["stock",
                "stock_inventory_exclude_sublocation",
                "stock_report_quantity_by_location",
                "stock_request_kanban",
                ],
    "data": [
        # "security/ao_stock_security.xml", --not approved yet
        # "security/ir.model.access.csv",
        "views/stock_view.xml",
        "views/report_stockpicking_operations.xml",
        "views/report_stockinventory.xml",
        "views/report_deliveryslip.xml",
        "views/stock_menu_views.xml",
        "wizard/stock_quantity_history.xml",
        "reports/report_paper_format.xml",
        "reports/stock_request_kanban_templates.xml",
    ],
    "license": "AGPL-3",
    'installable': True,
}
