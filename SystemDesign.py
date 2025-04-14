import pandas as pd

# ---------------------------------------------------------------
#  A) SWEDISH ANALYSIS
# ---------------------------------------------------------------

# 1. Core Data (Sweden)
total_swedish_participants = 10

technologies_mentioned = [
    ("Redis (caching)", 7, 70),
    ("Load balancing", 7, 70),
    ("Base62 encoding", 6, 60),
    ("PostgreSQL", 5, 50),
    ("Python/FastAPI", 5, 50),
    ("Docker/containerization", 5, 50),
    ("Kubernetes", 4, 40),
    ("Service separation", 4, 40),
    ("Go language", 3, 30),
    ("UUID-based approaches", 3, 30),
    ("Analytics/Logging", 3, 30),
    ("DynamoDB", 3, 30),
    ("CDN", 2, 20),
    ("MongoDB", 1, 10),
    ("Message queuing", 1, 10),
    ("Java", 1, 10)
]

component_matrix = [
    ("Iley Alvarez",    "Generic DB",         False,        False, "Encryption",   False,         "Not specified"),
    ("Atheer Salim",    "MongoDB",            "Redis",      True,  "UUID",         False,         "Not specified"),
    ("Milad Farahani",  "Redis/DynamoDB",     True,         True,  "Not specified", False,         "Not specified"),
    ("Noel Tesfalidet", "SQL DB",             "Redis",      True,  "Base62",       "Docker/K8s",  "Java/Go"),
    ("Leo Hammar",      "DynamoDB/Redis",     "Redis",      True,  "Base62",       "Docker",      "Go"),
    ("Filip Amgren",    "PostgreSQL",         "Redis",      True,  "Base62/UUID",  "Docker",      "Python/FastAPI/Node"),
    ("Maja",            "PostgreSQL",         "Redis",      True,  "Hash",         "Docker",      "Python/FastAPI"),
    ("Daniel",          "PostgreSQL",         "Redis",      True,  "Base62",       "Docker/K8s",  "Python/FastAPI/Go"),
    ("Isak Nyström",    "PostgreSQL/DynamoDB","Redis",      True,  "Base62",       "Docker",      "Python/FastAPI/Go"),
    ("Freja Lindholm",  "PostgreSQL",         "Redis",      True,  "Base62",       "Docker/K8s",  "Go/Python")
]

# 2. Design Considerations (Exact Counts & Percentages out of 10)
design_considerations_counts = [
    ("Performance optimization", 9),   # 9/10 -> 90%
    ("Scalability approaches", 8),     # 8/10 -> 80%
    ("Collision handling", 4),         # 4/10 -> 40%
    ("Regional distribution (CDN)", 2),# 2/10 -> 20%
    ("Analytics/metrics", 3),         # 3/10 -> 30%
    ("Service separation", 4),        # 4/10 -> 40%
    ("Cloud-native approaches", 6)     # 6/10 -> 60%
]

dc_list_for_df = []
for (label, count) in design_considerations_counts:
    pct = (count / 10) * 100
    dc_list_for_df.append((label, count, pct))

df_design_considerations = pd.DataFrame(
    dc_list_for_df,
    columns=["Design Consideration", "Count (out of 10)", "Exact Percentage"]
)

# 3. Key Patterns (Sweden)
key_patterns = [
    "Strong emphasis on caching (7/10 participants specifically mentioned Redis).",
    "High adoption of Base62 encoding for short URL generation (6/10 participants).",
    "Consistent focus on load balancing for scalability (7/10 participants).",
    "Modern infrastructure patterns (Docker, Kubernetes) prevalent in responses.",
    "Preference for PostgreSQL as primary database (5/10 participants).",
    "Clear understanding of read vs. write operation differences.",
    "Strong technical specificity rather than conceptual approaches.",
    "Python/FastAPI commonly mentioned implementation language (5/10 participants)."
]

# 4. Create DataFrames (Sweden)
df_tech = pd.DataFrame(
    technologies_mentioned,
    columns=["Technology", "Count", "Percentage"]
)

