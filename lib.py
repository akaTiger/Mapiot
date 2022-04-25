def version():
    versions = [
        "EMPTY",
        "1.13.1.0",
        "1.14.1.0",
        "1.18 (Bedrock)",
        "1.18 (Java)",
        "1.18.2",
        "1.18.30",
        "1.19.0.26 Beta",
        "1.19.0.27 Preview",
        "1.6.93 (legacy)",
        "2.2.12145 (Windows)",
        "2.2.12146 (New Windows App)",
        "2.2.12147 (Mac)", "2.2.12148 (Linux)",
        "2.2.2040 (macOS - 10.9 only)",
        "2.3.136 (Linux)", "2.3.136 (Mac)",
        "2.3.136 (New Windows App)",
        "2.3.136 (Windows)",
        "PS4 1.85",
        "PS4 1.88",
        "PS4 1.89",
        "PS4 1.90",
        "PS4 1.91",
        "PS4 1.92",
        "PS4 1.93",
        "PS4 1.94",
        "PS4 1.95"
    ]
    return versions

def project():
    projects = [
        "BDS",
        "MCPE",
        "MCCE",
        "MCD",
        "MCL",
        "REALMS",
        "MC",
        "WEB"
    ]
    return projects

def status():
    stat = [
        "Open",
        "In Progress",
        "Reopened",
        "Resolved",
        "Closed",
        "Postponed"
    ]
    return stat

def getParameters():
    p = {
        0: ["List All", "listResources"],
        1: ["Resource Info By ID", "getResource"],
        2: ["Resource Info By Author", "getResourcesByAuthor"],
        3: ["List Avaliable Categories", "listResourceCategories"],
        4: ["Resource Update By ID", "getResourceUpdate"],
        5: ["Resource ALL Updates By ID", "getResourceUpdates"],
        6: ["Author Information By User ID", "getAuthor"],
        7: ["Author Information By Excact User Name", "findAuthor"]
    }
    return p

def errorMessage():
    e = {
        "unexpected": "*** UNEXPECTED ERROR: PLEASE SUBMIT A ISSUE ***",
        "id": "*** ID ERROR: SHOULD NOT CONTAIN ALPHABET ***",
        "parameter": "*** Input Parameter ERROR: CHECK GITHUB PAGE FOR CORRECT USEAGE ***"
    }
    return e