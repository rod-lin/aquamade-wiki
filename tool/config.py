
IGEM_YEAR = "2017"
TEAM_NAME = "HFLS_H2Z_Hangzhou"
ABS_BASE = "src"

PAGES = {
    "main": (ABS_BASE + "/main.html",           "Template:%s" % TEAM_NAME),
    "home": (ABS_BASE + "/sub/home.html",       "Team:%s" % TEAM_NAME),
    "hp": (ABS_BASE + "/sub/hp.html",           "Team:%s/hp" % TEAM_NAME),
    "note": (ABS_BASE + "/sub/note.html",       "Team:%s/note" % TEAM_NAME),
    "parts": (ABS_BASE + "/sub/parts.html",     "Team:%s/parts" % TEAM_NAME),
    "project": (ABS_BASE + "/sub/project.html", "Team:%s/project" % TEAM_NAME),
    "team": (ABS_BASE + "/sub/team.html",       "Team:%s/Team" % TEAM_NAME),
    
    # standard pages
    "attrib": (ABS_BASE + "/sub/attrib.html",       "Team:%s/Attributions" % TEAM_NAME),
    "interlab": (ABS_BASE + "/sub/interlab.html",   "Team:%s/InterLab" % TEAM_NAME),
    "collab": (ABS_BASE + "/sub/collab.html",       "Team:%s/Collaborations" % TEAM_NAME),
    "model": (ABS_BASE + "/sub/model.html",         "Team:%s/Model" % TEAM_NAME),
    
    "silver": (ABS_BASE + "/sub/silver.html",         "Team:%s/HP/Silver" % TEAM_NAME),
    "gold": (ABS_BASE + "/sub/gold.html",         "Team:%s/HP/Gold_Integrated" % TEAM_NAME),
}
