import csv
import json
from pathlib import Path

RAW = Path(r"C:\Users\marti\OneDrive\Desktop\JIBU\raw_text")
OUT = Path(r"C:\Users\marti\OneDrive\Desktop\JIBU\necta-papers\geography_final.csv")

def load(name):
    return json.loads((RAW / name).read_text(encoding="utf-8-sig"))

topics = {
    "2005": ["Earth's Shape", "Eclipses", "Time Zones", "Altitude and Temperature", "Tectonic Forces",
             "River Deltas", "Springs", "Drainage Patterns", "Limestone Features", "Earth's Core"],
    "2007": ["Rock Permeability", "Glacial Features", "Drainage Patterns", "Earth's Crust Layers",
             "Desert Landforms", "Chemical Weathering", "Igneous Intrusions", "Coral Reefs",
             "Altitude and Temperature", "River Rejuvenation"],
    "2009": ["Solar System", "Time Zones", "Lunar Eclipse", "Sun Composition", "Limestone Drainage",
             "Marine Deposition", "Climate and Vegetation", "Soil Texture", "Temperate Cyclones", "Soil Profile"],
    "2010": ["Volcanic Landforms", "Earthquakes", "Time Zones", "Igneous Rocks", "Weathering Features",
             "River Erosion Processes", "Map Scale", "Desert Landforms", "River Terraces", "Igneous Rocks"],
    "2011": ["Forest Types", "Pressure Belts", "Coastal Landforms", "Time Zones", "Surveying Instruments",
             "River Functions", "Map Grid References", "Weather Elements", "Earth's Rotation", "Volcanic Landforms"],
    "2012": ["Earth's Layers", "Mass Wasting", "Weathering Features", "River Erosion", "Earth's Rotation",
             "Fold Mountains", "Wind Erosion", "Great Circles", "Earthquake Measurement", "Soil Texture"],
    "2013": ["Glacial Landforms", "Geysers", "Coral Reefs", "Standard Time", "Rainfall Formation",
             "Weather Instruments", "Faulting", "Equatorial Climate", "Earth's Crust", "Compass Bearings"],
    "2014": ["Wind Erosion Landforms", "River Stages", "Solstices", "Weather Instruments", "Desert Types",
             "Altitude and Temperature", "Tectonic Forces", "Condensation", "Glacial Landforms", "Earthquake Waves"],
    "2015": ["Seasons", "Southern Hemisphere Geography", "Continental Shelf", "Temperature Factors",
             "River Erosion", "Soil Processes", "Vertical Crust Movements", "Desert Landforms",
             "Soil Organic Matter", "Earthquake Measurement"],
    "2016": ["Earth's Crust Layers", "Time Zones", "Solstices", "Day Length", "Solar System",
             "Ocean Winds", "Rainfall Types", "Mountain Classification", "River Features"],  # only 9, item vi dropped
    "2017": ["Solar System", "Earth's Crust Layers", "Wind Erosion", "River Rejuvenation", "Weather Forecasting",
             "Water Infiltration", "Metamorphic Rocks", "Climate Types", "Weathering Processes", "Ocean Floor Features"],
    "2018": ["Weather Instruments", "Volcanic Features", "Soil Formation", "Atmosphere Layers", "Solar System",
             "Climate Types", "Navigation Instruments", "Chemical Weathering", "Coastal Landforms", "Map Scale"],
    "2019": ["Earth's Crust Layers", "Mass Wasting", "Forest Types", "Pastoralism", "Forest Resources",
             "Soil Types", "Migration", "Weather for Agriculture", "Monsoon Climate"],  # only 9, item ii dropped
    "2020": ["Solar System", "Earth's Crust Layers", "Soil Properties", "River Processes", "Desertification",
             "Fuel Resources", "Natural Regions", "Mineral Types", "Altitude and Temperature", "Eclipses"],
    "2021": ["Solar System", "Soil Erosion Types", "Population Structure", "Environmental Conservation",
             "Forest Types", "Time Zones", "Ecotourism", "Temperature Factors", "Mining Alternatives", "Renewable Energy"],
    "2022": ["Climate Classification", "Time Zones", "Urban Environmental Problems", "Drainage Patterns",
             "Livestock Keeping", "Mountain Formation", "Soil Types", "Earthquake Zones", "Mining Methods"],  # only 9, item vii dropped
    "2023": ["Perihelion and Aphelion", "Soil Horizons", "Transport Modes", "Farming Types",
             "Earthquake Measurement", "Coastal Erosion", "Time Zones", "Population Dynamics",
             "Mining Methods", "Industrial Location"],
    "2024": ["Meteors and Space Objects", "Surveying", "Transport Modes", "Mining Methods",
             "Urban Environmental Problems", "Time Zones", "Renewable Energy", "Earth's Crust",
             "Soil Components", "Industrial Location"],
    "2025": ["Time Zones", "Renewable Energy", "Livestock Keeping", "Desert Landforms", "Equatorial Climate",
             "Environmental Conservation", "Tourism", "Industrial Location", "Fold Types", "Population Fertility"],
}

