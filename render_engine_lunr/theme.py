import pathlib

from jinja2 import PackageLoader
from render_engine.utils.themes import Theme
# Add plugins here

Lunr = Theme(
    loader=PackageLoader(f"render_engine_lunr", "templates"),
    static_dir= pathlib.Path(__file__).parent / "static",
    plugins = [],
    filters = {},
    prefix = 'lunr',
    template_globals = {"head": "lunrjs_head.html"}
)