from bs4 import BeautifulSoup

def get_paragraph_count(html_doc):
    file = open(html_doc, "r", encoding="utf8")
    soup = BeautifulSoup(file, 'html.parser')
    return len(soup.find_all("p"))

def extract_text(html_doc):

    file = open(html_doc, "r", encoding="utf8")
    soup = BeautifulSoup(file, 'html.parser')
    return soup.get_text()

if __name__ == "__main__":
    # print("hello")
    print(extract_text("books/pg11CarolAlice-content.html"))