df_components = pd.DataFrame(
    component_matrix,
    columns=[
        "Participant",
        "Database",
        "Caching",
        "Load Balancing",
        "URL Algorithm",
        "Containerization",
        "Programming Language"
    ]
)

df_patterns = pd.DataFrame({"Key Patterns": key_patterns})

# 5. Display/analysis functions (Sweden)
def display_tables_sweden():
    print("\n=== Key Technologies Mentioned (Sweden) ===")
    print(df_tech.to_string(index=False))

    print("\n=== System Design Components (Raw) (Sweden) ===")
    print(df_components.to_string(index=False))

    print("\n=== Design Considerations (Now Out of 10) (Sweden) ===")
    print(df_design_considerations.to_string(index=False))

    print("\n=== Key Patterns Observed (Sweden) ===")
    print(df_patterns.to_string(index=False))


def analyze_components_sweden():
    """
    Perform deeper analysis on the Swedish component matrix
    """
    db_counts = df_components["Database"].value_counts()

    expanded_db_list = []
    for participant, db_field in zip(df_components["Participant"], df_components["Database"]):
        dbs = db_field.split("/")
        for db in dbs:
            expanded_db_list.append((participant, db.strip()))

    df_db_expanded = pd.DataFrame(expanded_db_list, columns=["Participant", "Database"])
    db_counts_expanded = df_db_expanded["Database"].value_counts()

    # Caching usage
    def is_caching_used(x):
        return x not in [False, None, "Not specified"]

    caching_boolean_series = df_components["Caching"].apply(is_caching_used)
    caching_usage = caching_boolean_series.value_counts()

    # Load Balancing usage
    lb_boolean_series = df_components["Load Balancing"].apply(lambda x: bool(x))
    lb_usage = lb_boolean_series.value_counts()

    # Docker / K8s usage
    df_components["Used Docker"] = df_components["Containerization"].str.contains("Docker", case=False)
    df_components["Used K8s"] = df_components["Containerization"].str.contains("K8s", case=False)

    print("\n=== Simple Database Counts (Sweden, exact strings) ===")
    print(db_counts.to_string())

    print("\n=== Expanded Database Counts (Sweden, split on '/') ===")
    print(db_counts_expanded.to_string())

    print("\n=== Caching Usage (Sweden, True/False) ===")
    print(caching_usage.to_string())

    print("\n=== Load Balancing Usage (Sweden, True/False) ===")
    print(lb_usage.to_string())

    print("\n=== Docker Usage Summary (Sweden) ===")
    print(df_components["Used Docker"].value_counts(dropna=False).to_string())

    print("\n=== Kubernetes Usage Summary (Sweden) ===")
    print(df_components["Used K8s"].value_counts(dropna=False).to_string())

    ct_db_lb = pd.crosstab(df_components["Database"], lb_boolean_series)
    print("\n=== Crosstab: Database vs. Load Balancing (Sweden) ===")
    print(ct_db_lb.to_string())


def main_sweden():
    print(f"\n=== ANALYSIS FOR SWEDISH PARTICIPANTS (Total: {total_swedish_participants}) ===\n")
    display_tables_sweden()
    analyze_components_sweden()


# ---------------------------------------------------------------
#  B) NETHERLANDS ANALYSIS
# ---------------------------------------------------------------

# 1. Core Data (Netherlands)
total_netherlands_participants = 11

technologies_mentioned_nl = [
    ("PostgreSQL",        11, 100),
    ("Redis (caching)",   11, 100),
    ("Base62 encoding",    9, 82),
    ("Docker",             8, 73),
    ("Kubernetes",         5, 45),
    ("Python/FastAPI",     6, 55),
    ("Load balancing",     3, 27),
    ("Express/Node.js",    2, 18),
    ("Go language",        1,  9),
    ("Memcached",          1,  9),
    ("DynamoDB",           1,  9)
]

