import logging

import azure.functions as func
import microdata


def main(myblob: func.InputStream, outputblob: func.Out[func.InputStream]):
    contents = myblob.read()
    processed = convert_recipe(contents)
    outputblob.set(processed)

    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes\n"
                 f"Blob properties:\n"
                 f"Blob URI: {myblob.uri}")
                 

def convert_recipe(recipe):
    items = microdata.get_items(recipe)
    item = items[0]
    item.itemtype
    item.name

    return item.json()