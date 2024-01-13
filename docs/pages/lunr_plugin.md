---
title: "Lunr Theme"
---

The Lunr theme is the primary way to interface with the lunr plugin and theme. Render Engine themes can have plugins as dependencies.

The Lunr theme, unlike many other Render Engine themes, is not a full theme. Instead it creates a set of components usable by your site.

## Registering the Lunr Theme

You can register the Lunr theme with the site's `register_theme` method.

```python
from render_engine_lunr import LunrTheme
from render_engine.core import Site

site = Site()
site.register_theme(LunrTheme)
```

## Global Variables

The Lunr theme adds a few global variables to the site's context. These variables are available to all templates.

### Passive Variables

Passive variables are available to all templates, but **are not meant to be called by the user.**

| Variable | Description | Value |
| -------- | ----------- | ----- |
| `head` | the template included in the "base" of the site | `components/lunrjs/lunrjs_head.html`|
| `lunrjs_path` | the path to the lunrjs javascript file | `https://unpkg.com/lunr/lunr.js` |
| `corpus_filename` | the filename of the corpus file | `corpus.json` |
| `search_index_filename` | the filename of the search index file | `search_index.json` |

## Using the Lunr Theme Components

The Lunr theme adds a few components to the site's context. These components can be included/imported and used in any template.

Since these are components, they are found in the `components` directory of the templates.

### lunrjs_head.html

`lunrjs_head.html` is the template included in the "head" of the site that calls the `lunrjs_path` | `components/lunrjs/lunrjs_head.html`|

```html
{% extends 'base.html' %} 

<head>
{{super()}} 
{% include 'components/lunrjs_head.html' %}
</head>

```

### `lunr_search.html`

`lunr_search.html` is a collection of macros that can be imported into a page and called where you would like your search and search functionality defined.

#### `search_form`

The `search_form` macro is a form that can be used to search the site. It is a simple form that takes a `search` input and a `submit` button.

```html
{% import 'components/lunr_search.html' as lunr_search with context %}

{{ lunr_search.search_form() }}
```

While you don't need to use the search form there are some defined values that make it easier to setup your javascript for returning search results.

The `input` of the form has the id `lunrSearchInput` and calls `updateSearchResults`. 

That javascript function is defined in `lunr_search.search_script`.

#### `search_script`

`search_script` is a javascript function that fetches the search results and updates a attribute with the id `lunrSearchResults` with the results.

```html
{% import 'components/lunr_search.html' as lunr_search with context %}

{{ lunr_search.search_script() }}
```