rows = []

def add_rows(year, items):
    for item, topic in zip(items, topics[year]):
        opts = item["options"]
        rows.append(dict(
            Subject="Geography", Form_Level="Form 4", Topic=topic,
            Question=item["question"],
            Option_A=opts.get("A", ""), Option_B=opts.get("B", ""), Option_C=opts.get("C", ""),
            Option_D=opts.get("D", ""), Option_E=opts.get("E", ""),
            Correct_Answer=item["answer"], Explanation=item["reason"],
        ))

clean_years = ["2005", "2007", "2009", "2010", "2011", "2012", "2013", "2014", "2015",
               "2017", "2020", "2021", "2024", "2025"]
for year in clean_years:
    items = load(f"geo_{year}.json")
    assert len(items) == 10, f"{year}: expected 10, got {len(items)}"
    add_rows(year, items)

# 2016: drop item vi - question text and options are mismatched in the source
# PDF itself (a genuine content error, not a parsing artifact): the stem asks
# about soil deposition between horizons, but the options list slope-shape
# terms (convex/concave-sided) that belong to a different question entirely.
items_2016 = load("geo_2016.json")
assert len(items_2016) == 10
items_2016_kept = [it for idx, it in enumerate(items_2016) if idx != 5]
assert len(items_2016_kept) == 9
add_rows("2016", items_2016_kept)

# 2018: item x (index 9) has a genuine source error - the answer key first
# says "Correct answer: D" then, after showing the worked calculation
# (900,000 cm = 9 km), restates "Correct answer: A" at the very end. The math
# clearly supports A (9 km), so we take the source's own final correction.
# Also fixes a minor OCR typo in item iii option C ("tim." -> "time").
items_2018 = load("geo_2018.json")
assert len(items_2018) == 10
items_2018[2]["options"]["C"] = "time"
items_2018[9]["answer"] = "A"
items_2018[9]["reason"] = "1 cm on the map represents 50,000 cm on the ground. 18 cm x 50,000 = 900,000 cm = 9 km."
add_rows("2018", items_2018)

# 2019: drop item ii (index 1) - the source's own reason text admits its
# worked calculation (5:00 pm) does not match any of the given options
# ("this question seems to have a miscalculation in the options, and none
# fits exactly"), so the marked answer (C) cannot be trusted.
items_2019 = load("geo_2019.json")
assert len(items_2019) == 10
items_2019_kept = [it for idx, it in enumerate(items_2019) if idx != 1]
assert len(items_2019_kept) == 9
add_rows("2019", items_2019_kept)

# 2022: item vii (lunar eclipse diagram question) never parsed - its answer
# options were position labels on a diagram image with no extractable text,
# so there is nothing to faithfully reconstruct. The remaining 9 auto-parsed
# cleanly.
items_2022 = load("geo_2022.json")
assert len(items_2022) == 9, f"2022: expected 9, got {len(items_2022)}"
add_rows("2022", items_2022)

# 2023: item vi (index 5) was manually re-derived from the raw PDF text - the
# automated parser swallowed it into item v's reason because of its nested
# (i)-(iv) sub-statement list (the same class of issue as the Biology Darwin
# question).
items_2023 = load("geo_2023.json")
assert len(items_2023) == 9, f"2023 auto: expected 9 (item vi missing), got {len(items_2023)}"
items_2023[4]["reason"] = "The Richter Scale measures the magnitude of earthquakes or earth vibrations."
coastal_item = {
    "question": ("Coastal areas do not maintain their shape due to erosional and depositional processes. "
                 "Which factors influence those processes? (i) The strength of the wind that blows over the sea "
                 "(ii) Weather condition in the area (iii) The depth of the sea water along the coast "
                 "(iv) The nature of the rocks on the coast"),
    "options": {
        "A": "(i), (ii) and (iv)", "B": "(i), (ii) and (iii)", "C": "(i), (iii) and (iv)",
        "D": "(ii), (iii) and (iv)", "E": "(ii) and (iv)",
    },
    "answer": "C",
    "reason": "These physical factors directly influence erosion and deposition on coastal areas.",
}
items_2023_full = items_2023[:5] + [coastal_item] + items_2023[5:]
assert len(items_2023_full) == 10
add_rows("2023", items_2023_full)

fieldnames = ["Subject", "Form_Level", "Topic", "Question", "Option_A", "Option_B", "Option_C", "Option_D", "Option_E", "Correct_Answer", "Explanation"]
with open(OUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {len(rows)} rows to {OUT}")
