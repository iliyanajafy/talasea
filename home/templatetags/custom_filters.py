from django import template
from markdown import markdown
from bs4 import BeautifulSoup

register = template.Library()

@register.filter(name='first_paragraph')
def first_paragraph(value):
    # Convert Markdown to HTML
    html = markdown(value)
    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html, 'html.parser')
    # Find the first <p> tag and return its content
    first_p = soup.find('p')
    return str(first_p) if first_p else ''
