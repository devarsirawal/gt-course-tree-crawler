from collections import defaultdict
import json
import re
import requests
from bs4 import BeautifulSoup
from antlr4 import *
from grammar.PrefixNotationVisitor import PrefixNotationVisitor
# from grammar.DependentsVisitor import DependentsVisitor
from grammar.PrerequisitesParser import PrerequisitesParser
from grammar.PrerequisitesLexer import PrerequisitesLexer
from util import *
from constants import *



def download(term):
    payload = {
    "term_in" : term,
    "call_proc" : "bwckctlg.p_disp_dyn_ctlg",
    }
    payload.update({**{k: ["dummy", "%"] for k in DUMMY_PARAMS},
                    **{k: "" for k in EMPTY_PARAMS},
                    **{"sel_subj": ["dummy"] + SUBJECT_NAMES}})

    return requests.post(COURSES_BASE_URL, data=payload)

def parse(prereq_text):
    char_stream = InputStream(prereq_text)
    lexer = PrerequisitesLexer(char_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PrerequisitesParser(token_stream)
    tree = parser.parse()
    prereq_visitor = PrefixNotationVisitor()
    prerequisite_clause = prereq_visitor.visit(tree)

    if prerequisite_clause is None:
        prereqs = [] 
    elif is_single_course(prerequisite_clause):
        prereqs = ["and", prerequisite_clause]
    elif is_single_and(prerequisite_clause):
        prereqs = flatten_clause(prerequisite_clause[1])
    else:
        prereqs = flatten_clause(prerequisite_clause)

    return prereqs
        
def main():
    prereqs = {}
    print(f"Downloading course data from term {TERM}......")
    html_data = download(TERM)
    soup = BeautifulSoup(html_data.content, "html.parser")
    titles = soup.findAll("td", {"class": "nttitle"})
    print("Parsing prerequisite data......")
    for title in titles:
        course_title = title.text.split("-")[0].strip()
        course_link = title.find("a", recursive=False)
        print(f"Parsing prerequisites for {course_title}.......")
        r = requests.get(BASE_URL + course_link["href"])
        start_index = r.content.find(PREREQ_TITLE_HTML.encode())
        prereq_tree = []
        if start_index != -1:
            prereq_section = re.search(PREREQ_SEC_REGEX.encode(), r.content[start_index:])
            prereq_text = BeautifulSoup(prereq_section.group(0), "html.parser").text.strip()
            prereq_tree = parse(prereq_text)

        prereqs[course_title] = prereq_tree
        print("Done!.....")
    print(f"Done!......")
    

    print(f"Parsing postrequisite data......")
    postreqs = defaultdict(list)
    for title, data in prereqs.items():
        prereq_ids = extract_prereq_ids(data)
        postreqs[title]
        for id in prereq_ids:
            postreqs[id].append(title)
    print("Done!.....")

    print("Dumping data......")
    with open("./data/prereqs.json", "w") as f:
        json.dump(prereqs, f)
    
    with open("./data/postreqs.json", "w") as f:
        json.dump(postreqs, f)
    print("Finished!")
    
if __name__ == "__main__":
    main()
    




