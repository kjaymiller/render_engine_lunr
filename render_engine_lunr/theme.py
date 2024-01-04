from jinja2 import PackageLoader
from render_engine.themes import Theme

from .plugins import LunrPlugin

LunrTheme = Theme(
    loader=PackageLoader("render_engine_lunr", "templates"),
    plugins = [LunrPlugin],
    filters = {},
    prefix = 'lunrjs',
    template_globals={
            "head": "components/lunrjs/lunrjs_head.html",
            "lunrjs_path": "https://unpkg.com/lunr/lunr.js",
            "corpus_filename": 'corpus.json',
            "search_index_filename": 'lunr_index.json',
    }
)
