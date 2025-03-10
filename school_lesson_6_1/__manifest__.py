# Copyright © 2022 Garazd Creation (<https://garazd.biz>)
# @author: Yurii Razumovskyi (<support@garazd.biz>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'School Lesson 6 1',
    'version': '17.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """
        Odoo School
        Lesson 6-1: Master and demo data.
    """,
    'license': 'LGPL-3',
    'author': 'Garazd Creation',
    'website': 'https://garazd.biz',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/res_partner_data.xml',
        'views/library_book_menus.xml',
        'views/library_book_views.xml',
        'data/library_book_data.xml',
        'data/library_book_demo.xml',
        'data/library_book_edit_data.xml',
    ],
    'demo': [
        'data/res_partner_demo.xml',
        'data/res_partner_bank_demo.xml',
    ],
    'support': 'school@garazd.biz',
    'application': False,
    'installable': True,
    'auto_install': False,
}
