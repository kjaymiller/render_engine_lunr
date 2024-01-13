from render_engine.collection import Collection
from render_engine.page import Page
from render_engine.parsers.markdown import MarkdownPageParser
from render_engine.site import Site
from render_engine_lunr import LunrTheme

app = Site()
app.output_path = "./docs/output"
app.template_path = "./docs/templates"
app.site_vars.update ({
    "SITE_TITLE": f"Render Engine Lunr Theme",
    "SITE_URL": "https://kjaymiller.github.io/render_engine_theme_kjaymiller/",
    "NAVIGATION": [
        {
            "text": "Docs",
            "url": "/docs.html",
        },
        {
            "test": "GitHub",
            "url": "https://github.com/kjaymiller/render_engine_kjaymiller_theme",
        }    
    ],
    "head": [
        "pico.html"
    ],
})



@app.collection
class Docs(Collection):
    content_path = 'docs/pages'
    template = "page.html"
    Parser = MarkdownPageParser
    parser_extras = {"markdown_extras": ["fenced-code-blocks", "codehilite", "header-ids"]}
    has_archive = True

@app.page
class Index(Page):
    template = "page.html"
    title = ""
    slug = "index"
    Parser = MarkdownPageParser
    content_path = "README.md"
    parser_extras = {"markdown_extras": ["fenced-code-blocks", "codehilite"]}
