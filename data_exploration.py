import xml.etree.ElementTree as et

xml_data_path = "./data/pubmed_result_sjogren.xml"

pubmed_tree = et.parse(xml_data_path)

pubmed_xml_root = pubmed_tree.getroot()

root_tag_type = pubmed_xml_root.tag

articles = pubmed_xml_root.findall("./PubmedArticle")

articles_count = len(articles)
print(articles_count)