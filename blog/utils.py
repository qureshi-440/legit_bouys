import bs4
import requests
# from .models import Post

# def homeSnippet():
#     page = requests.get('blog:post_detail')
#     soup = bs4.BeautifulSoup(page.text,'lxml')
#     blog_content = soup.select('.entry-content')[0].getText(separator=" ")
#     snippet = " ".join(blog_content.split()).strip()[0:300]
#     return snippet


def modelsnippet(Post_body):
    html_text = Post_body
    soup = bs4.BeautifulSoup(html_text,'lxml')
    blog_content = soup.select("body")[0].getText(separator=" ")
    snippet = " ".join(blog_content.split()).strip()[0:250]
    if len(snippet) >= 245:
        snippet += "..."
    return snippet