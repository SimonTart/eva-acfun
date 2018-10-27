import logging
import traceback
from server.spiders.content import crawl_all_sections_articles, crawl_all_sections_videos
from server.spiders.comment import CommentSpider, crawl_content_latest_comments
from server.schedule import scheduler
from time import time
from server import server
from config import ARTICLE_SECTIONS, VIDEO_SECTIONS, contentTypes


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

# 获取最近10页的内容
# crawl_all_sections_articles(ARTICLE_SECTIONS, total_page=10)
# crawl_all_sections_videos(VIDEO_SECTIONS, total_page=10)

# 获取这个之前的内容
# crawl_all_sections_videos(VIDEO_SECTIONS, min_published_date='2018-10-26 00:00:00')
# crawl_all_sections_articles(ARTICLE_SECTIONS, min_published_date='2018-10-26 00:00:00')

# 获取新动态的文章
# crawl_all_sections_articles(ARTICLE_SECTIONS, article_order_type=1, min_latest_comment_time='2018-10-26 00:00:00')

# 获取content所有的评论
# CommentSpider(content_id=4667805, crawl_all=True).crawl_comments()

# 抓取时间范围内的评论
# CommentSpider(content_id=4667805, min_comment_time='2018-10-26 12:00:00').crawl_comments()

# 抓取文章中没抓取的评论
# crawl_content_latest_comments(ARTICLE_SECTIONS[0], contentTypes['article'])

# 抓取最近的三天的视频评论
# crawl_content_latest_comments(VIDEO_SECTIONS[1]['subSections'][0], contentTypes['video'])