component_matrix_nl = [
    ("Tess de Vries",    "PostgreSQL/DynamoDB", "Redis/Memcached", True,  "Base62/UUID",         "Docker/K8s", "FastAPI/Go"),
    ("Rick",             "PostgreSQL",          "Redis",           True,  "Base62/UUID/Counter", "Docker",     "FastAPI/Express"),
    ("Sanne Visser",     "PostgreSQL/Redis",    "Redis",           False, "Hash/Random",         "Docker",     "FastAPI"),
    ("Maarten",          "PostgreSQL",          "Redis",           True,  "Base62/UUID",         "Docker/K8s", "FastAPI"),
    ("Esmee",            "PostgreSQL",          "Redis",           False, "Base62/UUID",         "Docker/K8s", "FastAPI"),
    ("Cas",              "PostgreSQL",          "Redis",           False, "Crypto-random",       "Not specified","Not specified"),
    ("Lucas",            "PostgreSQL",          "Redis",           False, "Base62/UUID/Counter", "Docker/K8s", "Not specified"),
    ("Hanous Dedki",     "PostgreSQL",          "Redis",           False, "Base62/UUID",         "Docker",     "Not specified"),
    ("Thjis",            "PostgreSQL",          "Redis",           False, "Base62/Snowflake",     "Not specified","Not specified"),
    ("Bram",             "PostgreSQL",          "Redis",           False, "Base62/Hash",         "Docker/K8s", "FastAPI/Express"),
    ("Pjotr",            "PostgreSQL",          "Redis",           False, "Base62 from numeric ID","Not specified","Not specified")
]

# 2. Design Considerations (Approx or exact out of 11)
design_considerations_nl = [
    ("Performance optimization", 80),
    ("Scalability approaches",    70),
    ("Collision handling",        60),
    ("Caching strategy",         100),
    ("Rate limiting",             70),
    ("Input validation",          60),
    ("Cloud-native approaches",   50)
]

df_design_considerations_nl = pd.DataFrame(
    design_considerations_nl,
    columns=["Design Consideration", "Approx. Percentage"]
)

# 3. Key Patterns (Netherlands)
key_patterns_nl = [
    "PostgreSQL is universally mentioned (11/11).",
    "Redis caching is used by all participants (11/11).",
    "9/11 participants specifically mention Base62 encoding for short-code generation.",
    "Docker is very common (8/11), and about half also mention Kubernetes (5/11).",
    "Many highlight rate limiting and input validation to prevent abuse.",
    "FastAPI is mentioned more often than other languages/frameworks (6/11).",
    "Some mention load balancing (3/11).",
    "A few mention alternative DB or caching (DynamoDB, Memcached)."
]

# 4. Create DataFrames (Netherlands)
df_tech_nl = pd.DataFrame(
    technologies_mentioned_nl,
    columns=["Technology", "Count", "Percentage"]
)

df_components_nl = pd.DataFrame(
    component_matrix_nl,
    columns=[
        "Participant",
        "Database",
        "Caching",
        "Load Balancing",
        "URL Algorithm",
        "Containerization",
        "Programming Language"
    ]
)

df_patterns_nl = pd.DataFrame({"Key Patterns": key_patterns_nl})

# 5. Display/analysis functions (Netherlands)
def display_netherlands_tables():
    print(f"\n=== Key Technologies Mentioned (Netherlands) ===")
    print(df_tech_nl.to_string(index=False))

    print("\n=== System Design Components (Raw) (Netherlands) ===")
    print(df_components_nl.to_string(index=False))

    print("\n=== Design Considerations (Approx.) (Netherlands) ===")
    print(df_design_considerations_nl.to_string(index=False))

    print("\n=== Key Patterns Observed (Netherlands) ===")
    print(df_patterns_nl.to_string(index=False))

