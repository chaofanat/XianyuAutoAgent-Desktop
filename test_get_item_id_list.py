from XianyuApis import XianyuApis
from XianyuAgent import XianyuReplyBot
from main import XianyuLive
from dotenv import load_dotenv
import os
if __name__ == '__main__':
    #加载环境变量 cookie
    load_dotenv()
    cookies_str = os.getenv("COOKIES_STR")
    bot = XianyuReplyBot()
    xianyuLive = XianyuLive(cookies_str, bot)
    api = xianyuLive.xianyu
    # 可根据需要修改页码和每页数量
    page = 1
    page_size = 20
    item_ids = api.get_item_id_list(user_id=xianyuLive.myid, page=page, page_size=page_size)
    print(f'第{page}页商品ID列表:')
    print(item_ids) 