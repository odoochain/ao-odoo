# Copyright 2013 Ursa Information Systems (http://www.ursainfosystems.com).
# Copyright 2018 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "United States - Localizations",
    "category": "Accounting & Finance",
    "version": "11.0.1.0.1",
    "summary": "This module quickly configures OpenERP for the "
               "most common needs of the United States market.",
    "author": "Ursa Information Systems",
    "license": "AGPL-3",
    "website": "http://www.ursainfosystems.com",
    "depends": ["base"],
    "data": [
        "data/base_data.xml",
        "data/res_country_data.xml",
        "data/res.country.state.csv",
        "data/changed_views.xml",
    ],
    "installable": True,
    "images": [
        "images/sale_crm_crm_dashboard.png",
        "images/crm_dashboard.jpeg",
        "images/leads.jpeg",
        "images/meetings.jpeg",
        "images/opportunities.jpeg",
        "images/outbound_calls.jpeg",
        "images/stages.jpeg",
    ],
}