def analyze_components_netherlands():
    """
    Perform deeper analysis on the Netherlands component matrix
    """
    db_counts = df_components_nl["Database"].value_counts()

    expanded_db_list = []
    for participant, db_field in zip(df_components_nl["Participant"], df_components_nl["Database"]):
        dbs = db_field.split("/")
        for db in dbs:
            expanded_db_list.append((participant, db.strip()))

    df_db_expanded = pd.DataFrame(expanded_db_list, columns=["Participant", "Database"])
    db_counts_expanded = df_db_expanded["Database"].value_counts()

    # Caching usage
    def is_caching_used(x):
        return x not in [False, None, "Not specified"]

    caching_boolean_series = df_components_nl["Caching"].apply(is_caching_used)
    caching_usage = caching_boolean_series.value_counts()

    # Load Balancing usage
    lb_boolean_series = df_components_nl["Load Balancing"].apply(lambda x: bool(x))
    lb_usage = lb_boolean_series.value_counts()

    # Docker / K8s usage
    df_components_nl["Used Docker"] = df_components_nl["Containerization"].str.contains("Docker", case=False)
    df_components_nl["Used K8s"]   = df_components_nl["Containerization"].str.contains("K8s",   case=False)

    print("\n=== Simple Database Counts (Netherlands, exact strings) ===")
    print(db_counts.to_string())

    print("\n=== Expanded Database Counts (Netherlands, split on '/') ===")
    print(db_counts_expanded.to_string())

    print("\n=== Caching Usage (Netherlands, True/False) ===")
    print(caching_usage.to_string())

    print("\n=== Load Balancing Usage (Netherlands, True/False) ===")
    print(lb_usage.to_string())

    print("\n=== Docker Usage Summary (Netherlands) ===")
    print(df_components_nl["Used Docker"].value_counts(dropna=False).to_string())

    print("\n=== Kubernetes Usage Summary (Netherlands) ===")
    print(df_components_nl["Used K8s"].value_counts(dropna=False).to_string())

    ct_db_lb = pd.crosstab(df_components_nl["Database"], lb_boolean_series)
    print("\n=== Crosstab: Database vs. Load Balancing (Netherlands) ===")
    print(ct_db_lb.to_string())

def main_netherlands():
    print(f"\n=== ANALYSIS FOR NETHERLANDS PARTICIPANTS (Total: {total_netherlands_participants}) ===\n")
    display_netherlands_tables()
    analyze_components_netherlands()


# ---------------------------------------------------------------
#  C) RWANDA ANALYSIS (NEW)
# ---------------------------------------------------------------

# 1. Core Data (Rwanda)
total_rwanda_participants = 10

technologies_mentioned_rwanda = [
    ("Redis (caching/DB)",   4, 40),  # e.g. Brian, Mihigo, Pacifique, (Tubirye also mentions Redis/Memcached)
    ("DynamoDB",             2, 20),
    ("MongoDB",              1, 10),
    ("PostgreSQL",           1, 10),
    ("Cassandra",            1, 10),
    ("Base62 encoding",      3, 30),
    ("TSID / custom ID",     2, 20),
    ("Load balancing/scaling",2, 20),
    ("Serverless (Lambda)",  1, 10)
]

component_matrix_rwanda = [
    ("Brian Gitego",         "Redis",            "Redis",            True,  "TSID",                "Not specified",        "Not specified"),
    ("David Hitimana",       "Not specified",    "Not specified",    False, "Not specified",       "Not specified",        "Not specified"),
    ("David Tubirye",        "Cassandra/DynamoDB","Redis/Memcached", True,  "Random/Base62",       "Not specified",        "Not specified"),
    ("Mihigo Prince Jordan", "Redis",            "Redis",            False, "Base62",              "Not specified",        "Not specified"),
    ("Iradukunda Pacifique", "Redis/PostgreSQL", "Redis",            False, "Custom unique func",  "Not specified",        "Not specified"),
    ("Issa Jean Marie",      "Not specified",    "Not specified",    False, "Not specified",       "Not specified",        "Not specified"),
    ("Merlyne Iradukunda",   "Not specified",    "Not specified",    False, "Not specified",       "Not specified",        "Not specified"),
    ("Muhire",               "DynamoDB",         False,              False, "Random 6-char",       "Serverless (Lambda)",  "Not specified"),
    ("Adeline",              "Not specified",    "Not specified",    False, "Not specified",       "Not specified",        "Not specified"),
    ("Elvis Rugamba",        "MongoDB",          "Not specified",    False, "Base62/random check", "Not specified",        "Not specified")
]

design_considerations_rwanda = [
    ("Scalability / horizontal scaling", 70),
    ("Uniqueness / collision handling",  60),
    ("Caching strategy (Redis)",         50),
    ("High availability",                50),
    ("Rate limiting to prevent abuse",   40),
    ("Serverless / distributed approach",30)
]

