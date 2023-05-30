import xml.etree.ElementTree as et
from typing import Optional
from xml.etree.ElementTree import Element

xml_data_path = "./data/pubmed_result_sjogren.xml"

pubmed_tree = et.parse(xml_data_path)

pubmed_xml_root = pubmed_tree.getroot()

root_tag_type = pubmed_xml_root.tag

articles = pubmed_xml_root.findall("./PubmedArticle")

articles_count = len(articles)
print(articles_count)

def get_element_text(element: Element) ->Optional[str]:
    """Gets the text content of the given XML element

    Args:
        element (Element): XML Element that contains text to be retrieved

    Returns:
        Optional[Element]: Text content, or none if not available
    """
    return element.text or 'None'

