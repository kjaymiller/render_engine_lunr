import json
import logging
import pathlib

from lunr import lunr
from render_engine.plugins import hook_impl


def get_document_fields(page, *args):
    """
    This hook is used to get the fields for the lunr.js index.
    """

    document = {}

    for field in args:
        if attr:=getattr(page, field, None):
            document[field] = attr
    document['url'] = page.url_for()
    return document

class LunrPlugin:
    default_settings = {
        "collections": [],
        "pages": [],
        "fields": ['url', 'title', 'content'],
        "corpus_filename": 'corpus.json',
        "search_index_filename": 'lunr_index.json',
    }


    @hook_impl
    def pre_build_site(site):

        """
        This hook grabs corpus and index from from the lunrThemePlugin and sets 
        Generate the search index and serializer for lunr.js
        """

        lunr_settings = site.plugin_manager.plugin_settings['LunrPlugin']
        index = []
        # Create the index
        for collection in lunr_settings['collections']:
            collection = site.route_list[collection]

            for document in collection:
                index.append(get_document_fields(document, *lunr_settings['fields']))
                
        for page in lunr_settings['pages']:
            index.append(get_document_fields(page, *lunr_settings['fields']))

        documents = [] 

        for _id, fields in enumerate(index):
            documents.append({
                **{"id": _id},
                **fields,
            })
            
        search = lunr(
                ref='id',
                fields=lunr_settings['fields'],
                documents=documents
            )

        # Create the corpus
        corpus_path = pathlib.Path(site.output_path).joinpath(lunr_settings['corpus_filename'])
        pathlib.Path(site.output_path).mkdir(parents=True, exist_ok=True)
        logging.info("Creating corpus at: %s", corpus_path)
        with open(str(corpus_path), 'w') as corpus:
            json.dump(index, corpus)

        # Create the index
        search_index = pathlib.Path(site.output_path).joinpath(lunr_settings['search_index_filename'])
        logging.info("Creating search_index_filename at: %s", corpus_path)
        with open(str(search_index), 'w') as index_file:
            json.dump(search.serialize(), index_file)

        site.theme_manager.engine.globals.update({
            'corpus_path': corpus_path.relative_to(site.output_path),
            'search_index_filename': search_index.relative_to(site.output_path),
        })
        