df_design_considerations_rwanda = pd.DataFrame(
    design_considerations_rwanda,
    columns=["Design Consideration", "Approx. Percentage"]
)

key_patterns_rwanda = [
    "Significant mention of NoSQL (Redis, DynamoDB, Cassandra, MongoDB).",
    "Redis used for caching or primary store in multiple solutions.",
    "Variety of short-code generation: Base62, TSID, or custom random ID.",
    "Two mention load balancing or horizontal scaling approaches.",
    "One participant uses a serverless approach (AWS Lambda).",
    "Most do not specify containerization or programming languages."
]

df_tech_rwanda = pd.DataFrame(
    technologies_mentioned_rwanda,
    columns=["Technology", "Count", "Percentage"]
)

df_components_rwanda = pd.DataFrame(
    component_matrix_rwanda,
    columns=[
        "Participant",
        "Database",
        "Caching",
        "Load Balancing",
        "URL Algorithm",
        "Containerization",
        "Programming Language"
    ]
)

df_patterns_rwanda = pd.DataFrame({"Key Patterns": key_patterns_rwanda})

def display_rwanda_tables():
    print(f"\n=== Key Technologies Mentioned (Rwanda) ===")
    print(df_tech_rwanda.to_string(index=False))

    print("\n=== System Design Components (Raw) (Rwanda) ===")
    print(df_components_rwanda.to_string(index=False))

    print("\n=== Design Considerations (Approx.) (Rwanda) ===")
    print(df_design_considerations_rwanda.to_string(index=False))

    print("\n=== Key Patterns Observed (Rwanda) ===")
    print(df_patterns_rwanda.to_string(index=False))

def analyze_components_rwanda():
    """
    Perform deeper analysis on the Rwanda component matrix
    """
    db_counts = df_components_rwanda["Database"].value_counts()

    expanded_db_list = []
    for participant, db_field in zip(df_components_rwanda["Participant"], df_components_rwanda["Database"]):
        dbs = db_field.split("/")
        for db in dbs:
            expanded_db_list.append((participant, db.strip()))

    df_db_expanded = pd.DataFrame(expanded_db_list, columns=["Participant", "Database"])
    db_counts_expanded = df_db_expanded["Database"].value_counts()

    # Standardize caching usage
    def is_caching_used(x):
        return x not in [False, None, "Not specified"]

    caching_boolean_series = df_components_rwanda["Caching"].apply(is_caching_used)
    caching_usage = caching_boolean_series.value_counts()

    # Load Balancing usage
    lb_boolean_series = df_components_rwanda["Load Balancing"].apply(lambda x: bool(x))
    lb_usage = lb_boolean_series.value_counts()

    # Docker / K8s usage?  We'll do the same approach, though they mostly said "Not specified"
    df_components_rwanda["Used Docker"] = df_components_rwanda["Containerization"].str.contains("Docker", case=False)
    df_components_rwanda["Used K8s"]   = df_components_rwanda["Containerization"].str.contains("K8s",   case=False)

    print("\n=== Simple Database Counts (Rwanda, exact strings) ===")
    print(db_counts.to_string())

    print("\n=== Expanded Database Counts (Rwanda, split on '/') ===")
    print(db_counts_expanded.to_string())

    print("\n=== Caching Usage (Rwanda, True/False) ===")
    print(caching_usage.to_string())

    print("\n=== Load Balancing Usage (Rwanda, True/False) ===")
    print(lb_usage.to_string())

    print("\n=== Docker Usage Summary (Rwanda) ===")
    print(df_components_rwanda["Used Docker"].value_counts(dropna=False).to_string())

    print("\n=== Kubernetes Usage Summary (Rwanda) ===")
    print(df_components_rwanda["Used K8s"].value_counts(dropna=False).to_string())

    ct_db_lb = pd.crosstab(df_components_rwanda["Database"], lb_boolean_series)
    print("\n=== Crosstab: Database vs. Load Balancing (Rwanda) ===")
    print(ct_db_lb.to_string())

