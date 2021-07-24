PREREQ_SEC_REGEX = r"<br \/>\s*(.*)\s*<br \/>"
PREREQ_TITLE_HTML = '<SPAN class="fieldlabeltext">Prerequisites: </SPAN>'

SUBJECT_NAMES = [
    "ACCT","AE", "AS", "APPH", "ASE","ARBC", "ARCH",
    "BIOS", "BIOL", "BMEJ", "BMED", "BMEM", "BCP", 
    "BC", "CETL", "CHBE", "CHEM", "CHIN", "CP", 
    "CEE", "COA", "COE", "COS", "CX", "CSE", "CS", 
    "COOP", "UCGA", "GTJD", "EAS", "ECON", "ECEP", 
    "ECE", "ENGL", "FS", "FREN", "GT", "GTL", 
    "GRMN", "GMC", "HP", "HS", "HEBW", "HIN", 
    "HIST", "HTS", "ISYE", "ID", "IPCO", "IPIN", 
    "IPFS", "IPSA", "INTA", "IL", "INTN", "IMBA", 
    "IAC", "JAPN", "KOR", "LATN", "LS", "LING", 
    "LMC", "MGT", "MOT",  "MLDR", "MSE", "MATH", 
    "ME", "MP", "MSL", "ML", "MUSI", "NS", "NEUR", 
    "NRE", "PERS", "PHIL", "PHYS", "POL", "PTFE", 
    "PORT", "DOPP", "PSYC", "PUBP", "PUBJ", "RUSS", 
    "SCI", "SLS", "SOC", "SPAN", "SWAH", "VIP", "WOLO"
]

BASE_URL = "https://oscar.gatech.edu"
COURSES_BASE_URL = "https://oscar.gatech.edu/bprod/bwckctlg.p_display_courses"
TERM = "202108"

DUMMY_PARAMS = [
    "sel_subj",
    "sel_levl",
    "sel_schd",
    "sel_coll",
    "sel_divs",
    "sel_dept",
    "sel_attr"
]

EMPTY_PARAMS = [
    "sel_crse_strt",
    "sel_crse_end",
    "sel_title",
    "sel_from_cred",
    "sel_to_cred"
]

OUTPUT_JSON_FILE = f"reqs_{TERM}.json"