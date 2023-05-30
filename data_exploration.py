import xml.etree.ElementTree as et
from typing import Optional


xml_data_path = "./data/pubmed_result_sjogren.xml"

pubmed_tree = et.parse(xml_data_path)

pubmed_xml_root = pubmed_tree.getroot()

root_tag_type = pubmed_xml_root.tag

articles = pubmed_xml_root.findall("./PubmedArticle")

articles_count = len(articles)
print(articles_count)


def extract_article_data(article_no: int, root: et.Element) -> dict[str]:
    """Extracts article data, from xml file given an article number

    Args:
        article_no (int): Index of article in XML File
        root (et.Element): Root element of XML Tree

    Returns:
        dict[str]: A dictionary containing the extracted data:
            - 'title' (str): The title of the article
            - 'pmid' (str): The PMID (PubMed ID) of the article
            - 'year' (str): The publication year of the article
            - 'keyword_list' (List[str]): List of keywords associated with the article
            - 'mesh_list' (List[str]): List of Mesh Headings associated with the article
    """
    article = root[article_no]
    title = article.find('.//ArticleTitle').text
    pmid = article.find('.//PMID').text
    year = article.find(".//PubDate/Year").text
    keyword_list = [keyword.text for keyword in article.findall('.//Keyword')]
    mesh_list = [descriptor.get('UI') for descriptor in article.findall(".//MeshHeading/DescriptorName")]
    
    return {
        "title": title,
        "pmid": pmid,
        "year": year,
        "keyword_list": keyword_list,
        "mesh_list": mesh_list
    }