def main_rwanda():
    print(f"\n=== ANALYSIS FOR RWANDA PARTICIPANTS (Total: {total_rwanda_participants}) ===\n")
    display_rwanda_tables()
    analyze_components_rwanda()


# ---------------------------------------------------------------
#  D) MAIN ENTRY POINT
# ---------------------------------------------------------------


# ---------------------------------------------------------------
#  E) DETAILED CROSS-COUNTRY COMPARISONS
# ---------------------------------------------------------------

def compare_countries_detailed():
    """
    Provides a multi-metric comparison of caching usage, load balancing,
    Docker, K8s, and expanded database usage across Sweden, Netherlands, Rwanda.
    Prints a single DataFrame for each group of metrics plus an overall summary.
    """

    # 1) Summarize usage for Sweden
    sweden_caching_usage = _compute_caching_usage(df_components)
    sweden_lb_usage = _compute_load_balancing_usage(df_components)
    sweden_docker_usage = _compute_docker_usage(df_components)
    sweden_k8s_usage = _compute_k8s_usage(df_components)
    sweden_db_expanded_counts = _compute_expanded_db_counts(df_components)
    sweden_count = total_swedish_participants

    # 2) Summarize usage for Netherlands
    netherlands_caching_usage = _compute_caching_usage(df_components_nl)
    netherlands_lb_usage = _compute_load_balancing_usage(df_components_nl)
    netherlands_docker_usage = _compute_docker_usage(df_components_nl)
    netherlands_k8s_usage = _compute_k8s_usage(df_components_nl)
    netherlands_db_expanded_counts = _compute_expanded_db_counts(df_components_nl)
    netherlands_count = total_netherlands_participants

    # 3) Summarize usage for Rwanda
    rwanda_caching_usage = _compute_caching_usage(df_components_rwanda)
    rwanda_lb_usage = _compute_load_balancing_usage(df_components_rwanda)
    rwanda_docker_usage = _compute_docker_usage(df_components_rwanda)
    rwanda_k8s_usage = _compute_k8s_usage(df_components_rwanda)
    rwanda_db_expanded_counts = _compute_expanded_db_counts(df_components_rwanda)
    rwanda_count = total_rwanda_participants

    # -----------------------------------------------------------
    # A) Build a DataFrame for “Caching / LB / Docker / K8s” usage
    # -----------------------------------------------------------
    data_usage_comparison = [
        {
            "Metric": "Caching Usage (True)",
            "Sweden": f"{sweden_caching_usage} / {sweden_count} ({sweden_caching_usage/sweden_count*100:.0f}%)",
            "Netherlands": f"{netherlands_caching_usage} / {netherlands_count} ({netherlands_caching_usage/netherlands_count*100:.0f}%)",
            "Rwanda": f"{rwanda_caching_usage} / {rwanda_count} ({rwanda_caching_usage/rwanda_count*100:.0f}%)"
        },
        {
            "Metric": "Load Balancing (True)",
            "Sweden": f"{sweden_lb_usage} / {sweden_count} ({sweden_lb_usage/sweden_count*100:.0f}%)",
            "Netherlands": f"{netherlands_lb_usage} / {netherlands_count} ({netherlands_lb_usage/netherlands_count*100:.0f}%)",
            "Rwanda": f"{rwanda_lb_usage} / {rwanda_count} ({rwanda_lb_usage/rwanda_count*100:.0f}%)"
        },
        {
            "Metric": "Docker Usage (True)",
            "Sweden": f"{sweden_docker_usage} / {sweden_count} ({sweden_docker_usage/sweden_count*100:.0f}%)",
            "Netherlands": f"{netherlands_docker_usage} / {netherlands_count} ({netherlands_docker_usage/netherlands_count*100:.0f}%)",
            "Rwanda": f"{rwanda_docker_usage} / {rwanda_count} ({rwanda_docker_usage/rwanda_count*100:.0f}%)"
        },
        {
            "Metric": "K8s Usage (True)",
            "Sweden": f"{sweden_k8s_usage} / {sweden_count} ({sweden_k8s_usage/sweden_count*100:.0f}%)",
            "Netherlands": f"{netherlands_k8s_usage} / {netherlands_count} ({netherlands_k8s_usage/netherlands_count*100:.0f}%)",
            "Rwanda": f"{rwanda_k8s_usage} / {rwanda_count} ({rwanda_k8s_usage/rwanda_count*100:.0f}%)"
        }
    ]
    df_usage_comparison = pd.DataFrame(data_usage_comparison)

    # -----------------------------------------------------------
    # B) Build DB expansions summary
    #    We'll unify the top DB expansions from each country
    # -----------------------------------------------------------
    # We'll gather the union of all DB expansions across countries
    all_dbs = set(sweden_db_expanded_counts.keys()) \
              | set(netherlands_db_expanded_counts.keys()) \
              | set(rwanda_db_expanded_counts.keys())

    db_rows = []
    for db_name in sorted(all_dbs):
        sw_count = sweden_db_expanded_counts.get(db_name, 0)
        nl_count = netherlands_db_expanded_counts.get(db_name, 0)
        rw_count = rwanda_db_expanded_counts.get(db_name, 0)
        db_rows.append({
            "Database": db_name,
            "Sweden": f"{sw_count} / {sweden_count} ({sw_count/sweden_count*100:.0f}%)" if sweden_count>0 else sw_count,
            "Netherlands": f"{nl_count} / {netherlands_count} ({nl_count/netherlands_count*100:.0f}%)" if netherlands_count>0 else nl_count,
            "Rwanda": f"{rw_count} / {rwanda_count} ({rw_count/rwanda_count*100:.0f}%)" if rwanda_count>0 else rw_count
        })

    df_db_comparison = pd.DataFrame(db_rows)

    # -----------------------------------------------------------
    # Print out the DataFrames
    # -----------------------------------------------------------
    print("\n=== CROSS-COUNTRY COMPARISON: USAGE STATISTICS ===")
    print(df_usage_comparison.to_string(index=False))

    print("\n=== CROSS-COUNTRY COMPARISON: DATABASE USAGE (Expanded) ===")
    print(df_db_comparison.to_string(index=False))


