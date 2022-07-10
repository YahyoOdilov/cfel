from aiogram import executor

from cfel_project.loader import dp, db
import cfel_project.middlewares, cfel_project.filters, cfel_project.handlers
from cfel_project.utils.notify_admins import on_startup_notify
from cfel_project.utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    db.Database_primary.create()
    db.users.create_table()
    db.telegram_ids.create_table()
    db.kreteria.create_table()
    db.link.create_table()
    db.product.create_table()
    db.product_o.create_table()
    db.product_s.create_table()
    db.order.create_table()
    db.sent.create_table()
    db.paid.create_table()
    db.additional_value.create_table()
    db.businesses.create_table()
    db.production.create_table()
    db.product_p.create_table()
    db.production_add_value.create_table()
    db.productioners.create_table()
    db.loading.create_table()
    db.bag_value.create_table()
    db.diliver.create_table()
    # p_kreterias = []
    # for x in p_kreterias:
    #     result = db.kreteria.fetch_kreteria(x, -2)
    #     if not result:
    #         db.kreteria.insert(x, -2)
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)
    


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
    
