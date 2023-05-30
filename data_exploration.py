import xml.etree.ElementTree as et


xml_data_path = "./data/pubmed_result_sjogren.xml"

pubmed_tree = et.parse(xml_data_path)

pubmed_xml_root = pubmed_tree.getroot()

root_tag_type = pubmed_xml_root.tag

articles = pubmed_xml_root.findall("./PubmedArticle")

articles_count = len(articles)
print(articles_count)

#Keywords:
#Mesh - Medical Subject Headline
#GRID - Global Research Identifier Database

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
    mesh_list = [desc.get('UI') for desc in article.findall(".//MeshHeading/DescriptorName")]

    return {
        "title": title,
        "pmid": pmid,
        "year": year,
        "keyword_list": keyword_list,
        "mesh_list": mesh_list
    }


def extract_author_data(article_no: int, author_no: int, root: et.Element)-> dict[str]:
    """Extracts author's data based on article number and author number

    Args:
        article_no (int): Index of article in XML File
        author_no (int): Index of author in XML File
        root (et.Element): Root element of XML Tree

    Returns:
        dict[str]: Dictionary containing author details:
         - 'forename' (str): Forename of author
         - 'lastname' (str): Lastname of author
         - 'initials' (str): Initials of Author
         - 'identifier' (str): Unique ID from Global Research Identifier Database
         - 'affiliation' (List[str]): List of Affiliations
    """
    author = root[article_no].findall('.//AuthorList/Author')[author_no]
    first_name = author.find('.//ForeName').text
    last_name = author.find('.//LastName').text
    initials = author.find('.//Initials').text
    grid_identity = author.find(".//Identifier[@Source='GRID']").text
    affiliation_list = [affiliation.text for affiliation in author.findall('.//Affiliation')]

    return {
        'forename': first_name,
        'lastname': last_name,
        'initials': initials,
        'identifier': grid_identity,
        'affiliation': affiliation_list
    }

print(extract_article_data(23, pubmed_xml_root))
print(extract_author_data(208,0,pubmed_xml_root))