# ---------------------------------------------------------------
#  F) HELPER FUNCTIONS (for above)
# ---------------------------------------------------------------

def _compute_caching_usage(df):
    """
    Returns the count of participants using caching (True)
    in the given DataFrame.
    """
    def is_caching_used(x):
        return x not in [False, None, "Not specified"]

    caching_bool = df["Caching"].apply(is_caching_used)
    return caching_bool.sum()


def _compute_load_balancing_usage(df):
    """
    Returns the count of participants for which "Load Balancing" is True (non-false).
    """
    lb_bool = df["Load Balancing"].apply(lambda x: bool(x))
    return lb_bool.sum()


def _compute_docker_usage(df):
    """
    Returns how many participants mention "Docker" in Containerization.
    We assume a column "Used Docker" might be created, but let's do a direct check here.
    """
    contain_str = df["Containerization"].astype(str)
    is_docker = contain_str.str.contains("Docker", case=False, na=False)
    return is_docker.sum()


def _compute_k8s_usage(df):
    """
    Returns how many participants mention "K8s" in Containerization.
    """
    contain_str = df["Containerization"].astype(str)
    is_k8s = contain_str.str.contains("K8s", case=False, na=False)
    return is_k8s.sum()


def _compute_expanded_db_counts(df):
    """
    Splits DB fields like 'Redis/DynamoDB' and counts each mention across participants.
    Returns a dict: { 'Redis': x, 'DynamoDB': y, ... }
    """
    db_counts = {}
    for db_field in df["Database"]:
        # handle None or false
        if not db_field or db_field in [False, "Not specified"]:
            continue
        for db in db_field.split("/"):
            db_str = db.strip()
            db_counts[db_str] = db_counts.get(db_str, 0) + 1

    return db_counts

def main():
    # 1) Run Swedish analysis
    main_sweden()

    # 2) Run Netherlands analysis
    main_netherlands()

    # 3) Run Rwanda analysis
    main_rwanda()


    compare_countries_detailed()

if __name__ == "__main__":
    main()
