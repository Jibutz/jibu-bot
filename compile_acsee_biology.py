import csv

def lettered(*phrases):
    letters = "abcdefghijklmnop"
    return ", ".join(f"{letters[i]}) {p}" for i, p in enumerate(phrases))


rows = []

# ============================== YEAR 1991 ==============================
rows.append(dict(Topic="Cell Division", Question="Explain the appearance of an animal cell at each of the following stages of division: (i) Pachytene (ii) Diplotene (iii) Metaphase I of Meiosis (iv) Metaphase of Mitosis",
    Answer_Summary=lettered(
        "pachytene: homologous chromosomes fully paired (synapsed), crossing over occurs",
        "diplotene: homologous chromosomes begin to separate but stay joined at chiasmata",
        "metaphase I of meiosis: homologous pairs align at the metaphase plate, spindle fibers attach to centromeres",
        "metaphase of mitosis: chromosomes align at the equatorial plate, spindle fibers attach to centromeres of sister chromatids",
    ), Explanation=""))
rows.append(dict(Topic="Cell Division", Question="Briefly describe the events taking place at each of the stages in Q.1(a) above (pachytene, diplotene, metaphase I of meiosis, metaphase of mitosis).",
    Answer_Summary=lettered(
        "pachytene: crossing over exchanges genetic material between non-sister chromatids, increasing variation",
        "diplotene: chromosomes separate slightly as chiasmata become visible, preparing for segregation",
        "metaphase I of meiosis: homologous pairs align so spindle fibers ensure correct segregation in anaphase I",
        "metaphase of mitosis: chromosomes align so each daughter cell receives an identical chromosome set",
    ), Explanation=""))
rows.append(dict(Topic="Plant Transport Tissues", Question="Describe the structure and function of xylem and phloem tissues.",
    Answer_Summary=lettered(
        "xylem structure: tracheids, vessels, xylem parenchyma and xylem fibers",
        "xylem function: conducts water and minerals from roots, gives mechanical support",
        "phloem structure: sieve tubes, companion cells, phloem parenchyma and fibers",
        "phloem function: transports organic nutrients (sucrose) from leaves to other parts",
    ), Explanation=""))
rows.append(dict(Topic="Plant Life Cycles", Question="Compare the life cycle of a fern with that of a moss.",
    Answer_Summary=lettered(
        "fern: sporophyte is the dominant, independent, diploid stage",
        "fern: produces spores that grow into a small independent gametophyte",
        "moss: gametophyte is the dominant stage; sporophyte depends on it",
        "moss: produces spores that develop into a protonema, which forms the gametophyte",
    ), Explanation=""))
rows.append(dict(Topic="Classification of Organisms", Question="Giving one example in each case, describe the main features used to place organisms into each of the following groups: Protozoa, Arthropoda, Aschelminthes, Monocotyledonae, Dicotyledonae.",
    Answer_Summary=lettered(
        "protozoa (e.g. Amoeba): single-celled, no tissues, heterotrophic, moves by pseudopodia/cilia/flagella",
        "arthropoda (e.g. grasshopper): jointed appendages, chitinous exoskeleton, open circulatory system",
        "aschelminthes (e.g. Ascaris): cylindrical unsegmented body, pseudocoelom, complete digestive system",
        "monocotyledonae (e.g. maize): parallel leaf venation, fibrous roots, scattered vascular bundles",
        "dicotyledonae (e.g. bean): reticulate venation, taproot system, vascular bundles in a ring",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction", Question="\"Asexual reproduction produces offspring identical with parent, whereas sexual reproduction produces variation.\" Discuss these statements.",
    Answer_Summary=lettered(
        "asexual: one parent, offspring genetically identical (no recombination), e.g. binary fission in bacteria",
        "asexual: rapid reproduction in stable environments, but no variation to cope with change",
        "sexual: two parents, variation from meiosis and fertilization, e.g. mammals",
        "sexual: variation aids adaptation, but reproduction is slower and costs more energy",
    ), Explanation=""))
rows.append(dict(Topic="Digestion and Metabolism", Question="What is the role of the liver and pancreas in: (i) digestion? (ii) metabolism of the end products of digestion?",
    Answer_Summary=lettered(
        "digestion - liver: produces bile to emulsify fats, increasing surface area for enzymes",
        "digestion - pancreas: produces amylase, lipase and proteases released into the duodenum",
        "metabolism - liver: converts glucose to glycogen for storage, converts excess amino acids to urea",
        "metabolism - pancreas: regulates blood sugar via insulin and glucagon",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Sex-Linked Inheritance)", Question="Mrs. Lutu has two haemophiliac sons and two normal sons. What is her genotype and that of her husband with respect to this gene? Explain your answer.",
    Answer_Summary=lettered(
        "haemophilia is a sex-linked (X-linked) recessive disorder",
        "Mrs Lutu must be a carrier (XhX) since she passed the gene to her haemophiliac sons",
        "her husband must be normal (XY) since a father only passes his Y chromosome to sons",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Sex-Linked Inheritance)", Question="Giving reasons, explain whether Mrs. Lutu could have a haemophiliac daughter.",
    Answer_Summary=lettered(
        "a haemophiliac daughter (XhXh) needs a defective X chromosome from both parents",
        "since her husband is normal, he cannot supply that defective X",
        "so Mrs Lutu cannot have a haemophiliac daughter in this case",
    ), Explanation=""))
rows.append(dict(Topic="Water Balance in Mammals", Question="How does a mammal obtain and lose water?",
    Answer_Summary=lettered(
        "gained by drinking, eating water-rich food, and metabolic water from respiration",
        "lost through urination, sweating, exhaling and defecation",
    ), Explanation=""))
rows.append(dict(Topic="Excretion", Question="In what forms is nitrogen excreted in animals?",
    Answer_Summary=lettered(
        "ammonia in aquatic animals",
        "urea in mammals",
        "uric acid in birds and reptiles",
    ), Explanation=""))
rows.append(dict(Topic="Evolution", Question="What do you understand by the following as used in evolution? (i) Law of use and disuse (ii) Convergent evolution",
    Answer_Summary=lettered(
        "law of use and disuse (Lamarck): frequently used parts become more developed and unused ones diminish, passed to offspring",
        "convergent evolution: unrelated species evolve similar traits from similar environmental pressures, e.g. wings in bats and birds",
    ), Explanation=""))
rows.append(dict(Topic="Evolution", Question="How do the following bring about speciation? (i) Adaptive radiation (ii) Genetic variability",
    Answer_Summary=lettered(
        "adaptive radiation: one species evolves into multiple species each adapted to a niche, e.g. Darwin's finches",
        "genetic variability: variation within a population gives natural selection raw material, allowing new species to form over time",
    ), Explanation=""))

# ============================== YEAR 1993 ==============================
# Note: this year's paper is largely a practical exam tied to specific
# diagrams/specimens we don't have images for. Skipped anything where the
# source's own answer hedges on an unseen specimen (e.g. "if it is an
# insect... the class would be...") since that's the source speculating, not
# stating a fact. Kept only the parts that state generalizable, definitive
# biology facts, occasionally rephrasing the question to drop "specimen S3"
# style references the reader can't see.
rows.append(dict(Topic="Cell Organelles", Question="Without using diagrams, outline the processes taking place in the cristae of a mitochondrion and the thylakoids of a chloroplast.",
    Answer_Summary=lettered(
        "cristae: site of the electron transport chain and oxidative phosphorylation, producing ATP from NADH/FADH2",
        "cristae: proton gradient forms across the inner membrane as electrons move to oxygen",
        "thylakoids: site of the light-dependent reactions of photosynthesis",
        "thylakoids: chlorophyll captures light to produce ATP and NADPH, splitting water and releasing oxygen",
    ), Explanation=""))
rows.append(dict(Topic="Cell Organelles", Question="Explain briefly how the mitochondrion and chloroplast are adapted to the functions they perform.",
    Answer_Summary=lettered(
        "mitochondrion: double membrane gives separate compartments for different reactions",
        "mitochondrion: cristae on the inner membrane increase surface area for the electron transport chain",
        "mitochondrion: matrix contains enzymes for the citric acid cycle",
        "chloroplast: stroma contains enzymes for the Calvin cycle",
        "chloroplast: thylakoids stacked into grana increase surface area for light absorption",
    ), Explanation=""))
rows.append(dict(Topic="Biochemical Tests", Question="Which reagent is used to test for the presence of proteins, and how does it work?",
    Answer_Summary=lettered(
        "Millon's reagent tests for proteins",
        "reacts with tyrosine, an amino acid found in proteins",
        "produces a reddish-brown coloration confirming protein presence",
    ), Explanation=""))
rows.append(dict(Topic="Biochemical Tests", Question="Why is it necessary to boil then cool a sample before testing it with a reagent such as Millon's reagent?",
    Answer_Summary=lettered(
        "boiling denatures proteins, making them more accessible for the reagent",
        "cooling prevents decomposition or further denaturation that could interfere with the test",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Arthropods)", Question="What observable features enable an insect to inhabit terrestrial environments?",
    Answer_Summary=lettered(
        "chitinous exoskeleton reduces water loss",
        "spiracles and a tracheal system allow efficient gas exchange on land",
        "jointed legs allow locomotion on varied terrestrial surfaces",
        "excretes uric acid instead of ammonia to conserve water",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Arthropods)", Question="How does the class Arachnida differ from the class Insecta within the phylum Arthropoda?",
    Answer_Summary=lettered(
        "arachnids have two body segments (cephalothorax, abdomen); insects have three (head, thorax, abdomen)",
        "arachnids have four pairs of legs; insects have three pairs",
        "arachnids lack antennae; insects have one pair",
    ), Explanation=""))
rows.append(dict(Topic="Plant Tissues", Question="Which plant tissues stain with phloroglucinol, and what are their functions and structural adaptations?",
    Answer_Summary=lettered(
        "phloroglucinol stains lignified tissues: xylem and sclerenchyma",
        "xylem conducts water and minerals and gives mechanical support",
        "xylem has thick lignified walls and hollow lumens for efficient conduction",
        "sclerenchyma gives strength and rigidity via lignified cell walls",
    ), Explanation=""))

# ============================== YEAR 1994 ==============================
rows.append(dict(Topic="Meiosis", Question="What is meiosis?",
    Answer_Summary=lettered(
        "reduces chromosome number by half, producing four haploid cells from one diploid cell",
        "occurs in two stages, meiosis I and meiosis II",
        "essential for sexual reproduction - produces gametes in animals and spores in plants",
    ), Explanation=""))
rows.append(dict(Topic="Meiosis", Question="Outline the events occurring in the 1st meiotic prophase and 1st meiotic metaphase.",
    Answer_Summary=lettered(
        "leptotene: chromosomes condense and appear as thin threads",
        "zygotene: homologous chromosomes pair up (synapsis) to form bivalents",
        "pachytene: crossing over exchanges genetic material between non-sister chromatids",
        "diplotene: homologous chromosomes begin to separate but stay joined at chiasmata",
        "diakinesis: chromosomes condense further and the nuclear membrane starts to disintegrate",
        "metaphase I: bivalents align at the equatorial plane and spindle fibers attach to centromeres",
    ), Explanation=""))
rows.append(dict(Topic="Plant Tissues", Question="Discuss the location and functions of meristematic tissue in the body of a flowering plant.",
    Answer_Summary=lettered(
        "apical meristem (root/shoot tips): drives primary growth in length",
        "lateral meristem (vascular bundles): drives secondary growth in thickness",
        "intercalary meristem (leaf bases/nodes): enables regrowth of leaves and stems",
    ), Explanation=""))
rows.append(dict(Topic="Animal Tissues", Question="Discuss the location and functions of adipose tissue in the body of a mammal.",
    Answer_Summary=lettered(
        "located beneath the skin, around organs, in bone marrow and breast tissue",
        "stores energy as lipids",
        "insulates to maintain body temperature",
        "cushions and protects internal organs",
    ), Explanation=""))
rows.append(dict(Topic="Animal Tissues", Question="Discuss the location and functions of smooth muscle in the body of a mammal.",
    Answer_Summary=lettered(
        "located in walls of internal organs - stomach, intestines, blood vessels, bladder",
        "involuntary contraction propels substances through organs (e.g. peristalsis)",
        "regulates blood flow by contracting/relaxing blood vessels",
        "controls fluid movement in urinary and reproductive systems",
    ), Explanation=""))
rows.append(dict(Topic="Fungi", Question="In what ways are fungi important to man?",
    Answer_Summary=lettered(
        "food production: yeast used in baking and fermentation",
        "medicine: some fungi (e.g. Penicillium) produce antibiotics",
        "nutrient recycling: decomposers that recycle organic matter",
        "agriculture: mycorrhizal fungi boost plant nutrient absorption",
        "food source: edible mushrooms provide protein and nutrients",
        "industry: used to produce enzymes and organic acids",
        "biotechnology: used in genetic research and GMO production",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Arthropods)", Question="What are the distinguishing features of the different classes of arthropods?",
    Answer_Summary=lettered(
        "insects: 3 body segments, 3 pairs of legs, antennae present (e.g. grasshopper)",
        "arachnids: 2 body segments, 4 pairs of legs, no antennae (e.g. spiders)",
        "crustaceans: cephalothorax and abdomen, 5+ pairs of legs, 2 pairs of antennae, mostly aquatic (e.g. crabs)",
        "myriapods: elongated segmented body, 1-2 pairs of legs per segment",
        "chilopoda (centipedes): carnivorous, flattened body, one pair of legs per segment",
        "diplopoda (millipedes): herbivorous, cylindrical body, two pairs of legs per segment",
    ), Explanation=""))
rows.append(dict(Topic="Human Eye Defects", Question="Explain the following defects of the human eye: myopia, hypermetropia, and astigmatism. What corrective measures can be taken for each defect?",
    Answer_Summary=lettered(
        "myopia: eyeball too long/lens too curved, light focuses in front of the retina - corrected with concave lenses",
        "hypermetropia: eyeball too short/lens not curved enough, light focuses behind the retina - corrected with convex lenses",
        "astigmatism: irregular cornea/lens shape, light focuses at multiple points - corrected with cylindrical lenses",
    ), Explanation=""))
rows.append(dict(Topic="Hormones and Growth", Question="Give an account of hormones that influence growth and development in mammals.",
    Answer_Summary=lettered(
        "growth hormone (pituitary): stimulates bone, muscle and tissue growth via protein synthesis",
        "thyroxine (thyroid): regulates metabolic rate, supports tissue growth",
        "insulin (pancreas): regulates glucose metabolism for energy",
        "testosterone: drives male secondary sexual characteristics, muscle/bone growth",
        "estrogen: drives female secondary sexual characteristics and reproductive development",
        "cortisol (adrenal glands): regulates metabolism and stress response, indirectly supports growth",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis", Question="Describe the cyclic and non-cyclic photophosphorylation pathways of the light reactions of photosynthesis. What are the products of these reactions?",
    Answer_Summary=lettered(
        "cyclic: occurs in photosystem I only, electrons return to photosystem I via the electron transport chain",
        "cyclic: produces ATP only (no NADPH or oxygen)",
        "non-cyclic: involves both photosystem I and II, splits water (photolysis) to release oxygen",
        "non-cyclic: produces ATP and NADPH",
    ), Explanation=""))
rows.append(dict(Topic="Evolution", Question="Discuss the various types of evidence from living organisms which support the theory of evolution.",
    Answer_Summary=lettered(
        "fossil evidence: shows progression of life forms and transitional species (e.g. Archaeopteryx)",
        "comparative anatomy: homologous structures indicate common ancestry",
        "embryology: similar embryonic stages across species suggest common ancestry",
        "molecular biology: similarities in DNA/RNA/proteins indicate evolutionary relationships",
        "biogeography: geographic distribution of species supports evolution (e.g. Darwin's finches)",
        "observable evolution: antibiotic resistance in bacteria, pesticide resistance in insects",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Monohybrid Inheritance)", Question="In man, the ability to roll the tongue is determined by a dominant gene while its recessive allele fails to produce this ability. A man and his wife can both roll their tongues, but their daughter cannot. Explain this by showing the genotypes of all three persons.",
    Answer_Summary=lettered(
        "tongue-rolling is controlled by dominant allele R; inability by recessive allele r",
        "both parents must be heterozygous (Rr) since they can roll their tongues but have a non-rolling child",
        "the daughter is homozygous recessive (rr), inheriting r from each parent",
        "a cross of Rr x Rr gives a 1:2:1 genotype ratio (RR:Rr:rr), so 1 in 4 offspring is expected to be rr",
    ), Explanation=""))
rows.append(dict(Topic="Speciation", Question="Discuss the role of isolating mechanisms in the formation of new species.",
    Answer_Summary=lettered(
        "isolating mechanisms prevent interbreeding, letting populations evolve independently",
        "prezygotic isolation: temporal, behavioral or mechanical differences prevent mating",
        "postzygotic isolation: hybrid inviability, sterility (e.g. mule) or breakdown in later generations",
        "reduced gene flow from isolation drives genetic divergence and speciation",
    ), Explanation=""))

# ============================== YEAR 1995 ==============================
rows.append(dict(Topic="Cell Organelles", Question="Describe the structure and functions of the Golgi apparatus.",
    Answer_Summary=lettered(
        "consists of flattened membrane-bound sacs (cisternae) with a cis face (receives from the ER) and trans face (ships out)",
        "modifies, sorts and packages proteins and lipids for secretion or cell use",
        "produces lysosomes",
        "helps synthesize polysaccharides for plant cell walls",
    ), Explanation=""))
rows.append(dict(Topic="Cell Organelles", Question="Describe the structure and functions of the chloroplast.",
    Answer_Summary=lettered(
        "double-membrane organelle with thylakoids stacked into grana, surrounded by the stroma; chlorophyll is in the thylakoids",
        "site of photosynthesis, converting light energy into chemical energy",
        "produces oxygen as a byproduct of the light-dependent reactions",
        "synthesizes glucose via the Calvin cycle",
    ), Explanation=""))
rows.append(dict(Topic="Cell Division", Question="How does the relative DNA content of a cell change through the stages of mitosis and meiosis?",
    Answer_Summary=lettered(
        "early interphase: normal DNA content (2C) as the cell prepares for division",
        "metaphase of mitosis: DNA content doubles (4C) after chromosome duplication",
        "late telophase (mitosis): DNA content returns to normal (2C) once division completes",
        "meiosis I (zygotene): DNA content is 4C due to homologous pairing after duplication",
        "late telophase I: DNA content is 2C - homologs have separated but each chromosome still has two chromatids",
        "prophase II: DNA content stays at 2C since no further replication occurs between meiosis I and II",
        "end of meiosis II: DNA content halves to 1C as gametes form",
    ), Explanation=""))
rows.append(dict(Topic="Glands and Hormones", Question="Distinguish between exocrine and endocrine glands.",
    Answer_Summary=lettered(
        "exocrine glands secrete via ducts to external/internal surfaces (e.g. sweat glands)",
        "endocrine glands secrete hormones directly into the bloodstream without ducts (e.g. adrenal glands)",
    ), Explanation=""))
rows.append(dict(Topic="Glands and Hormones", Question="Discuss, with examples, the structure of the major types of exocrine glands in mammals.",
    Answer_Summary=lettered(
        "merocrine glands: release secretions by exocytosis (e.g. sweat glands)",
        "apocrine glands: release secretions along with part of the cell membrane (e.g. mammary glands)",
        "holocrine glands: release secretions by rupturing the entire cell (e.g. sebaceous glands)",
    ), Explanation=""))
rows.append(dict(Topic="Plant Classification", Question="What are the similarities and differences between bryophytes and pteridophytes?",
    Answer_Summary=lettered(
        "similarity: both are non-flowering plants that reproduce by spores",
        "similarity: both need water for male gametes to move during fertilization",
        "difference: bryophytes lack true vascular tissue; pteridophytes have xylem and phloem",
        "difference: the gametophyte is dominant in bryophytes; the sporophyte is dominant in pteridophytes",
    ), Explanation=""))
rows.append(dict(Topic="Plant Classification", Question="What do you understand by the term \"Alternation of Generations\"? Discuss its significance to the life histories of plants.",
    Answer_Summary=lettered(
        "a life cycle that alternates between a haploid gametophyte stage and a diploid sporophyte stage",
        "ensures genetic diversity through sexual reproduction",
        "gametophyte produces gametes for fertilization; sporophyte produces spores for dispersal, aiding adaptation",
        "lets plants exploit both sexual and asexual reproductive strategies",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Chordata/Mammalia)", Question="Justify the position of Homo sapiens in the phylum Chordata and class Mammalia.",
    Answer_Summary=lettered(
        "chordata: has a notochord during embryonic development",
        "chordata: has a dorsal hollow nerve cord",
        "chordata: has pharyngeal slits/pouches during development",
        "mammalia: has mammary glands for feeding offspring",
        "mammalia: has hair or fur on the body",
        "mammalia: has three middle ear bones and a neocortex",
    ), Explanation=""))
rows.append(dict(Topic="Plant Water Transport", Question="Discuss the process of water absorption by roots and the movement of water from the roots to the leaves.",
    Answer_Summary=lettered(
        "roots absorb water via root hairs by osmosis, moving to the xylem via apoplastic/symplastic pathways",
        "root pressure pushes water upward via osmotic pressure in the roots",
        "capillary action: adhesion and cohesion move water through narrow xylem vessels",
        "transpiration pull: evaporation from leaf stomata creates suction that pulls water upward",
    ), Explanation=""))
rows.append(dict(Topic="Fight-or-Flight Response", Question="State the changes that take place in the organs named below and discuss their importance during the fight-or-flight response: heart, liver, lungs, skin, skeletal muscles, alimentary canal, eyes.",
    Answer_Summary=lettered(
        "heart: heart rate increases to pump more oxygenated blood to muscles",
        "liver: releases glucose into the blood for energy",
        "lungs: breathing rate increases for more oxygen intake",
        "skin: blood is redirected to vital organs, causing pale skin",
        "skeletal muscles: get more oxygen and glucose for movement and strength",
        "alimentary canal: digestion slows to conserve energy for immediate action",
        "eyes: pupils dilate to improve vision",
    ), Explanation=""))
rows.append(dict(Topic="Biomolecules", Question="Discuss the roles of water and carbohydrates in organisms.",
    Answer_Summary=lettered(
        "water: solvent for biochemical reactions, regulates temperature, transports nutrients/waste, gives structural support via turgor pressure in plants",
        "carbohydrates: provide energy through respiration",
        "carbohydrates: structural role (e.g. cellulose in plants)",
        "carbohydrates: storage molecules (e.g. starch, glycogen)",
    ), Explanation=""))
rows.append(dict(Topic="Species Concept", Question="How may a species be defined by a geneticist, an evolutionist, and an ecologist?",
    Answer_Summary=lettered(
        "geneticist: a group sharing a common gene pool that can interbreed to produce fertile offspring",
        "evolutionist: a group sharing common evolutionary ancestry and distinct traits",
        "ecologist: a group occupying a specific ecological niche, interacting uniquely with its environment",
    ), Explanation=""))
rows.append(dict(Topic="Population Ecology", Question="Discuss the relationship between biotic potential and environmental resistance.",
    Answer_Summary=lettered(
        "biotic potential: the maximum reproductive capacity of a population under ideal conditions",
        "environmental resistance: factors like predation, resource scarcity and climate that limit population growth",
        "environmental resistance counteracts biotic potential, keeping populations within the ecosystem's carrying capacity",
        "a balance between the two keeps ecosystems stable and prevents overexploitation of resources",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Blood Groups)", Question="Maula (blood type A) had a baby with blood type O, and named Kasheshe (whose mother is type A and father is type B) as the father, which he denies. Using genetic crosses, determine whether Kasheshe could be the father.",
    Answer_Summary=lettered(
        "Maula must be genotype AO, since she needed an O allele to produce an O-type baby",
        "Kasheshe's possible genotypes (from an A-type mother and B-type father) are AB, AO, BO, or OO",
        "if Kasheshe is AB, a cross with Maula (AO) can never produce an OO child, so he cannot be the father",
        "if Kasheshe is AO, BO, or OO, a cross with Maula (AO) can produce an OO child, so he could be the father",
    ), Explanation=""))

# ============================== YEAR 1999 ==============================
# Note: 1(a)/(b)/(d) reference specific unseen photographs labeled A-D. Kept
# only where the underlying answer is a real, generalizable biology fact
# (rephrasing away the photo reference); dropped the pure drawing/identify-
# the-photo parts entirely.
rows.append(dict(Topic="Cell Division (Mitosis vs Meiosis)", Question="How can you tell that a set of cell-division images shows mitosis rather than meiosis?",
    Answer_Summary=lettered(
        "distinct stages (prophase, metaphase, anaphase, telophase) are visible with clear chromosomes",
        "no homologous chromosome pairing occurs",
        "no crossing over occurs (both are meiosis-only features)",
    ), Explanation=""))
rows.append(dict(Topic="Cell Division (Mitosis)", Question="Describe the events taking place during metaphase, anaphase, telophase and cytokinesis of mitosis.",
    Answer_Summary=lettered(
        "metaphase: chromosomes align at the equatorial plane, spindle fibers attach to centromeres",
        "anaphase: spindle fibers shorten, pulling sister chromatids to opposite poles",
        "telophase: chromatids reach the poles, nuclear membranes reform, chromosomes uncoil into chromatin",
        "cytokinesis: the cytoplasm divides, forming two genetically identical daughter cells",
    ), Explanation=""))
rows.append(dict(Topic="Cell Division (Mitosis)", Question="Explain the importance of mitosis.",
    Answer_Summary=lettered(
        "drives growth, repair and maintenance in multicellular organisms",
        "produces daughter cells genetically identical to the parent, maintaining genetic stability",
        "enables asexual reproduction in some organisms",
    ), Explanation=""))
rows.append(dict(Topic="Plant Tissues", Question="Describe the location of parenchyma tissue in plants and show how its structure relates to its functions.",
    Answer_Summary=lettered(
        "located in the cortex/pith of stems and roots, leaf mesophyll, and as storage tissue in fruits/seeds",
        "thin cell walls allow easy transport of water and nutrients",
        "large vacuoles store food, water and waste products",
        "chloroplasts in some parenchyma (chlorenchyma) enable photosynthesis",
        "air spaces in some cells (aerenchyma) aid gas exchange in aquatic plants",
    ), Explanation=""))
rows.append(dict(Topic="Classification", Question="Explain why we classify organisms.",
    Answer_Summary=lettered(
        "organizes the vast diversity of organisms for easier study",
        "aids identification and understanding relationships (e.g. evolutionary connections)",
        "helps predict characteristics based on related groups",
        "provides a universal naming system for global scientific communication",
    ), Explanation=""))
rows.append(dict(Topic="Classification", Question="Discuss the artificial and natural systems of classification, with their advantages and disadvantages.",
    Answer_Summary=lettered(
        "artificial system: groups by a few observable traits (size, shape, habitat), ignoring evolution",
        "artificial: easy and quick to use, but ignores genetic/evolutionary relationships and can wrongly group unrelated organisms",
        "natural system: groups by genetic, morphological and evolutionary relationships",
        "natural: scientifically grounded, but requires detailed research and can misclassify with incomplete data",
    ), Explanation=""))
rows.append(dict(Topic="Fungi Classification", Question="What features led early classification schemes to group fungi with plants, and what led to separating them into different kingdoms?",
    Answer_Summary=lettered(
        "grouped with plants because fungi are immobile, have a cell wall, and reproduce by spores",
        "separated because fungi lack chlorophyll and cannot photosynthesize, relying on organic material for nutrition",
        "fungal cell walls contain chitin, unlike cellulose in plant cell walls",
    ), Explanation=""))
rows.append(dict(Topic="Fungi", Question="Discuss the ways in which fungi are harmful to human beings.",
    Answer_Summary=lettered(
        "cause diseases such as athlete's foot, ringworm and candidiasis",
        "some produce toxins (e.g. aflatoxins) that contaminate food",
        "spoil food and other organic materials, causing economic losses",
        "fungal crop infections reduce agricultural productivity",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis and Respiration", Question="Compare photosynthetic phosphorylation and oxidative phosphorylation.",
    Answer_Summary=lettered(
        "photosynthetic: occurs in chloroplasts, generates ATP using light energy to drive the electron transport chain",
        "oxidative: occurs in mitochondria, generates ATP by oxidizing glucose-derived molecules with oxygen as the final electron acceptor",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis", Question="Describe how ATP is formed during cyclic photophosphorylation.",
    Answer_Summary=lettered(
        "light excites electrons from chlorophyll in photosystem I",
        "electrons pass through the electron transport chain and return to photosystem I",
        "electron movement creates a proton gradient across the thylakoid membrane",
        "the gradient drives ATP synthesis through ATP synthase",
    ), Explanation=""))
rows.append(dict(Topic="Stomata", Question="Discuss the physiological processes that account for the opening of stomata during the day and closing at night.",
    Answer_Summary=lettered(
        "day: light stimulates active transport of potassium ions into guard cells, lowering water potential",
        "day: water enters guard cells by osmosis, causing them to swell and open the stomata",
        "night: potassium ions diffuse out, raising water potential in guard cells",
        "night: water leaves guard cells by osmosis, making them flaccid and closing the stomata",
    ), Explanation=""))
rows.append(dict(Topic="Xerophyte Adaptations", Question="Explain six features or methods used by xerophytes in minimizing water loss.",
    Answer_Summary=lettered(
        "thick cuticle reduces water loss through the epidermis",
        "sunken stomata trap moist air, reducing transpiration",
        "reduced leaf size or spines minimize surface area for water loss",
        "deep roots access water from deep soil layers",
        "stomata open at night (CAM plants) to reduce daytime water loss",
        "storing water in tissues acts as a reservoir during drought",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Autonomic)", Question="What do you understand by the Autonomic Nervous System?",
    Answer_Summary=lettered(
        "controls involuntary actions such as heartbeat, digestion, and glandular secretions",
        "made of sympathetic and parasympathetic divisions",
        "regulates body functions to maintain homeostasis",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Autonomic)", Question="Differentiate between the sympathetic and parasympathetic systems and explain their antagonistic effects, giving five examples.",
    Answer_Summary=lettered(
        "sympathetic drives fight-or-flight (raises heart rate, dilates pupils, reduces digestion); parasympathetic drives rest-and-digest (opposite effects)",
        "heart rate: sympathetic increases it, parasympathetic decreases it",
        "pupils: sympathetic dilates them, parasympathetic constricts them",
        "digestion: sympathetic inhibits it, parasympathetic stimulates it",
        "saliva: sympathetic reduces it, parasympathetic increases it",
        "bronchial muscles: sympathetic relaxes them, parasympathetic contracts them",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Albinism)", Question="Albinism is caused by a recessive gene. A phenotypically normal couple has four children - the first three normal, the fourth albino. What is the genotype of the parents, and what is the probability the fifth child will be albino?",
    Answer_Summary=lettered(
        "both parents must be carriers (Aa), since two recessive alleles (aa) are needed for an albino child",
        "an Aa x Aa cross gives a 1:2:1 ratio - 25% AA, 50% Aa, 25% aa",
        "so there's a 25% (1 in 4) chance the fifth child will be albino",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Albinism)", Question="If one of the couple's normal-skinned children (Aa) marries a normal-skinned woman, what predictions can be made about their first child's skin, depending on the woman's genotype?",
    Answer_Summary=lettered(
        "if the woman is homozygous dominant (AA), none of the children will be albino, though 50% will be carriers",
        "if the woman is a carrier (Aa), there's a 25% chance of an albino child (from an Aa x Aa cross)",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Albinism)", Question="If the albino child marries a normal-skinned widow who already had an albino child (making her a carrier), what is the probability of this couple producing a normal-skinned child?",
    Answer_Summary=lettered(
        "the cross is aa (albino) x Aa (carrier)",
        "50% of offspring are Aa (normal-skinned but carriers), 50% are aa (albino)",
        "so there's a 50% probability of a normal-skinned child, though it will always be a carrier",
    ), Explanation=""))
rows.append(dict(Topic="Evolution (Darwin)", Question="Discuss Darwin's contributions to the theory of evolution and show how this theory has been updated.",
    Answer_Summary=lettered(
        "natural selection: better-adapted organisms survive and reproduce, passing on favorable traits",
        "descent with modification: all species share a common ancestor and evolve through gradual change",
        "struggle for existence: organisms compete for limited resources, and only the fittest survive",
        "updated by Mendelian genetics, which explained the genetic basis of variation Darwin could not",
        "updated by the modern synthesis, integrating natural selection with population genetics",
        "updated by molecular biology (DNA sequencing) confirming common ancestry",
        "updated by epigenetics, showing environmental factors can influence and be inherited",
        "updated by new fossil discoveries that keep filling gaps in the evolutionary record",
    ), Explanation=""))

# ============================== YEAR 2000 ==============================
rows.append(dict(Topic="Cell Structure", Question="Point out two similarities and two differences between an animal cell and a plant cell.",
    Answer_Summary=lettered(
        "similarity: both are eukaryotic with a true nucleus and membrane-bound organelles",
        "similarity: both have a plasma membrane, cytoplasm, mitochondria and other organelles",
        "difference: plant cells have a rigid cellulose cell wall; animal cells don't",
        "difference: plant cells have chloroplasts for photosynthesis; animal cells don't",
    ), Explanation=""))
rows.append(dict(Topic="Cell Structure", Question="Outline the functions of a nucleus.",
    Answer_Summary=lettered(
        "controls all cellular activities including growth, metabolism and reproduction",
        "contains DNA that provides instructions for protein synthesis",
        "regulates cell division and differentiation",
        "produces ribosomes in the nucleolus",
    ), Explanation=""))
rows.append(dict(Topic="Insect Metamorphosis", Question="What is the difference between incomplete and complete metamorphosis in insects, with examples?",
    Answer_Summary=lettered(
        "incomplete metamorphosis: three stages (egg, nymph, adult), no pupal stage - e.g. cockroaches, grasshoppers",
        "complete metamorphosis: four stages (egg, larva, pupa, adult) - e.g. butterflies, beetles",
    ), Explanation=""))
rows.append(dict(Topic="Plant Water Transport", Question="Can water enter xylem vessels by osmosis? Give reasons to support your answer.",
    Answer_Summary=lettered(
        "no - osmosis needs a semi-permeable membrane, which xylem vessels lack",
        "water instead enters via apoplastic or symplastic pathways",
        "driven by root pressure and capillary action",
    ), Explanation=""))
rows.append(dict(Topic="Plant Water Transport", Question="Name three forces believed to cause the flow of water through xylem, and state whether each is active or passive.",
    Answer_Summary=lettered(
        "root pressure - active",
        "capillary action - passive",
        "transpirational pull - passive",
    ), Explanation=""))
rows.append(dict(Topic="Biomolecules (Carbohydrates)", Question="Mention four roles of carbohydrates in the plant body.",
    Answer_Summary=lettered(
        "provide energy through respiration",
        "structural role (e.g. cellulose in cell walls)",
        "storage molecules (e.g. starch)",
        "role in cell signaling and recognition",
    ), Explanation=""))
rows.append(dict(Topic="Biomolecules (Carbohydrates)", Question="Explain what you understand by the term disaccharides and name any two examples.",
    Answer_Summary=lettered(
        "formed by condensation of two monosaccharides linked by a glycosidic bond",
        "examples: sucrose and lactose",
    ), Explanation=""))
rows.append(dict(Topic="Excretory System (Kidney)", Question="State the roles of the Bowman's capsule, proximal convoluted tubule, loop of Henle, distal convoluted tubule, and collecting duct.",
    Answer_Summary=lettered(
        "Bowman's capsule: filters blood to form the glomerular filtrate",
        "proximal convoluted tubule: reabsorbs nutrients, salts and water from the filtrate",
        "loop of Henle: concentrates urine by reabsorbing water and salts",
        "distal convoluted tubule: regulates ion balance and pH by reabsorbing salts and secreting hydrogen ions",
        "collecting duct: collects urine and finalizes its concentration by reabsorbing water",
    ), Explanation=""))
rows.append(dict(Topic="Plant Hormones", Question="Name the plant hormones that initiate root development, ripen fruit rapidly, and induce cell division.",
    Answer_Summary=lettered(
        "auxins initiate root development",
        "ethylene ripens fruit (e.g. oranges) rapidly",
        "cytokinins induce cell division",
    ), Explanation=""))
rows.append(dict(Topic="Genetics", Question="Distinguish between sex determination and sex linkage.",
    Answer_Summary=lettered(
        "sex determination: the process by which an organism's sex is set, often by specific chromosomes (e.g. XX/XY)",
        "sex linkage: genes on sex chromosomes inherited differently in males and females (e.g. hemophilia, color blindness)",
    ), Explanation=""))
rows.append(dict(Topic="Genetics", Question="Define chromosomal mutation, co-dominance, and polygenic inheritance.",
    Answer_Summary=lettered(
        "chromosomal mutation: a permanent change in chromosome structure or number",
        "co-dominance: both alleles in a heterozygote are fully expressed (e.g. AB blood type)",
        "polygenic inheritance: traits controlled by multiple genes, giving continuous variation (e.g. height, skin color)",
    ), Explanation=""))
rows.append(dict(Topic="Seed Germination", Question="In an experiment testing the factors needed for seed germination, what was the aim, and why were pyrogallic acid and caustic soda included in one of the flasks?",
    Answer_Summary=lettered(
        "aim: to investigate factors necessary for germination, such as water, warmth and oxygen",
        "pyrogallic acid and caustic soda absorb oxygen, creating an anaerobic flask to test whether oxygen is needed for germination",
    ), Explanation=""))
rows.append(dict(Topic="Seed Germination", Question="What could be the possible reasons for viable seeds failing to germinate under optimum conditions?",
    Answer_Summary=lettered(
        "dormancy - some seeds need treatments like scarification or stratification to break it",
        "poor seed quality - old, damaged, or pathogen-infected seeds may fail despite being viable",
        "chemical inhibitors present in the seed that block germination until conditions are met",
        "genetic defects or abnormalities in the seed",
        "contamination from harmful chemicals or microorganisms in the soil",
    ), Explanation=""))
rows.append(dict(Topic="Respiration and Exercise", Question="What happens to breathing rate and heart rate during intense physical activity, and why?",
    Answer_Summary=lettered(
        "both increase because muscles need more oxygen and energy",
        "faster breathing boosts oxygen intake",
        "faster heartbeat distributes oxygen/nutrients and removes carbon dioxide and waste more efficiently",
    ), Explanation=""))
rows.append(dict(Topic="Respiration and Exercise", Question="Why do muscles switch to anaerobic respiration during intense physical activity?",
    Answer_Summary=lettered(
        "oxygen supply becomes insufficient for the high energy demand",
        "muscles break down glucose without oxygen, producing energy and lactic acid",
    ), Explanation=""))
rows.append(dict(Topic="Respiration", Question="How does anaerobic respiration differ from aerobic respiration?",
    Answer_Summary=lettered(
        "anaerobic: no oxygen needed, less ATP per glucose, produces lactic acid (animals) or ethanol/CO2 (plants/microbes)",
        "aerobic: requires oxygen, more ATP per glucose, produces carbon dioxide and water",
    ), Explanation=""))
rows.append(dict(Topic="Growth", Question="How does the meaning of \"growth\" in bacteria differ from its meaning in higher plants and animals?",
    Answer_Summary=lettered(
        "in bacteria, growth means an increase in population size via binary fission",
        "in plants/animals, growth means an increase in an individual's size and mass through mitosis, differentiation and elongation",
    ), Explanation=""))
rows.append(dict(Topic="Excretion vs Secretion", Question="Distinguish between the meaning of excretion and secretion.",
    Answer_Summary=lettered(
        "excretion: removing harmful metabolic waste (e.g. CO2, urea) from the body",
        "secretion: producing and releasing useful substances (e.g. enzymes, hormones, mucus)",
    ), Explanation=""))
rows.append(dict(Topic="Speciation", Question="Define speciation, and explain how adaptive radiation and genetic variation bring it about.",
    Answer_Summary=lettered(
        "speciation: new species arising from existing ones via genetic isolation, natural selection and other mechanisms",
        "adaptive radiation: one ancestral species diversifies into multiple species adapted to different niches (e.g. Darwin's finches)",
        "genetic variation: mutations, gene flow and recombination create differences that, with reproductive isolation, form new species over time",
    ), Explanation=""))

# ============================== YEAR 2001 ==============================
# Note: skipped 2(a)/9(a)(ii)/6(a) which required identifying labeled parts
# (A-L, M-V) or a pedigree diagram we don't have; kept the parts of those
# questions whose answers state generic, self-contained facts.
rows.append(dict(Topic="Classification", Question="List the seven major categories of the taxonomic hierarchy.",
    Answer_Summary=lettered("kingdom", "phylum (or division in plants)", "class", "order", "family", "genus", "species"), Explanation=""))
rows.append(dict(Topic="Classification", Question="Give two merits and three demerits of the natural system of classification.",
    Answer_Summary=lettered(
        "merit: reflects evolutionary relationships, giving an accurate scientific basis (e.g. humans and primates grouped by shared ancestry)",
        "merit: creates a universal naming/categorizing system for consistent global scientific use",
        "demerit: needs extensive research into evolutionary relationships, hard without fossil/genetic data",
        "demerit: can misclassify organisms when evolutionary data is incomplete (e.g. due to convergent evolution)",
        "demerit: complex, making it hard for non-specialists to understand or apply",
    ), Explanation=""))
rows.append(dict(Topic="Plant Reproduction (Seeds)", Question="What is one major difference and one major similarity between a dicot seed and a monocot seed?",
    Answer_Summary=lettered(
        "difference: dicots have two cotyledons; monocots have only one",
        "similarity: both contain an embryo and a seed coat for protection and development",
    ), Explanation=""))
rows.append(dict(Topic="Digestive Disorders", Question="What is probably wrong if a healthy person develops ulcers or heartburn?",
    Answer_Summary=lettered(
        "ulcers: erosion of the stomach lining from excess acid, H. pylori infection, or long-term use of drugs like aspirin",
        "heartburn: stomach acid flows back into the esophagus due to a weak or malfunctioning sphincter muscle",
    ), Explanation=""))
rows.append(dict(Topic="Digestive Disorders", Question="How can ulcers and heartburn be counteracted?",
    Answer_Summary=lettered(
        "ulcers: avoid irritating foods/medications, use antacids, take antibiotics if caused by H. pylori",
        "heartburn: eat smaller meals, avoid trigger foods (spicy/acidic), use proton pump inhibitors",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Glycolysis)", Question="What is glycolysis?",
    Answer_Summary=lettered(
        "breaks glucose into two pyruvate molecules in the cytoplasm",
        "produces a small amount of ATP and NADH",
        "first step of cellular respiration; doesn't need oxygen",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Glycolysis)", Question="Summarize the essential features of glycolysis that lead to the release of energy from a glucose molecule.",
    Answer_Summary=lettered(
        "ten enzymatic steps in two phases",
        "energy investment phase: 2 ATP used to phosphorylate glucose into a more reactive form",
        "energy payoff phase: the 6-carbon molecule splits into two pyruvates, for a net gain of 2 ATP and 2 NADH",
    ), Explanation=""))
rows.append(dict(Topic="Homeostasis", Question="Define the term homeostasis.",
    Answer_Summary=lettered(
        "the ability to maintain a stable internal environment despite external changes",
        "e.g. regulating body temperature, blood pressure and glucose levels",
    ), Explanation=""))
rows.append(dict(Topic="Osmoregulation", Question="Point out four adaptations of marine bony fish against dehydration.",
    Answer_Summary=lettered(
        "drink seawater to offset water lost by osmosis",
        "specialized kidneys produce small amounts of highly concentrated urine",
        "chloride cells in the gills actively excrete excess salt",
        "impermeable, mucus-covered skin and scales limit water loss",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Inheritance Patterns)", Question="How is the inheritance of albinism similar to and different from that of hemophilia?",
    Answer_Summary=lettered(
        "both are genetic disorders from specific gene mutations",
        "albinism is autosomal recessive - needs the defective allele from both parents",
        "hemophilia is X-linked recessive - carried on the X chromosome, so it affects males more often",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Inheritance Patterns)", Question="Why are men more likely to be hemophiliacs than women?",
    Answer_Summary=lettered(
        "men have only one X chromosome (XY), so a single hemophilia allele on it isn't masked",
        "women have two X chromosomes (XX), so a normal allele on one X can mask the defective one, making them carriers instead",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Variation)", Question="What do you understand by continuous and discontinuous variation, with two examples each?",
    Answer_Summary=lettered(
        "continuous variation: gradual range of phenotypes from multiple genes/environment, e.g. height and skin color",
        "discontinuous variation: distinct categories with no intermediates, e.g. blood groups and tongue-rolling ability",
    ), Explanation=""))
rows.append(dict(Topic="Evolution", Question="State four areas which provide evidence for evolution.",
    Answer_Summary=lettered(
        "fossil records show transitional forms and extinct species over time",
        "comparative anatomy: homologous organs (e.g. vertebrate forelimbs) indicate common ancestry",
        "embryology: similar early embryonic stages across species suggest shared ancestry",
        "molecular biology: DNA/protein similarities support evolutionary relationships",
    ), Explanation=""))
rows.append(dict(Topic="Natural Resources", Question="What is meant by natural resources? Give four examples.",
    Answer_Summary=lettered(
        "naturally occurring materials used by humans for economic gain or survival, renewable or non-renewable",
        "examples: water, minerals, forests, fossil fuels",
    ), Explanation=""))
rows.append(dict(Topic="Natural Resources", Question="State three ways essential for achieving sustainable exploitation of natural resources.",
    Answer_Summary=lettered(
        "conservation practices like reforestation and habitat preservation",
        "shifting to alternative/renewable energy sources (solar, wind) to reduce reliance on fossil fuels",
        "enforcing environmental laws regulating extraction and pollution",
    ), Explanation=""))
rows.append(dict(Topic="Cell Structure", Question="How can you tell whether a cell is prokaryotic or eukaryotic?",
    Answer_Summary=lettered(
        "eukaryotic cells have a well-defined nucleus",
        "eukaryotic cells have membrane-bound organelles such as mitochondria and endoplasmic reticulum",
    ), Explanation=""))
rows.append(dict(Topic="Cell Structure", Question="State one function each of the nucleus, rough endoplasmic reticulum, vacuole, and lysosome.",
    Answer_Summary=lettered(
        "nucleus: controls cellular activities and stores genetic information",
        "rough ER: synthesizes and transports proteins",
        "vacuole: stores nutrients/waste and helps maintain turgor pressure in plant cells",
        "lysosome: breaks down waste and cellular debris via enzymatic digestion",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Synapse)", Question="Using acetylcholine as a neurotransmitter, explain how an impulse is transmitted across a synapse.",
    Answer_Summary=lettered(
        "an arriving impulse triggers release of acetylcholine from synaptic vesicles",
        "acetylcholine diffuses across the synaptic cleft and binds receptors on the postsynaptic membrane",
        "this opens ion channels, depolarizing the postsynaptic neuron and passing on the impulse",
        "acetylcholinesterase then breaks down the acetylcholine, ending the signal and resetting the synapse",
    ), Explanation=""))
rows.append(dict(Topic="Metabolism", Question="Explain the meaning of basal metabolic rate (BMR).",
    Answer_Summary=lettered(
        "the minimum energy needed to maintain vital functions (breathing, circulation, temperature regulation) at rest",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Fermentation)", Question="Compare alcohol fermentation by yeast cells with lactic acid fermentation in a vertebrate muscle cell during vigorous exercise.",
    Answer_Summary=lettered(
        "both occur without oxygen and yield less ATP than aerobic respiration",
        "alcohol fermentation (yeast): glucose becomes ethanol, CO2 and ATP",
        "lactic acid fermentation (muscle): glucose becomes lactic acid and ATP, with no CO2 produced",
    ), Explanation=""))
rows.append(dict(Topic="Circulatory Systems", Question="Differentiate between an open blood system and a closed blood system, with one example each.",
    Answer_Summary=lettered(
        "open system: blood isn't confined to vessels, flows freely bathing organs directly, e.g. insects",
        "closed system: blood stays confined to vessels for efficient circulation to all tissues, e.g. humans",
    ), Explanation=""))
rows.append(dict(Topic="Plant Transport", Question="How is the structure of xylem tissue suited to its function of water transport?",
    Answer_Summary=lettered(
        "long, hollow tubular vessels/tracheids allow unimpeded water movement",
        "lignin-reinforced walls give mechanical support, preventing collapse under transpiration tension",
        "pits allow lateral water movement between adjacent cells",
    ), Explanation=""))
rows.append(dict(Topic="Population Growth", Question="Suggest three possible reasons for a population's growth rate to decline after its initial exponential growth phase (e.g. in a yeast culture).",
    Answer_Summary=lettered(
        "depletion of available nutrients slows cell division and growth",
        "accumulation of toxic waste products from metabolism inhibits growth",
        "limited space causes competition that restricts further growth",
    ), Explanation=""))
rows.append(dict(Topic="Plant Growth", Question="State two external factors which influence growth in plants and mention one effect of each.",
    Answer_Summary=lettered(
        "light: intensity affects photosynthesis - low light slows growth",
        "water: affects turgor pressure and nutrient transport - lack of water causes wilting and stunted growth",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Sperm Structure)", Question="Describe the structure of a human sperm cell and how each part relates to its function.",
    Answer_Summary=lettered(
        "head: contains the nucleus holding genetic material for the egg",
        "acrosome: cap over the head with enzymes to penetrate the egg's outer layers",
        "neck: connects head to middle piece, contains centrioles for post-fertilization cell division",
        "middle piece: packed with spiral mitochondria providing energy for motility",
        "main piece and flagellum (tail): propels the sperm toward the egg via whip-like movement",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Ploidy)", Question="In a flowering plant where the radicle cell has 16 chromosomes, what is the chromosome number in the pollen tube nucleus, antipodal cell, endosperm cell, pollen mother cell, and integument cell?",
    Answer_Summary=lettered(
        "pollen tube nucleus: 16 (haploid)",
        "antipodal cell: 16 (haploid)",
        "endosperm cell: 24 (triploid)",
        "pollen mother cell: 32 (diploid)",
        "integument cell: 32 (diploid)",
    ), Explanation=""))

# ============================== YEAR 2002 ==============================
# Note: skipped the unseen-diagram labeling parts (2(a)(i) mushroom parts,
# 4(a) lung parts, 9(a) organelle parts) but kept the sub-parts whose
# answers are self-contained, generic facts.
rows.append(dict(Topic="Classification", Question="What is Binomial Nomenclature?",
    Answer_Summary=lettered(
        "system of naming organisms with two names: genus (capitalized) plus species (lowercase)",
        "both names are written in italics (typed) or underlined (handwritten)",
    ), Explanation=""))
rows.append(dict(Topic="Classification", Question="Give any three rules followed in naming organisms scientifically.",
    Answer_Summary=lettered(
        "genus name written first, capitalized",
        "species name written second, lowercase",
        "name is italicized if typed, or underlined if handwritten",
    ), Explanation=""))
rows.append(dict(Topic="Fungi", Question="What is the taxonomic classification (kingdom, phylum, genus) of a typical mushroom such as Agaricus?",
    Answer_Summary=lettered("kingdom: Fungi", "phylum: Basidiomycota", "genus: Agaricus"), Explanation=""))
rows.append(dict(Topic="Fungi", Question="State two ways the kingdom Fungi is of economic importance.",
    Answer_Summary=lettered(
        "used in food production (fermentation for bread, beer, wine)",
        "decomposes organic material, recycling nutrients in ecosystems",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis", Question="State two differences between non-cyclic and cyclic photophosphorylation.",
    Answer_Summary=lettered(
        "non-cyclic uses both photosystem I and II; cyclic uses only photosystem I",
        "non-cyclic produces ATP, NADPH and oxygen; cyclic produces only ATP",
    ), Explanation=""))
rows.append(dict(Topic="Digestion", Question="What are the products of Brunner's glands in the small intestine, and what are their roles?",
    Answer_Summary=lettered(
        "mucus protects the intestinal lining from digestive enzymes and acid",
        "alkaline secretions neutralize acidic chyme from the stomach for an optimal enzyme pH",
    ), Explanation=""))
rows.append(dict(Topic="Gas Exchange", Question="How are the alveoli of the lungs adapted to perform gas exchange efficiently?",
    Answer_Summary=lettered(
        "thin walls (one cell thick) allow rapid gas exchange",
        "surrounded by a dense capillary network to maintain the diffusion gradient for oxygen/carbon dioxide",
    ), Explanation=""))
rows.append(dict(Topic="Excretory System (Kidney)", Question="Briefly explain how the loop of Henle operates as a counter-current multiplier system.",
    Answer_Summary=lettered(
        "creates a concentration gradient in the kidney medulla",
        "descending limb: permeable to water (not solutes) - water leaves the filtrate",
        "ascending limb: impermeable to water, actively pumps Na+/Cl- into the medulla, maintaining the gradient for water reabsorption",
    ), Explanation=""))
rows.append(dict(Topic="Excretory System (Kidney)", Question="What would happen if our kidneys stopped working?",
    Answer_Summary=lettered(
        "waste and toxins accumulate, leading to uremia",
        "fluid imbalance causes swelling and high blood pressure, potentially fatal",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Sex Chromosomes)", Question="Give two differences between the X and Y chromosomes of humans.",
    Answer_Summary=lettered(
        "X is larger and has more genes than Y",
        "X occurs in both sexes; Y occurs only in males",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Sex-Linked Inheritance)", Question="Why are there more colorblind individuals than hemophiliacs, even though both are inherited the same (X-linked) way?",
    Answer_Summary=lettered(
        "the colorblindness gene is X-linked recessive, and one defective allele in males (XY) causes it",
        "hemophilia is also X-linked, but its gene has a lower mutation rate, making it rarer",
    ), Explanation=""))
rows.append(dict(Topic="Evolution", Question="Define convergent evolution.",
    Answer_Summary=lettered("unrelated organisms independently evolve similar traits by adapting to similar environments/niches"), Explanation=""))
rows.append(dict(Topic="Evolution", Question="What were Lamarck's ideas on evolution, and how are they explained by modern genetics?",
    Answer_Summary=lettered(
        "Lamarck: organisms acquire traits through use/disuse of organs during their lifetime, and pass these to offspring",
        "modern genetics refutes this - acquired traits don't alter DNA, so they can't be inherited",
        "evolution instead happens through natural selection acting on existing genetic variation",
    ), Explanation=""))
rows.append(dict(Topic="Food Webs", Question="In a freshwater food web with aquatic plants, small crustaceans, insect larvae, tadpoles, water beetles, frogs, roach, perch, pike and man, identify the trophic levels and the longest food chain.",
    Answer_Summary=lettered(
        "four trophic levels: producers (aquatic plants), primary consumers (crustaceans, insect larvae, tadpoles), secondary consumers (water beetles, frogs, roach), tertiary consumers (perch, pike, man)",
        "frogs feed at three trophic levels - eating insect larvae and crustaceans (primary) and water beetles (secondary)",
        "longest food chain: aquatic plants -> small crustaceans -> water beetles -> perch -> pike -> man",
    ), Explanation=""))
rows.append(dict(Topic="Population Ecology", Question="What are density-dependent factors and interspecific competition?",
    Answer_Summary=lettered(
        "density-dependent factors: effects on population size vary with density (e.g. competition, predation, disease, parasitism), regulating population as density rises",
        "interspecific competition: different species competing for the same limited resources, affecting distribution/abundance via exclusion or niche differentiation",
    ), Explanation=""))
rows.append(dict(Topic="Cell Organelles", Question="How are the mitochondrion, Golgi apparatus, secretory vesicles, and exocytosis involved in synthesizing and secreting an enzyme?",
    Answer_Summary=lettered(
        "mitochondrion: supplies ATP energy for synthesis and secretion",
        "Golgi apparatus: modifies, packages and sorts the enzyme into secretory vesicles",
        "secretory vesicle: transports the enzyme to the plasma membrane",
        "exocytosis: releases the enzyme into the extracellular space",
    ), Explanation=""))
rows.append(dict(Topic="Sensory Receptors", Question="Classify sensory receptors into five categories based on the stimuli they respond to, and name the stimulus in each case.",
    Answer_Summary=lettered(
        "mechanoreceptors - pressure or vibration",
        "thermoreceptors - heat or cold",
        "chemoreceptors - chemicals (e.g. oxygen, CO2, glucose)",
        "photoreceptors - light",
        "nociceptors - pain or damage",
    ), Explanation=""))
rows.append(dict(Topic="Human Eye", Question="Tabulate four differences between rods and cones.",
    Answer_Summary=lettered(
        "sensitivity: rods are more sensitive to dim light; cones to bright light",
        "color detection: rods can't detect color; cones can (RGB pigments)",
        "location: rods are in the peripheral retina; cones in the central retina (fovea)",
        "visual acuity: rods give low acuity; cones give high acuity",
    ), Explanation=""))
rows.append(dict(Topic="Gas Exchange (Plants)", Question="Describe three ways terrestrial flowering plants obtain gaseous oxygen.",
    Answer_Summary=lettered(
        "through stomata on leaves",
        "through lenticels on stems",
        "by diffusion through root hairs",
    ), Explanation=""))
rows.append(dict(Topic="Respiration", Question="Why does oxidizing fats release more than double the energy of the same quantity of carbohydrate?",
    Answer_Summary=lettered(
        "fats have more hydrogen atoms per molecule, giving more electrons for the electron transport chain",
        "this yields greater ATP production than carbohydrates",
    ), Explanation=""))
rows.append(dict(Topic="Cell Transport", Question="What process maintains a lower sodium concentration inside a cell, and how does it work?",
    Answer_Summary=lettered(
        "the sodium-potassium pump, an active transport process",
        "uses ATP to pump 3 sodium ions out and 2 potassium ions in, against their concentration gradients",
    ), Explanation=""))
rows.append(dict(Topic="Plant Water Transport", Question="What is guttation?",
    Answer_Summary=lettered("water droplets exuded from leaf tips/edges, usually at night, due to root pressure"), Explanation=""))
rows.append(dict(Topic="Growth Patterns", Question="What type of growth curve do arthropods show, and what causes it?",
    Answer_Summary=lettered(
        "discontinuous growth - rapid mass increase followed by plateaus",
        "caused by molting (ecdysis): the exoskeleton is shed, the organism grows quickly, then the new exoskeleton hardens",
    ), Explanation=""))
rows.append(dict(Topic="Growth Patterns", Question="What is meant by allometric growth and isometric growth, with an example of each?",
    Answer_Summary=lettered(
        "allometric: different body parts grow disproportionately relative to overall size, e.g. the human head grows slower than the limbs",
        "isometric: all body parts grow at the same rate, keeping proportions, e.g. fish grow uniformly",
    ), Explanation=""))
rows.append(dict(Topic="Plant Reproduction", Question="Explain the following parts of an unfertilized ovule in a flowering plant: micropyle, nucellus, integuments, embryo sac, polar nuclei, female nucleus.",
    Answer_Summary=lettered(
        "micropyle: small opening in the integuments where the pollen tube enters",
        "nucellus: central tissue enclosing the embryo sac, nourishing the gametophyte",
        "integuments: protective layers around the nucellus that become the seed coat",
        "embryo sac: the female gametophyte containing the egg cell and other cells for fertilization",
        "polar nuclei: two nuclei in the central cell that fuse with a sperm cell to form the triploid endosperm",
        "female nucleus (egg cell): haploid cell that becomes the zygote upon fertilization",
    ), Explanation=""))
rows.append(dict(Topic="Plant Reproduction", Question="With reference to a maize plant, describe double fertilization and explain its importance.",
    Answer_Summary=lettered(
        "one sperm nucleus fuses with the egg cell to form a diploid zygote (embryo)",
        "the second sperm nucleus fuses with the two polar nuclei to form the triploid endosperm",
        "importance: the endosperm nourishes the developing embryo/seedling, aiding reproductive success",
    ), Explanation=""))

# ============================== YEAR 2003 ==============================
# Note: dropped question 9 entirely - it references membrane diagram labels
# A-F but the source text for parts (b)/(c) refers to "E and F" which were
# never actually labeled in the visible answer text, making the real
# structures being asked about too ambiguous to state as fact. Also skipped
# 14(a)'s pure part-labeling sub-question.
rows.append(dict(Topic="Classification", Question="What is the importance of biological keys?",
    Answer_Summary=lettered(
        "help identify and classify organisms by their observable characteristics",
        "let you distinguish between closely related species",
        "support the study of biodiversity",
    ), Explanation=""))
rows.append(dict(Topic="Classification", Question="Explain briefly the significance of scientific naming of organisms.",
    Answer_Summary=lettered(
        "gives a universal language for identifying and classifying organisms, avoiding confusion from local names",
        "ensures consistency and shows relationships and evolutionary history",
    ), Explanation=""))
rows.append(dict(Topic="Fungi", Question="Why is yeast classified as a fungus?",
    Answer_Summary=lettered(
        "eukaryotic, lacks chlorophyll",
        "reproduces by budding or spore formation",
        "has a chitin cell wall",
        "heterotrophic, absorbs nutrients",
    ), Explanation=""))
rows.append(dict(Topic="Fungi", Question="What features place fungi in the plant kingdom, and what features place them in the animal kingdom?",
    Answer_Summary=lettered(
        "plant-like: has a cell wall (chitin, not cellulose); stationary lifestyle",
        "animal-like: heterotrophic (absorptive) nutrition; stores glycogen as a carbohydrate reserve",
    ), Explanation=""))
rows.append(dict(Topic="Digestive System", Question="How is the epithelial lining of the ileum adapted for absorption?",
    Answer_Summary=lettered(
        "villi and microvilli increase surface area",
        "thin walls allow easy diffusion",
        "blood capillaries and lacteals transport absorbed nutrients",
        "mucus is produced to aid smooth passage of food",
    ), Explanation=""))
rows.append(dict(Topic="Digestive System", Question="What features of a single ileum epithelial cell (enterocyte) adapt it for absorption?",
    Answer_Summary=lettered(
        "microvilli form a \"brush border\" that increases surface area",
        "tight junctions between cells stop enzymes/pathogens leaking through",
        "abundant mitochondria supply energy for active transport",
        "a basal nucleus leaves the apical region free for absorption organelles",
        "glycocalyx houses enzymes for final digestion and protects the microvilli",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Krebs Cycle)", Question="In what two main ways is the Krebs cycle (TCA) important in respiration?",
    Answer_Summary=lettered(
        "generates NADH and FADH2 that fuel the electron transport chain for ATP synthesis",
        "provides intermediate compounds for biosynthesis (e.g. amino acids, lipids)",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Krebs Cycle)", Question="Explain two significant relationships between the Krebs cycle and the electron transport chain.",
    Answer_Summary=lettered(
        "NADH and FADH2 from the Krebs cycle donate electrons to the electron transport chain, driving ATP synthesis",
        "carbon dioxide released in the Krebs cycle is a byproduct of aerobic respiration",
    ), Explanation=""))
rows.append(dict(Topic="Homeostasis", Question="Define homeostasis.",
    Answer_Summary=lettered("maintaining a stable internal environment despite changes in external conditions"), Explanation=""))
rows.append(dict(Topic="Homeostasis", Question="Describe the homeostatic roles of the digestive system, respiratory system, and kidneys.",
    Answer_Summary=lettered(
        "digestive system: breaks down and absorbs nutrients, regulates water/electrolyte balance",
        "respiratory system: maintains blood oxygen/CO2 levels, helps regulate blood pH by removing CO2",
        "kidneys: excrete metabolic waste (e.g. urea), regulate water/salt balance and blood pressure",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Mendelian)", Question="State Mendel's laws of heredity.",
    Answer_Summary=lettered(
        "law of segregation: alleles for each gene separate so each gamete gets only one",
        "law of independent assortment: genes for different traits assort independently (if not linked)",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Mendelian Crosses)", Question="What would the offspring phenotype ratio be from a cross of two heterozygous (Bb x Bb) parents, and from a cross of a homozygous grey male (GG) with a heterozygous grey female (Gg)?",
    Answer_Summary=lettered(
        "Bb x Bb gives a 3:1 ratio - 75% dominant body color, 25% recessive",
        "GG x Gg gives 100% grey offspring, with no recessive phenotype showing",
    ), Explanation=""))
rows.append(dict(Topic="Evolution", Question="State Darwin's theory of natural selection.",
    Answer_Summary=lettered(
        "organisms better suited to their environment survive and reproduce more",
        "these advantageous traits pass to the next generation, driving evolutionary change",
    ), Explanation=""))
rows.append(dict(Topic="Food Chains and Pyramids", Question="What is a food chain, and what does a pyramid of numbers for grass, a herbivorous mammal, fleas and Leptomonas parasites look like?",
    Answer_Summary=lettered(
        "a food chain is a linear sequence transferring energy from producers to top consumers/decomposers",
        "grass (producers) has the largest population at the base",
        "herbivorous mammals are fewer in number than grass",
        "fleas (parasites of the mammal) are more numerous than their mammal hosts",
        "Leptomonas (parasites of fleas) are the most numerous of all",
    ), Explanation=""))
rows.append(dict(Topic="Environmental Science", Question="How does deforestation increase atmospheric carbon dioxide levels?",
    Answer_Summary=lettered(
        "fewer trees to absorb CO2 during photosynthesis",
        "burning or decomposing trees releases their stored carbon",
        "disrupts ecosystems that help regulate the carbon cycle",
    ), Explanation=""))
rows.append(dict(Topic="Plant Hormones", Question="What is a phytohormone?",
    Answer_Summary=lettered("a plant chemical that regulates growth, development and response to environmental stimuli"), Explanation=""))
rows.append(dict(Topic="Plant Hormones", Question="In what ways are phytohormones important in plant growth and development?",
    Answer_Summary=lettered(
        "control cell elongation, division and differentiation",
        "control flowering and fruit development",
        "control seed dormancy and response to environmental stress",
    ), Explanation=""))
rows.append(dict(Topic="Respiratory Pigments", Question="How is a mammalian fetus adapted for oxygen uptake, based on the oxygen dissociation curves of adult versus fetal hemoglobin?",
    Answer_Summary=lettered(
        "fetal hemoglobin has a higher oxygen affinity than adult hemoglobin",
        "this lets it pull oxygen effectively from the mother's blood in the placenta",
    ), Explanation=""))
rows.append(dict(Topic="Digestion (Absorption)", Question="Why is active transport important in absorbing monosaccharides, dipeptides and amino acids?",
    Answer_Summary=lettered(
        "lets nutrients be absorbed against their concentration gradient",
        "allows efficient uptake even when gut concentration is lower than blood concentration",
    ), Explanation=""))
rows.append(dict(Topic="Gas Exchange", Question="What respiratory surface features are common to all vertebrates, and why does each matter?",
    Answer_Summary=lettered(
        "thin membrane - allows rapid gas exchange",
        "moist surface - lets gases dissolve and diffuse",
        "rich blood supply - maintains the diffusion gradient",
        "large surface area - increases gas exchange efficiency",
    ), Explanation=""))
rows.append(dict(Topic="Insect Metamorphosis", Question="Distinguish complete from incomplete metamorphosis.",
    Answer_Summary=lettered(
        "complete: four stages - egg, larva, pupa, adult",
        "incomplete: three stages - egg, nymph, adult",
    ), Explanation=""))
rows.append(dict(Topic="Insect Metamorphosis", Question="Explain the hormonal control of metamorphosis (molting) in insects.",
    Answer_Summary=lettered(
        "ecdysone stimulates molting and exoskeleton transformation",
        "juvenile hormone keeps juvenile characteristics when present at high levels",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Spermatogenesis)", Question="Which structure gives rise to spermatogonia?",
    Answer_Summary=lettered("spermatogonia form from undifferentiated germ cells in the germinal epithelium"), Explanation=""))
rows.append(dict(Topic="Reproduction (Spermatogenesis)", Question="What process transforms primary spermatocytes into secondary spermatocytes?",
    Answer_Summary=lettered("meiosis - specifically the first meiotic division"), Explanation=""))
rows.append(dict(Topic="Reproduction (Spermatogenesis)", Question="What is the function of Sertoli cells?",
    Answer_Summary=lettered(
        "provide nutritional and structural support to developing sperm",
        "secrete substances that regulate spermatogenesis",
        "protect sperm from the body's immune response",
    ), Explanation=""))
rows.append(dict(Topic="Plant Reproduction", Question="Define double fertilization and its consequences.",
    Answer_Summary=lettered(
        "one sperm fertilizes the egg to form a diploid zygote",
        "the other sperm fuses with the two polar nuclei to form a triploid endosperm",
        "consequence: produces both the embryo (next generation) and the endosperm (nourishment for the embryo)",
    ), Explanation=""))

# ============================== YEAR 2004 ==============================
rows.append(dict(Topic="Classification (Taxonomy)", Question="Who is a taxonomist?",
    Answer_Summary=lettered(
        "a scientist who classifies organisms by similarities/differences into hierarchical categories (kingdom to species)",
        "uses morphological, genetic and ecological traits to group organisms systematically",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Taxonomy)", Question="What problems is a taxonomist likely to encounter?",
    Answer_Summary=lettered(
        "morphological variation within a species from environmental factors",
        "convergent evolution causing unrelated organisms to look alike",
        "incomplete fossil records making evolutionary relationships hard to establish",
        "high genetic diversity blurring species/subspecies boundaries",
        "hybridization between species blurring species boundaries",
        "limited molecular data for some species",
    ), Explanation=""))
rows.append(dict(Topic="Classification", Question="Giving two reasons in each case, place the earthworm, mushroom, Taenia sp. and Trypanosoma sp. in their appropriate phyla/divisions.",
    Answer_Summary=lettered(
        "earthworm (phylum Annelida): segmented body (metamerism); closed circulatory system",
        "mushroom (division Basidiomycota, kingdom Fungi): reproduces by basidiospores on a basidium; chitinous cell walls",
        "Taenia sp. (phylum Platyhelminthes): dorso-ventrally flattened body; parasitic with no digestive system, absorbs nutrients directly",
        "Trypanosoma sp. (phylum Protozoa, class Kinetoplastida): unicellular and microscopic; has flagella for movement",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis", Question="What is the role of water, NADP, and light in photosynthesis?",
    Answer_Summary=lettered(
        "water: split during photolysis into oxygen (released), electrons (replace those lost by chlorophyll), and protons (help form ATP/NADPH)",
        "NADP: electron carrier - accepts electrons/H+ to form NADPH, used to reduce CO2 to glucose in the Calvin cycle",
        "light: excites electrons in chlorophyll and drives photolysis, generating oxygen and electrons for ATP/NADPH",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis (C3 vs C4)", Question="Give three differences between C3 and C4 plants.",
    Answer_Summary=lettered(
        "carbon fixation: C3 fixes CO2 directly via the Calvin cycle into a 3-carbon compound; C4 first fixes CO2 into a 4-carbon compound via the Hatch-Slack pathway",
        "photorespiration: high in C3 plants (less efficient in heat); minimized in C4 plants by separating carbon fixation from the Calvin cycle",
        "leaf anatomy: C3 lacks Kranz anatomy; C4 has Kranz anatomy with chloroplasts concentrated in bundle sheath cells",
    ), Explanation=""))
rows.append(dict(Topic="Gas Exchange", Question="What are the properties of respiratory surfaces?",
    Answer_Summary=lettered(
        "large surface area for maximum gas exchange",
        "thin walls to reduce diffusion distance",
        "moist surface so gases dissolve before diffusing",
        "rich blood supply for efficient gas transport",
        "permeability allowing free movement of O2/CO2",
    ), Explanation=""))
rows.append(dict(Topic="Gas Exchange", Question="Describe how gaseous exchange occurs in the mammalian lung.",
    Answer_Summary=lettered(
        "occurs at the alveoli",
        "oxygen diffuses from alveolar air into the blood",
        "carbon dioxide diffuses from the blood into the alveoli for exhalation",
    ), Explanation=""))
rows.append(dict(Topic="Osmosis in Plants", Question="Why do split, water-immersed pieces of a pawpaw petiole curl outward?",
    Answer_Summary=lettered(
        "differential osmotic pressure across the tissue",
        "outer cells absorb more water by osmosis than inner cells, expanding more and causing outward curling",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Sex-Linked Inheritance)", Question="A girl of normal vision whose father was colorblind marries a man of normal vision whose father was also colorblind. What is the expected vision of their children?",
    Answer_Summary=lettered(
        "the girl must be heterozygous (carrier, XNXn) since her father was colorblind",
        "half of her sons (XY) may inherit colorblindness",
        "all her daughters (XX) will have normal vision, but may be carriers",
    ), Explanation=""))
rows.append(dict(Topic="Evolution", Question="What do the terms \"primitive\" and \"advanced\" mean in evolution?",
    Answer_Summary=lettered(
        "primitive: ancestral traits from early evolutionary stages",
        "advanced: newly evolved, specialized traits",
    ), Explanation=""))
rows.append(dict(Topic="Evolution", Question="Outline the limitations of Darwin's theory of natural selection.",
    Answer_Summary=lettered(
        "lacked knowledge of genetics",
        "doesn't explain sudden mutations",
        "doesn't account for neutral traits",
        "doesn't explain inheritance of acquired traits",
    ), Explanation=""))
rows.append(dict(Topic="Pest Control", Question="Define the term \"biological control.\"",
    Answer_Summary=lettered("using natural predators, parasites or pathogens to control pests"), Explanation=""))
rows.append(dict(Topic="Pest Control", Question="What are the merits and demerits of biological control compared to other pest control methods?",
    Answer_Summary=lettered(
        "merit: environmentally friendly",
        "merit: pests don't develop chemical resistance",
        "demerit: slow to act",
        "demerit: may affect non-target species",
    ), Explanation=""))
rows.append(dict(Topic="Plant Reproduction", Question="Why are megaspores of Drimysperm sp. large while microspores are small?",
    Answer_Summary=lettered(
        "megaspores store nutrients for embryo development",
        "microspores stay small for easy dispersal",
    ), Explanation=""))
rows.append(dict(Topic="Enzymes", Question="How does denaturing an enzyme affect its efficiency as a catalyst?",
    Answer_Summary=lettered(
        "alters the shape of the active site",
        "prevents substrate binding, reducing enzyme activity",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Nerve Impulse)", Question="Describe how an impulse is transmitted along an axon.",
    Answer_Summary=lettered(
        "resting potential: inside is negative (-70mV) via the sodium-potassium pump",
        "depolarization: a stimulus above threshold opens voltage-gated Na+ channels, reversing polarity (+40mV)",
        "propagation: the positive charge spreads, triggering neighboring Na+ channels along the axon",
        "repolarization: Na+ channels close, K+ channels open, restoring the negative internal charge",
        "hyperpolarization: the membrane briefly goes more negative before returning to resting potential",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Nerve Impulse)", Question="Define a refractory period and state its significance.",
    Answer_Summary=lettered(
        "the time after an action potential when a neuron can't fire another impulse",
        "prevents impulses conducting backward",
        "ensures one-way transmission of nerve impulses",
        "lets the neuron recover before firing again",
    ), Explanation=""))
rows.append(dict(Topic="Oxygen Adaptations", Question="How do mountain dwellers adapt to low oxygen levels?",
    Answer_Summary=lettered(
        "increased red blood cell count for more hemoglobin",
        "higher lung capacity",
        "increased myoglobin to store more oxygen in muscles",
        "higher breathing rate",
    ), Explanation=""))
rows.append(dict(Topic="Oxygen Adaptations", Question="How do divers (e.g. whales, seals) adapt to prolonged underwater oxygen deprivation?",
    Answer_Summary=lettered(
        "more myoglobin and hemoglobin to store oxygen",
        "slower heartbeat (bradycardia) to reduce oxygen use",
        "peripheral vasoconstriction restricts blood flow to vital organs",
        "tolerance for anaerobic respiration",
    ), Explanation=""))
rows.append(dict(Topic="Oxygen Adaptations", Question="How does the mammalian fetus adapt to oxygen uptake in the womb?",
    Answer_Summary=lettered(
        "fetal hemoglobin (HbF) has a higher oxygen affinity than adult hemoglobin",
        "oxygen diffuses from maternal blood to fetal blood across the placenta",
        "increased capillary density boosts oxygen absorption in fetal tissue",
    ), Explanation=""))
rows.append(dict(Topic="Plant Transport (Phloem)", Question="What evidence supports the transport of organic material in the phloem?",
    Answer_Summary=lettered(
        "ring experiment: removing a bark ring (phloem) causes sugar buildup above the cut, showing downward transport",
        "radioactive labeling: carbon-14 labeled CO2 traces movement through the phloem",
        "aphid experiment: aphids feeding on phloem sap confirm sugar transport there",
    ), Explanation=""))
rows.append(dict(Topic="Plant Transport (Phloem)", Question="What evidence supports the mass flow theory of phloem transport?",
    Answer_Summary=lettered(
        "sap exudes under pressure when the phloem is cut, showing pressure-driven flow",
        "companion cells have many mitochondria, supporting active transport",
        "blocking ATP production with sucrose-transport inhibitors stops transport, showing active transport is involved",
    ), Explanation=""))
rows.append(dict(Topic="Seed Germination and Growth", Question="During germination and early seedling growth, why does dry weight first decrease, then increase as photosynthesis begins, and later decrease again after some weeks?",
    Answer_Summary=lettered(
        "initial decrease: the seed uses stored food reserves for respiration before it becomes photosynthetic",
        "later increase: once leaves/roots develop, photosynthesis produces organic matter and increases biomass",
        "eventual decrease: leaf senescence and respiration exceeding photosynthesis due to aging",
    ), Explanation=""))
rows.append(dict(Topic="Growth Patterns", Question="What type of growth curve does a germinating seedling show, and what happens in each phase?",
    Answer_Summary=lettered(
        "sigmoid (S-shaped) growth curve",
        "lag phase: slow growth as the seed adapts",
        "exponential phase: rapid growth from cell division and photosynthesis",
        "stationary phase: growth slows due to environmental limits",
        "senescence phase: dry mass declines due to aging",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction", Question="Define sexual reproduction and asexual reproduction.",
    Answer_Summary=lettered(
        "sexual reproduction: fusion of male and female gametes, producing genetically diverse offspring",
        "asexual reproduction: no gamete fusion, producing genetically identical offspring",
    ), Explanation=""))
rows.append(dict(Topic="Cell Division", Question="Why is mitosis called an equational division and meiosis a reduction division?",
    Answer_Summary=lettered(
        "mitosis: chromosome number stays the same in daughter cells",
        "meiosis: halves the chromosome number, producing haploid gametes",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Embryonic Membranes)", Question="Identify the embryonic membranes in mammals and state the role of each.",
    Answer_Summary=lettered(
        "amnion: encloses the embryo in amniotic fluid for protection",
        "chorion: forms part of the placenta, aiding nutrient/gas exchange",
        "yolk sac: provides early nutrients and helps form blood cells",
        "allantois: helps with waste removal and gas exchange",
    ), Explanation=""))

# ============================== YEAR 2005 ==============================
rows.append(dict(Topic="Cell Structure", Question="Define a cell.",
    Answer_Summary=lettered("the basic structural, functional and biological unit of life, able to carry out life's essential processes"), Explanation=""))
rows.append(dict(Topic="Cell Structure", Question="State four structural differences between an animal cell and a plant cell.",
    Answer_Summary=lettered(
        "plant cells have a cellulose cell wall; animal cells only have a plasma membrane",
        "plant cells have chloroplasts; animal cells don't",
        "plant cells usually have a large central vacuole; animal cells have small or no vacuoles",
        "animal cells have centrioles; most plant cells don't",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Kingdoms)", Question="Besides the presence of chloroplasts, what other characteristics distinguish the plant kingdom from the animal kingdom, and where does the fungi kingdom fit among the five kingdoms?",
    Answer_Summary=lettered(
        "plant cells have cellulose cell walls; animal cells lack cell walls",
        "plants store food as starch; animals store food as glycogen",
        "fungi form their own separate kingdom (Kingdom Fungi), distinct from both",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis and Respiration", Question="List six similarities (including biochemical ones) between photosynthesis and aerobic respiration.",
    Answer_Summary=lettered(
        "both involve electron transport chains",
        "both use ATP as an energy carrier",
        "both involve redox reactions",
        "both occur in specialized organelles (chloroplasts vs mitochondria)",
        "both depend on enzymes for catalysis",
        "both produce energy-rich molecules essential for life",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Respiratory Quotient)", Question="What is meant by the respiratory quotient (RQ) of a respiratory substrate?",
    Answer_Summary=lettered("ratio of CO2 produced to O2 consumed during respiration of a substrate"), Explanation=""))
rows.append(dict(Topic="Respiration (Respiratory Quotient)", Question="Calculate the respiratory quotient of fat (tripalmitin), given 2C51H98O6 + 145O2 -> 102CO2 + 98H2O.",
    Answer_Summary=lettered("RQ = CO2 produced / O2 consumed = 102/145 = approximately 0.7"), Explanation=""))
rows.append(dict(Topic="Respiration (Energy Efficiency)", Question="If one glucose molecule yields about 2830 kJ and one ATP equals 33 kJ, what is the efficiency of glycolysis and the Krebs cycle producing 38 ATP?",
    Answer_Summary=lettered(
        "energy in 38 ATP = 38 x 33 = 1254 kJ",
        "efficiency = (1254 / 2830) x 100 = approximately 44.3%",
    ), Explanation=""))
rows.append(dict(Topic="Human Ear", Question="What is the role of the organ of Corti in hearing?",
    Answer_Summary=lettered(
        "contains hair cells that convert sound vibrations into electrical impulses",
        "impulses are sent via the auditory nerve to the brain",
    ), Explanation=""))
rows.append(dict(Topic="Embryonic Development", Question="Explain briefly how the morula is formed from the zygote.",
    Answer_Summary=lettered("the zygote undergoes repeated mitotic divisions (cleavage), forming a solid ball of cells - the morula"), Explanation=""))
rows.append(dict(Topic="Embryonic Development", Question="What is meant by the formation of the morula from the zygote being \"radial and indeterminate\"?",
    Answer_Summary=lettered(
        "radial: cells divide parallel or perpendicular to the embryo's axis, forming a symmetrical arrangement",
        "indeterminate: each cell can still develop into a complete organism if separated",
    ), Explanation=""))
rows.append(dict(Topic="Growth Patterns", Question="Using examples, explain the differences between limited and unlimited growth.",
    Answer_Summary=lettered(
        "limited growth: an organism grows to a certain size then stops, e.g. humans",
        "unlimited growth: an organism keeps growing throughout life, e.g. many plants and fish",
    ), Explanation=""))
rows.append(dict(Topic="Genetics", Question="Distinguish between sex-linked and sex-limited traits.",
    Answer_Summary=lettered(
        "sex-linked: controlled by genes on sex chromosomes, e.g. haemophilia",
        "sex-limited: expressed in only one sex though the gene is present in both, e.g. milk production in cows",
    ), Explanation=""))
rows.append(dict(Topic="Genetics", Question="Define chromosomal mutation, codominance, and polygenic inheritance.",
    Answer_Summary=lettered(
        "chromosomal mutation: change in chromosome structure or number",
        "codominance: both alleles of a gene are expressed equally in a heterozygote",
        "polygenic inheritance: controlled by many genes, producing continuous variation",
    ), Explanation=""))
rows.append(dict(Topic="Evolution", Question="What is the law of use and disuse?",
    Answer_Summary=lettered("Lamarck's idea: organs develop when used frequently and shrink when not used"), Explanation=""))
rows.append(dict(Topic="Evolution", Question="What is convergent evolution?",
    Answer_Summary=lettered("unrelated organisms evolve similar traits by adapting to similar environments"), Explanation=""))
rows.append(dict(Topic="Food Webs", Question="In a food web, what happens if one of the middle-level consumer species suddenly disappears?",
    Answer_Summary=lettered(
        "species that depended on it for food decrease",
        "species it used to prey on then increase, since predation on them drops",
        "the ecosystem becomes unstable, causing population imbalance",
    ), Explanation=""))
rows.append(dict(Topic="Meiosis", Question="Give two events of meiosis that account for genetic differences among the four daughter cells it produces.",
    Answer_Summary=lettered(
        "crossing over in prophase I - homologous chromosomes exchange genetic material, creating new allele combinations",
        "independent assortment in metaphase I - homologous pairs align randomly, mixing maternal/paternal chromosomes in gametes",
    ), Explanation=""))
rows.append(dict(Topic="Respiratory System", Question="Why is it advised to breathe air in through the nose rather than the mouth?",
    Answer_Summary=lettered(
        "nose hairs and mucus filter out dust and microorganisms, reducing infection risk",
        "the nasal cavity warms incoming air, protecting delicate lung tissue",
        "the nose moistens air, reducing dryness of respiratory surfaces",
    ), Explanation=""))
rows.append(dict(Topic="Blood Sugar Regulation", Question="Two people, X and Y, drink a glucose solution and have their blood sugar tracked over time. X's blood sugar rises sharply then falls after 60 minutes; Y's rises slowly and stays low. What might explain each pattern?",
    Answer_Summary=lettered(
        "X: the rapid rise shows efficient glucose absorption; the sharp fall shows effective insulin secretion promoting glucose uptake",
        "Y: the slow rise and persistently low levels suggest reduced absorption or an insulin problem, possibly diabetes mellitus",
    ), Explanation=""))
rows.append(dict(Topic="Circulatory System", Question="In mammals and birds, blood flows to body tissues at high pressure but to the lungs at lower pressure. What are the advantages of each?",
    Answer_Summary=lettered(
        "high pressure to tissues ensures rapid oxygen/nutrient delivery for high metabolic demand",
        "high pressure to tissues also ensures fast removal of wastes like CO2 and urea",
        "lower pressure to lungs prevents damage to delicate alveoli and capillaries",
        "lower pressure to lungs gives enough time for gas exchange",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Fertilization)", Question="Describe the events that take place during fertilization in human beings.",
    Answer_Summary=lettered(
        "sperm is deposited in the female tract and swims to the ovum in the fallopian tube",
        "capacitation: enzymes modify the sperm membrane to allow penetration",
        "acrosome reaction: releases enzymes that digest the layers around the ovum",
        "one sperm penetrates the ovum, triggering the cortical reaction that blocks other sperm (polyspermy block)",
        "sperm and ovum nuclei fuse, forming a diploid zygote",
    ), Explanation=""))
rows.append(dict(Topic="Plant Reproduction (Floral Formula)", Question="What is the floral formula of a radially symmetric, bisexual flower with 5 sepals, 5 petals, many stamens, and a superior ovary of 5 fused carpels?",
    Answer_Summary=lettered("floral formula: bisexual, K5 C5 A(many) G(5)"), Explanation=""))
rows.append(dict(Topic="Genetics (Dominance)", Question="In certain plants, red x yellow flowers give a 1:1 ratio of offspring, while red x red gives only red offspring. Which gene is dominant, and what are the genotypes of red- and yellow-flowered plants?",
    Answer_Summary=lettered(
        "red is the dominant gene",
        "red-flowered plants can be RR or Rr",
        "yellow-flowered plants are rr",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Sex-Linked Inheritance)", Question="Why are sex-linked defects more common in males than females?",
    Answer_Summary=lettered(
        "males have only one X chromosome, so a recessive allele on it is always expressed (no matching allele on Y)",
        "females have two X chromosomes, so a recessive allele is often masked by a dominant one on the other X",
        "this makes males more vulnerable to defects like haemophilia and colorblindness",
    ), Explanation=""))

# ============================== YEAR 2006 ==============================
# Note: skipped 6(b) entirely - it depends on an unseen pedigree diagram and
# the source's own answer admits it cannot see it either ("This requires
# analyzing the pedigree, which I cannot see in detail"). Also dropped the
# gibberellins row in question 11 - the source duplicates auxins' function
# text for it verbatim, which is clearly a copy error, not a real answer.
rows.append(dict(Topic="Classification (Keys)", Question="What do you understand by a dichotomous identification key?",
    Answer_Summary=lettered(
        "a tool that identifies/classifies organisms via a series of paired contrasting choices",
        "each step narrows the identification down until the organism is determined",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Keys)", Question="Construct a simple dichotomous key to identify the chordate classes Mammalia, Aves, Reptilia, Amphibia, Chondrichthyes, and Osteichthyes using hair, feathers, scales and skeleton type.",
    Answer_Summary=lettered(
        "has hair -> Mammalia; no hair -> next",
        "has feathers -> Aves; no feathers -> next",
        "has scales -> next; no scales -> Amphibia",
        "cartilaginous skeleton -> Chondrichthyes; bony skeleton -> Osteichthyes",
    ), Explanation=""))
rows.append(dict(Topic="Classification", Question="Among a protozoan, a bacterium, a mould, a bryophyte and a flowering plant: which reproduces entirely asexually, which produce spores, which have mitochondria, which can fix nitrogen, and how do a bryophyte and flowering plant differ structurally?",
    Answer_Summary=lettered(
        "entirely asexual: the bacterium",
        "produce spores: the mould, bryophyte and flowering plant",
        "possess mitochondria: the protozoan, mould, bryophyte and flowering plant (bacteria lack mitochondria)",
        "can fix nitrogen: the bacterium",
        "bryophyte vs flowering plant: bryophyte lacks true vascular tissue and reproduces by spores; flowering plant has vascular tissue and reproduces by seeds",
    ), Explanation=""))
rows.append(dict(Topic="Classification", Question="What kingdoms do a protozoan, bacterium, mould, bryophyte and flowering plant belong to?",
    Answer_Summary=lettered(
        "protozoan: Kingdom Protista",
        "bacterium: Kingdom Monera",
        "mould: Kingdom Fungi",
        "bryophyte and flowering plant: Kingdom Plantae",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis", Question="What are the roles of ribulose bisphosphate (RuBP) and NADP in photosynthesis?",
    Answer_Summary=lettered(
        "RuBP: a 5-carbon CO2 acceptor in the Calvin cycle, combining with CO2 to start carbon fixation",
        "NADP: electron carrier, reduced to NADPH in the light reactions, supplying electrons/hydrogen for the Calvin cycle",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis (C3 vs C4)", Question="Why are C4 plants more efficient at photosynthesis than C3 plants, and what happens to C3 photosynthesis if oxygen concentration rises?",
    Answer_Summary=lettered(
        "C4 plants have a specialized CO2-fixing mechanism that minimizes photorespiration, working well even in low CO2/high O2",
        "raising oxygen increases photorespiration in C3 plants since oxygen competes with CO2 for RuBisCO's active site, reducing efficiency",
    ), Explanation=""))
rows.append(dict(Topic="Respiration", Question="What role do mitochondria, oxygen, cytochromes and glucose each play in releasing energy during aerobic respiration?",
    Answer_Summary=lettered(
        "mitochondria: site of the Krebs cycle and oxidative phosphorylation, generating ATP",
        "oxygen: final electron acceptor in the electron transport chain, forming water",
        "cytochromes: electron carriers in the electron transport chain that build the proton gradient for ATP synthesis",
        "glucose: the initial substrate for glycolysis, broken into pyruvate, generating ATP and NADH",
    ), Explanation=""))
rows.append(dict(Topic="Gas Exchange", Question="How might a decrease in environmental temperature affect gas exchange in a well-lit leaf and in a small mammal?",
    Answer_Summary=lettered(
        "leaf: lower temperature slows photosynthesis and respiration, reducing stomatal activity and gas exchange",
        "small mammal: lower temperature raises metabolic rate to maintain body heat, increasing oxygen use and CO2 output",
    ), Explanation=""))
rows.append(dict(Topic="Homeostasis (Feedback)", Question="What are the main differences between negative and positive feedback?",
    Answer_Summary=lettered(
        "negative feedback: reverses a deviation to maintain homeostasis (e.g. temperature regulation)",
        "positive feedback: amplifies a response until an outcome is reached (e.g. childbirth contractions)",
    ), Explanation=""))
rows.append(dict(Topic="Thermoregulation", Question="How do organisms gain and lose heat?",
    Answer_Summary=lettered(
        "gain heat: through metabolism, absorbing sunlight, and conduction from warmer surroundings",
        "lose heat: through sweating (evaporation), radiation, convection, and conduction to cooler surroundings",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Mendelian)", Question="State Mendel's first law of inheritance.",
    Answer_Summary=lettered("law of segregation: alleles for each gene separate during gamete formation, so each gamete carries only one allele per gene"), Explanation=""))
rows.append(dict(Topic="Selective Breeding", Question="What is meant by selective breeding?",
    Answer_Summary=lettered("intentionally breeding plants/animals with desirable traits so offspring inherit those traits"), Explanation=""))
rows.append(dict(Topic="Evolution", Question="How do homologous and vestigial structures support the theory of evolution?",
    Answer_Summary=lettered(
        "homologous structures: similar structure but different function across species (e.g. forelimbs of humans, bats, whales), suggesting common ancestry",
        "vestigial structures: parts that lost their original function but still exist (e.g. human appendix, whale pelvic bones), showing evolutionary change",
    ), Explanation=""))
rows.append(dict(Topic="Ecology (Succession)", Question="Define ecological succession.",
    Answer_Summary=lettered("the gradual process where ecosystems change over time as one community replaces another, ending in a stable climax community"), Explanation=""))
rows.append(dict(Topic="Ecology (Pyramids)", Question="What are the merits and demerits of a pyramid of numbers versus a pyramid of biomass?",
    Answer_Summary=lettered(
        "numbers - merit: simple to build and read, gives a quick population estimate",
        "numbers - demerit: ignores organism size, which can distort the picture and misrepresent energy flow",
        "biomass - merit: more accurately reflects energy flow, accounts for actual mass at each level",
        "biomass - demerit: hard to measure precisely (especially in water), and biomass can fluctuate over time",
    ), Explanation=""))
rows.append(dict(Topic="Biomolecules (Proteins)", Question="Describe the structure of a typical amino acid.",
    Answer_Summary=lettered("a central alpha carbon bonded to an amino group (-NH2), a carboxyl group (-COOH), a hydrogen atom, and a variable R-group"), Explanation=""))
rows.append(dict(Topic="Biomolecules (Proteins)", Question="How are two amino acids joined to form a dipeptide?",
    Answer_Summary=lettered(
        "the amino group of one reacts with the carboxyl group of the other",
        "forms a peptide bond and releases a water molecule",
    ), Explanation=""))
rows.append(dict(Topic="Evolution (Lamarck)", Question="What were Lamarck's useful contributions to the study of evolution?",
    Answer_Summary=lettered(
        "proposed inheritance of acquired characteristics",
        "emphasized that organisms adapt via use and disuse of organs, driving evolutionary change",
    ), Explanation=""))
rows.append(dict(Topic="Evolution (Weismann)", Question="What did Weismann conclude from his experiment of cutting mice tails over many generations?",
    Answer_Summary=lettered(
        "acquired traits (like a cut tail) are not inherited",
        "changes to the body during an organism's life don't alter its genetic material or pass to offspring",
    ), Explanation=""))
rows.append(dict(Topic="Plant Hormones", Question="What is the site of synthesis and what are three functions each of auxins and ethene?",
    Answer_Summary=lettered(
        "auxins: made in shoot apical meristems; promote cell elongation, regulate phototropism/gravitropism, inhibit abscission",
        "ethene: made in ripening fruit; promotes fruit ripening, stimulates leaf abscission, induces flowering in some plants",
    ), Explanation=""))
rows.append(dict(Topic="Plant Movements", Question="Compare tropisms, taxes, and nastic movements in plants.",
    Answer_Summary=lettered(
        "tropisms: directional growth response to a stimulus like light or gravity",
        "taxes: directional movement of a whole organism toward/away from a stimulus (e.g. phototaxis in algae)",
        "nastic movements: non-directional response to a stimulus (e.g. Mimosa leaves closing when touched)",
    ), Explanation=""))
rows.append(dict(Topic="Respiration", Question="Summarize the essential features of glycolysis and the electron transport chain in releasing energy from glucose.",
    Answer_Summary=lettered(
        "glycolysis occurs in the cytoplasm",
        "glycolysis breaks one glucose into two pyruvate molecules",
        "glycolysis produces 2 ATP and 2 NADH",
        "electron transport occurs on the inner mitochondrial membrane",
        "electron transport: electrons from NADH/FADH2 pass through the chain, building a proton gradient",
        "electron transport drives synthesis of about 32-34 ATP",
    ), Explanation=""))
rows.append(dict(Topic="Respiratory Pigments (Bohr Effect)", Question="How does hemoglobin's oxygen loading/unloading change with rising carbon dioxide levels, and what is this phenomenon called?",
    Answer_Summary=lettered(
        "oxygen unloading from hemoglobin increases as CO2 partial pressure rises; loading decreases",
        "this is called the Bohr effect",
        "caused by rising CO2 lowering blood pH, which reduces hemoglobin's oxygen affinity",
        "advantage: ensures efficient oxygen delivery to tissues with high metabolic activity, where CO2 is high and oxygen is most needed",
    ), Explanation=""))
rows.append(dict(Topic="Excretory System (Kidney)", Question="Why is glucose in the glomerular filtrate not normally found in urine?",
    Answer_Summary=lettered(
        "glucose is reabsorbed in the proximal convoluted tubule by active transport via carrier proteins",
        "if blood glucose exceeds the renal threshold (e.g. in diabetes), some isn't reabsorbed and appears in urine",
    ), Explanation=""))
rows.append(dict(Topic="Blood Functions", Question="State four functions of mammalian blood related to transport and defense.",
    Answer_Summary=lettered(
        "transports oxygen to tissues and CO2 to the lungs",
        "transports nutrients (glucose, amino acids, vitamins) to cells",
        "transports waste (e.g. urea) to excretory organs",
        "defends against infection via white blood cells, antibodies, and clotting",
    ), Explanation=""))
rows.append(dict(Topic="Growth", Question="What do you understand by the term growth?",
    Answer_Summary=lettered(
        "an irreversible increase in size, mass or cell number",
        "involves cell division, enlargement and differentiation",
    ), Explanation=""))
rows.append(dict(Topic="Growth Patterns", Question="In mice, when do young mice grow fastest, and how do the sexes compare in growth rate?",
    Answer_Summary=lettered(
        "mice grow fastest in the earlier weeks of life, then the growth rate slows",
        "tail growth rate is generally proportional to body growth rate, though slower",
        "in many rodents, males tend to grow faster/larger than females",
    ), Explanation=""))
rows.append(dict(Topic="Insect Metamorphosis", Question="Distinguish complete metamorphosis from incomplete metamorphosis.",
    Answer_Summary=lettered(
        "complete: 4 stages (egg, larva, pupa, adult); the larva looks completely different from the adult, e.g. butterfly",
        "incomplete: 3 stages (egg, nymph, adult); the nymph resembles the adult but lacks full features like wings, e.g. grasshopper",
    ), Explanation=""))
rows.append(dict(Topic="Insect Metamorphosis", Question="Explain the hormonal control of metamorphosis (molting) in insects.",
    Answer_Summary=lettered(
        "ecdysone (from the prothoracic gland) triggers molting, shedding the old exoskeleton for a new one",
        "juvenile hormone (from the corpora allata) determines the nature of the molt - high levels keep it juvenile, low levels let it advance to pupa/adult",
        "the interaction of these two hormones times and controls metamorphosis correctly",
    ), Explanation=""))

# ============================== YEAR 2007 ==============================
rows.append(dict(Topic="Cell Organelles", Question="Give two functions of each of the following cellular organelles: nucleus, endoplasmic reticulum, Golgi apparatus, lysosomes.",
    Answer_Summary=lettered(
        "nucleus: stores DNA and regulates gene expression; controls cell activities (growth, metabolism, reproduction)",
        "endoplasmic reticulum: rough ER synthesizes/transports proteins; smooth ER synthesizes lipids and detoxifies substances",
        "Golgi apparatus: modifies/sorts/packages proteins and lipids; produces lysosomes and vesicles",
        "lysosomes: break down waste and cellular debris; digest damaged organelles (autophagy)",
    ), Explanation=""))
rows.append(dict(Topic="Cell Organelles", Question="What advantages does a eukaryotic cell gain from having internal membrane-bound organelles?",
    Answer_Summary=lettered(
        "compartmentalization separates cellular processes, boosting efficiency",
        "gives specific environments for specialized reactions (e.g. acidic lysosomes)",
        "allows storage and transport of molecules in vesicles",
        "enables better regulation and coordination of cell functions",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Protista)", Question="Why are Entamoeba, Euglena, Spirogyra, and Phytophthora all placed in kingdom Protista despite their differences?",
    Answer_Summary=lettered(
        "all are unicellular or simple multicellular eukaryotes",
        "show diverse nutrition modes (autotrophic, heterotrophic, or mixotrophic)",
        "don't fit neatly into Plantae, Animalia, or Fungi (e.g. Euglena is photosynthetic but motile)",
    ), Explanation=""))
rows.append(dict(Topic="Fungi", Question="How is Agaricus (mushroom) adapted to its mode of life?",
    Answer_Summary=lettered(
        "mycelium grows in soil to absorb nutrients",
        "fruiting body is adapted for spore dispersal",
        "produces enzymes to break down organic matter for nutrition",
        "thrives in moist environments",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis", Question="In respiration and photosynthesis pathways, what process converts glucose to pyruvate, what does RuBP do in the Calvin cycle, and where in the chloroplast is glycerate-3-phosphate converted back to RuBP?",
    Answer_Summary=lettered(
        "glucose to pyruvate: glycolysis",
        "RuBP: acts as the CO2 acceptor in the Calvin cycle, fixing CO2 into 3-phosphoglycerate",
        "glycerate-3-phosphate is converted back to RuBP in the chloroplast's stroma",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System", Question="Distinguish between: action potential and generator potential; conduction and transduction of nerve impulses; synapses and synapsis; rods and cones.",
    Answer_Summary=lettered(
        "action potential: a rapid electrical signal once threshold is reached; generator potential: a graded response that may trigger an action potential",
        "conduction: transmitting an electrical signal along a neuron; transduction: converting a stimulus into an electrical signal at a receptor",
        "synapses: junctions between neurons for signal transmission; synapsis: pairing of homologous chromosomes in meiosis",
        "rods: photoreceptors for low light, black-and-white vision; cones: detect color, work in bright light",
    ), Explanation=""))
rows.append(dict(Topic="Homeostasis", Question="State the components of homeostatic mechanisms.",
    Answer_Summary=lettered(
        "receptors: detect changes (stimuli) and signal the control center",
        "control center: processes information and coordinates a response (e.g. brain, endocrine glands)",
        "effectors: organs/tissues that carry out the response to restore balance",
    ), Explanation=""))
rows.append(dict(Topic="Thermoregulation", Question="Why does a man's body temperature stay fairly constant on a hot day while a nearby rock heats up to about 50 degrees Celsius?",
    Answer_Summary=lettered(
        "the body regulates temperature via sweating, vasodilation and radiating heat",
        "the rock has no biological regulation - it just absorbs and stores solar heat with no way to cool itself",
    ), Explanation=""))
rows.append(dict(Topic="Cell Transport", Question="Distinguish between passive and active transport of materials in the body.",
    Answer_Summary=lettered(
        "passive: moves molecules down the concentration gradient with no energy needed (diffusion, osmosis, facilitated diffusion)",
        "active: uses ATP to move molecules against the gradient, via protein pumps (e.g. mineral uptake in roots, sodium-potassium exchange in nerves)",
    ), Explanation=""))
rows.append(dict(Topic="Plant Water Transport", Question="Explain how water travels from the soil to a leaf vein.",
    Answer_Summary=lettered(
        "root hairs absorb water from soil by osmosis",
        "water moves through the cortex via apoplastic or symplastic pathways to the endodermis",
        "the Casparian strip forces water into the xylem",
        "transpiration pull (from stomatal evaporation) is the main force drawing water up, aided by cohesion and adhesion",
    ), Explanation=""))
rows.append(dict(Topic="Seed Germination", Question="Why are oxygen and water required for seed germination?",
    Answer_Summary=lettered(
        "oxygen: needed for aerobic respiration, providing ATP for enzyme activity, cell division and growth",
        "water: breaks seed dormancy, softens the seed coat, activates enzymes, and dissolves/transports stored nutrients",
    ), Explanation=""))
rows.append(dict(Topic="Seed Structure", Question="State two differences between endospermic and non-endospermic seeds.",
    Answer_Summary=lettered(
        "endospermic seeds keep the endosperm as food storage (e.g. maize); non-endospermic seeds absorb the endosperm into the cotyledons before germinating (e.g. beans)",
        "endospermic seeds have small cotyledons; non-endospermic seeds have large cotyledons since they store the food there",
    ), Explanation=""))
rows.append(dict(Topic="Growth", Question="Define growth as applied to multicellular organisms.",
    Answer_Summary=lettered("an irreversible increase in size and mass from cell division and enlargement, developing tissues/organs over time"), Explanation=""))
rows.append(dict(Topic="Growth Measurement", Question="What are the advantages and disadvantages of using fresh mass versus dry mass to measure growth?",
    Answer_Summary=lettered(
        "fresh mass: easy and quick to measure, but fluctuates with water content",
        "dry mass: gives an accurate measure of organic material, but requires drying (often killing) the organism, making repeat measurements impractical",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Mutation)", Question="Define mutation.",
    Answer_Summary=lettered("a permanent change in a gene's or chromosome's DNA sequence, which can be beneficial, harmful, or neutral"), Explanation=""))
rows.append(dict(Topic="Genetics (Mutation)", Question="Why do harmful recessive mutations persist across generations more than harmful dominant ones?",
    Answer_Summary=lettered(
        "recessive mutations stay hidden in heterozygous carriers (Aa) and don't harm survival unless inherited from both parents",
        "dominant mutations show up in heterozygotes too, so they're selected against and removed from the gene pool faster",
    ), Explanation=""))
rows.append(dict(Topic="Selective Breeding", Question="What is meant by artificial selection?",
    Answer_Summary=lettered("humans selectively breed organisms with desirable traits to improve things like yield, disease resistance or growth rate"), Explanation=""))
rows.append(dict(Topic="Speciation", Question="What are the differences between allopatric and sympatric speciation?",
    Answer_Summary=lettered(
        "allopatric: driven by physical barriers (mountains, rivers) separating populations; sympatric: no geographic barrier, driven by mutation or ecological differences",
        "allopatric prevents gene flow between the separated groups; sympatric lets populations coexist but evolve separately under different pressures",
        "example: Darwin's finches (allopatric); polyploidy in plants (sympatric)",
    ), Explanation=""))
rows.append(dict(Topic="Enzymes", Question="State the properties of enzymes.",
    Answer_Summary=lettered(
        "specificity: each enzyme acts on one substrate/reaction via its unique active site",
        "catalytic: speeds up reactions without being consumed",
        "reversibility: some enzyme reactions can run both ways",
        "temperature sensitivity: works best at an optimum temperature, denatures if too hot",
        "pH sensitivity: works only within a specific pH range",
        "inhibition: activity can be reduced by competitive or non-competitive inhibitors",
        "lowers the activation energy needed for a reaction",
    ), Explanation=""))
rows.append(dict(Topic="Enzymes", Question="What shape do reaction-rate curves take when investigating enzyme activity with a fixed enzyme quantity versus excess substrate?",
    Answer_Summary=lettered(
        "fixed enzyme, rising substrate: rate increases then plateaus once all active sites are occupied",
        "excess substrate, rising enzyme: rate keeps increasing as more enzyme is added, since substrate is not limiting",
    ), Explanation=""))
rows.append(dict(Topic="Biomolecules (Lipids)", Question="Describe the roles of lipids in living organisms.",
    Answer_Summary=lettered(
        "energy storage - a concentrated, long-term energy reserve",
        "structural - phospholipids form the cell membrane bilayer",
        "insulation - reduce heat loss in mammals",
        "protection - cushion delicate organs like kidneys and heart",
        "hormone production - some lipids (e.g. cholesterol) are precursors for steroid hormones",
        "waterproofing - waxes prevent water loss in plants and animals",
        "buoyancy - help aquatic animals like whales float",
    ), Explanation=""))
rows.append(dict(Topic="Human Eye", Question="Why can't humans see clearly at night while cats and owls can?",
    Answer_Summary=lettered(
        "human vision is cone-dominated, good in bright light but poor in dim light",
        "night vision relies on rod cells, which are more light-sensitive but don't detect color well",
        "cats/owls have more rod cells, a reflective tapetum lucidum that amplifies low light, and pupils that open wider",
    ), Explanation=""))
rows.append(dict(Topic="Plant Hormones", Question="What is the importance of natural and synthetic phytohormones in crop production?",
    Answer_Summary=lettered(
        "gibberellins break seed dormancy for faster germination",
        "auxins encourage root formation, useful for vegetative propagation",
        "cytokinins and gibberellins help control flowering and fruit size",
        "ethylene regulates fruit ripening (can be delayed or hastened)",
        "synthetic auxins act as selective herbicides against weeds",
        "auxins and cytokinins support tissue culture and cloning (micropropagation)",
    ), Explanation=""))
rows.append(dict(Topic="Gas Transport in Blood", Question="Discuss how oxygen and carbon dioxide are transported in a mammalian body.",
    Answer_Summary=lettered(
        "oxygen binds to hemoglobin in red blood cells to form oxyhemoglobin, releasing it in tissues due to lower oxygen and higher CO2",
        "about 70% of CO2 is converted to carbonic acid, which dissociates into bicarbonate ions carried in plasma",
        "about 20% of CO2 binds hemoglobin to form carbaminohemoglobin",
        "about 10% of CO2 is dissolved directly in blood plasma",
        "at the lungs, CO2 is released from hemoglobin/bicarbonate, diffuses into alveoli, and is exhaled",
    ), Explanation=""))
rows.append(dict(Topic="Reproductive Strategies", Question="Why do animals with external fertilization lay many more eggs than those with internal fertilization?",
    Answer_Summary=lettered(
        "external fertilization exposes eggs to predation and environmental hazards, so many eggs compensate for high losses",
        "internal fertilization protects the fertilized egg inside the body, so fewer eggs are needed",
    ), Explanation=""))
rows.append(dict(Topic="Reproductive Hormones", Question="What hormonal changes trigger ovulation and cause the corpus luteum to degenerate?",
    Answer_Summary=lettered(
        "ovulation: a surge in luteinizing hormone (LH) triggers the mature follicle to rupture and release an egg",
        "corpus luteum degeneration: without fertilization, LH support drops, progesterone falls, and the corpus luteum shrinks, triggering menstruation",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Sex-Linked Inheritance)", Question="Why are there more colorblind individuals than hemophiliacs, even though both are sex-linked in the same way?",
    Answer_Summary=lettered(
        "colorblindness-causing mutations occur more frequently than hemophilia-causing ones",
        "hemophilia causes more severe health complications, reducing survival/reproduction and its frequency",
        "colorblindness has little effect on survival, so it persists at a higher frequency",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Sex-Linked Crosses)", Question="In flies where eye color is sex-linked and red is dominant over white, what are the phenotypes/genotypes of F1 and F2 offspring from a white-eyed female (XaXa) crossed with a white-eyed male (XaY)?",
    Answer_Summary=lettered(
        "F1: all offspring are white-eyed - females XaXa, males XaY",
        "F2 (from an F1 x F1 cross): also all white-eyed - females XaXa, males XaY",
        "since both parents only carry the white allele, no red-eyed offspring are possible in either generation",
    ), Explanation=""))

# ============================== YEAR 2008 ==============================
rows.append(dict(Topic="Biomolecules (Amino Acids)", Question="What is the general name of an amino acid's structural formula, what is the simplest R group, and which parts give it acidic and basic properties?",
    Answer_Summary=lettered(
        "general structure: an amino acid",
        "simplest R group: hydrogen (making glycine)",
        "acidic properties come from the carboxyl group (-COOH)",
        "basic properties come from the amino group (-NH2)",
    ), Explanation=""))
rows.append(dict(Topic="Biomolecules (Amino Acids)", Question="What compound forms when two amino acids join, and what is the bond called?",
    Answer_Summary=lettered(
        "forms a dipeptide via a condensation reaction",
        "the bond formed is called a peptide bond",
    ), Explanation=""))
rows.append(dict(Topic="Skeletal Systems", Question="What are the differences between the skeleton of arthropods and that of a mammal?",
    Answer_Summary=lettered(
        "arthropods have a chitin exoskeleton; mammals have an internal bone/cartilage endoskeleton",
        "the exoskeleton limits growth (needs molting); the endoskeleton supports growth without molting",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Vertebrates)", Question="What characteristic features do fish and mammals have in common?",
    Answer_Summary=lettered(
        "both have a vertebral column",
        "both have a closed circulatory system with a heart",
    ), Explanation=""))
rows.append(dict(Topic="Synthetic Hormones", Question="Giving examples, how are synthetic hormones used in animal husbandry, crop production, and improving livelihoods?",
    Answer_Summary=lettered(
        "animal husbandry: oxytocin boosts milk production and stimulates ovulation in dairy animals",
        "crop production: gibberellins promote stem elongation, delay fruit aging, and boost germination",
        "livelihoods: higher agricultural/livestock productivity from hormone use raises income and food security",
    ), Explanation=""))
rows.append(dict(Topic="Meiosis", Question="During meiosis, what happens to the amount of DNA per cell across its phases, and what type of cells result?",
    Answer_Summary=lettered(
        "DNA replicates during the S-phase of interphase",
        "meiosis I (reduction division) halves the DNA content as homologous chromosomes separate",
        "meiosis II separates sister chromatids",
        "the final products are haploid gametes",
    ), Explanation=""))
rows.append(dict(Topic="Decomposers and Nutrient Cycling", Question="What would happen if detritus feeders and decomposers disappeared from the earth?",
    Answer_Summary=lettered(
        "organic waste and dead organisms would pile up, causing pollution",
        "nutrient recycling would stop, harming soil fertility and plant growth",
        "energy flow through ecosystems would break down, collapsing food chains",
        "carbon and nitrogen cycles would be disrupted",
        "microorganisms depending on decomposition would lose their habitat",
        "overall ecosystem function would degrade severely",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis", Question="Why are the reaction centers of photosystem I and II called P700 and P680?",
    Answer_Summary=lettered("named for their peak light-absorption wavelength - 700 nm for photosystem I, 680 nm for photosystem II"), Explanation=""))
rows.append(dict(Topic="Photosynthesis", Question="Compare cyclic and non-cyclic photophosphorylation.",
    Answer_Summary=lettered(
        "cyclic: electrons return to the same chlorophyll molecule; non-cyclic: electrons pass to NADP+ to form NADPH",
        "cyclic produces only ATP; non-cyclic produces both ATP and NADPH",
        "cyclic uses only photosystem I; non-cyclic uses both photosystem I and II",
        "non-cyclic causes photolysis of water, releasing oxygen; cyclic doesn't",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System", Question="What does it mean that a nerve impulse obeys the \"all-or-nothing\" principle?",
    Answer_Summary=lettered("an impulse either fires fully once the stimulus reaches threshold, or doesn't fire at all"), Explanation=""))
rows.append(dict(Topic="Plant Hormones", Question="What is meant by antagonism and synergism between plant growth substances?",
    Answer_Summary=lettered(
        "antagonism: one hormone counteracts another, e.g. auxins inhibiting cytokinin-driven cell division",
        "synergism: two hormones work together to boost a response, e.g. auxins and gibberellins both promoting stem elongation",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Placenta)", Question="Outline the transport mechanisms exchanging substances between mother and fetus.",
    Answer_Summary=lettered(
        "the placenta lets oxygen and nutrients diffuse from maternal to fetal blood",
        "fetal waste (CO2, urea) diffuses back into maternal blood",
        "active transport moves ions like calcium and iron to the fetus",
        "facilitated diffusion (via carrier proteins) moves glucose to the fetus",
    ), Explanation=""))
rows.append(dict(Topic="Circulatory Systems", Question="Using examples, explain two advantages of a closed double circulatory system.",
    Answer_Summary=lettered(
        "blood pumped at high pressure delivers oxygen to tissues quickly and efficiently, as in mammals",
        "oxygenated and deoxygenated blood stay separate, so the heart sends oxygen-rich blood to tissues and oxygen-poor blood to the lungs, improving efficiency",
    ), Explanation=""))
rows.append(dict(Topic="Metabolism and Body Size", Question="Why do small and large mammals differ so much in daily energy requirements on a weight-for-weight basis?",
    Answer_Summary=lettered(
        "smaller mammals (e.g. mice) have a larger surface-area-to-volume ratio, losing heat faster",
        "this forces a higher metabolic rate/energy use to maintain body temperature",
        "larger mammals (e.g. humans) have a smaller surface-area-to-volume ratio, losing less heat, so need less energy per unit weight",
    ), Explanation=""))
rows.append(dict(Topic="Thermoregulation", Question="Differentiate between endothermic and ectothermic organisms, with examples.",
    Answer_Summary=lettered(
        "endothermic: regulate body temperature internally via metabolism, e.g. mammals and birds",
        "ectothermic: rely on the environment to regulate temperature, e.g. reptiles and amphibians basking or seeking shade",
    ), Explanation=""))
rows.append(dict(Topic="Plant Growth (Meristems)", Question="Define the term meristem.",
    Answer_Summary=lettered("a region of actively dividing, undifferentiated cells responsible for plant growth"), Explanation=""))
rows.append(dict(Topic="Plant Growth (Meristems)", Question="Write short notes on lateral meristems (location, role, effect).",
    Answer_Summary=lettered(
        "located along the sides of stems and roots, mainly in woody plants",
        "made of the vascular cambium (produces xylem/phloem for secondary growth) and cork cambium (produces protective bark)",
        "their activity widens plant structures, supporting bigger plants and more water/nutrient flow",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Blood Groups)", Question="If the father is blood group A and the mother blood group B, what blood groups are possible in their children?",
    Answer_Summary=lettered(
        "father's genotype: IAIA or IAi; mother's genotype: IBIB or IBi",
        "possible combinations: IAIB (AB), IAi (A), IBi (B), ii (O)",
        "so children could have blood group A, B, AB, or O",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Probability)", Question="If these parents have non-identical twins, what's the probability both twins have blood group A?",
    Answer_Summary=lettered(
        "probability of one child being blood group A is 25%",
        "for two independent children: 0.25 x 0.25 = 6.25%",
    ), Explanation=""))
rows.append(dict(Topic="Nervous vs Endocrine Coordination", Question="Write three differences between nervous and endocrine coordination.",
    Answer_Summary=lettered(
        "nervous: electrical impulses via neurons; endocrine: hormones via the bloodstream",
        "nervous responses are fast and short-lived; endocrine responses are slower but longer-lasting",
        "nervous coordination targets specific cells; endocrine coordination affects tissues more broadly",
    ), Explanation=""))
rows.append(dict(Topic="Human Ear", Question="How does the eustachian tube work, and why does pressure change cause ear discomfort during flights or deep diving?",
    Answer_Summary=lettered(
        "the eustachian tube connects the middle ear to the nasopharynx, equalizing pressure on both sides of the eardrum",
        "rapid altitude/depth changes shift outside pressure faster than the tube can equalize it, causing pain, discomfort or temporary hearing loss",
    ), Explanation=""))
rows.append(dict(Topic="Plant Movements", Question="What are tactic movements and nastic movements?",
    Answer_Summary=lettered(
        "tactic movements: directional response to a stimulus like light or chemicals, e.g. phototaxis in algae",
        "nastic movements: non-directional response depending on stimulus intensity, e.g. Mimosa leaves closing when touched",
    ), Explanation=""))
rows.append(dict(Topic="Plant Movements", Question="Give examples of tactic and nastic movements, and how phototropism occurs, in plants.",
    Answer_Summary=lettered(
        "tactic: positive phototaxis moves algae toward light for photosynthesis",
        "nastic: thigmonasty closes Mimosa pudica leaves on touch via rapid loss of turgor pressure",
        "phototropism: plant stems bend toward light due to unequal cell elongation driven by auxins",
    ), Explanation=""))
rows.append(dict(Topic="Plant Vascular Tissues", Question="Identify the vascular tissues in plants and explain how each is adapted to its function.",
    Answer_Summary=lettered(
        "xylem transports water and minerals from roots upward",
        "xylem's hollow, lignified tubes reduce flow resistance and give structural support; pits allow sideways water movement",
        "phloem transports sugars from leaves to the rest of the plant",
        "phloem's sieve plates let nutrients flow, while companion cells provide ATP and metabolic support",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Terminology)", Question="Define gene, genotype, and phenotype.",
    Answer_Summary=lettered(
        "gene: a DNA segment encoding a specific protein or functional RNA, the basic unit of heredity",
        "genotype: an organism's genetic makeup (e.g. IAIA or IAi for blood group)",
        "phenotype: the observable trait resulting from genotype and environment (e.g. blood group A, B, AB, O)",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Mendelian Crosses)", Question="Both parents have wrinkled hair, but one child has straight hair. How can this be explained genetically?",
    Answer_Summary=lettered(
        "both parents must be heterozygous (Ww) for the trait",
        "a Ww x Ww cross gives 25% WW, 50% Ww (wrinkled), and 25% ww (straight)",
        "so it's genetically possible for a child to have straight hair (ww) if they inherit the recessive w allele from both parents",
    ), Explanation=""))

# ============================== YEAR 2009 ==============================
rows.append(dict(Topic="Classification (Taxonomic Keys)", Question="Define a taxonomic key.",
    Answer_Summary=lettered("a tool that identifies/classifies organisms via a series of statements or questions leading to species identification"), Explanation=""))
rows.append(dict(Topic="Classification (Scientific Naming)", Question="In what ways is scientific naming of organisms important?",
    Answer_Summary=lettered(
        "universal communication - recognized globally, avoiding confusion from local names",
        "reflects evolutionary relationships (phylogeny)",
        "gives a consistent, standard way to identify and categorize organisms",
        "supports research and conservation efforts",
        "avoids redundancy - prevents multiple names for the same organism",
    ), Explanation=""))
rows.append(dict(Topic="Classification", Question="What is the significance of classifying organisms?",
    Answer_Summary=lettered("organizes and simplifies the vast diversity of life, aiding study, comparison, and understanding evolutionary relationships"), Explanation=""))
rows.append(dict(Topic="Classification (Common Names)", Question="What are the merits and demerits of using a common name to identify an organism?",
    Answer_Summary=lettered(
        "merit: common names are familiar, easy to remember and often descriptive",
        "merit: locally relevant to a region or language",
        "demerit: not standardized - the same species can have different names in different places",
        "demerit: ambiguous - different species can share the same common name",
        "demerit: gives no evolutionary information",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis", Question="What are the roles of ribulose diphosphate (RuBP) and NADP in photosynthesis?",
    Answer_Summary=lettered(
        "RuBP: a 5-carbon sugar that accepts CO2 in the Calvin cycle, forming two molecules of 3-phosphoglycerate",
        "NADP: an electron carrier reduced to NADPH in the light reactions, used to fix carbon in the Calvin cycle",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis (C3 vs C4)", Question="Why is photorespiration more common in C3 plants, and why are C4 plants more efficient at photosynthesis?",
    Answer_Summary=lettered(
        "C3 plants lack a CO2-concentrating mechanism, so RuBisCO oxygenates RuBP under heat or low CO2",
        "C4 plants have a CO2-concentrating mechanism that minimizes photorespiration, letting them thrive in hot, dry conditions",
    ), Explanation=""))
rows.append(dict(Topic="Respiration", Question="How does the electron transport chain release ATP?",
    Answer_Summary=lettered(
        "builds a proton gradient across the inner mitochondrial membrane",
        "protons flow back through ATP synthase, which makes ATP from ADP and phosphate",
    ), Explanation=""))
rows.append(dict(Topic="Respiration", Question="Why is the electron transport chain important in living organisms?",
    Answer_Summary=lettered(
        "it's the main source of ATP in aerobic organisms",
        "it powers metabolic processes like synthesis and active transport",
    ), Explanation=""))
rows.append(dict(Topic="Thermoregulation", Question="What roles does the mammalian hypothalamus play in temperature regulation?",
    Answer_Summary=lettered(
        "detects temperature changes via thermoreceptors",
        "triggers responses like sweating or shivering to restore balance",
        "regulates hormones (e.g. thyroxine) that control metabolic heat production",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Terminology)", Question="Define genotype, phenotype, homozygous, and heterozygous.",
    Answer_Summary=lettered(
        "genotype: an organism's genetic makeup (its inherited alleles)",
        "phenotype: the observable traits, shaped by genotype and environment",
        "homozygous: two identical alleles for a gene",
        "heterozygous: two different alleles for a gene",
    ), Explanation=""))
rows.append(dict(Topic="Natural Selection", Question="Explain natural selection using the example of the peppered moth.",
    Answer_Summary=lettered(
        "before industrialization, light moths were common, camouflaged against lichen-covered trees",
        "soot from industrialization darkened tree trunks, favoring dark moths, which were now better camouflaged",
        "over time, dark moths became more frequent - an environmental change driving natural selection",
    ), Explanation=""))
rows.append(dict(Topic="Natural Selection", Question="Explain natural selection using the example of bacterial antibiotic resistance.",
    Answer_Summary=lettered(
        "an antibiotic kills most bacteria, but those with resistance mutations survive",
        "resistant bacteria reproduce and come to dominate the population over generations",
        "this makes the antibiotic ineffective, showing selective pressure driving evolution of resistance",
    ), Explanation=""))
rows.append(dict(Topic="Ecology", Question="Explain ecological succession and ecological niche.",
    Answer_Summary=lettered(
        "succession: the gradual change in an ecosystem's species over time, from pioneer species to a stable climax community",
        "niche: the role/position a species occupies in its ecosystem, including its habitat, diet and behavior",
    ), Explanation=""))
rows.append(dict(Topic="Environmental Pollution", Question="What damage can result from smoke and fumes being absorbed into rainwater?",
    Answer_Summary=lettered(
        "forms acid rain: sulfur dioxide/nitrogen oxides react with water vapor to form acidic compounds",
        "degrades soil: lowers soil pH, harming plant growth and farm productivity",
        "pollutes water: contaminates water bodies, harming aquatic life",
        "damages structures: corrodes buildings, monuments and infrastructure",
        "affects human health: can worsen respiratory diseases",
    ), Explanation=""))
rows.append(dict(Topic="DNA and RNA Structure", Question="What are the components of a DNA nucleotide (phosphate group, sugar, base, hydrogen bonds), and how does DNA structure compare to RNA?",
    Answer_Summary=lettered(
        "a DNA nucleotide is made of a phosphate group, a deoxyribose sugar, and a nitrogenous base (e.g. adenine or thymine), joined by hydrogen bonds",
        "sugars: DNA has deoxyribose; RNA has ribose",
        "bases: DNA has thymine; RNA has uracil instead",
        "strands: DNA is double-stranded; RNA is single-stranded",
        "shape: DNA forms a double helix; RNA is usually linear or forms simpler secondary structures",
    ), Explanation=""))
rows.append(dict(Topic="Speciation", Question="Define speciation.",
    Answer_Summary=lettered("the evolutionary process where populations of one species diverge into distinct species through genetic isolation and evolutionary pressure"), Explanation=""))
rows.append(dict(Topic="Speciation", Question="How can geographical isolation bring about speciation?",
    Answer_Summary=lettered(
        "isolation stops interbreeding between separated populations",
        "genetic differences build up via mutation, natural selection, and genetic drift",
        "eventually this leads to reproductive isolation and new species forming",
    ), Explanation=""))
rows.append(dict(Topic="Plant Hormones (Phototropism)", Question="In a phototropism experiment, mica pieces are inserted into coleoptile tips in different positions. Using auxin theory, what results would you expect?",
    Answer_Summary=lettered(
        "if auxin is spread evenly, growth is uniform and the tip doesn't bend",
        "if a mica block fully blocks auxin flow, no bending occurs since auxin can't reach the elongation zone",
        "if auxin can only accumulate on the shaded side, that side elongates more, bending the tip toward the light",
    ), Explanation=""))
rows.append(dict(Topic="ATP", Question="What is ATP?",
    Answer_Summary=lettered(
        "adenosine triphosphate - the cell's energy currency, made of adenine, ribose and three phosphate groups",
        "stores and transfers energy for cellular processes",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Lipids and Proteins)", Question="Outline how the respiratory pathway processes lipid and protein substrates.",
    Answer_Summary=lettered(
        "lipids break into glycerol and fatty acids - glycerol enters glycolysis, fatty acids undergo beta-oxidation to acetyl-CoA for the Krebs cycle",
        "proteins break into amino acids - deaminated amino acids enter glycolysis or the Krebs cycle as intermediates",
    ), Explanation=""))
rows.append(dict(Topic="Plant Transport (Phloem)", Question="How is phloem tissue adapted for transporting materials?",
    Answer_Summary=lettered(
        "sieve tube elements have perforated sieve plates for sap to flow through",
        "companion cells give metabolic support",
        "plasmodesmata connect cells for efficient transfer",
    ), Explanation=""))
rows.append(dict(Topic="Plant Transport (Roots)", Question="What is the function and location of the Casparian strip?",
    Answer_Summary=lettered(
        "located in the endodermis of roots",
        "forces selective mineral uptake by blocking passive flow through the apoplast pathway",
    ), Explanation=""))
rows.append(dict(Topic="Insect Metamorphosis", Question="Define metamorphosis and give its significance.",
    Answer_Summary=lettered(
        "metamorphosis: major physical changes in structure/function during development, e.g. larva to adult",
        "lets life stages specialize for different functions (e.g. feeding vs reproduction)",
        "reduces competition for resources between larval and adult stages",
    ), Explanation=""))
rows.append(dict(Topic="Metabolism and Body Size", Question="Why do small mammals have a higher metabolic rate than large ones?",
    Answer_Summary=lettered(
        "small mammals lose heat faster due to a larger surface-area-to-volume ratio",
        "they need a higher metabolic rate to generate enough heat to maintain body temperature",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Female System)", Question="What are the main parts of the female reproductive system and their functions?",
    Answer_Summary=lettered(
        "ovary: produces eggs and hormones",
        "fallopian tube: carries eggs from ovary to uterus",
        "uterus: supports fetal development",
        "cervix: connects uterus to vagina, acting as a barrier",
        "vagina: passageway for childbirth and intercourse",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Male System)", Question="What are the main parts of the male reproductive system and their functions?",
    Answer_Summary=lettered(
        "testis: produces sperm and testosterone",
        "epididymis: stores and matures sperm",
        "vas deferens: transports sperm",
        "prostate gland: produces seminal fluid",
        "penis: delivers sperm during intercourse",
    ), Explanation=""))

# ============================== YEAR 2011 ==============================
# Note: skipped 1(b) (a drawing task) and 2(b) (identifying plant species
# from an unseen key/diagram - the identities are arbitrary without it).
rows.append(dict(Topic="Cell Structure (Size)", Question="Why is it advantageous for cells to be small?",
    Answer_Summary=lettered(
        "higher surface-area-to-volume ratio for efficient exchange",
        "enables faster diffusion of oxygen, nutrients and waste",
        "supports better intracellular transport and communication",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Monocots)", Question="State one characteristic each of leaf morphology, stem anatomy, seed morphology, flowers, and root morphology of a wheat plant, as an example of a monocot.",
    Answer_Summary=lettered(
        "leaves: narrow with parallel veins",
        "stem: hollow and cylindrical, with scattered vascular bundles",
        "seeds: monocotyledonous, single cotyledon",
        "flowers: small, usually lacking sepals/petals, wind-pollinated",
        "roots: fibrous, spreading near the surface",
    ), Explanation=""))
rows.append(dict(Topic="Digestive System", Question="Describe the structure of the columnar epithelium of the human digestive system and how it relates to its digestive role.",
    Answer_Summary=lettered(
        "tall, column-shaped cells with microvilli on the apical surface, increasing surface area for absorption",
        "goblet cells among them secrete mucus to lubricate and protect the lining",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Anaerobic)", Question="What happens to pyruvate under anaerobic conditions in plants/microorganisms versus in animals?",
    Answer_Summary=lettered(
        "plants/microorganisms: pyruvate becomes ethanol and CO2 via alcoholic fermentation",
        "animals: pyruvate is reduced to lactic acid via lactic acid fermentation, regenerating NAD+ for glycolysis",
    ), Explanation=""))
rows.append(dict(Topic="Gas Transport", Question="Briefly explain three ways carbon dioxide is transported in a vertebrate body.",
    Answer_Summary=lettered(
        "a small amount dissolves directly in blood plasma",
        "most reacts with water to form carbonic acid, which becomes bicarbonate ions",
        "some binds to hemoglobin as carbaminohemoglobin",
    ), Explanation=""))
rows.append(dict(Topic="Excretory System (Kidney)", Question="How are the chemical compositions of blood and glomerular filtrate similar and different?",
    Answer_Summary=lettered(
        "both contain water, glucose, amino acids and ions",
        "blood also has large proteins and blood cells, which are filtered out of the glomerular filtrate",
    ), Explanation=""))
rows.append(dict(Topic="Excretory System (Kidney)", Question="List, in sequence, the blood vessels and organs that urea passes through to reach the kidney from the liver.",
    Answer_Summary=lettered("hepatic vein -> inferior vena cava -> heart -> aorta -> renal artery"), Explanation=""))
rows.append(dict(Topic="Plant Transport (Phloem)", Question="In the mass flow hypothesis of phloem transport, what cell types are involved, what is the source and the sink, and how does the hydrostatic pressure gradient develop?",
    Answer_Summary=lettered(
        "mesophyll cells load sugar into companion cells and sieve tube elements at the source (e.g. a leaf)",
        "xylem and root cells relate to the sink end, where sugars are used or stored",
        "this explanation is called the mass flow hypothesis",
        "the loading site is called the source; the unloading site is called the sink",
        "active loading of sugar at the source draws water in by osmosis, creating high pressure; unloading at the sink lowers pressure there, so sap flows from source to sink",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Synapse)", Question="Describe the sequence of events at a synapse, from vesicle fusion to postsynaptic depolarization, including the ions and neurotransmitter involved.",
    Answer_Summary=lettered(
        "sequence: vesicle fuses with membrane -> transmitter released into the synaptic cleft -> transmitter binds receptors -> ions move through the postsynaptic membrane -> postsynaptic membrane depolarizes",
        "calcium ions trigger vesicle fusion; sodium ions cause postsynaptic depolarization",
        "the transmitter crosses the synaptic cleft by diffusion",
        "acetylcholine is a common neurotransmitter released from synaptic vesicles",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Synapse)", Question="Why does one impulse often fail to trigger a postsynaptic action potential, while several impulses in a row can, and what is this called?",
    Answer_Summary=lettered(
        "a single impulse may not release enough neurotransmitter to reach the depolarization threshold",
        "successive impulses add up (summation), raising neurotransmitter levels enough to reach threshold",
        "this is called temporal summation",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Blood Groups)", Question="If the father is heterozygous blood group A and the mother heterozygous blood group B, what blood groups can their children have?",
    Answer_Summary=lettered(
        "father: IAi; mother: IBi",
        "possible children genotypes: IAIB (AB), IAi (A), IBi (B), ii (O)",
        "so children can be blood group A, B, AB, or O",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Probability)", Question="If these parents have non-identical twins, what is the probability both are blood group A?",
    Answer_Summary=lettered(
        "probability one child is blood group A is 1/4",
        "for two independent children: 1/4 x 1/4 = 1/16",
    ), Explanation=""))
rows.append(dict(Topic="Evolution (Lamarck)", Question="What is the shortcoming of Lamarck's theory of evolution?",
    Answer_Summary=lettered(
        "claimed traits acquired during life could be inherited",
        "modern genetics shows traits pass through genes, unaffected by acquired characteristics",
    ), Explanation=""))
rows.append(dict(Topic="Evolution (Darwin)", Question="Why did Darwin conclude that natural selection operates in nature?",
    Answer_Summary=lettered(
        "individuals in a population vary in traits, and some traits give a survival/reproductive advantage",
        "more offspring are produced than can survive, causing competition for resources",
        "advantageous traits become more common over time - natural selection",
    ), Explanation=""))
rows.append(dict(Topic="Spermatogenesis", Question="During sperm production, why are some daughter cells genetically identical to their parent cell, while others (formed later) are genetically different?",
    Answer_Summary=lettered(
        "mitotic divisions early in spermatogenesis produce daughter cells identical to the parent cell",
        "meiotic divisions later on involve recombination and independent assortment, producing genetically varied cells",
    ), Explanation=""))
rows.append(dict(Topic="Meiosis", Question="Describe two events during cell division that create genetic variation in offspring.",
    Answer_Summary=lettered(
        "crossing over in prophase I - homologous chromosomes exchange genetic material",
        "independent assortment in metaphase I - homologous pairs align randomly, mixing parental chromosomes",
    ), Explanation=""))
rows.append(dict(Topic="Cardiac Muscle", Question="Identify the features and adaptations of cardiac muscle to its role in the heart.",
    Answer_Summary=lettered(
        "intercalated discs allow synchronized contraction by fast electrical transmission between cells",
        "striations aid contraction and relaxation",
        "branching, interconnected fibers spread contraction evenly through the heart",
        "myogenic activity lets it contract on its own without external stimulation",
        "rich blood supply delivers oxygen/nutrients and removes waste",
        "abundant mitochondria supply energy for continuous contraction",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Sex Determination)", Question="How is sex genetically determined in humans and in birds?",
    Answer_Summary=lettered(
        "humans (XY system): males are XY, females are XX; the sperm determines offspring sex",
        "birds (ZW system): males are ZZ, females are ZW; the egg determines offspring sex",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Sex-Linked Inheritance)", Question="A woman has four sons, one of whom is a hemophiliac. What are the likely genotypes of the woman and her husband?",
    Answer_Summary=lettered(
        "mother: XhX (carrier)",
        "father: XY (normal)",
    ), Explanation=""))
rows.append(dict(Topic="Genetics (Sex-Linked Inheritance)", Question="Could this couple have a hemophiliac daughter?",
    Answer_Summary=lettered("no - a hemophiliac daughter needs an affected X chromosome from both parents, but the father (XY, normal) can't supply one"), Explanation=""))
rows.append(dict(Topic="Exercise Physiology", Question="What adjustments occur to the heart rate and circulatory system before, during, and after a 100m race?",
    Answer_Summary=lettered(
        "before: heart rate rises early from anticipatory adrenaline release",
        "during: the heart pumps faster, blood is redirected to skeletal muscles, and stroke volume/cardiac output rise",
        "after: heart rate gradually falls back to resting level, oxygen debt is repaid, and sweating/vasodilation help cool the body",
    ), Explanation=""))
rows.append(dict(Topic="Menstrual Cycle", Question="In a typical 28-day human menstrual cycle, on what day does ovulation happen, when is fertilization most likely, when does the corpus luteum start breaking down, and when does menstruation begin?",
    Answer_Summary=lettered(
        "ovulation: around day 14",
        "fertilization window: around days 14-16",
        "corpus luteum breakdown starts: around day 24",
        "menstruation begins: around day 28",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Placenta)", Question="State four protective and two endocrine roles of the placenta.",
    Answer_Summary=lettered(
        "protective: acts as a barrier against certain infections",
        "protective: stops maternal immune cells attacking the fetus",
        "protective: cushions the fetus from physical shocks",
        "protective: filters out harmful substances before they reach the fetus",
        "endocrine: secretes progesterone to maintain the uterine lining",
        "endocrine: produces hCG to sustain the corpus luteum",
    ), Explanation=""))
rows.append(dict(Topic="Plant Hormones (Phototropism)", Question="Using oat coleoptiles, how did classic experiments (Darwin, Boysen-Jensen) show that phototropism is caused by a chemical from the tip moving down into the growth region?",
    Answer_Summary=lettered(
        "removing the coleoptile tip stopped the phototropic response, showing the tip's role",
        "inserting a gelatin block (which lets chemicals diffuse through) between the tip and shoot still allowed the response",
        "inserting a mica barrier (which blocks chemical diffusion) stopped the response, confirming a diffusible chemical was responsible",
    ), Explanation=""))
rows.append(dict(Topic="Plant Hormones", Question="What is the name of the chemical responsible for phototropism in these experiments?",
    Answer_Summary=lettered("auxin"), Explanation=""))

# ============================== YEAR 2012 ==============================
rows.append(dict(Topic="Biomolecules (Lipids)", Question="State four functions of lipids in living organisms.",
    Answer_Summary=lettered(
        "energy storage - more energy per gram than carbohydrates or proteins",
        "insulation - especially in adipose tissue, for temperature regulation",
        "protection - cushions vital organs",
        "structural role - key components of cell membranes",
    ), Explanation=""))
rows.append(dict(Topic="Cell Membrane", Question="Outline four roles of a cell's plasma membrane.",
    Answer_Summary=lettered(
        "regulates what enters/exits the cell, maintaining homeostasis",
        "enables cell signaling via receptors",
        "separates the cell's interior from the outside (compartmentalization)",
        "facilitates passive and active transport",
    ), Explanation=""))
rows.append(dict(Topic="Digestive System", Question="What glands are found in the buccal cavity and stomach, and what do their secretions do?",
    Answer_Summary=lettered(
        "buccal cavity: salivary glands secrete saliva, which lubricates food and starts starch digestion (amylase)",
        "stomach: gastric glands secrete gastric juice, which breaks down proteins (pepsin) and activates enzymes",
    ), Explanation=""))
rows.append(dict(Topic="Digestive Disorders", Question="How can peptic ulcers and heartburn be prevented?",
    Answer_Summary=lettered(
        "ulcers: avoid excess NSAID use, reduce stress, treat infections like H. pylori",
        "heartburn: avoid overeating, keep a healthy weight, cut back on acidic/spicy food",
    ), Explanation=""))
rows.append(dict(Topic="Cell Transport (Diffusion)", Question="Briefly explain five factors affecting the rate of diffusion across membranes.",
    Answer_Summary=lettered(
        "concentration gradient - a steeper gradient means faster diffusion",
        "temperature - higher temperature speeds up molecular movement",
        "surface area - a larger area allows more diffusion",
        "membrane thickness - thinner membranes diffuse faster",
        "molecule size - smaller molecules diffuse faster",
    ), Explanation=""))
rows.append(dict(Topic="Plant Water Transport", Question="What is the significance of root pressure?",
    Answer_Summary=lettered(
        "helps push water and nutrients up the plant, especially when transpiration is low",
        "helps rehydrate xylem tissue",
    ), Explanation=""))
rows.append(dict(Topic="Respiration", Question="Give four differences between aerobic and anaerobic respiration.",
    Answer_Summary=lettered(
        "oxygen: aerobic needs it; anaerobic doesn't",
        "end products: aerobic gives CO2 and water; anaerobic gives lactic acid or ethanol",
        "energy yield: aerobic produces much more ATP",
        "location: aerobic happens in mitochondria; anaerobic happens in the cytoplasm",
    ), Explanation=""))
rows.append(dict(Topic="Metabolism and Body Size", Question="Why might a larger resting mammal consume more total oxygen than a smaller one, even though the smaller one needs more oxygen per gram of tissue?",
    Answer_Summary=lettered(
        "a bigger mammal has more total tissue, so its overall oxygen use is higher even at a lower rate per gram",
        "a smaller mammal has a higher metabolic rate per gram, so it needs more oxygen per gram to sustain cellular processes",
    ), Explanation=""))
rows.append(dict(Topic="Hormones", Question="Outline one function each of thyroxine, insulin, gibberellin, and auxins.",
    Answer_Summary=lettered(
        "thyroxine: regulates metabolic rate and growth",
        "insulin: regulates blood glucose by promoting cellular glucose uptake",
        "gibberellin: promotes seed germination and stem elongation",
        "auxins: regulate cell elongation and phototropism",
    ), Explanation=""))
rows.append(dict(Topic="Sensory Organs", Question="What function do the sclerotic layer and bony labyrinth share; eye lenses and basilar membranes; and rods, cones and sensory hair cells?",
    Answer_Summary=lettered(
        "sclerotic layer and bony labyrinth: both protect internal structures",
        "eye lenses and basilar membranes: both focus incoming light/sound waves",
        "rods, cones and sensory hair cells: all detect sensory stimuli (light or sound)",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Ovarian Cycle)", Question="What are the stages of ovarian follicle development, from primary follicle to corpus albicans?",
    Answer_Summary=lettered(
        "primary follicle develops into the secondary follicle",
        "secondary follicle matures into the Graafian follicle",
        "the ovum is released from the Graafian follicle at ovulation",
        "the remaining follicle tissue becomes the corpus luteum",
        "if fertilization doesn't occur, the corpus luteum degenerates into the corpus albicans",
    ), Explanation=""))
rows.append(dict(Topic="Classification", Question="What reasons make natural classification systems dynamic (subject to change)?",
    Answer_Summary=lettered(
        "new scientific knowledge about genetics, behavior and ecology updates classifications",
        "discovery of new species requires adjusting existing frameworks",
        "new technology (e.g. molecular phylogenetics) reveals deeper evolutionary relationships",
        "reevaluating evolutionary relationships can show species are more/less related than thought",
    ), Explanation=""))
rows.append(dict(Topic="Classification", Question="What are the differences between natural and artificial classification systems?",
    Answer_Summary=lettered(
        "natural groups by evolutionary/genetic relationships; artificial groups by observable traits like morphology or habitat",
        "natural reflects true phylogenetic relationships; artificial doesn't necessarily",
        "natural has predictive value about shared traits; artificial often doesn't",
        "natural is more flexible to new discoveries; artificial tends to be more rigid",
    ), Explanation=""))
rows.append(dict(Topic="Enzymes", Question="Explain the properties of enzymes.",
    Answer_Summary=lettered(
        "catalytic efficiency: speeds up reactions massively, letting biology happen under mild conditions",
        "specificity: acts on a specific substrate or closely related group",
        "reversibility: many enzyme reactions can run both ways",
        "sensitivity to conditions: temperature, pH and substrate concentration all affect activity, with denaturation possible outside optimal ranges",
    ), Explanation=""))
rows.append(dict(Topic="Enzymes (Inhibition)", Question="Why is understanding competitive inhibition important?",
    Answer_Summary=lettered(
        "drug development: many drugs work as competitive inhibitors (e.g. methotrexate in cancer therapy)",
        "metabolic regulation: helps fine-tune enzyme activity in response to changing substrate levels",
        "toxicology: some toxins act via competitive inhibition, aiding development of antidotes",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Synapse)", Question="Describe the structure of a synapse.",
    Answer_Summary=lettered(
        "presynaptic terminal: holds synaptic vesicles with neurotransmitters, released when an impulse arrives",
        "synaptic cleft: a narrow gap (~20 nm) ensuring one-way transmission and letting neurotransmitters diffuse across",
        "postsynaptic membrane: has receptors that bind neurotransmitters, generating a new signal in the receiving neuron",
    ), Explanation=""))
rows.append(dict(Topic="Plant Reproduction (Seeds)", Question="Describe four advantages and three disadvantages of plant reproduction by seeds.",
    Answer_Summary=lettered(
        "advantage: genetic diversity - creates variation and potentially superior, adaptable hybrids",
        "advantage: seeds can be stored long-term without losing viability",
        "advantage: seed propagation can produce disease/virus-free plants",
        "advantage: cheaper and simpler than other propagation methods",
        "disadvantage: genetic variability makes it hard to consistently keep specific desirable traits",
        "disadvantage: seed-grown plants often take longer to mature",
        "disadvantage: some seeds have long dormancy or need special treatment to germinate",
    ), Explanation=""))
rows.append(dict(Topic="Hormonal Feedback Mechanisms", Question="Discuss, with examples, the feedback mechanisms of hormonal coordination in animals.",
    Answer_Summary=lettered(
        "negative feedback counteracts a change to restore balance - e.g. insulin lowers blood glucose after a meal, glucagon raises it when low",
        "negative feedback also regulates the HPA axis - rising cortisol inhibits further CRH/ACTH release",
        "positive feedback amplifies a change to drive a process to completion - e.g. oxytocin intensifies uterine contractions during childbirth until delivery",
        "positive feedback also drives blood clotting - platelets recruit more platelets until the wound is sealed",
    ), Explanation=""))

# ============================== YEAR 2013 ==============================
rows.append(dict(Topic="Cell Membrane", Question="List two roles of the cell membrane.",
    Answer_Summary=lettered(
        "regulates substances moving in/out, maintaining homeostasis",
        "gives structural support and defines the cell boundary",
    ), Explanation=""))
rows.append(dict(Topic="Cell Organelles", Question="State one function of the Golgi body, endoplasmic reticulum, chloroplast, and mitochondrion, and how each is adapted to it.",
    Answer_Summary=lettered(
        "Golgi body: modifies/packages/transports proteins and lipids; adapted via stacked cisternae for efficient processing",
        "endoplasmic reticulum: rough ER makes proteins, smooth ER makes lipids; adapted via extensive membranes giving a large surface area",
        "chloroplast: carries out photosynthesis; adapted via thylakoid membranes with chlorophyll for light absorption",
        "mitochondrion: produces ATP via aerobic respiration; adapted via cristae (folded inner membrane) that increase surface area",
    ), Explanation=""))
rows.append(dict(Topic="Gas Exchange", Question="Explain the characteristic features of a respiratory surface.",
    Answer_Summary=lettered(
        "thin, to allow efficient gas diffusion",
        "large surface area, to increase gas exchange",
        "moist, so gases dissolve and diffuse more easily",
        "richly supplied with blood vessels, to transport gases quickly",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Respiratory Quotient)", Question="Given 2C51H98O6 + 145O2 -> 102CO2 + 98H2O for tripalmitin, what is its respiratory quotient (RQ)?",
    Answer_Summary=lettered("RQ = CO2 produced / O2 consumed = 102/145 = 0.7"), Explanation=""))
rows.append(dict(Topic="Human Ear", Question="What parts make up the organ of Corti, and how is it adapted for sound perception?",
    Answer_Summary=lettered(
        "made of hair cells, the basilar membrane, and the tectorial membrane",
        "hair cells with stereocilia detect vibrations and convert them into electrical signals",
        "the tectorial membrane interacts with the stereocilia to help detect sound",
        "the basilar membrane vibrates at different frequencies to distinguish different sounds",
        "its position in the cochlea exposes it to pressure changes in the inner ear fluid",
    ), Explanation=""))
rows.append(dict(Topic="Plant Growth (Meristems)", Question="What is meristematic tissue?",
    Answer_Summary=lettered("undifferentiated cells that keep dividing, enabling plant growth in length and girth"), Explanation=""))
rows.append(dict(Topic="Plant Growth (Meristems)", Question="What types of meristematic tissue exist in dicot plants, and where is each located?",
    Answer_Summary=lettered(
        "apical meristem: at root/shoot tips, drives primary growth",
        "lateral meristem: in the vascular cambium and cork cambium, drives secondary growth",
        "intercalary meristem: at the base of leaves/internodes, aids regrowth and elongation",
    ), Explanation=""))
rows.append(dict(Topic="Plant Transport (Xylem)", Question="State four adaptations of xylem tissue to its function.",
    Answer_Summary=lettered(
        "elongated, hollow vessels allow unimpeded water flow",
        "lignified walls give structural support and prevent collapse",
        "pits in the walls let water move sideways between vessels",
        "no cytoplasm, reducing resistance to water flow",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Ovum and Fertilization)", Question="What are the main parts of a mature mammalian ovum, and what are the events of fertilization?",
    Answer_Summary=lettered(
        "nucleus: holds the haploid genetic material for fusing with sperm DNA",
        "cytoplasm (ooplasm): nutrient-rich, supports early embryo development",
        "zona pellucida: a glycoprotein layer for species-specific sperm binding and blocking polyspermy",
        "corona radiata: cumulus cells that support the oocyte and help sperm entry",
        "plasma membrane (oolemma): controls what enters, and changes after fertilization to block extra sperm",
        "cortical granules: release contents at fertilization to modify the zona pellucida and prevent polyspermy",
        "fertilization: sperm binds the zona pellucida, the acrosome reaction digests through it, the sperm nucleus enters, the cortical reaction blocks polyspermy, and the two nuclei fuse into a diploid zygote",
    ), Explanation=""))
rows.append(dict(Topic="Digestion (Absorption)", Question="Why is active transport important in absorbing the end products of digestion?",
    Answer_Summary=lettered(
        "lets nutrients be absorbed against their concentration gradient",
        "ensures nutrients like glucose, amino acids and ions get absorbed even when levels are low in the gut",
    ), Explanation=""))
rows.append(dict(Topic="Digestion (Liver)", Question="What role does the liver play in digestion and metabolism?",
    Answer_Summary=lettered(
        "converts excess glucose to glycogen for storage",
        "produces bile to emulsify fats for digestion and absorption",
        "detoxifies harmful substances, e.g. converting ammonia to urea",
        "metabolizes lipids - makes cholesterol and breaks down fatty acids for energy",
        "stores vitamins and minerals (e.g. vitamin A, iron) for later use",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis (Limiting Factors)", Question="Under what conditions can light intensity, CO2 concentration, and temperature become limiting factors in photosynthesis?",
    Answer_Summary=lettered(
        "low light limits the light reactions, reducing ATP/NADPH for the Calvin cycle",
        "low CO2 limits the substrate available for RuBisCO, slowing carbon fixation",
        "low temperature slows enzyme activity; high temperature can denature enzymes like RuBisCO",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis (Photorespiration)", Question="How does photorespiration affect the rate of photosynthesis?",
    Answer_Summary=lettered(
        "it competes with the Calvin cycle when oxygen binds RuBisCO instead of CO2",
        "this produces less glucose and releases CO2, wasting energy",
        "it's worse under high oxygen/low CO2 conditions, reducing photosynthetic efficiency",
    ), Explanation=""))
rows.append(dict(Topic="Cell Theory", Question="Why is a cell considered the basic unit of life?",
    Answer_Summary=lettered(
        "all organisms are made of cells (single-celled or multicellular)",
        "cells carry out life's essential functions (metabolism, energy production, waste removal)",
        "cells only arise from pre-existing cells via mitosis/meiosis",
        "cells contain DNA, the genetic blueprint guiding development and function",
    ), Explanation=""))
rows.append(dict(Topic="Cell Organelles", Question="Explain three roles each of the nucleus, lysosomes, and microtubules.",
    Answer_Summary=lettered(
        "nucleus: stores DNA; directs mRNA transcription for protein synthesis; the nucleolus assembles ribosomal subunits",
        "lysosomes: digest macromolecules with hydrolytic enzymes; degrade damaged organelles (autophagy); digest invading pathogens",
        "microtubules: support cell shape (cytoskeleton); act as tracks for intracellular transport; form the mitotic spindle during cell division",
    ), Explanation=""))
rows.append(dict(Topic="Cell Organelles", Question="Describe four advantages of membrane-bound organelles.",
    Answer_Summary=lettered(
        "compartmentalization lets specialized functions happen without interference",
        "organelle membranes add surface area for biochemical reactions",
        "confining molecules raises local substrate/enzyme concentration, speeding reactions",
        "isolates potentially harmful reactions/substances from the rest of the cell (e.g. lysosome enzymes)",
    ), Explanation=""))
rows.append(dict(Topic="Transpiration", Question="Explain four internal and four external factors affecting transpiration.",
    Answer_Summary=lettered(
        "internal - leaf surface area: bigger leaves transpire more",
        "internal - stomatal density: more stomata means more water vapor loss",
        "internal - cuticle thickness: a thicker waxy cuticle reduces water loss",
        "internal - leaf orientation: angling away from direct sun lowers leaf temperature and transpiration",
        "external - temperature: higher temperature speeds evaporation",
        "external - humidity: low humidity increases the moisture gradient, raising transpiration",
        "external - wind speed: wind removes the saturated air layer around the leaf, keeping the gradient favorable",
        "external - light intensity: light opens stomata for CO2 entry, which also lets water vapor escape",
    ), Explanation=""))
rows.append(dict(Topic="Transpiration", Question="Give five effects of transpiration in plants.",
    Answer_Summary=lettered(
        "cools the plant as water evaporates",
        "creates negative pressure in the xylem, pulling water/minerals up from the roots",
        "maintains cell turgor for structural support and growth",
        "influences stomatal behavior, balancing water loss with gas exchange",
        "can deplete soil moisture if not matched by water uptake",
    ), Explanation=""))
rows.append(dict(Topic="Balance (Vestibular System)", Question="Explain the mechanism of body balance in mammals.",
    Answer_Summary=lettered(
        "the vestibular system in the inner ear (3 semicircular canals plus the utricle and saccule) detects rotation and linear movement",
        "fluid (endolymph) in the semicircular canals shifts with head movement, bending hair cells that signal the brain",
        "proprioception (from muscle, tendon and joint receptors) gives continuous feedback on body position",
        "visual input adds information about the body's position relative to its surroundings",
        "the vestibulo-ocular reflex stabilizes vision during head movement",
        "the cerebellum and brainstem integrate all this input to fine-tune balance and posture",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Oestrus Cycle)", Question="Define oestrus.",
    Answer_Summary=lettered("the \"heat\" phase in non-primate female mammals when they're sexually receptive and able to conceive, driven by hormonal changes"), Explanation=""))
rows.append(dict(Topic="Reproduction (Oestrus Cycle)", Question="What are the four stages of the oestrus cycle?",
    Answer_Summary=lettered(
        "proestrus: follicles mature, estrogen rises, uterine lining thickens; not yet receptive",
        "estrus (\"heat\"): peak estrogen, sexually receptive, ovulation occurs",
        "metestrus (diestrus): the ruptured follicle becomes the corpus luteum, secreting progesterone to maintain the uterine lining",
        "anestrus: a resting period of sexual inactivity between cycles",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Oestrus Cycle)", Question="What is the significance of the oestrus cycle?",
    Answer_Summary=lettered("synchronizes mating with ovulation, maximizing the chance of conception and supporting species survival"), Explanation=""))
rows.append(dict(Topic="Reproduction (Oestrus vs Menstrual Cycle)", Question="How does the oestrus cycle differ from the menstrual cycle?",
    Answer_Summary=lettered(
        "oestrus occurs in non-primate mammals (e.g. dogs, cattle); the menstrual cycle occurs in primates (including humans)",
        "in the menstrual cycle, the uterine lining is shed as menstruation if no fertilization occurs; in oestrus, it's usually reabsorbed instead",
        "oestrus animals are only sexually receptive during \"heat\"; menstrual-cycle females can be sexually active throughout the cycle",
    ), Explanation=""))

# ============================== YEAR 2014 ==============================
rows.append(dict(Topic="Plant Vascular System", Question="Briefly explain the functions of the vascular system in plants.",
    Answer_Summary=lettered(
        "xylem transports water/minerals from roots to leaves, supporting photosynthesis",
        "phloem distributes sugars from leaves to the rest of the plant",
        "the vascular system also gives the plant structural support",
    ), Explanation=""))
rows.append(dict(Topic="Plant Water Transport", Question="Explain the processes involved in moving water from the soil to the xylem.",
    Answer_Summary=lettered(
        "osmosis: root hairs absorb water since soil has a higher water potential than root cells",
        "apoplast/symplast pathways move water through the root cortex to the endodermis",
        "water enters the xylem via active transport, then is pulled upward by root pressure and transpiration (cohesion/adhesion)",
    ), Explanation=""))
rows.append(dict(Topic="Nutrition (Modes)", Question="Define photoautotrophs and chemoheterotrophs.",
    Answer_Summary=lettered(
        "photoautotrophs: make their own food using light, CO2 and water, e.g. plants and algae",
        "chemoheterotrophs: get energy by consuming organic compounds, e.g. animals and fungi",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis (C3 vs C4)", Question="What effect does lower oxygen concentration have on C3 versus C4 photosynthesis?",
    Answer_Summary=lettered(
        "C3: lower oxygen reduces photorespiration, boosting photosynthetic efficiency and glucose production",
        "C4: less affected, since these plants already concentrate CO2 around RuBisCO, minimizing photorespiration",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis (C4 Anatomy)", Question="Why is it an advantage that bundle sheath chloroplasts lack grana, and what happens to intestinal enzymes if intestinal pH stays at 2?",
    Answer_Summary=lettered(
        "lacking grana reduces photorespiration, letting these cells focus on the Calvin cycle for carbon fixation",
        "intestinal enzymes work best at neutral/slightly alkaline pH, so pH 2 would inhibit them, reducing digestion and absorption",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Glycolysis)", Question="What is glycolysis?",
    Answer_Summary=lettered("breaks glucose into pyruvate, producing ATP and NADH in the cytoplasm"), Explanation=""))
rows.append(dict(Topic="Fermentation", Question="In what ways are fermentation processes useful to human beings?",
    Answer_Summary=lettered(
        "makes alcoholic drinks (beer, wine)",
        "used in food production (bread, yogurt, cheese)",
        "used in pharmaceuticals to produce antibiotics and other drugs",
        "provides energy under anaerobic conditions, e.g. during vigorous exercise",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Twins)", Question="How do identical, fraternal, and conjoined twins each arise?",
    Answer_Summary=lettered(
        "identical twins: one fertilized egg splits into two embryos with identical genes",
        "fraternal twins: two separate eggs are fertilized by two separate sperm, giving genetically different siblings",
        "conjoined twins: identical twins that don't fully separate during early embryonic development",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Twins)", Question="What is one distinguishing feature of each type of twin (identical, fraternal, conjoined)?",
    Answer_Summary=lettered(
        "identical twins: share the same genes, always the same sex",
        "fraternal twins: different genes, can be same or different sex",
        "conjoined twins: physically joined, may share organs/body parts",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Cell Types)", Question="Classify cells into two major groups, giving four features of each.",
    Answer_Summary=lettered(
        "prokaryotic (e.g. bacteria): no nucleus, one circular chromosome, no membrane-bound organelles, peptidoglycan cell wall",
        "eukaryotic (e.g. plant/animal cells): has a nucleus, multiple linear chromosomes, membrane-bound organelles, generally bigger",
    ), Explanation=""))
rows.append(dict(Topic="Cell Organelles", Question="What are three advantages of having membranes in cell organelles?",
    Answer_Summary=lettered(
        "compartmentalizes cell functions so different processes can run at once",
        "increases surface area for biochemical reactions (e.g. in mitochondria, chloroplasts)",
        "regulates what moves in/out of organelles, maintaining internal balance",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Taxonomic Keys)", Question="What is a taxonomic key?",
    Answer_Summary=lettered("a tool for identifying/classifying organisms via paired contrasting statements leading to identification"), Explanation=""))
rows.append(dict(Topic="Classification (Dichotomous Keys)", Question="How do you construct and use a dichotomous key?",
    Answer_Summary=lettered(
        "observe and record distinguishing traits",
        "group organisms by similarities/differences",
        "write paired statements (couplets) offering two contrasting options at each step",
        "test and revise the key for accuracy",
        "follow the statements step by step to identify the organism",
    ), Explanation=""))
rows.append(dict(Topic="Plant Movements", Question="Distinguish nastic movements from tactic movements, with an example each.",
    Answer_Summary=lettered(
        "nastic: non-directional response to a stimulus, e.g. Mimosa leaves closing when touched",
        "tactic: directional movement toward/away from a stimulus, e.g. Euglena moving toward light (positive phototaxis)",
    ), Explanation=""))
rows.append(dict(Topic="Plant Movements (Tropisms)", Question="Explain the importance of tropic movements in plants.",
    Answer_Summary=lettered(
        "phototropism: growth toward light, maximizing photosynthesis",
        "gravitropism: roots grow down for anchorage/nutrients, shoots grow up for light",
        "hydrotropism: roots grow toward water sources for hydration",
    ), Explanation=""))
rows.append(dict(Topic="Biomolecules (Protein Structure)", Question="Describe the tertiary structure of a protein.",
    Answer_Summary=lettered(
        "the 3D shape from folding of the polypeptide chain",
        "stabilized by hydrogen bonds, ionic bonds, disulfide bridges and hydrophobic interactions between R-groups",
        "this shape determines the protein's function and how it interacts with other molecules",
    ), Explanation=""))
rows.append(dict(Topic="Biomolecules (Protein Functions)", Question="What are the six categories of protein, based on function?",
    Answer_Summary=lettered(
        "structural: support tissues, e.g. collagen, keratin",
        "enzymatic: catalyze reactions, e.g. amylase",
        "transport: move substances, e.g. hemoglobin carrying oxygen",
        "defensive: protect against pathogens, e.g. antibodies",
        "hormonal: regulate physiology, e.g. insulin",
        "contractile: enable movement, e.g. actin and myosin in muscle",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Synapse)", Question="Explain seven roles of the synapse.",
    Answer_Summary=lettered(
        "transmits electrical signals between neurons/effector cells",
        "ensures one-way (directional) signal flow",
        "allows signal summation, determining if a neuron fires",
        "can amplify or inhibit signals (modulation)",
        "supports learning and memory via neural circuits",
        "filters out weak signals so only significant stimuli get a response",
        "coordinates communication across neural networks",
    ), Explanation=""))
rows.append(dict(Topic="Respiratory System (Lung Structure)", Question="Describe the internal structure of the mammalian lung.",
    Answer_Summary=lettered(
        "trachea splits into bronchi, which branch into smaller bronchi and bronchioles",
        "bronchioles lack cartilage and lead toward the gas-exchange regions",
        "respiratory bronchioles and alveolar ducts are lined with alveoli",
        "alveoli are tiny air sacs surrounded by capillaries for gas exchange",
        "alveoli have Type I cells (form the wall) and Type II cells (secrete surfactant to stop collapse)",
        "the thin blood-air barrier between alveoli and capillaries allows efficient gas diffusion",
        "the pleura (a double membrane around each lung) reduces friction during breathing",
    ), Explanation=""))
rows.append(dict(Topic="Respiratory Hazards", Question="Why is it dangerous to heat a closed room at night using charcoal while people sleep inside?",
    Answer_Summary=lettered(
        "burning charcoal produces carbon monoxide",
        "carbon monoxide binds hemoglobin more strongly than oxygen, blocking oxygen transport",
        "this causes hypoxia, unconsciousness, or death",
    ), Explanation=""))
rows.append(dict(Topic="Circulatory Systems", Question="State three disadvantages of a closed circulatory system compared to an open one.",
    Answer_Summary=lettered(
        "needs more energy to maintain the high pressure needed to circulate blood",
        "needs a more complex heart and vessel system, more vulnerable to failure",
        "high blood pressure can damage delicate capillaries or cause other cardiovascular problems",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Fetal Circulation)", Question="Describe fetal blood circulation in humans.",
    Answer_Summary=lettered(
        "the fetus gets oxygen from the placenta, bypassing the lungs",
        "oxygen-rich blood travels via the umbilical vein to the fetus",
        "the ductus venosus lets blood bypass the liver into the inferior vena cava",
        "the foramen ovale lets most blood pass from the right to left atrium, bypassing the lungs",
        "the ductus arteriosus connects the pulmonary artery to the aorta, also bypassing the lungs",
        "blood returns to the placenta via the umbilical arteries for reoxygenation",
    ), Explanation=""))

# ============================== YEAR 2015 ==============================
rows.append(dict(Topic="Cell Structure (Prokaryote vs Eukaryote)", Question="Differentiate eukaryotic and prokaryotic cells by cell division, genetic material, cell wall, flagella, respiration, photosynthesis, and nitrogen fixation.",
    Answer_Summary=lettered(
        "cell division: prokaryotes divide by binary fission; eukaryotes by mitosis and meiosis",
        "genetic material: prokaryotes have no nucleus (DNA in the nucleoid); eukaryotes enclose DNA in a nucleus",
        "cell wall: prokaryotes (bacteria) have peptidoglycan; eukaryotic plants have cellulose, or none in animals",
        "flagella: simple, made of flagellin in prokaryotes; complex, made of microtubules in eukaryotes",
        "respiration: happens in the cytoplasm in prokaryotes; in mitochondria in eukaryotes",
        "photosynthesis: happens in thylakoids (if present) in prokaryotes; in chloroplasts in eukaryotic plants",
        "nitrogen fixation: done by specialized prokaryotes; uncommon in eukaryotes",
    ), Explanation=""))
rows.append(dict(Topic="Cell Differentiation", Question="What is cell differentiation?",
    Answer_Summary=lettered("the process where a less specialized cell becomes more specialized in structure and function, e.g. muscle cells for contraction, nerve cells for signaling"), Explanation=""))
rows.append(dict(Topic="Biomolecules (Proteins)", Question="What is the chemical composition of proteins?",
    Answer_Summary=lettered(
        "made of carbon, hydrogen, oxygen, nitrogen, and sometimes sulfur",
        "polymers of amino acids joined by peptide bonds",
    ), Explanation=""))
rows.append(dict(Topic="Biomolecules (Carbohydrates)", Question="Give one example each of a supporting and a storage function of carbohydrates.",
    Answer_Summary=lettered(
        "supporting: cellulose gives structural rigidity to plant cell walls",
        "storage: starch stores glucose in plants for later energy use",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Taxonomic Keys)", Question="What steps are used to construct a simple taxonomic key?",
    Answer_Summary=lettered(
        "observe and identify distinguishing features",
        "group organisms by shared characteristics",
        "write contrasting statements (couplets) from those features",
        "test the key for clarity and accuracy",
        "finalize and publish the key",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Binomial Nomenclature)", Question="What rules govern binomial nomenclature?",
    Answer_Summary=lettered(
        "the scientific name is Latin, italicized or underlined",
        "genus name starts with a capital letter; species name is lowercase",
        "the name must be unique and universally accepted",
        "the genus name can be abbreviated after first full use",
        "priority goes to the earliest published name",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Nerve Impulse)", Question="Explain three characteristics of a nerve impulse.",
    Answer_Summary=lettered(
        "unidirectional - moves only from presynaptic to postsynaptic neuron",
        "all-or-nothing - needs a threshold stimulus to trigger",
        "transmitted rapidly due to myelination (saltatory conduction)",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Nerve Impulse)", Question="Why might myelinated axons of the same diameter conduct impulses at different speeds in different animals (e.g. frogs at 30 m/s vs cats at 90 m/s)?",
    Answer_Summary=lettered("differences in how advanced/effective the myelination is between species affect saltatory conduction speed"), Explanation=""))
rows.append(dict(Topic="Photosynthesis", Question="Write the balanced equation for photosynthesis, and state factors affecting its rate.",
    Answer_Summary=lettered(
        "6CO2 + 6H2O -> C6H12O6 + 6O2",
        "rate depends on light intensity, CO2 concentration, temperature, and water availability",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis (Calvin Cycle)", Question="Explain the events of the dark reaction (Calvin cycle) of photosynthesis.",
    Answer_Summary=lettered(
        "occurs in the stroma of the chloroplast",
        "CO2 combines with RuBP to form 3-phosphoglycerate (carbon fixation)",
        "ATP and NADPH from the light reactions convert 3-PGA into G3P",
        "G3P is used to make glucose and regenerate RuBP",
    ), Explanation=""))
rows.append(dict(Topic="Metabolism", Question="What is basal metabolic rate (BMR)?",
    Answer_Summary=lettered("the minimum energy needed to maintain basic body functions (breathing, circulation, metabolism) at rest"), Explanation=""))
rows.append(dict(Topic="Respiration (Anaerobic)", Question="Describe the fate of pyruvic acid under anaerobic respiration.",
    Answer_Summary=lettered(
        "in animals, it's converted to lactic acid (lactic acid fermentation)",
        "in plants/yeast, it's converted to ethanol and CO2 (alcoholic fermentation)",
        "this happens without oxygen and regenerates NAD+ so glycolysis can continue producing ATP",
    ), Explanation=""))
rows.append(dict(Topic="Plant Reproduction", Question="What is double fertilization in angiosperms?",
    Answer_Summary=lettered(
        "one sperm fuses with the egg cell to form a diploid zygote",
        "the other sperm fuses with the two polar nuclei to form the triploid endosperm, which nourishes the embryo",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Sperm Structure)", Question="What is the role of a sperm cell, what are its main parts, and how are they adapted to its function?",
    Answer_Summary=lettered(
        "role: delivers the male haploid genetic material to the egg for fertilization",
        "head: contains the haploid nucleus and an acrosome with enzymes to penetrate the egg",
        "midpiece: packed with mitochondria for energy to move",
        "tail (flagellum): long and whip-like, propelling the sperm toward the egg",
    ), Explanation=""))
rows.append(dict(Topic="Plant Reproduction (Flower Structure)", Question="What are the main parts of a flower (e.g. from a hibiscus) and their roles?",
    Answer_Summary=lettered(
        "stigma: receives pollen during pollination",
        "style: lets pollen tubes grow down toward the ovary",
        "ovary: holds ovules and develops into fruit after fertilization",
        "ovule: holds the female gametes and becomes a seed after fertilization",
        "petal: attracts pollinators with color/scent",
        "sepal: protects the flower bud before it opens",
        "anther: produces pollen containing male gametes",
        "filament: supports and positions the anther",
        "receptacle: holds all the flower parts together",
    ), Explanation=""))
rows.append(dict(Topic="Biomolecules (Protein Functions)", Question="Describe categories of proteins based on their structures and functions.",
    Answer_Summary=lettered(
        "structural: support cells/tissues, e.g. collagen, keratin",
        "enzymatic: catalyze reactions, e.g. amylase",
        "transport: move substances, e.g. hemoglobin",
        "defensive: protect against pathogens, e.g. antibodies",
        "hormonal: regulate physiology, e.g. insulin",
        "contractile: enable movement, e.g. actin and myosin",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Nerve Impulse)", Question="Explain how a nerve impulse travels along the axon and across the synapse.",
    Answer_Summary=lettered(
        "a threshold stimulus opens voltage-gated sodium channels, letting Na+ in and depolarizing the membrane (action potential)",
        "the action potential spreads by depolarizing neighboring regions, with repolarization restoring the resting potential behind it",
        "at the synapse, calcium influx triggers vesicles to release neurotransmitter into the synaptic cleft",
        "the neurotransmitter binds postsynaptic receptors, opening ion channels and generating a new action potential",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis (Calvin Cycle)", Question="What are the main steps of the Calvin cycle (light-independent reactions)?",
    Answer_Summary=lettered(
        "carbon fixation: CO2 combines with RuBP",
        "reduction: glycerate-3-phosphate is reduced to triose phosphate",
        "triose phosphate is converted into carbohydrates and other products",
        "regeneration of RuBP to keep the cycle running",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis (C4 Pathway)", Question="Explain the Hatch-Slack pathway in C4 plants.",
    Answer_Summary=lettered(
        "CO2 is first fixed into a 4-carbon compound (oxaloacetate) in mesophyll cells",
        "this is converted to malate and transported to bundle-sheath cells",
        "malate releases CO2 there, feeding it into the Calvin cycle",
        "this concentrates CO2 around RuBisCO, boosting efficiency in high light/heat, minimizing photorespiration",
    ), Explanation=""))

# ============================== YEAR 2014 ==============================
rows.append(dict(Topic="Plant Transport (Vascular System)", Question="Briefly explain the functions of the vascular system in plants.",
    Answer_Summary=lettered(
        "xylem transports water and dissolved minerals from roots to leaves, supporting photosynthesis and metabolism",
        "phloem distributes organic nutrients (e.g. sugars from photosynthesis) from leaves to the rest of the plant",
        "the vascular system also gives the plant structural support to stay upright",
    ), Explanation=""))
rows.append(dict(Topic="Plant Transport (Water Uptake)", Question="Explain the processes involved in transportation of water from the soil to the xylem.",
    Answer_Summary=lettered(
        "osmosis: root hair cells absorb water because the soil has higher water potential than the root cells",
        "apoplast/symplast pathways: water moves through cell walls (apoplast) or cytoplasm (symplast) until it reaches the endodermis",
        "root pressure and transpiration pull: water enters the xylem by active transport and is pulled upward by cohesion and adhesion during transpiration",
    ), Explanation=""))
rows.append(dict(Topic="Nutrition (Modes)", Question="Define the terms photoautotrophs and chemoheterotrophs.",
    Answer_Summary=lettered(
        "photoautotrophs: organisms that make their own food using light energy, CO2, and water, e.g. plants and algae",
        "chemoheterotrophs: organisms that get energy by consuming organic compounds, e.g. animals and fungi",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis (C3 vs C4)", Question="What would be the effect of lowering oxygen concentration on C3 photosynthesis and on C4 photosynthesis?",
    Answer_Summary=lettered(
        "C3: lower oxygen reduces photorespiration, improving photosynthetic efficiency and glucose production",
        "C4: barely affected, since C4 plants already concentrate CO2 around RuBisCO, which minimizes photorespiration",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis (Bundle Sheath Cells)", Question="Why is it an advantage that bundle sheath chloroplasts lack grana?",
    Answer_Summary=lettered("lacking grana reduces photorespiration in these cells, letting them focus on the Calvin cycle for efficient carbon fixation"), Explanation=""))
rows.append(dict(Topic="Digestion (Enzymes and pH)", Question="What would happen to the activities of intestinal enzymes if the pH in the intestine remains at 2?",
    Answer_Summary=lettered("intestinal enzyme activity would be inhibited, since they work best at neutral/slightly alkaline pH, reducing digestion and nutrient absorption"), Explanation=""))
rows.append(dict(Topic="Respiration (Glycolysis)", Question="What is glycolysis?",
    Answer_Summary=lettered("the metabolic pathway that breaks down glucose into pyruvate, producing ATP and NADH, in the cytoplasm"), Explanation=""))
rows.append(dict(Topic="Respiration (Fermentation)", Question="In what ways are fermentation processes useful to human beings?",
    Answer_Summary=lettered(
        "used to produce alcoholic beverages like beer and wine",
        "used in the food industry for bread, yogurt, and cheese",
        "used in pharmaceuticals to produce antibiotics and other drugs",
        "lets cells keep producing energy anaerobically, e.g. during vigorous exercise",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Multiple Births)", Question="Account for the birth of identical, fraternal, and conjoined twins, and give one feature of each.",
    Answer_Summary=lettered(
        "identical twins: from one fertilized egg splitting into two embryos; share identical genetic material and are always the same sex",
        "fraternal twins: from two separate eggs each fertilized by a separate sperm; genetically different and can be the same or different sexes",
        "conjoined twins: from incomplete separation of identical twins during early development; remain physically attached, sometimes sharing organs",
    ), Explanation=""))
rows.append(dict(Topic="Cell Classification", Question="Classify cells into two major groups using examples, giving four features of each group.",
    Answer_Summary=lettered(
        "prokaryotic cells (e.g. bacteria): no nucleus, single circular chromosome, no membrane-bound organelles, cell wall of peptidoglycan",
        "eukaryotic cells (e.g. plant and animal cells): have a nucleus, multiple linear chromosomes, membrane-bound organelles, and are larger",
    ), Explanation=""))
rows.append(dict(Topic="Cell Structure (Organelle Membranes)", Question="Outline three advantages of the presence of membranes in cell organelles.",
    Answer_Summary=lettered(
        "compartmentalize cell functions so different processes can happen at once",
        "increase surface area for biochemical reactions, e.g. in mitochondria and chloroplasts",
        "regulate movement of substances in and out of organelles, maintaining homeostasis",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Taxonomic Keys)", Question="What do you understand by the term Taxonomic Key as used in Biology?",
    Answer_Summary=lettered("a tool for identifying/classifying organisms using paired statements describing contrasting traits, guiding the user to the correct identification"), Explanation=""))
rows.append(dict(Topic="Classification (Dichotomous Keys)", Question="Explain how to construct and use a Dichotomous Key.",
    Answer_Summary=lettered(
        "observe and record distinguishing characteristics of the organisms",
        "group organisms by similarities and differences in traits",
        "create paired contrasting statements (couplets) at each step",
        "test the key for accuracy and revise as needed",
        "use the key by following the statements step by step until the organism is identified",
    ), Explanation=""))
rows.append(dict(Topic="Plant/Animal Movement", Question="Distinguish nastic movements from tactic movements in living organisms, giving one example of each.",
    Answer_Summary=lettered(
        "nastic movement: a non-directional response to a stimulus, e.g. Mimosa pudica leaves closing when touched",
        "tactic movement: a directional movement toward or away from a stimulus, e.g. Euglena moving toward light (positive phototaxis)",
    ), Explanation=""))
rows.append(dict(Topic="Plant Movement (Tropisms)", Question="Explain the importance of tropic movement in plants.",
    Answer_Summary=lettered(
        "phototropism: growth toward light, maximizing photosynthesis",
        "gravitropism: roots grow downward for anchorage/nutrients, shoots grow upward for light",
        "hydrotropism: root growth directed toward water sources for hydration",
    ), Explanation=""))
rows.append(dict(Topic="Biomolecules (Protein Structure)", Question="Describe the tertiary structure of a protein.",
    Answer_Summary=lettered(
        "the 3D shape formed by folding of the polypeptide chain",
        "stabilized by hydrogen bonds, ionic bonds, disulfide bridges, and hydrophobic interactions between R-groups",
        "this shape determines the protein's function and how it interacts with other molecules",
    ), Explanation=""))
rows.append(dict(Topic="Biomolecules (Protein Functions)", Question="Elaborate six categories of protein based on their functions.",
    Answer_Summary=lettered(
        "structural: support cells/tissues, e.g. collagen, keratin",
        "enzymatic: catalyze reactions, e.g. amylase",
        "transport: move substances, e.g. hemoglobin",
        "defensive: protect against pathogens, e.g. antibodies",
        "hormonal: regulate physiology, e.g. insulin",
        "contractile: enable movement via the cytoskeleton, e.g. actin and myosin",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Synapse)", Question="Explain the seven roles of the synapse.",
    Answer_Summary=lettered(
        "transmission: passes electrical signals between neurons and to effector cells",
        "directionality: ensures one-way flow of information",
        "signal integration: sums multiple signals to decide if a neuron fires",
        "signal modulation: amplifies or inhibits signals via neurotransmitter release",
        "learning and memory: forms neural circuits underlying learning",
        "filtering: screens out weak signals so only significant stimuli get a response",
        "coordination: enables communication within neural networks for coordinated responses",
    ), Explanation=""))
rows.append(dict(Topic="Respiratory System (Lung Structure)", Question="Describe the internal structure of the mammalian lung.",
    Answer_Summary=lettered(
        "trachea and bronchi: air enters via the trachea, which splits into main bronchi leading to each lung, dividing further into the bronchial tree",
        "bronchioles: smaller airways without cartilage, continuing to branch down to terminal bronchioles",
        "respiratory bronchioles and alveolar ducts: have alveoli budding off them, leading into alveoli-lined alveolar ducts",
        "alveoli: tiny sacs surrounded by capillaries where gas exchange happens",
        "alveolar cells: Type I pneumocytes form the alveolar wall; Type II pneumocytes secrete surfactant to stop alveolar collapse",
        "blood-air barrier: the thin membrane between alveolar air and capillaries that allows efficient gas diffusion",
        "pleura: a double-layered membrane around each lung, with fluid between the layers reducing friction during breathing",
    ), Explanation=""))
rows.append(dict(Topic="Respiratory System (Carbon Monoxide)", Question="Why is it not advisable to warm a room at night using charcoal while people sleep with doors and windows closed?",
    Answer_Summary=lettered("charcoal burning in a closed room produces carbon monoxide, which binds hemoglobin more strongly than oxygen, blocking oxygen transport and causing hypoxia, unconsciousness, or death"), Explanation=""))
rows.append(dict(Topic="Circulatory System", Question="State three disadvantages of a closed compared to an open circulatory system.",
    Answer_Summary=lettered(
        "more energy-intensive, since high pressure is needed to circulate blood",
        "needs a more complex, well-developed heart and blood vessels, which are more vulnerable to failure",
        "high blood pressure can damage delicate capillaries or cause other cardiovascular problems",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Fetal Circulation)", Question="Describe foetal blood circulation in human beings.",
    Answer_Summary=lettered(
        "the fetus gets oxygen from the placenta, bypassing the lungs",
        "oxygen- and nutrient-rich blood flows from the placenta via the umbilical vein to the fetus",
        "the ductus venosus routes blood into the inferior vena cava, bypassing the liver",
        "most blood passes from the right to left atrium via the foramen ovale, bypassing the lungs",
        "the ductus arteriosus connects the pulmonary artery to the aorta, also bypassing the lungs",
        "blood returns to the placenta via the umbilical arteries for reoxygenation",
    ), Explanation=""))

# ============================== YEAR 2013 ==============================
rows.append(dict(Topic="Cell Structure (Cell Membrane)", Question="List two roles of the cell membrane.",
    Answer_Summary=lettered(
        "regulates movement of substances in and out of the cell, maintaining homeostasis",
        "gives structural support and defines the cell's boundary, protecting its internal components",
    ), Explanation=""))
rows.append(dict(Topic="Cell Structure (Organelles)", Question="Give one function of the Golgi body, endoplasmic reticulum, chloroplast, and mitochondrion, and briefly explain how each is adapted to that function.",
    Answer_Summary=lettered(
        "Golgi body: modifies, packages, and transports proteins/lipids; adapted with stacked membrane cisternae for efficient sorting",
        "endoplasmic reticulum: rough ER makes proteins, smooth ER makes lipids; adapted with extensive membranes giving a large surface area",
        "chloroplast: carries out photosynthesis; adapted with thylakoid membranes containing chlorophyll for light absorption",
        "mitochondrion: produces ATP via aerobic respiration; adapted with a double membrane and cristae to increase surface area",
    ), Explanation=""))
rows.append(dict(Topic="Gas Exchange (Respiratory Surfaces)", Question="Explain the characteristic features of a respiratory surface.",
    Answer_Summary=lettered(
        "thin, to allow efficient gas diffusion",
        "large surface area, to increase the rate of gas exchange",
        "moist, so gases can dissolve and diffuse easily",
        "richly supplied with blood vessels, to transport gases rapidly",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Respiratory Quotient)", Question="Given the respiration equation for tripalmitin (2C51H98O6 + 145O2 -> 102CO2 + 98H2O), what is its respiratory quotient (RQ)?",
    Answer_Summary=lettered(
        "RQ = volume of CO2 produced / volume of O2 consumed",
        "RQ = 102 / 145 = 0.7",
    ), Explanation=""))
rows.append(dict(Topic="Ear Structure (Cochlea)", Question="What are the parts of the cochlea labeled A to H, which parts make up the organ of Corti, and how is the organ of Corti adapted to its function?",
    Answer_Summary=lettered(
        "A: scala vestibuli, B: scala tympani, C: basilar membrane, D: Reissner's membrane, E: tectorial membrane, F: hair cells, G: spiral ganglion, H: organ of Corti",
        "the organ of Corti is made up of the hair cells, basilar membrane, and tectorial membrane",
        "hair cells with stereocilia detect vibrations and convert them into electrical signals",
        "the tectorial membrane interacts with the stereocilia for sound detection",
        "the basilar membrane vibrates at different frequencies to distinguish sounds",
        "its location within the cochlea keeps it exposed to the inner ear's pressure changes",
    ), Explanation=""))
rows.append(dict(Topic="Plant Tissues (Meristems)", Question="What is meristematic tissue, what types occur in dicot plants and where are they located, and what adaptations does xylem tissue have for its function?",
    Answer_Summary=lettered(
        "meristematic tissue: undifferentiated cells that keep dividing, enabling growth in length and girth",
        "apical meristem: at root/shoot tips, drives primary growth",
        "lateral meristem: in vascular cambium and cork cambium, drives secondary growth",
        "intercalary meristem: at the base of leaves/internodes, aids regrowth and elongation",
        "xylem adaptations: elongated hollow vessels for unimpeded water flow, lignified walls for support, pits for lateral water movement, and no cytoplasm to reduce resistance",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Ovum Structure)", Question="What are the parts of a mature mammalian ovum, and what role does each play?",
    Answer_Summary=lettered(
        "nucleus: central, holds the haploid genetic material for combining with sperm DNA at fertilization",
        "cytoplasm (ooplasm): nutrient-rich substance supporting early embryonic development",
        "zona pellucida: glycoprotein layer around the oocyte, handles species-specific sperm binding and blocks polyspermy after fertilization",
        "corona radiata: cumulus cells around the zona pellucida, supplying proteins and aiding sperm entry",
        "plasma membrane (oolemma): controls entry of ions/molecules, changes after fertilization to block extra sperm",
        "cortical granules: vesicles beneath the membrane that release contents at fertilization to modify the zona pellucida and prevent polyspermy",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Fertilization)", Question="Describe the events that take place during fertilization of a mature mammalian ovum.",
    Answer_Summary=lettered(
        "the sperm binds to the zona pellucida of the ovum",
        "the acrosome reaction releases enzymes that digest the zona pellucida",
        "the sperm penetrates the ovum membrane and its nucleus enters the cytoplasm",
        "the cortical reaction occurs, preventing polyspermy",
        "the sperm and ovum nuclei fuse, forming a diploid zygote",
    ), Explanation=""))
rows.append(dict(Topic="Digestion (Absorption and Liver)", Question="Why is active transport important in absorbing the end products of digestion, and what role does the liver play in digesting and metabolizing them?",
    Answer_Summary=lettered(
        "active transport lets nutrients be absorbed against their concentration gradient, so glucose, amino acids, and ions still reach the bloodstream even when gut levels are low",
        "liver converts excess glucose into glycogen for storage",
        "liver produces bile, which emulsifies fats for digestion and absorption",
        "liver detoxifies harmful substances, e.g. converting ammonia into urea",
        "liver metabolizes lipids, synthesizing cholesterol and breaking down fatty acids for energy",
        "liver stores vitamins and minerals like vitamin A and iron for later use",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis (Limiting Factors)", Question="Suggest the conditions under which light intensity, carbon dioxide concentration, and temperature may become limiting factors in photosynthesis, and explain how photorespiration affects the rate of photosynthesis.",
    Answer_Summary=lettered(
        "low light intensity limits the light-dependent reactions, reducing ATP/NADPH for the Calvin cycle",
        "low CO2 concentration reduces substrate for RuBisCO, limiting carbon fixation",
        "low temperature slows enzyme activity; high temperature can denature enzymes like RuBisCO",
        "photorespiration: when O2 binds RuBisCO instead of CO2, the Calvin cycle makes less glucose and releases CO2, wasting energy and lowering photosynthetic efficiency, especially in high O2/low CO2 conditions",
    ), Explanation=""))
rows.append(dict(Topic="Cell Biology (Cell as Basic Unit)", Question="Justify why a cell is said to be the basic unit of life.",
    Answer_Summary=lettered(
        "structural basis: all organisms are made of cells, uni- or multicellular",
        "functional unit: cells carry out life processes like metabolism, energy production, and waste removal",
        "reproduction: cells arise from pre-existing cells via mitosis/meiosis, continuing life",
        "genetic information: cells hold DNA, the genetic blueprint guiding development and function",
    ), Explanation=""))
rows.append(dict(Topic="Cell Structure (Organelle Roles)", Question="Explain three roles each played by the nucleus, lysosomes, and microtubules.",
    Answer_Summary=lettered(
        "nucleus: stores the cell's DNA; is where DNA is transcribed into mRNA for protein synthesis; its nucleolus assembles ribosomal subunits",
        "lysosomes: digest macromolecules via hydrolytic enzymes; break down damaged organelles (autophagy) for recycling; digest invading pathogens as a defense mechanism",
        "microtubules: give structural support as part of the cytoskeleton; act as tracks for intracellular transport via motor proteins; form the mitotic spindle to segregate chromosomes during division",
    ), Explanation=""))
rows.append(dict(Topic="Cell Structure (Membrane-Bound Organelles)", Question="Describe four advantages of membrane-bound organelles.",
    Answer_Summary=lettered(
        "compartmentalization: creates distinct environments so specialized functions run without interference",
        "increased surface area for biochemical reactions, boosting metabolic capacity",
        "concentrates substrates and enzymes locally, speeding up reactions",
        "isolates harmful substances/reactions from the rest of the cell, e.g. lysosome enzymes kept away from the cytoplasm",
    ), Explanation=""))
rows.append(dict(Topic="Plant Transport (Transpiration Factors)", Question="Explain four internal and four external factors affecting transpiration.",
    Answer_Summary=lettered(
        "leaf surface area: larger leaves transpire more; plants can adjust leaf size or shed leaves",
        "stomatal density/distribution: more stomata mean more water vapor loss",
        "cuticle thickness: a thicker waxy cuticle reduces water loss",
        "leaf orientation: orienting away from direct sun lowers leaf temperature and reduces transpiration",
        "temperature: higher temperature increases evaporation and transpiration",
        "humidity: low humidity steepens the moisture gradient, increasing transpiration",
        "wind speed: wind removes the saturated air layer around the leaf, maintaining the gradient",
        "light intensity: light opens stomata for CO2 entry, which also lets water vapor escape",
    ), Explanation=""))
rows.append(dict(Topic="Plant Transport (Transpiration Effects)", Question="Give an account of five effects of transpiration in plants.",
    Answer_Summary=lettered(
        "cooling: evaporation from leaves dissipates heat, regulating plant temperature",
        "nutrient uptake: transpiration creates negative pressure in the xylem, pulling water and minerals upward",
        "turgor maintenance: continuous water flow keeps cells turgid for support and growth",
        "stomatal function: transpiration balances water loss against gas exchange needs",
        "soil moisture depletion: high transpiration can lower soil moisture, causing water stress if not replenished",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Body Balance)", Question="Account for the mechanism of body balance in mammals.",
    Answer_Summary=lettered(
        "the vestibular system in the inner ear (three semicircular canals plus the utricle and saccule) detects rotation and linear acceleration",
        "endolymph fluid shifts in the canals as the head moves, bending hair cells that signal the brain about motion/orientation",
        "proprioception (receptors in muscles, tendons, joints) feeds the brain continuous info on limb position and muscle tension",
        "vision contributes position information, integrated with vestibular/proprioceptive input, e.g. via the vestibulo-ocular reflex stabilizing gaze during head movement",
        "the cerebellum and brainstem integrate all this input to fine-tune movement and maintain balance",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Oestrus Cycle)", Question="Define oestrus, describe the stages of the oestrus cycle, explain its significance, and distinguish it from the menstrual cycle.",
    Answer_Summary=lettered(
        "oestrus ('heat') is the phase in non-primate female mammals when they become sexually receptive and able to conceive",
        "proestrus: follicles mature, estrogen rises, uterine lining thickens; not yet receptive",
        "estrus: peak estrogen, female receptive, ovulation occurs",
        "metestrus/diestrus: corpus luteum forms and secretes progesterone; regresses if no fertilization",
        "anestrus: a resting/repair period between cycles",
        "significance: synchronizes mating with ovulation, boosting conception odds and reproductive success",
        "vs. menstrual cycle: oestrus occurs in non-primates and the endometrium is reabsorbed if no conception; the menstrual cycle occurs in primates/humans, sheds the endometrium as menstruation, and allows sexual activity throughout the cycle",
    ), Explanation=""))

# ============================== YEAR 2012 ==============================
rows.append(dict(Topic="Biomolecules (Lipids)", Question="State any four functions of lipids in living organisms.",
    Answer_Summary=lettered(
        "energy storage: lipids store more energy per gram than carbohydrates or proteins",
        "insulation: adipose tissue insulates the body and helps maintain temperature",
        "protection: lipids cushion and protect vital organs from physical damage",
        "structural role: lipids are key components of cell membranes, maintaining fluidity and integrity",
    ), Explanation=""))
rows.append(dict(Topic="Cell Structure (Plasma Membrane)", Question="Outline four roles of the plasma membrane of a cell.",
    Answer_Summary=lettered(
        "regulates movement of substances in and out, maintaining homeostasis",
        "enables communication via receptors for cell signaling",
        "compartmentalizes the cell, separating internal components from the environment",
        "carries out passive and active transport of molecules",
    ), Explanation=""))
rows.append(dict(Topic="Digestion (Glands and Disorders)", Question="Name the digestive glands in the buccal cavity and stomach with their secretions and roles, and state how to prevent peptic ulcers and heartburn.",
    Answer_Summary=lettered(
        "buccal cavity: salivary gland secretes saliva, which lubricates food and starts starch digestion (amylase)",
        "stomach: gastric gland secretes gastric juice, which breaks down proteins (pepsin) and activates enzymes",
        "prevent peptic ulcers: avoid excess NSAID use, reduce stress, treat H. pylori infection",
        "prevent heartburn: avoid overeating, maintain a healthy weight, cut down acidic/spicy foods",
    ), Explanation=""))
rows.append(dict(Topic="Cell Transport (Diffusion)", Question="Briefly explain five factors affecting the rate of diffusion across membranes.",
    Answer_Summary=lettered(
        "concentration gradient: a bigger gradient speeds up diffusion",
        "temperature: higher temperature increases molecular movement and diffusion",
        "surface area: a larger area allows more diffusion",
        "membrane thickness: thinner membranes diffuse more efficiently",
        "molecule size: smaller molecules diffuse faster than larger ones",
    ), Explanation=""))
rows.append(dict(Topic="Plant Transport (Root Pressure)", Question="Briefly explain the significance of root pressure.",
    Answer_Summary=lettered(
        "pushes water and nutrients from roots to the upper plant parts, especially when transpiration is low",
        "helps rehydrate xylem tissue",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Aerobic vs Anaerobic)", Question="Give four differences between aerobic and anaerobic respiration.",
    Answer_Summary=lettered(
        "oxygen requirement: aerobic needs oxygen; anaerobic does not",
        "end products: aerobic gives CO2 and water; anaerobic gives lactic acid or ethanol",
        "energy yield: aerobic produces more ATP than anaerobic",
        "location: aerobic occurs in mitochondria; anaerobic occurs in the cytoplasm",
    ), Explanation=""))
rows.append(dict(Topic="Metabolism (Body Mass and Oxygen Use)", Question="Why might a larger mammal consume the largest total volume of oxygen at rest despite a lower oxygen consumption per gram, while a smaller mammal needs much more oxygen per hour per gram of tissue?",
    Answer_Summary=lettered(
        "a larger body mass means a bigger total oxygen requirement even at a lower per-gram rate",
        "a smaller mammal typically has a higher metabolic rate, so it needs more oxygen per gram of tissue for its cellular processes",
    ), Explanation=""))
rows.append(dict(Topic="Endocrine System (Hormone Functions)", Question="Outline one function each for thyroxine, insulin, gibberellin, and auxins.",
    Answer_Summary=lettered(
        "thyroxine: regulates metabolic rate and growth",
        "insulin: regulates blood glucose by promoting glucose uptake into cells",
        "gibberellin: promotes seed germination and stem elongation",
        "auxins: regulate cell elongation and phototropism",
    ), Explanation=""))
rows.append(dict(Topic="Sensory Organs (Shared Functions)", Question="State one function that the sclerotic layer and bony labyrinth share, that eye lenses and basilar membranes share, and that rods, cones, and sensory hair cells share.",
    Answer_Summary=lettered(
        "sclerotic layer and bony labyrinth: both protect internal structures",
        "eye lenses and basilar membranes: both focus light or sound waves respectively",
        "rods, cones, and sensory hair cells: all detect sensory stimuli like light and sound",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Ovarian Follicle Development)", Question="What are the stages of ovarian follicle development, labeled primary follicle, secondary follicle, Graafian follicle, ovum, corpus luteum, and corpus albicans, and what is the correct developmental sequence?",
    Answer_Summary=lettered(
        "sequence: primary follicle -> secondary follicle -> Graafian follicle -> ovum -> corpus luteum -> corpus albicans",
        "the primary follicle develops into the secondary follicle, which matures into the Graafian follicle",
        "the ovum is released at ovulation, and the remaining follicle tissue forms the corpus luteum",
        "if fertilization doesn't occur, the corpus luteum degenerates into the corpus albicans",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Dynamic Classification)", Question="What reasons lead to a dynamic natural classification system?",
    Answer_Summary=lettered(
        "advances in scientific knowledge update classifications as new genetic/behavioral/ecological info emerges",
        "discovery of new species requires adjusting existing frameworks",
        "technological progress, e.g. molecular phylogenetics, reveals deeper evolutionary relationships",
        "reevaluation of evolutionary relationships from ongoing research leads to taxonomic revisions",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Natural vs Artificial)", Question="State the differences between natural and artificial classification systems.",
    Answer_Summary=lettered(
        "basis: natural classification uses evolutionary relationships/genetic similarity; artificial uses observable traits like morphology or habitat",
        "natural systems aim to reflect true phylogenetic relationships; artificial systems don't necessarily do so",
        "natural classification has predictive value about shared characteristics; artificial classification often doesn't",
        "natural classification is more flexible to new discoveries; artificial classification is more rigid",
    ), Explanation=""))
rows.append(dict(Topic="Enzymes (Properties)", Question="Explain the properties of enzymes.",
    Answer_Summary=lettered(
        "catalytic efficiency: speed up reactions by huge factors, enabling life processes under mild conditions",
        "specificity: each enzyme acts on a specific substrate or closely related group",
        "reversibility: many enzyme reactions are reversible, helping maintain metabolic balance",
        "sensitivity to conditions: activity depends on temperature, pH, and substrate concentration; extremes cause denaturation or reduced efficiency",
    ), Explanation=""))
rows.append(dict(Topic="Enzymes (Competitive Inhibition)", Question="In what way is knowledge of competitive inhibition important?",
    Answer_Summary=lettered(
        "drug development: many drugs act as competitive inhibitors, e.g. methotrexate in cancer therapy",
        "metabolic regulation: helps cells finely control enzyme reaction rates as substrate availability changes",
        "toxicology: some toxins work via competitive inhibition, so understanding it helps develop antidotes",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Synapse Structure)", Question="Describe the structure of a synapse.",
    Answer_Summary=lettered(
        "presynaptic terminal: end of the transmitting neuron's axon, holds synaptic vesicles with neurotransmitters, releases them when an action potential arrives",
        "synaptic cleft: the ~20 nm gap between neurons, keeps transmission one-way and lets neurotransmitters diffuse across",
        "postsynaptic membrane: on the receiving neuron, has receptors that bind neurotransmitters and generate a new electrical signal",
    ), Explanation=""))
rows.append(dict(Topic="Plant Reproduction (Seed Propagation)", Question="Describe four advantages and three disadvantages of reproduction by seeds.",
    Answer_Summary=lettered(
        "advantage - genetic diversity: promotes variation, giving hybrids better adaptability",
        "advantage - long-term storage: seeds stay viable in storage until conditions improve",
        "advantage - disease resistance: seed propagation can yield virus-free plants",
        "advantage - cost-effectiveness: cheaper and simpler than other propagation methods",
        "disadvantage - genetic variability: hard to consistently retain specific superior traits",
        "disadvantage - longer maturation: seed-grown plants can take longer to mature than vegetatively propagated ones",
        "disadvantage - dormancy/germination issues: some seeds need special treatment or long dormancy before germinating",
    ), Explanation=""))
rows.append(dict(Topic="Endocrine System (Feedback Mechanisms)", Question="Discuss, with specific examples, the feedback mechanisms of hormonal coordination in animals.",
    Answer_Summary=lettered(
        "negative feedback counteracts a change to restore balance, e.g. insulin lowers blood glucose after a meal and glucagon raises it when it drops too low",
        "the HPA axis is another negative feedback example: CRH from the hypothalamus triggers ACTH, which triggers cortisol; high cortisol then suppresses CRH and ACTH",
        "positive feedback amplifies a change until a process completes, e.g. oxytocin increases uterine contractions during childbirth, which triggers more oxytocin release until delivery",
        "blood clotting is another positive feedback example: platelets attract more platelets at an injury site until a clot fully forms",
    ), Explanation=""))

# ============================== YEAR 2016 ==============================
rows.append(dict(Topic="Cell Structure (Chloroplast)", Question="Describe the structure of a chloroplast, labeling its main parts, and state three structural adaptations of the chloroplast to its role.",
    Answer_Summary=lettered(
        "outer membrane: smooth outer layer that protects and regulates material movement in/out",
        "inner membrane: beneath the outer membrane, also regulates passage of substances and holds transport proteins",
        "stroma: fluid matrix with enzymes, ribosomes, and chloroplast DNA; site of the Calvin cycle",
        "thylakoids: flattened disc structures stacked into grana, membranes hold chlorophyll for light-dependent reactions",
        "grana: stacks of thylakoids that increase surface area for light absorption",
        "adaptations: thylakoid membranes hold light-capturing pigments, grana stacking maximizes surface area, and the stroma's enzymes enable carbon fixation",
    ), Explanation=""))
rows.append(dict(Topic="Biomolecules (Amino Acids and Enzymes)", Question="What is the general name for the amino acid molecular formula (R-CH(NH2)-COOH), what is the simplest form of the R group, and what are six properties of enzymes?",
    Answer_Summary=lettered(
        "the formula represents an amino acid",
        "the simplest R group is hydrogen (H), giving the amino acid glycine",
        "specificity: enzymes match specific substrates, forming enzyme-substrate complexes",
        "catalytic efficiency: speed up reactions without being consumed",
        "optimum temperature/pH: each enzyme works best under specific conditions",
        "denaturation: lose function under extreme temperature or pH",
        "reusability: not consumed, so can be used repeatedly",
        "sensitivity to inhibitors: activity can be regulated or blocked by specific molecules",
    ), Explanation=""))
rows.append(dict(Topic="Enzymes (Temperature Effect)", Question="Discuss the effect of temperature on the rate of an enzyme-controlled reaction, and describe how ATP is formed.",
    Answer_Summary=lettered(
        "low temperature: enzymes have less kinetic energy, so reactions are slower",
        "rising temperature: more frequent enzyme-substrate collisions speed up the reaction",
        "very high temperature: enzymes denature as their 3D structure breaks down, stopping the reaction",
        "ATP is made of a ribose sugar, an adenine base, and three phosphate groups",
        "ATP forms via cellular respiration or photosynthesis, storing energy in its phosphate bonds; hydrolysis to ADP + Pi releases that energy",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Taxonomic Hierarchy)", Question="Define taxonomic hierarchy and illustrate it using man as an example.",
    Answer_Summary=lettered(
        "taxonomic hierarchy: classifying organisms into ranked levels by shared traits, from broadest (kingdom) to most specific (species)",
        "for humans: Kingdom Animalia, Phylum Chordata, Class Mammalia, Order Primates, Family Hominidae, Genus Homo, Species Homo sapiens",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Artificial System)", Question="Explain four advantages of using an artificial system of classification.",
    Answer_Summary=lettered(
        "simplicity: classifies by observable traits, easy to use",
        "ease of comparison: traits like flower color or leaf shape compare easily across species",
        "practical application: useful for identifying plants/animals in agriculture or horticulture",
        "quick identification: doesn't require deep genetic or evolutionary knowledge",
    ), Explanation=""))
rows.append(dict(Topic="Respiration and Photosynthesis (Comparison)", Question="State three similarities between respiration and photosynthesis, and explain what happens to the rate of respiration if temperature rises above the optimal point or if an organism's health is impaired.",
    Answer_Summary=lettered(
        "both exchange gases, with oxygen and carbon dioxide involved",
        "both happen in specific organelles: mitochondria for respiration, chloroplasts for photosynthesis",
        "both rely on electron transport chains to produce ATP",
        "above-optimal temperature: rate first rises, then falls as enzymes denature and the reaction halts",
        "impaired health: respiration rate can decline from reduced metabolic activity or damaged respiratory enzymes, lowering energy production",
    ), Explanation=""))
rows.append(dict(Topic="Cell Transport (Osmosis)", Question="Between two solutions of different solute concentration, which has higher water potential, which has higher solute potential, which way will osmosis occur, and what are the roles of osmosis in living organisms?",
    Answer_Summary=lettered(
        "the solution with less solute has the higher water potential (more free water molecules)",
        "the solution with more solute has the higher solute potential (lower water potential)",
        "osmosis moves water from the higher water potential solution to the lower one, across the partially permeable membrane",
        "role: lets plant roots absorb water from soil",
        "role: maintains turgidity for mechanical support in non-woody plant parts",
        "role: regulates water movement in/out of cells, preventing bursting or shrinking",
        "role: supports kidney function in animals via water reabsorption for fluid balance",
    ), Explanation=""))
rows.append(dict(Topic="Cell Division (Mitosis vs Meiosis)", Question="Give five differences between mitosis and meiosis, and state two significances of meiosis in sexually reproducing organisms.",
    Answer_Summary=lettered(
        "mitosis occurs in somatic cells; meiosis occurs in germ cells",
        "mitosis makes two identical daughter cells; meiosis makes four genetically different haploid cells",
        "mitosis is one division; meiosis is two divisions (meiosis I and II)",
        "mitosis keeps the parent's chromosome number; meiosis halves it",
        "crossing over happens in meiosis (creating variation) but not in mitosis",
        "significance: meiosis produces haploid gametes, keeping the chromosome number stable across generations at fertilization",
        "significance: crossing over and independent assortment introduce genetic variation, important for evolution and adaptability",
    ), Explanation=""))
rows.append(dict(Topic="Plant Transport (Water Pathways)", Question="Describe the symplast, vacuolar, and apoplast pathways of water and mineral movement across the root, and explain five roles of water in plants.",
    Answer_Summary=lettered(
        "symplast: water/solutes move through the cytoplasm, cell to cell via plasmodesmata",
        "vacuolar: water moves from vacuole to vacuole, crossing the tonoplast between cells",
        "apoplast: water moves through cell walls and intercellular spaces without entering the cytoplasm, until the Casparian strip forces it into the symplast at the endodermis",
        "role: water is a reactant in photosynthesis, providing hydrogen for glucose production",
        "role: acts as a solvent, dissolving nutrients for transport in xylem and phloem",
        "role: maintains turgidity, supporting leaves and stems",
        "role: regulates temperature through transpiration cooling",
        "role: aids seed germination by activating enzymes and softening the seed coat",
    ), Explanation=""))
rows.append(dict(Topic="Cell Structure (Bacterial Cell)", Question="What are the parts of a bacterial cell labeled A to G, and what are five differences between a bacterial cell and a trypanosome cell?",
    Answer_Summary=lettered(
        "A: flagellum, B: capsule, C: cell wall, D: plasma membrane, E: cytoplasm, F: ribosomes, G: nucleoid (genetic material)",
        "the bacterial cell is prokaryotic; the trypanosome cell is eukaryotic",
        "bacteria lack membrane-bound organelles; trypanosomes have organelles like a nucleus and mitochondria",
        "bacterial genetic material isn't enclosed in a nucleus; the trypanosome's is enclosed in a nuclear membrane",
        "bacteria have a rigid cell wall; trypanosomes have a flexible pellicle instead of a cell wall",
        "bacteria reproduce by binary fission; trypanosomes reproduce by mitosis and cytokinesis",
    ), Explanation=""))
rows.append(dict(Topic="Muscle Tissue (Cardiac Muscle)", Question="Describe how the structure of cardiac muscle is adapted to its function.",
    Answer_Summary=lettered(
        "branched fibers let electrical impulses spread in multiple directions for synchronized contractions",
        "intercalated discs (gap junctions plus desmosomes) allow electrical communication and mechanical strength between cells",
        "striations from organized actin/myosin filaments (sarcomeres) allow efficient contraction",
        "a single central nucleus per cell optimizes genetic material distribution",
        "abundant mitochondria supply the continuous ATP needed for nonstop heart contractions",
        "involuntary control by the autonomic nervous system keeps the heart beating without conscious effort",
    ), Explanation=""))
rows.append(dict(Topic="Biomolecules (Protein Functions)", Question="Name the chemical composition of proteins and explain six categories of protein based on their functions.",
    Answer_Summary=lettered(
        "composition: carbon, hydrogen, oxygen, nitrogen, and sometimes sulfur; amino acids linked by peptide bonds",
        "structural: support cells/tissues, e.g. collagen, keratin",
        "enzymatic: catalyze reactions, e.g. amylase",
        "transport: carry molecules, e.g. hemoglobin",
        "defensive: protect against pathogens, e.g. antibodies",
        "regulatory: control cellular processes, e.g. insulin",
        "contractile: enable movement, e.g. actin and myosin",
    ), Explanation=""))

# ============================== YEAR 2017 ==============================
rows.append(dict(Topic="Cell Structure (Plasma Membrane)", Question="What are the parts of the plasma membrane (fluid mosaic model) labeled A to D, what are four functions of an integral protein, and what are three functions of microtubules?",
    Answer_Summary=lettered(
        "A: phospholipid bilayer, B: integral protein, C: peripheral protein, D: cholesterol",
        "integral protein: acts as a channel/transporter for molecules across the membrane",
        "integral protein: acts as a receptor for cell signaling, e.g. binding hormones",
        "integral protein: can act as an enzyme, catalyzing reactions at the membrane surface",
        "integral protein: anchors the cytoskeleton, giving structural support",
        "microtubules: give structural support and maintain cell shape",
        "microtubules: enable intracellular transport of organelles and vesicles",
        "microtubules: form the mitotic spindle for chromosome separation during division",
    ), Explanation=""))
rows.append(dict(Topic="Cell Biology (Cyanobacteria vs Yeast)", Question="Analyze the differences between cyanobacteria and yeast cells in cell division, respiration, photosynthesis, and protein synthesis, and give five similarities between mitochondria and chloroplasts.",
    Answer_Summary=lettered(
        "cell division: cyanobacteria divide by binary fission (no nucleus); yeast divides by budding (has a nucleus and eukaryotic organelles)",
        "respiration: cyanobacteria respire aerobically or anaerobically without mitochondria; yeast respires aerobically in mitochondria and can ferment anaerobically",
        "photosynthesis: cyanobacteria are photosynthetic using chlorophyll and thylakoids; yeast is non-photosynthetic",
        "protein synthesis: cyanobacteria use 70S ribosomes in the cytoplasm; yeast uses 80S ribosomes in the cytoplasm and rough ER",
        "mitochondria/chloroplast similarities: both have a double membrane, their own DNA, ribosomes, generate energy (ATP or glucose), and have folded inner membranes (cristae or thylakoids) for extra surface area",
    ), Explanation=""))
rows.append(dict(Topic="Biomolecules (Protein Testing and Denaturation)", Question="How do you test for protein using the Biuret test and what is its chemical basis, and how do heat, acid, alkalis, mechanical force, and chemical agents each cause protein denaturation?",
    Answer_Summary=lettered(
        "Biuret test: add sodium hydroxide to make the sample alkaline, then add copper sulfate; a purple color means protein is present, blue means none",
        "basis: peptide bonds react with copper ions in alkaline solution to give a violet/purple color",
        "heat: disrupts hydrogen bonds and non-covalent interactions, unfolding the protein",
        "acid: alters pH, disrupting ionic and hydrogen bonds, changing the protein's shape",
        "alkalis: disrupt hydrogen bonds and ionic interactions by changing pH, altering tertiary structure",
        "mechanical force (e.g. stirring/shaking): breaks the weak bonds stabilizing the structure",
        "chemical agents (e.g. urea, detergents): disrupt hydrophobic interactions and hydrogen bonds, unfolding the protein",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Synapse Structure)", Question="What are the parts of a synapse labeled T, U, V, W, X, and Z, what state is region Y in, what roles do U and W play, and why do some impulses fail to trigger an action potential while several in succession succeed?",
    Answer_Summary=lettered(
        "T: axon terminal, U: synaptic vesicles, V: neurotransmitters, W: calcium ion channels, X: synaptic cleft, Z: postsynaptic membrane",
        "Y: the presynaptic membrane, active and releasing neurotransmitters when calcium ions flow in",
        "U (synaptic vesicles): store and release neurotransmitters into the synaptic cleft when triggered",
        "W (calcium ion channels): let calcium into the presynaptic neuron, triggering neurotransmitter release",
        "a single weak impulse may not release enough neurotransmitter to reach threshold, but successive impulses summate (temporally/spatially), building up enough neurotransmitter to cross the threshold and fire an action potential",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis (Light Reactions and Factors)", Question="Explain the roles of NADP, ribulose diphosphate (RuBP), and photosystems I and II in photosynthesis; explain the effect of lowering oxygen concentration on C3 and C4 photosynthesis; and explain why the rate of photosynthesis decreases at high temperatures.",
    Answer_Summary=lettered(
        "NADP accepts electrons in the light reactions to form NADPH, supplying reducing power for the Calvin cycle",
        "RuBP is the 5-carbon substrate that combines with CO2 (via RuBisCO) in carbon fixation, forming 3-phosphoglycerate",
        "PSII splits water into oxygen, protons, and electrons (photolysis); PSI excites electrons that go on to form NADPH; together they generate ATP and NADPH",
        "lower oxygen boosts C3 photosynthesis by reducing photorespiration (less RuBisCO binding O2 instead of CO2)",
        "C4 photosynthesis is less affected by lower oxygen since it already concentrates CO2 near the Calvin cycle, limiting RuBisCO-oxygen interaction",
        "high temperature denatures enzymes like RuBisCO and closes stomata (from faster water loss), cutting CO2 supply, both lowering the photosynthesis rate",
    ), Explanation=""))
rows.append(dict(Topic="Cell Structure (Animal Cell Organelles)", Question="Describe the structure of an animal cell as seen under an electron microscope, and name a double-membrane organelle found only in plant cells and explain how it's adapted to its role.",
    Answer_Summary=lettered(
        "nucleus: control center holding DNA, regulates gene expression and division",
        "nucleolus: inside the nucleus, makes rRNA and assembles ribosomes",
        "mitochondria: generate ATP via cellular respiration",
        "endoplasmic reticulum: rough ER (with ribosomes) makes/modifies proteins; smooth ER makes lipids, detoxifies, stores calcium",
        "Golgi apparatus: modifies, sorts, and packages proteins/lipids for delivery",
        "lysosomes: digest macromolecules, old cell parts, and invaders with hydrolytic enzymes",
        "centrioles: organize microtubules in division and form the base of cilia/flagella",
        "ribosomes: make proteins, free in the cytoplasm or attached to rough ER",
        "plasma membrane: phospholipid bilayer controlling what moves in/out of the cell",
        "cytoplasm: gel-like substance holding the organelles",
        "plant-only double-membrane organelle: the chloroplast, adapted with a double membrane, a stroma holding Calvin-cycle enzymes, thylakoids stacked into grana for light absorption, and its own DNA/ribosomes for making photosynthesis proteins",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Natural System)", Question="What is meant by a natural system of classification, and why is it difficult to achieve a complete one?",
    Answer_Summary=lettered(
        "natural classification groups organisms by evolutionary relationships, structural similarity, and shared genetic ancestry into hierarchical taxa (kingdom to species)",
        "it's hard to complete because of the huge diversity of organisms, many still undiscovered",
        "evolutionary relationships are often unclear due to limited fossil evidence or convergent evolution",
        "genetic variation and horizontal gene transfer in microorganisms further complicate classification",
    ), Explanation=""))
rows.append(dict(Topic="Circulatory System (Exercise Response)", Question="Explain the main adjustments to heart rate and the circulatory system just before, during, and after a 100m race.",
    Answer_Summary=lettered(
        "before: sympathetic activation raises heart rate and cardiac output in anticipation; adrenaline causes vasodilation in skeletal muscles and vasoconstriction elsewhere",
        "during: heart rate peaks, stroke volume rises, blood is directed to active muscles, and respiratory rate increases to match oxygen demand",
        "after: heart rate gradually falls as the parasympathetic system restores normal function; blood vessels dilate to clear lactic acid and repay the oxygen debt",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Capacitation and Placenta)", Question="Briefly explain capacitation in reproduction, and outline two protective roles of the mammalian placenta for the fetus.",
    Answer_Summary=lettered(
        "capacitation: changes sperm undergo in the female tract that boost motility and prepare it for the acrosomal reaction, needed to fertilize the egg",
        "placenta role 1: acts as a barrier protecting the fetus from toxins and pathogens in maternal blood",
        "placenta role 2: suppresses the mother's immune response so it doesn't attack fetal tissue",
    ), Explanation=""))
rows.append(dict(Topic="Plant Reproduction (Chromosome Numbers)", Question="If the chromosome number in a radicle of a flowering plant species is 16, what is the chromosome number in its pollen tube nucleus, antipodal cell, endosperm, pollen mother cell, and integument cell?",
    Answer_Summary=lettered(
        "pollen tube nucleus: 16 (haploid)",
        "antipodal cell: 16 (haploid)",
        "endosperm: 24 (triploid, from one sperm nucleus fusing with two polar nuclei)",
        "pollen mother cell: 32 (diploid, the precursor that divides into haploid gametes)",
        "integument cell: 32 (diploid, part of the seed coat)",
    ), Explanation=""))
rows.append(dict(Topic="Plant Transport (Vascular Tissue Adaptations)", Question="Identify the vascular tissues in plants and explain how they are adapted to their roles.",
    Answer_Summary=lettered(
        "xylem: dead cells (vessels/tracheids) forming hollow, lignified tubes that carry water and minerals upward while resisting collapse under tension",
        "phloem: living sieve tube elements connected by sieve plates, carrying sap (sucrose) between plant parts, supported by companion cells that provide energy for active transport",
    ), Explanation=""))

# ============================== YEAR 2018 ==============================
rows.append(dict(Topic="Cell Structure (Membrane and Mitochondria)", Question="Describe the features of the cell membrane, and assess the suitability of the structure of a mitochondrion to its function (five points).",
    Answer_Summary=lettered(
        "cell membrane: a semi-permeable phospholipid bilayer with hydrophobic tails inward and hydrophilic heads outward, embedded proteins for transport/signaling/enzymes, cholesterol for stability/fluidity, and carbohydrate chains for cell recognition",
        "mitochondrion: double membrane with folded cristae increases surface area for the electron transport chain",
        "the matrix holds Krebs cycle enzymes for breaking down metabolites to make ATP",
        "the intermembrane space lets protons build up, creating the gradient needed for ATP synthesis",
        "mitochondrial DNA and ribosomes let it make some of its own proteins",
        "its elongated shape gives a large surface area-to-volume ratio for energy production and distribution",
    ), Explanation=""))
rows.append(dict(Topic="Biomolecules (Carbohydrate Groups and Testing)", Question="State three importance of pentose, hexose, and disaccharide sugars in living things, and explain the role of dilute hydrochloric acid and dilute sodium hydroxide in testing carbohydrates.",
    Answer_Summary=lettered(
        "pentoses (e.g. ribose, deoxyribose): form the backbone of RNA/DNA, are part of ATP, and are intermediates in the pentose phosphate pathway making NADPH",
        "hexoses (e.g. glucose, fructose): main energy source in respiration and building blocks for disaccharides/polysaccharides",
        "disaccharides (e.g. sucrose, lactose, maltose): transport energy in plants, provide nutrition in milk, or are intermediates in starch/glycogen digestion",
        "dilute hydrochloric acid: hydrolyzes disaccharides/polysaccharides into monosaccharides so non-reducing sugars can be tested via Benedict's",
        "dilute sodium hydroxide: neutralizes the solution after HCl hydrolysis so the pH suits the Benedict's test",
    ), Explanation=""))
rows.append(dict(Topic="Coordination (Nervous vs Hormonal)", Question="Distinguish nervous from hormonal coordination (four points) and positive from negative feedback in body temperature regulation (two points), and examine four properties of a hormone that let it do its job.",
    Answer_Summary=lettered(
        "nervous coordination uses electrical impulses via neurons; hormonal coordination uses chemical messengers in the blood",
        "nervous responses are fast and short-lived; hormonal responses are slower but longer-lasting",
        "nervous coordination targets specific cells via synapses; hormones can reach many target cells with the right receptors",
        "nervous coordination handles immediate responses; hormonal coordination regulates long-term processes like growth",
        "positive feedback amplifies a response, e.g. shivering to generate more heat when cold",
        "negative feedback reduces deviation from normal, e.g. sweating to cool an overheated body, and stabilizes the system",
        "hormone properties: highly specific to target cells with matching receptors, effective in small amounts, stable enough to travel in blood, and versatile across many physiological processes",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis (Equation and Factors)", Question="Give two reasons the balanced photosynthesis equation (6CO2 + 6H2O -> C6H12O6 + 6O2) isn't fully correct, identify the two types of photosynthesis reactions and where each occurs, and explain how temperature and inorganic ions affect the rate of photosynthesis.",
    Answer_Summary=lettered(
        "the equation oversimplifies by skipping intermediate steps like ATP/NADPH formation, and it doesn't show that the released oxygen comes from water, not CO2",
        "light-dependent reactions happen in the thylakoid membranes, producing ATP and NADPH",
        "light-independent reactions (Calvin cycle) happen in the stroma, fixing CO2 into glucose",
        "temperature: low temperature slows enzyme activity; high temperature can denature enzymes, lowering the photosynthesis rate",
        "inorganic ions: magnesium is part of chlorophyll and manganese is needed for the photolysis of water, so both are essential cofactors",
    ), Explanation=""))
rows.append(dict(Topic="Biomolecules (Carbohydrate Functions)", Question="Identify two categories of carbohydrates, and describe six functions of carbohydrates in organisms with an example for each.",
    Answer_Summary=lettered(
        "categories: simple carbohydrates (monosaccharides/disaccharides) and complex carbohydrates (polysaccharides)",
        "primary energy source: glucose is broken down for ATP",
        "energy storage: glycogen (animals) and starch (plants) store energy for later use",
        "structural support: cellulose in plant cell walls, chitin in arthropod exoskeletons/fungal walls",
        "component of nucleic acids: ribose in RNA, deoxyribose in DNA",
        "cell recognition/signaling: glycoproteins and glycolipids on cell surfaces, e.g. blood group antigens",
        "protein sparing: enough carbohydrate intake stops the body breaking down protein for energy",
    ), Explanation=""))
rows.append(dict(Topic="Plant Hormones (Phytohormones)", Question="What is a phytohormone, and what are three roles each of auxins, gibberellins, and cytokinins?",
    Answer_Summary=lettered(
        "phytohormone: a natural plant compound made in small amounts that regulates growth, development, and responses to stimuli",
        "auxins: promote cell elongation (phototropism/gravitropism), enforce apical dominance by suppressing lateral buds, and stimulate root initiation",
        "gibberellins: promote stem elongation, break seed dormancy, and stimulate flowering/fruit development",
        "cytokinins: promote cell division, delay leaf senescence, and work with auxins to regulate root/shoot formation",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Constructing a Key)", Question="Given observable features (wings, antennae, leg pairs) for organisms S3-S7 (S3: 2 wing pairs, antennae, 3 leg pairs, no 4 leg pairs; S4: no wings, antennae, no 3 leg pairs, 4 leg pairs; S5: no wings, no antennae, no 3 leg pairs, 4 leg pairs; S6: 2 wing pairs, antennae, 3 leg pairs, no 4 leg pairs; S7: no wings, antennae, no 3 leg pairs, 4 leg pairs), construct a simple bracketed key to identify them.",
    Answer_Summary=lettered(
        "1a) wings present -> go to 2; 1b) wings absent -> go to 3",
        "2a) two pairs of wings -> S3; 2b) one pair of wings -> S6",
        "3a) three pairs of legs -> S4; 3b) four pairs of legs -> go to 4",
        "4a) antennae present -> S7; 4b) antennae absent -> S5",
    ), Explanation=""))
rows.append(dict(Topic="Transport (Movement of Materials)", Question="Explain the concepts of active transport, closed circulatory system, symplast, and apoplast as used in the movement of materials in an organism's body.",
    Answer_Summary=lettered(
        "active transport: moves substances against their concentration gradient using ATP-powered carrier proteins/pumps",
        "closed circulatory system: blood stays within vessels in a continuous circuit, giving higher pressure and efficient delivery",
        "symplast: the interconnected cytoplasm of plant cells linked by plasmodesmata, moving water/ions/solutes without crossing membranes",
        "apoplast: the non-living cell walls and intercellular spaces where water/solutes move without crossing the cell membrane, enabling rapid water movement",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Fertilization Mechanism)", Question="Describe the events that make up the mechanism of fertilization in mammals.",
    Answer_Summary=lettered(
        "ovulation releases a mature egg into the fallopian tube",
        "sperm deposited during copulation travels toward the egg guided by chemical signals",
        "the acrosomal reaction releases enzymes that digest the corona radiata and zona pellucida",
        "the sperm fuses with the egg's membrane and its nucleus enters",
        "the cortical reaction alters the zona pellucida to block further sperm entry",
        "the sperm and egg nuclei fuse into a diploid zygote, which divides while moving to the uterus to implant",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Metabolic Pathways)", Question="Define respiratory quotient (RQ), and for glycolysis, the Krebs cycle, and alcoholic fermentation, state where in the cell each occurs, its substrates, and its products; also explain how temperature and organism size affect the rate of respiration.",
    Answer_Summary=lettered(
        "RQ: the ratio of CO2 produced to O2 consumed during respiration, showing which substrate (carbs, fats, protein) is being used",
        "glycolysis: in the cytoplasm, uses glucose, produces pyruvate, ATP, and NADH",
        "Krebs cycle: in the mitochondrial matrix, uses acetyl-CoA, produces ATP, NADH, FADH2, and CO2",
        "alcoholic fermentation: in the cytoplasm, uses glucose, produces ethanol, CO2, and ATP",
        "temperature: low temperature slows enzyme activity and respiration; rate rises to an optimum then falls as enzymes denature at high temperatures",
        "organism size: smaller organisms have higher metabolic rates and need more energy per unit mass, so they respire faster; larger organisms respire more slowly relative to size",
    ), Explanation=""))

# ============================== YEAR 2019 ==============================
rows.append(dict(Topic="Cell Structure (Bacterial Cell)", Question="What are the parts of a bacterial cell labeled U, V, W, and X and their roles, and what broader roles does the bacterial cell play (e.g. in ecosystems, research, and industry)?",
    Answer_Summary=lettered(
        "U: capsule, protects from desiccation and the host immune system",
        "V: cell wall, gives structural support and protects from mechanical damage and osmotic lysis",
        "W: plasma membrane, regulates what moves in/out, maintaining homeostasis",
        "X: cytoplasm, site of biochemical reactions, houses ribosomes and genetic material",
        "bacteria drive nutrient cycling and decomposition of organic matter in ecosystems",
        "bacteria form symbiotic relationships, e.g. nitrogen fixation in legumes that supports plant growth",
        "bacteria serve as model organisms in molecular biology and genetics research",
        "bacteria are used industrially in fermentation and antibiotic production",
    ), Explanation=""))
rows.append(dict(Topic="Biomolecules (Sugar Testing and Composition)", Question="Explain the procedure for testing non-reducing sugar in a solution, and analyze the chemical composition of lipids and proteins.",
    Answer_Summary=lettered(
        "first test with Benedict's solution for reducing sugar; if no precipitate, hydrolyze with dilute HCl and heat to break glycosidic bonds into reducing sugars",
        "neutralize with sodium hydroxide, then add Benedict's solution again and heat; a brick-red precipitate confirms non-reducing sugar",
        "lipids: mainly carbon, hydrogen, and oxygen, hydrophobic, used for energy storage, membrane structure (phospholipids), and signaling (steroids)",
        "proteins: amino acids linked by peptide bonds, containing carbon, hydrogen, oxygen, nitrogen, and sometimes sulfur; function as enzymes, structural components, transporters, and signaling molecules",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Taxonomic Hierarchy)", Question="Identify the lowest taxon, illustrate the taxonomic hierarchy of humans, explain why classification of organisms is needed, and analyze three differences between natural and artificial classification systems.",
    Answer_Summary=lettered(
        "lowest taxon: species",
        "human hierarchy: Domain Eukarya, Kingdom Animalia, Phylum Chordata, Class Mammalia, Order Primates, Family Hominidae, Genus Homo, Species sapiens",
        "classification is needed to organize the diversity of life, show evolutionary relationships, and standardize naming across scientists",
        "natural classification groups by evolutionary relationships and is more universally informative; artificial classification groups by observable traits like size/color and can group unrelated species superficially",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Receptors and Impulse Speed)", Question="Identify four main types of receptors and their roles, and describe how axon diameter and myelin sheath affect nerve impulse transmission.",
    Answer_Summary=lettered(
        "mechanoreceptors detect pressure/vibration/touch",
        "chemoreceptors respond to chemical stimuli like blood pH changes",
        "thermoreceptors detect temperature changes",
        "photoreceptors respond to light, enabling vision",
        "larger axon diameter conducts impulses faster due to lower electrical resistance",
        "myelin sheath speeds transmission via saltatory conduction, letting the signal jump between nodes of Ranvier",
    ), Explanation=""))
rows.append(dict(Topic="Digestion (Villus Structure)", Question="What tissue is shown in a small intestine cross-section (villus with columnar epithelium), what role does it play in digestion, how does its structure relate to its function, what three features of the ileum increase its surface area, and why is a large surface area an advantage?",
    Answer_Summary=lettered(
        "tissue: the villus epithelium of the small intestine, lined with columnar epithelial cells",
        "villi increase surface area for absorbing nutrients like glucose, amino acids, and fatty acids; epithelial cells secrete enzymes for final digestion",
        "microvilli form a brush border adding even more surface area; epithelial cells are rich in mitochondria for active transport; a dense capillary network carries absorbed nutrients into the blood",
        "ileum surface-area features: villi, microvilli (brush border), and plicae circulares (folds that slow food movement, giving more time for absorption)",
        "advantage of large surface area: maximizes nutrient absorption for energy/growth, and speeds up water/electrolyte uptake for fluid balance",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Neuron Types and Synapse Direction)", Question="State the function of motor, sensory, and relay neurons, explain how receptors communicate with effectors, and describe how the synapse structure ensures one-way signal transmission.",
    Answer_Summary=lettered(
        "motor neurons: carry impulses from the CNS to effectors like muscles/glands",
        "sensory neurons: carry signals from receptors to the CNS",
        "relay (inter)neurons: connect sensory and motor neurons within the CNS, processing information",
        "receptors detect a stimulus and generate impulses that travel via sensory neurons to the CNS, which sends commands via motor neurons to effectors",
        "one-way transmission: neurotransmitter vesicles sit only on the presynaptic side and receptors only on the postsynaptic side, so signals can only cross the cleft in one direction",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis (Light and Dark Reactions)", Question="Evaluate the importance of the light and dark reaction processes of photosynthesis to life.",
    Answer_Summary=lettered(
        "the light reaction (thylakoid membranes) captures solar energy into ATP and NADPH, and splits water to release oxygen for aerobic respiration",
        "the dark reaction (Calvin cycle, in the stroma) uses that ATP/NADPH to fix CO2 into glucose",
        "glucose from the dark reaction fuels plant growth and, through the food chain, herbivores and carnivores",
        "together, the two reactions sustain life by supplying energy, oxygen, and organic matter",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Oestrogen and Birth Stages)", Question="State three roles of oestrogen in reproduction, and identify and describe the three stages of birth.",
    Answer_Summary=lettered(
        "oestrogen thickens the uterine endometrium for possible implantation",
        "oestrogen promotes maturation of ovarian follicles, enabling ovulation",
        "oestrogen drives female secondary sexual characteristics like mammary gland growth and hip widening",
        "stage 1 (dilation): the cervix dilates and thins as contractions build, ending at full dilation (~10 cm)",
        "stage 2 (expulsion): strong contractions and pushing deliver the baby, head first",
        "stage 3 (placental): the placenta, umbilical cord, and membranes are expelled shortly after birth",
    ), Explanation=""))
rows.append(dict(Topic="Plant Structure (Stomata)", Question="Describe the structure and functioning of stomata.",
    Answer_Summary=lettered(
        "guard cells: kidney-shaped (dicots) or dumbbell-shaped (monocots) cells with chloroplasts, whose thicker inner walls control opening/closing",
        "stomatal pore: the central opening between guard cells for gas exchange",
        "subsidiary cells: adjacent epidermal cells that support and help regulate the guard cells",
        "epidermal cells: outer layer surrounding the stomata, giving general protection",
        "function: lets CO2 in for photosynthesis and O2 out; regulates water loss through transpiration; helps maintain internal gas balance",
        "the pore opens when guard cells take up water and become turgid, and closes when they lose water and go flaccid, controlled by light, CO2 level, and internal signals",
    ), Explanation=""))
rows.append(dict(Topic="Plant Reproduction (Carpel Structure and Fertilization)", Question="What parts of a mature carpel receive the pollen grain, transfer it to the ovule, fuse with the male gamete, attach the ovule to the ovary, protect the egg cell, control pollen tube growth, fertilize the female gamete, and fuse with the male nucleus to form the endosperm, and what events make up double fertilization in plants?",
    Answer_Summary=lettered(
        "stigma: receives the pollen grain",
        "style: transfers/guides the pollen tube to the ovule",
        "egg cell (in the ovule): fuses with a sperm nucleus to form the zygote",
        "funiculus: attaches the ovule to the ovary wall",
        "ovary wall: protects the egg cell and later becomes the fruit",
        "pollen tube nucleus: fertilizes the female gamete by guiding the sperm cells down",
        "polar nuclei: fuse with the second sperm nucleus to form the triploid endosperm",
        "double fertilization: the pollen tube delivers two sperm cells; one fuses with the egg cell to form a diploid zygote, and the other fuses with the two polar nuclei to form the endosperm that nourishes the embryo",
    ), Explanation=""))

# ============================== YEAR 2020 ==============================
rows.append(dict(Topic="Cell Structure (Plant Cell Organelles)", Question="Which parts of a generalised plant cell are responsible for strengthening the cell, controlling exchange with the environment, providing energy, protein synthesis, food manufacture, and controlling cell activities; what four structures occur in plant but not animal cells; and why are phagocytosis, pinocytosis, and exocytosis important to a cell?",
    Answer_Summary=lettered(
        "strengthening: cell wall, gives mechanical support and shape",
        "controlling exchange: cell (plasma) membrane, regulates substances in/out",
        "energy: mitochondria, the site of cellular respiration producing ATP",
        "protein synthesis: ribosomes",
        "food manufacture: chloroplasts, carry out photosynthesis",
        "controlling cell activities: nucleus, holds DNA and directs the cell",
        "plant-only structures: cell wall, chloroplasts, a large central vacuole (storage and turgor), and plasmodesmata (channels linking neighboring cells)",
        "phagocytosis: engulfs large particles like bacteria, supporting immune defense and digestion of engulfed material",
        "pinocytosis: takes in extracellular fluid/dissolved substances, helping absorb nutrients and regulate the outside environment",
        "exocytosis: releases substances like proteins/enzymes/hormones and removes cell waste",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Neuron Types and Axon Speed)", Question="Identify three types of nerve cells and their roles, and give a reason why giant axons conduct impulses faster than thin axons.",
    Answer_Summary=lettered(
        "sensory neurons: carry signals from receptors to the CNS",
        "motor neurons: carry signals from the CNS to muscles/glands",
        "interneurons: connect sensory and motor neurons, processing signals within the CNS",
        "giant (larger-diameter) axons conduct faster because their bigger diameter lowers internal resistance to the electrical signal",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Naming and Kingdoms)", Question="What is the scientific name of a human being, what is the full hierarchical classification, why are Animalia, Plantae, Protoctista, and Fungi classed as Eukaryote kingdoms while bacteria are Kingdom Prokaryotae, and what are five rules of binomial nomenclature?",
    Answer_Summary=lettered(
        "scientific name: Homo sapiens",
        "hierarchy: Domain Eukarya, Kingdom Animalia, Phylum Chordata, Class Mammalia, Order Primates, Family Hominidae, Genus Homo, Species sapiens",
        "eukaryote kingdoms have cells with a true nucleus and membrane-bound organelles; bacteria lack both, so they're placed in Kingdom Prokaryotae",
        "binomial nomenclature rules: two Latin words (genus + species); genus capitalized, species lowercase; italicized in print or underlined when handwritten; universal across languages; unique per species",
    ), Explanation=""))
rows.append(dict(Topic="Cell Structure (Organelle Damage)", Question="Where in a mammal's body are large numbers of lysosomes and microbodies found and why, and what happens if the nucleus, lysosome, vacuole, or endoplasmic reticulum is severely damaged?",
    Answer_Summary=lettered(
        "lysosomes: abundant in white blood cells, which need digestive enzymes to break down foreign substances",
        "microbodies: abundant in liver cells, aiding detoxification",
        "damaged nucleus: cell loses control of its functions, DNA replication/repair is disrupted, protein synthesis suffers, and uncontrolled division (cancer) can result",
        "damaged lysosome: waste accumulates, harmful invaders can't be digested, metabolism is disrupted, and toxic buildup can kill the cell",
        "damaged vacuole: cell loses water/nutrient storage, plant cells wilt from low turgor, waste builds up, and the cell shrinks and dies",
        "damaged ER: protein and lipid synthesis suffer, internal transport is disrupted, detoxification slows, and the cell may fail to grow properly",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Placenta Functions)", Question="Why is the placenta considered a structure for excretion, digestion, and respiration of a foetus, and why doesn't removing the ovaries of a three-months-pregnant woman cause abortion?",
    Answer_Summary=lettered(
        "excretion: the placenta transfers foetal waste like CO2 and urea into the mother's blood for her body to remove",
        "digestion: it moves nutrients (glucose, amino acids, vitamins, minerals) from mother to foetus, since the foetus can't digest food itself",
        "respiration: oxygen diffuses from mother to foetus and CO2 the other way, standing in for the foetus's non-functional lungs",
        "by three months, the placenta (not the ovaries/corpus luteum) has taken over producing the progesterone and estrogen needed to maintain the uterine lining and prevent contractions",
        "the foetus by then depends more on the placenta than on ovarian hormones, so ovary removal doesn't end the pregnancy",
    ), Explanation=""))
rows.append(dict(Topic="Digestion (Epithelium and Liver)", Question="How does the columnar epithelium of the stomach and of the small intestine relate to its digestive role, and what two points describe the liver's role in digestion?",
    Answer_Summary=lettered(
        "stomach epithelium: secretes protective mucus, produces HCl and activates pepsin for protein digestion, allows minor absorption (water, alcohol, some drugs), and helps food move smoothly",
        "small intestine epithelium: has microvilli that boost surface area for absorption, secretes enzymes (maltase, sucrase, lactase) for carbohydrate digestion, moves digested food into capillaries/lacteals, and its goblet cells secrete protective mucus",
        "liver: produces bile to emulsify fats for easier digestion, and detoxifies harmful substances absorbed from the gut before they reach the bloodstream",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Respiratory Quotient)", Question="What is the respiratory quotient (RQ), what does RQ = 1.0, 0.9, and 0.7 each indicate, and what respiratory problems occur in a baby born without lung surfactant?",
    Answer_Summary=lettered(
        "RQ = CO2 eliminated / O2 consumed, and varies with the substrate being metabolized",
        "RQ = 1.0: carbohydrates are the main fuel, being fully oxidized under aerobic conditions",
        "RQ = 0.9: partial carbohydrate use or protein oxidation, suggesting a mixed diet being metabolized",
        "RQ = 0.7: fats are the main fuel, since fat oxidation needs more oxygen relative to CO2 produced, common during starvation or endurance exercise",
        "without surfactant: alveoli collapse after each breath (atelectasis/respiratory distress syndrome)",
        "the baby struggles to breathe, with rapid shallow breaths and poor oxygen exchange",
        "hypoxia results, risking organ failure without oxygen therapy or artificial surfactant",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Glycolysis and Electron Transport Chain)", Question="In cellular respiration, what are processes A and B (glycolysis and the electron transport chain), what do X and Y represent (oxygen and ATP), and what happens if process A or B is impaired?",
    Answer_Summary=lettered(
        "A: glycolysis; B: electron transport chain",
        "X: oxygen, the final electron acceptor in the electron transport chain; Y: ATP, the energy-carrying product of respiration",
        "if glycolysis (A) fails: glucose can't be broken down to pyruvate, ATP production drops sharply, and the Krebs cycle/electron transport chain can't proceed since they depend on its products",
        "if the electron transport chain (B) fails: oxidative phosphorylation stops, most ATP production is lost, NADH/FADH2 build up, and the cell must rely on inefficient glycolysis alone, risking lactic acid buildup",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Fermentation Importance)", Question="In seven points, explain the importance of fermentation processes to human beings.",
    Answer_Summary=lettered(
        "food and beverage production: makes bread rise, and produces yogurt, cheese, beer, and wine",
        "human metabolism: lactic acid fermentation supplies ATP in muscles when oxygen is insufficient during intense exercise",
        "food preservation: the acidic environment in fermented foods like pickles/kimchi inhibits spoilage bacteria",
        "nutrition: breaks down complex compounds into simpler forms, e.g. converting lactose in yogurt, and can boost vitamin content",
        "pharmaceuticals: produces antibiotics like penicillin",
        "energy/waste management: ferments organic waste into biogas (methane) as renewable energy",
        "culture: fermented foods/drinks like kombucha and kefir hold traditional and cultural significance",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Meiosis Location and Chromosome Numbers)", Question="Where and when does meiosis occur in a moss plant, in angiosperms, and in mammals; if a flowering plant's radicle has 16 chromosomes, what is the chromosome number in the pollen tube nucleus, antipodal cell, endosperm, and pollen mother cell; and how are the uterus, cervix, and ovaries adapted to their reproductive functions?",
    Answer_Summary=lettered(
        "moss: meiosis happens in spore mother cells in the sporophyte's capsule, producing haploid spores",
        "angiosperms: meiosis happens in the anther's microspore mother cells (making pollen) and the ovule's megaspore mother cell (making the embryo sac)",
        "mammals: meiosis happens in the seminiferous tubules of the testes (sperm) and in the ovaries (eggs), with female meiosis pausing at prophase I until ovulation",
        "chromosome numbers (radicle = 16, diploid): pollen tube nucleus = 8 (haploid), antipodal cell = 8 (haploid), endosperm = 24 (triploid), pollen mother cell = 16 (diploid)",
        "uterus: thick muscular walls (myometrium) support and expel the baby at birth, a vascularized endometrium nourishes an implanted embryo, and it's elastic enough to expand during pregnancy",
        "cervix: produces mucus that changes to allow/block sperm at ovulation, acts as a barrier against infection, and dilates during labor",
        "ovaries: hold follicles containing immature eggs, secrete estrogen/progesterone to regulate the cycle and pregnancy, and release mature eggs into the fallopian tubes",
    ), Explanation=""))
rows.append(dict(Topic="Plant Transport (Phloem Mass Flow Hypothesis)", Question="Describe the mechanism of food transport in phloem based on Munch's mass flow hypothesis.",
    Answer_Summary=lettered(
        "at the source (leaf mesophyll), photosynthesis makes sugars, raising osmotic pressure there",
        "water enters from the xylem by osmosis, raising turgor pressure; sugars are actively loaded into sieve tubes, raising pressure further",
        "at the sink, sugars are unloaded into sink cells, lowering osmotic/turgor pressure in the sieve tubes there, so water exits back to the xylem",
        "the resulting pressure difference between source and sink drives mass flow of phloem sap from source to sink",
    ), Explanation=""))

# ============================== YEAR 2021 ==============================
rows.append(dict(Topic="Reproduction (Oestrus Cycle)", Question="Briefly describe the stages of the oestrus cycle, and justify why female animals need an oestrus cycle.",
    Answer_Summary=lettered(
        "proestrus: follicles mature and estrogen rises, thickening the uterine lining",
        "estrus ('heat'): female is receptive, estrogen peaks, and ovulation occurs",
        "metestrus: the ruptured follicle becomes a corpus luteum secreting progesterone; regresses without fertilization",
        "diestrus: corpus luteum fully develops if pregnant, or hormones drop and the cycle restarts if not",
        "the cycle synchronizes mating with peak fertility, prepares the uterus for implantation, balances reproductive hormones, and enables regular reproduction",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Respiratory Quotient and Fermentation)", Question="Find the respiratory quotient (RQ) for complete respiration of glucose, and give seven points justifying the need for fermentation in animals.",
    Answer_Summary=lettered(
        "for glucose: C6H12O6 + 6O2 -> 6CO2 + 6H2O, so RQ = 6/6 = 1",
        "fermentation makes ATP possible without oxygen",
        "it regenerates NAD+ from NADH so glycolysis can keep running",
        "it lets cells survive temporarily in low-oxygen conditions, e.g. during hard exercise",
        "it clears pyruvate into waste products like lactic acid instead of letting it build up",
        "it helps animals adapted to hypoxic environments meet their energy needs",
        "in some species it supports specific metabolite production",
        "it keeps metabolic pathways running when aerobic respiration isn't possible",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Limits of Natural Classification)", Question="Give four points supporting the fact that a natural classification system has never been fully achieved, and four reasons scientists prefer natural over artificial classification.",
    Answer_Summary=lettered(
        "incomplete fossil records and unknown ancestors leave evolutionary gaps",
        "convergent evolution creates similar traits in unrelated organisms, causing confusion",
        "new species keep being discovered, forcing revisions",
        "molecular/genetic analysis keeps revealing hidden relationships the system hadn't accounted for",
        "natural classification reflects true evolutionary relationships and common ancestry",
        "it has predictive value, letting scientists infer traits of related species",
        "it's more universally consistent since it uses objective genetic/evolutionary criteria",
        "it supports broader research into biodiversity, ecology, and evolution",
    ), Explanation=""))
rows.append(dict(Topic="Cell Structure (Organelle Substructures and Enzymes)", Question="How does the tonoplast in the vacuole, the glycocalyx on the plasma membrane, DNA in the nucleus, and cristae in the mitochondria each enable their organelle's role, and what is the lock-and-key model of enzyme action?",
    Answer_Summary=lettered(
        "tonoplast: a selectively permeable membrane around the vacuole, controlling ion/nutrient/waste movement and osmotic balance",
        "glycocalyx: a carbohydrate coat on the plasma membrane enabling cell recognition, adhesion, communication, and protection",
        "DNA in the nucleus: stores genetic information for protein synthesis, with the nuclear envelope protecting it and controlling exchange with the cytoplasm",
        "cristae: folds in the inner mitochondrial membrane that boost surface area for the electron transport chain and ATP synthesis",
        "lock-and-key model: an enzyme's active site fits a specific substrate exactly, like a key in a lock; binding forms an enzyme-substrate complex that catalyzes the reaction, and the enzyme is released unchanged",
    ), Explanation=""))
rows.append(dict(Topic="Digestion (Pancreatic Damage and Acidic Duodenum)", Question="What digestive roles are impaired if the pancreas is severely damaged, and what happens to duodenal enzymes if the duodenum's pH stays at 2?",
    Answer_Summary=lettered(
        "protein digestion suffers without pancreatic trypsin/chymotrypsin",
        "carbohydrate digestion suffers without pancreatic amylase",
        "fat digestion suffers without pancreatic lipase, leading to undigested fats",
        "stomach acid entering the duodenum isn't neutralized without pancreatic bicarbonate, damaging the gut lining",
        "at pH 2, duodenal enzymes like amylase and lipase (which need alkaline conditions) denature, stopping digestion, causing malabsorption, and damaging the intestinal lining",
    ), Explanation=""))
rows.append(dict(Topic="Cell Biology (Cytoplasm Functions)", Question="Why do most reactions of the cell take place in the cytoplasm, and why is the cytoplasm an important part of the cell (six points)?",
    Answer_Summary=lettered(
        "the cytoplasm is rich in enzymes that catalyze reactions like glycolysis",
        "it's a medium for diffusion/transport of substrates and products",
        "it surrounds organelles, allowing coordinated interactions between them",
        "it gives structural support that keeps conditions right for reactions",
        "importance: provides the aqueous medium for biochemical reactions",
        "importance: stores ions, amino acids, and carbohydrates for cell use",
        "importance: helps organize and position organelles",
        "importance: its cytoskeleton enables intracellular transport",
        "importance: helps maintain cell shape",
        "importance: buffers intracellular pH and ion concentration",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Unmyelinated Nerve Conduction)", Question="Describe the conduction of a nerve impulse along an unmyelinated neuron.",
    Answer_Summary=lettered(
        "at rest, the membrane sits at about -70 mV, kept polarized by the sodium-potassium pump (Na+ out, K+ in)",
        "a threshold stimulus opens voltage-gated sodium channels, letting Na+ rush in and depolarize the membrane to about +30 mV",
        "this local depolarization triggers the same response in the next segment of membrane, propagating the impulse along the whole axon (continuous conduction)",
        "afterward, voltage-gated potassium channels open, K+ exits, and the membrane repolarizes; the sodium-potassium pump then resets ion levels for the next impulse",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Oxygen Uptake Adaptations)", Question="Describe how the mammalian foetus, mountain dwellers, and divers are adapted for oxygen uptake.",
    Answer_Summary=lettered(
        "foetus: fetal hemoglobin has a higher oxygen affinity than adult hemoglobin, the placenta enables efficient gas exchange, and shunts (ductus arteriosus, foramen ovale) direct oxygen-rich blood to vital organs",
        "high-altitude dwellers: higher red blood cell count and hemoglobin concentration, larger lung volumes, and genetic adaptations improving oxygen use and blood flow",
        "divers: high muscle myoglobin stores oxygen for sustained activity, and a diving reflex (bradycardia plus selective vasoconstriction) prioritizes oxygen for the brain and heart while conserving stores",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Menstrual Cycle Hormones)", Question="Why are oestrogen, luteinizing hormone (LH), progesterone, and follicle-stimulating hormone (FSH) important in the menstrual cycle, and what hormonal changes follow if pregnancy occurs on day 18 of the cycle?",
    Answer_Summary=lettered(
        "oestrogen: thickens the endometrium and triggers the LH surge that causes ovulation",
        "LH: causes the mature follicle to rupture (ovulation) and forms the corpus luteum, which secretes progesterone",
        "progesterone: maintains the uterine lining during the luteal phase; without pregnancy its drop triggers menstruation",
        "FSH: drives follicle growth and maturation during the follicular phase",
        "if pregnancy occurs: hCG from the embryo keeps the corpus luteum making progesterone, oestrogen rises to support uterine blood flow and the placenta, and FSH/LH fall due to negative feedback from high progesterone/hCG, preventing further ovulation",
    ), Explanation=""))
rows.append(dict(Topic="Plant Transport (Xylem Water Adaptations)", Question="How is xylem adapted to water transportation (six points), and how does capillarity force drive the upward movement of water and mineral salts?",
    Answer_Summary=lettered(
        "xylem vessels are elongated, hollow, dead cells forming continuous tubes for unobstructed water flow",
        "walls reinforced with lignin give structural support and resist collapse under tension",
        "narrow vessel diameter boosts capillary action, aiding upward movement",
        "pits in the walls let water move laterally between vessels if one is blocked",
        "cohesion between water molecules keeps a continuous water column",
        "adhesion between water and vessel walls helps pull water upward",
        "capillarity works via cohesion (a continuous column), adhesion (water clinging to xylem walls), and narrow vessel diameter, combined with root pressure and transpirational pull, to move water and minerals up the plant",
    ), Explanation=""))

# ============================== YEAR 2022 ==============================
rows.append(dict(Topic="Enzymes (Denaturation) and Cell Structure (Membrane-Bound Organelles)", Question="If saliva is boiled to 75°C before a starch test and the test still comes back positive for starch, what does this show, and why is it advantageous for eukaryotic organelles to be membrane-bound (three points)?",
    Answer_Summary=lettered(
        "a positive starch test after boiled saliva shows starch wasn't broken down, because boiling denatured the amylase, destroying its active site",
        "compartmentalization: membranes let specific reactions happen in isolated environments, e.g. respiration inside mitochondria",
        "increased efficiency: concentrating enzymes/substrates inside organelles (e.g. lysosome's acidic interior) speeds up reactions",
        "protection: the nuclear membrane shields DNA and controls what enters/exits the nucleus",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Dichotomous Keys)", Question="Why does a biologist need a biological key when classifying new insects, how would you construct a dichotomous key, and how would you use it to classify organisms?",
    Answer_Summary=lettered(
        "a biological key is needed to systematically identify/classify organisms by comparing their features against set criteria",
        "construction: observe distinguishing features, list contrasting characteristics, group organisms by shared traits, write paired contrasting statements, organize from broad to specific, then test the key on known organisms",
        "usage: start with the first pair of statements, pick the one matching the organism, and follow the resulting path through further pairs until it's identified",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Damage Effects and Neuron Structure)", Question="What happens to an organism if its nervous system is severely damaged (four points), what type of neuron has multiple dendrites on the cell body and a long axon to an effector, and what happens if that neuron's cell body or axon is severely damaged?",
    Answer_Summary=lettered(
        "loss of coordination between brain, spinal cord, and body, causing uncoordinated movement or paralysis",
        "sensory impairment, losing feelings like touch, pain, or temperature",
        "cognitive dysfunction affecting memory, decision-making, or consciousness",
        "loss of reflexes, raising injury risk from delayed responses",
        "a neuron with several dendrites on the cell body and a long axon to an effector is a motor neuron",
        "damaged cell body: the neuron can't process signals or generate action potentials, and may die since it can't make proteins or maintain itself",
        "damaged axon: signal transmission to the target muscle/gland is impaired, which can cause paralysis or loss of function",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis (Light-Dependent Reactions)", Question="How does the trapping of light energy by the photosystems take place at the start of photosynthesis, and how does electron transport occur in photosystems I and II?",
    Answer_Summary=lettered(
        "chlorophyll in photosystems I and II absorbs light, exciting electrons to a higher energy state",
        "in PSII, excited electrons pass to the electron transport chain, generating ATP via photophosphorylation, while water is split (photolysis) to replace the lost electrons and release oxygen",
        "in PSI, light re-excites electrons which are used to reduce NADP+ to NADPH for the Calvin cycle",
        "together, PSII and PSI convert light energy into the chemical energy stored in ATP and NADPH",
    ), Explanation=""))
rows.append(dict(Topic="Gas Exchange (Respiratory Surfaces) and Fermentation", Question="Why does a respiratory surface need a large surface area to volume ratio, a moist surface, a thin membrane, and a permeable membrane, and how is pyruvic acid converted to ethanol during fermentation?",
    Answer_Summary=lettered(
        "large surface area to volume ratio: lets enough gas exchange happen to meet metabolic demand, e.g. in alveoli",
        "moist surface: lets gases dissolve before diffusing across the membrane",
        "thin membrane: minimizes diffusion distance for fast gas exchange",
        "permeable membrane: lets gases pass freely in and out",
        "decarboxylation: pyruvate decarboxylase converts pyruvic acid to acetaldehyde, releasing CO2",
        "reduction: alcohol dehydrogenase reduces acetaldehyde to ethanol using NADH, regenerating NAD+ for glycolysis",
    ), Explanation=""))
rows.append(dict(Topic="Cell Structure (Membrane Antigens) and Plant Water Roles", Question="What would happen to a cell if its membrane lacked antigens (two points), and in what ways is water important to plants (four points)?",
    Answer_Summary=lettered(
        "without antigens, the immune system may not recognize the cell as 'self,' risking an autoimmune attack",
        "without antigens, cell signaling/communication is impaired, affecting things like tissue repair and immune response",
        "water is the solvent medium for reactions like photosynthesis",
        "water carries dissolved minerals through the xylem",
        "water keeps cells turgid, supporting structure and stomatal function",
        "water lost via transpiration cools the plant and prevents overheating",
    ), Explanation=""))
rows.append(dict(Topic="Plant Reproduction (Seed and Fruit Development)", Question="After successful fertilization in a flowering plant, what does the funiculus connect and what role does it play, what does the seed coat, embryo, and fruit wall each develop from, and what happens to the stigma and the micropyle after fertilization?",
    Answer_Summary=lettered(
        "the funiculus connects the developing seed to the parent plant, playing a role like the umbilical cord in humans",
        "the seed coat (testa) develops from the outer integument",
        "the embryo develops from the fertilized egg cell",
        "the fruit wall (pericarp) develops from the ovary wall",
        "after fertilization, the stigma withers, while the micropyle remains as a small opening that lets water in during germination",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Glycolysis, Krebs Cycle, Electron Transport Chain)", Question="What are two essential features each of glycolysis, the Krebs cycle, and the electron transport chain, and how does the electron transport chain work in aerobic respiration?",
    Answer_Summary=lettered(
        "glycolysis: happens in the cytoplasm, splitting one glucose into two pyruvate while netting 2 ATP and 2 NADH",
        "Krebs cycle: happens in the mitochondrial matrix, processing pyruvate (as acetyl-CoA) to yield NADH, FADH2, and a little ATP",
        "electron transport chain: happens in the inner mitochondrial membrane, passing electrons from NADH/FADH2 through protein complexes to make ATP via oxidative phosphorylation",
        "ETC mechanism: electrons from NADH/FADH2 move through the complexes, pumping protons into the intermembrane space to build a proton gradient; oxygen accepts electrons at the end to form water, and protons flowing back through ATP synthase generate ATP",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Placenta Formation)", Question="Why should the mammalian placenta form immediately after implantation? Give six points.",
    Answer_Summary=lettered(
        "supplies nutrients (glucose, amino acids, fatty acids) from mother to embryo",
        "delivers oxygen for the embryo's cellular respiration",
        "removes fetal waste like CO2 and urea",
        "produces hormones like progesterone and hCG that maintain the pregnancy",
        "protects the fetus from pathogens and the mother's immune system",
        "anchors the embryo to the uterine wall, giving structural stability for growth",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Oxygen Transport)", Question="Describe three ways oxygen is transported in the human body after entering the lungs.",
    Answer_Summary=lettered(
        "a small amount (1-2%) dissolves directly in blood plasma",
        "most (about 98%) binds hemoglobin in red blood cells as oxyhemoglobin",
        "at tissues, oxygen dissociates from oxyhemoglobin where oxygen levels are low and diffuses into cells for respiration",
    ), Explanation=""))

# ============================== YEAR 2023 ==============================
rows.append(dict(Topic="Cell Structure (Mitochondrion)", Question="Why can a mitochondrion be regarded as 'a cell within the cell' (four points), and what are the main parts of a mitochondrion?",
    Answer_Summary=lettered(
        "it has a double membrane, giving it its own compartmentalized structure like a cell",
        "it has its own circular DNA, letting it make some proteins independently of the nucleus",
        "it has ribosomes to translate those proteins itself",
        "it can self-replicate by binary fission, like a prokaryotic cell",
        "outer membrane: smooth, with porins letting ions/small molecules through",
        "intermembrane space: involved in oxidative phosphorylation",
        "inner membrane (folded into cristae): holds the electron transport chain and ATP synthase, with cristae boosting surface area",
        "matrix: gel-like interior with enzymes, mitochondrial DNA, and ribosomes, where the Krebs cycle happens",
    ), Explanation=""))
rows.append(dict(Topic="Respiratory System (Pleural Membrane and Alveoli)", Question="What happens if the pleural membrane is severely damaged (three points), and why are alveoli so efficient at gas exchange (seven points)?",
    Answer_Summary=lettered(
        "loss of lubrication: without the pleural fluid, friction between lungs and chest wall increases, causing pain when breathing",
        "impaired lung expansion: damage can cause pneumothorax, collapsing the lung",
        "inflammation/infection: pleuritis or infection can follow, reducing oxygen exchange",
        "alveoli efficiency: large surface area for gas exchange, walls only one cell thick, rich capillary supply, a moist lining for gases to dissolve in, elasticity for expansion/recoil, close proximity to capillaries, and a steep partial-pressure gradient driving diffusion",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Binomial Nomenclature)", Question="If a student writes the scientific name of a human being as 'homo sapiens' (lowercase, unformatted), what two mistakes have they made?",
    Answer_Summary=lettered(
        "the genus name should be capitalized ('Homo'), with the species name lowercase ('sapiens')",
        "the whole scientific name should be italicized in print or underlined when handwritten",
    ), Explanation=""))
rows.append(dict(Topic="Microscopy (Magnification and Biological Drawing)", Question="If a specimen's linear dimension is 2 cm and its drawing's linear dimension is 6 cm, what is the magnification, what principles of biological drawing are commonly violated in a poorly made student diagram, and what are two purposes of biological drawing?",
    Answer_Summary=lettered(
        "magnification = drawing size / specimen size = 6 cm / 2 cm = 3x",
        "commonly violated principles: inaccurate proportions between parts, unclear/imprecise labeling lines, unnecessary shading (lack of simplicity), and rough/untidy outlines",
        "purposes: accurate documentation of a specimen's structure, and communicating findings clearly to others",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Corpus Luteum in Early Pregnancy)", Question="Why is it not advisable to surgically remove the corpus luteum during the first three weeks of pregnancy? Give four points.",
    Answer_Summary=lettered(
        "the corpus luteum secretes progesterone, essential for maintaining the uterine lining and early pregnancy",
        "removing it drops hormone levels, risking embryo detachment and miscarriage",
        "the placenta isn't fully functional yet in these early weeks, so the corpus luteum is still the main hormone source",
        "progesterone from the corpus luteum supports implantation, so removing it can prevent the embryo from attaching properly",
    ), Explanation=""))
rows.append(dict(Topic="Photosynthesis (Limiting Factors) and Digestion (Brunner's Glands)", Question="Under what conditions do temperature and carbon dioxide concentration limit photosynthesis, and what six digestive processes are impaired if Brunner's glands are severely damaged?",
    Answer_Summary=lettered(
        "temperature limits photosynthesis when too low (slow enzymes) or too high (denatured enzymes)",
        "low CO2 concentration limits photosynthesis by reducing substrate for the Calvin cycle",
        "Brunner's gland damage impairs: neutralizing stomach acid entering the duodenum",
        "protecting the duodenal lining from acid (raising ulcer risk)",
        "creating the right pH to activate pancreatic enzymes like trypsin and amylase",
        "carbohydrate digestion, from reduced enzyme activity",
        "protein digestion, from impaired proteolytic enzyme activation",
        "fat digestion, since poor acid neutralization disrupts bile salt function and fat emulsification",
    ), Explanation=""))
rows.append(dict(Topic="Coordination (Nervous vs Endocrine) and Nervous Tissue Adaptations", Question="How do endocrine and nervous coordination differ (five points), and how is nervous tissue adapted for its role (five points)?",
    Answer_Summary=lettered(
        "nervous system uses fast electrical impulses via neurons; endocrine system uses hormones traveling in the blood, more slowly",
        "nervous responses are quick (milliseconds) and short-lived; endocrine responses are slower but longer-lasting",
        "nervous coordination targets specific cells via direct connections; hormones can affect many tissues at once",
        "nervous system handles rapid short-term processes (movement, sensation); endocrine system handles slow long-term processes (growth, metabolism, reproduction)",
        "adaptations: specialized neurons with dendrites/axons for signal transmission",
        "myelin sheath speeds up conduction via saltatory conduction",
        "synapses let neurons communicate precisely with other cells",
        "glial cells give structural/metabolic support and help repair nervous tissue",
        "neurons are highly excitable and conductive, letting them respond quickly to stimuli",
    ), Explanation=""))
rows.append(dict(Topic="Respiratory System (Lung Structure)", Question="Describe the structure of mammalian lungs using nine points.",
    Answer_Summary=lettered(
        "paired organs in the thorax, with the right lung having three lobes and the left two (to fit the heart)",
        "each lung is wrapped in a double-layered pleural membrane with fluid between the layers to reduce friction",
        "a branching bronchial tree (bronchi to bronchioles) carries air in",
        "terminal bronchioles lead to alveoli, thin-walled sacs where gas exchange happens",
        "rich blood supply: pulmonary arteries bring deoxygenated blood in, pulmonary veins take oxygenated blood out",
        "cartilage rings in the trachea/large bronchi keep the airway open",
        "elastic fibers let the lungs expand and recoil during breathing",
        "ciliated epithelium lining the airway traps and clears dust/microbes",
        "surfactant coats the alveoli, reducing surface tension so they don't collapse",
    ), Explanation=""))
rows.append(dict(Topic="Cell Transport (Active vs Passive)", Question="How do active and passive transport of materials differ? Give seven points.",
    Answer_Summary=lettered(
        "energy: active transport needs ATP; passive transport doesn't",
        "direction: active transport moves substances low-to-high concentration; passive moves high-to-low",
        "examples: active includes the sodium-potassium pump and endocytosis; passive includes diffusion, osmosis, and facilitated diffusion",
        "carrier proteins: active transport always needs specific carriers/pumps; passive transport may or may not (e.g. facilitated diffusion does, simple diffusion doesn't)",
        "speed: active transport is slower (energy-dependent); passive transport is generally faster",
        "metabolic dependency: active transport depends on the cell's metabolic state; passive transport doesn't",
        "example in organisms: plants use active transport to absorb minerals into root hairs; lungs use passive diffusion for oxygen uptake in alveoli",
    ), Explanation=""))
rows.append(dict(Topic="Plant Reproduction (Double Fertilization)", Question="Describe the process that leads to embryo and endosperm formation in flowering plants.",
    Answer_Summary=lettered(
        "pollination moves pollen from anther to stigma",
        "the pollen grain germinates into a pollen tube that grows down the style",
        "the tube enters the ovule through the micropyle, carrying two male gametes",
        "one male gamete fuses with the egg cell, forming a diploid zygote that becomes the embryo",
        "the other male gamete fuses with the two polar nuclei, forming a triploid cell that becomes the endosperm",
        "the zygote divides to form embryonic tissues (cotyledons, shoot apex, root apex)",
        "the endosperm divides repeatedly into nutritive tissue feeding the embryo",
        "the embryo and endosperm are enclosed in the seed coat as the seed matures for dispersal and germination",
    ), Explanation=""))

# ============================== YEAR 2024 ==============================
rows.append(dict(Topic="Biomolecules (Globular Proteins and Denaturation)", Question="What five features characterize globular proteins, and what five ways can prevent protein denaturation?",
    Answer_Summary=lettered(
        "soluble in water, forming colloidal solutions via their hydrophilic outer layer",
        "compact, spherical shape suited to specific biological functions",
        "have a complex tertiary structure held by hydrogen and ionic bonds",
        "perform specific biological roles (enzymes, hormones, antibodies) via their active sites",
        "sensitive to pH, temperature, and ionic strength changes, which can denature them",
        "prevent denaturation by keeping proteins at their optimal temperature",
        "keeping the surrounding pH within the protein's optimal range",
        "avoiding harmful chemicals like strong detergents, heavy metals, or organic solvents",
        "using stabilizing agents like glycerol or specific salts",
        "avoiding excessive mechanical agitation (shaking/stirring)",
    ), Explanation=""))
rows.append(dict(Topic="Physiology (Roles of Water) and Cell Structure (Animal Organelles)", Question="How is water used in transportation, waste removal, secretion, and hearing/balance in the human body, and why do animal cells need peroxisomes, lysosomes, rough ER, and the glycocalyx?",
    Answer_Summary=lettered(
        "transportation: water in blood plasma carries nutrients, hormones, gases, and waste to and from cells",
        "waste removal: water lets the kidneys dissolve and excrete waste like urea, and carries waste out via sweat",
        "secretion: water is the solvent/medium for saliva, mucus, and digestive juices",
        "hearing/balance: endolymph fluid in the cochlea and semicircular canals transmits vibrations and movement to hair cells",
        "peroxisomes: break down reactive oxygen species like hydrogen peroxide, protecting the cell, and help metabolize fatty acids",
        "lysosomes: digest macromolecules, damaged organelles, and pathogens, maintaining cellular cleanup",
        "rough ER: its ribosomes synthesize and fold proteins destined for secretion or the membrane",
        "glycocalyx: enables cell recognition, adhesion, and protection at the cell surface",
    ), Explanation=""))
rows.append(dict(Topic="Nervous System (Synapse Structure and Adaptation)", Question="What are the four main parts of a synapse, and how is the synapse's structure adapted for transmitting impulses (four points)?",
    Answer_Summary=lettered(
        "presynaptic neuron: sends the signal, releasing neurotransmitters from synaptic vesicles",
        "synaptic cleft: the ~20 nm gap neurotransmitters cross to reach the next neuron",
        "postsynaptic neuron: receives the signal via receptor sites that trigger a new electrical signal",
        "receptor sites: proteins on the postsynaptic membrane that bind neurotransmitters and open ion channels",
        "adaptation: synaptic vesicles let neurotransmitters release quickly on demand",
        "adaptation: the narrow cleft lets neurotransmitters diffuse across rapidly",
        "adaptation: specific postsynaptic receptors ensure the signal is received accurately",
        "adaptation: voltage-gated calcium channels open on impulse arrival, triggering precisely timed vesicle release",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Preventing Anaerobic Respiration and ATP Yield)", Question="How can wasteful anaerobic respiration in animal cells be prevented, and how many ATP are produced at each stage (glycolysis, Krebs cycle, electron transport chain) when glucose is fully oxidized to 38 ATP?",
    Answer_Summary=lettered(
        "improve blood circulation through exercise and cardiovascular health, so oxygen reaches tissues efficiently",
        "manage respiratory conditions (e.g. asthma, COPD) to maintain oxygen intake",
        "keep hemoglobin levels adequate (iron-rich diet, treating anemia) for good oxygen transport",
        "avoid overexertion beyond what the body can supply with oxygen",
        "glycolysis (cytoplasm): nets 2 ATP directly, plus 2 NADH",
        "Krebs cycle (mitochondrial matrix): produces 2 ATP directly, plus 6 NADH and 2 FADH2",
        "electron transport chain (inner mitochondrial membrane): produces about 34 ATP from the NADH/FADH2, the majority of the total",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Multiple Births) and Birth Stages", Question="How could a woman give birth to triplets where two are genetically identical and one is different (seven points), and what is the importance of cervical dilation, head-first delivery, and placental expulsion during birth?",
    Answer_Summary=lettered(
        "two identical babies (monozygotic twins) came from one fertilized egg splitting early into two embryos",
        "the third baby (dizygotic) came from a separate egg fertilized by a different sperm",
        "this happens when two eggs are released and fertilized independently alongside the split zygote",
        "the monozygotic twins likely shared one placenta, while the dizygotic triplet had its own",
        "the dizygotic sibling has its own distinct genetic makeup from independent fertilization",
        "assisted reproduction (e.g. IVF with multiple embryos) could also explain a mixed identical/fraternal set",
        "cervical dilation: widens the birth canal so the fetus can pass through safely",
        "head-first delivery: minimizes injury risk since the head is the largest part and eases the rest of the body out",
        "placental expulsion: prevents postpartum infection/bleeding and lets the uterus start contracting back to size",
    ), Explanation=""))
rows.append(dict(Topic="Classification (Importance and Limits of Artificial Systems)", Question="What is the importance of classifying organisms (five points), and why do scientists not prefer artificial classification systems (five points)?",
    Answer_Summary=lettered(
        "classification makes it easier to identify and study organisms systematically",
        "it lets scientists predict traits of an organism based on its group",
        "it reveals evolutionary relationships and how species diversified",
        "standardized scientific names avoid confusion from local/common names",
        "it highlights biodiversity, guiding conservation priorities",
        "artificial systems ignore evolutionary relationships, relying on superficial traits like size or habitat",
        "they ignore internal anatomy, physiology, and molecular biology",
        "they can't handle variation within or between closely related species well",
        "they give little insight into an organism's actual function or ecological role",
        "they can group organisms with similar looks but very different genetics, giving misleading relationships",
    ), Explanation=""))
rows.append(dict(Topic="Digestion (Hydrochloric Acid and Mucus)", Question="What is the importance of hydrochloric acid in gastric juice for digestion (seven points), and why is mucus secretion in the stomach epithelium and gastric glands needed (three points)?",
    Answer_Summary=lettered(
        "activates pepsinogen into pepsin for protein digestion",
        "creates the acidic environment pepsin needs to work",
        "denatures proteins, making them easier for enzymes to break down",
        "kills ingested harmful microorganisms",
        "helps solubilize minerals like iron and calcium for absorption",
        "triggers release of other gastric/pancreatic digestive enzymes",
        "softens food, aiding mechanical digestion",
        "mucus protects the stomach lining from acid and pepsin, preventing ulcers",
        "mucus lubricates food for smooth movement through the stomach",
        "mucus traps bicarbonate to keep a slightly alkaline layer right at the epithelial surface, shielding it from acid",
    ), Explanation=""))
rows.append(dict(Topic="Plant Transport (Water Uptake from Soil)", Question="Describe the process of water uptake from the soil to the xylem.",
    Answer_Summary=lettered(
        "root hairs absorb water from the soil by osmosis, since root cells have lower water potential",
        "water crosses the root cortex via the apoplast (cell walls), symplast (cytoplasm/plasmodesmata), or transmembrane pathway",
        "the endodermis's Casparian strip forces water into the symplast pathway, allowing selective mineral uptake",
        "water then enters the xylem vessels (dead, hollow tubes) via osmosis or root pressure",
        "cohesion between water molecules and adhesion to xylem walls help pull water upward against gravity",
        "transpiration from the leaves creates negative pressure that pulls water continuously up through the xylem",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Infertility Causes)", Question="What are possible causes of infertility in a couple unable to conceive after ten years, for the male partner, the female partner, and shared causes?",
    Answer_Summary=lettered(
        "male: low sperm count from hormonal imbalance, lifestyle, or medical issues",
        "male: poor sperm motility from genetics, infection, or toxin exposure",
        "male: erectile dysfunction preventing successful intercourse",
        "male: blockage in the vas deferens/epididymis obstructing sperm",
        "female: ovulation disorders like PCOS or hormonal imbalance",
        "female: blocked fallopian tubes from infection or scarring",
        "female: endometriosis interfering with implantation or damaging organs",
        "female: uterine abnormalities like fibroids affecting implantation",
        "shared: genetic/immunological incompatibility between partners",
        "shared: lifestyle factors like smoking, alcohol, poor diet, or stress",
    ), Explanation=""))
rows.append(dict(Topic="Respiratory System (Air Pathway and Alveolar Adaptations)", Question="What path does air take from the nose to the alveoli, and what are six adaptations of the alveoli for gas exchange?",
    Answer_Summary=lettered(
        "air path: nose -> nasal cavity -> pharynx -> larynx -> trachea -> bronchi -> bronchioles -> alveoli",
        "large surface area: about 300 million alveoli give roughly 70-80 square meters for gas exchange",
        "thin membrane: alveolar walls are a single layer of squamous cells, minimizing diffusion distance",
        "moist lining: a thin fluid layer lets gases dissolve before diffusing",
        "rich capillary network: maintains a steep concentration gradient for efficient diffusion",
        "elasticity: elastic fibers let alveoli expand on inhalation and recoil on exhalation",
        "pores of Kohn: small openings between alveoli allow collateral ventilation and even air distribution",
    ), Explanation=""))

# ============================== YEAR 2025 ==============================
rows.append(dict(Topic="Cell Structure (Mitochondrion and Organelles)", Question="How do the mitochondrion's folded inner membrane, matrix, circular DNA, and ribosomes each help release energy from food, and what are two importances each of microtubules, the Golgi body, and lysosomes?",
    Answer_Summary=lettered(
        "folded inner membrane (cristae): increases surface area for electron transport chain enzymes, boosting ATP production",
        "matrix: holds the Krebs cycle enzymes that generate NADH and FADH2 for the electron transport chain",
        "circular DNA: codes for some of the mitochondrion's own proteins, letting it self-replicate and function semi-independently",
        "ribosomes: make proteins the mitochondrion needs, including ones for the electron transport chain",
        "microtubules: give structural support/shape, and form the spindle fibers that move chromosomes during division",
        "Golgi body: modifies, sorts, and packages proteins/lipids for transport, and helps form lysosomes",
        "lysosomes: break down waste, old organelles, and debris, and drive autolysis of damaged or unwanted cells",
    ), Explanation=""))
rows.append(dict(Topic="Cell Biology (Yeast vs Bacteria) and Vacuole", Question="Analyze five differences between yeast cells and bacterium cells, and justify (two points) why a plant cell needs a vacuole.",
    Answer_Summary=lettered(
        "yeast is eukaryotic with a true nucleus; bacteria are prokaryotic without one",
        "yeast has membrane-bound organelles (mitochondria, ER, Golgi); bacteria have none",
        "yeast reproduces by budding; bacteria reproduce by binary fission",
        "yeast's cell wall is chitin; the bacterial cell wall is peptidoglycan",
        "yeast cells are larger and structurally more complex than bacteria",
        "vacuole: maintains turgor pressure for structural support, keeping the plant upright",
        "vacuole: stores water, nutrients, and waste, helping maintain the cell's internal environment",
    ), Explanation=""))
rows.append(dict(Topic="Biomolecules (ATP) and Gas Exchange (Gills and Lungs)", Question="What molecule provides energy for muscle contraction, nerve conduction, and active transport, and is also used in macromolecule synthesis and signal transduction, and what four features do gills and lungs share?",
    Answer_Summary=lettered(
        "ATP (adenosine triphosphate) powers cellular processes like muscle contraction, nerve impulses, and active transport",
        "ATP supplies energy for building macromolecules like proteins and nucleic acids",
        "ATP acts as a substrate for kinases that phosphorylate proteins, regulating cellular processes",
        "gills and lungs both have a large surface area for gas exchange",
        "both have a moist surface so gases can dissolve before diffusing",
        "both are richly supplied with capillaries to move gases to and from the surface",
        "both have thin walls/membranes that minimize the diffusion distance",
    ), Explanation=""))
rows.append(dict(Topic="Reproduction (Spermatogenesis vs Oogenesis)", Question="How do spermatogenesis and oogenesis differ in site of occurrence, number of cells formed, cytoplasmic division during meiosis I and II, size of cells formed, and how the cells transform?",
    Answer_Summary=lettered(
        "site: spermatogenesis happens in the seminiferous tubules of the testes; oogenesis happens in the ovaries",
        "cell number: spermatogenesis makes four functional sperm from one germ cell; oogenesis makes one functional ovum and three non-functional polar bodies",
        "cytoplasmic division: equal in spermatogenesis (equal-sized cells); unequal in oogenesis, with most cytoplasm kept in one large ovum",
        "cell size: sperm are small and motile; the ovum is large, non-motile, and cytoplasm-rich for nourishing the embryo",
        "transformation: spermatids become mature spermatozoa with a head, midpiece, and tail; the secondary oocyte matures directly into a fertilizable ovum",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Glycolysis)", Question="Explain how a 6-carbon compound (glucose) is converted into two 3-carbon compounds during respiration.",
    Answer_Summary=lettered(
        "glucose is phosphorylated using ATP into glucose-6-phosphate, then isomerized to fructose-6-phosphate, then phosphorylated again to fructose-1,6-bisphosphate",
        "this 6-carbon molecule splits into two 3-carbon molecules, DHAP and G3P; DHAP converts into a second G3P",
        "each G3P is oxidized and processed, producing ATP and NADH, and eventually converted into a pyruvate molecule",
        "the overall process (glycolysis) needs no oxygen, happens in the cytoplasm, and yields 2 pyruvate, a net 2 ATP, and 2 NADH per glucose",
    ), Explanation=""))
rows.append(dict(Topic="Respiration (Factors Affecting Rate) and Energy Yield of Lipids", Question="How do organism size, age, health, and body temperature affect the rate of respiration, and why does respiring the same amount of lipid release more energy than respiring glucose?",
    Answer_Summary=lettered(
        "smaller organisms have a higher surface-area-to-volume ratio and respire faster to meet energy needs",
        "younger, actively growing organisms respire faster than older ones with slower metabolism",
        "healthy organisms respire more efficiently than sick or damaged ones",
        "respiration speeds up with rising body temperature up to the optimum, then falls as heat denatures enzymes",
        "lipids have more carbon-hydrogen bonds storing more energy than glucose's bonds",
        "lipids are more reduced, providing more electrons for the electron transport chain, boosting NADH/FADH2 and so ATP output",
        "beta-oxidation of fatty acids yields more acetyl-CoA entering the Krebs cycle than glycolysis from one glucose, giving a higher ATP yield overall",
    ), Explanation=""))
rows.append(dict(Topic="Microbiology (Viruses vs Bacteria)", Question="What four features do viruses have that bacteria don't, and what are two merits and two demerits of viruses in human life?",
    Answer_Summary=lettered(
        "viruses have a protein capsid instead of a peptidoglycan cell wall",
        "viruses carry only DNA or only RNA, never both, unlike bacteria which have both",
        "viruses can't reproduce alone and need a host cell, unlike bacteria which self-replicate by binary fission",
        "viruses lack cytoplasm, ribosomes, and organelles, making them metabolically inactive outside a host",
        "merit: viral vectors are used in gene therapy and vaccine development",
        "merit: some viruses help control agricultural pests, cutting chemical pesticide use",
        "demerit: viruses cause serious diseases like HIV/AIDS, influenza, and COVID-19",
        "demerit: viral outbreaks strain healthcare systems and disrupt economies",
    ), Explanation=""))
rows.append(dict(Topic="Cell Transport (Osmosis and Diffusion Benefits)", Question="What are four benefits of osmosis and four benefits of diffusion to living organisms?",
    Answer_Summary=lettered(
        "osmosis lets plant roots absorb water from the soil for hydration and nutrient uptake",
        "osmosis maintains turgor pressure, keeping plant cells firm and the plant upright",
        "osmosis regulates water balance in animal cells, e.g. preventing red blood cells from bursting or shrinking",
        "osmosis drives water reabsorption in the kidney nephron, conserving body water",
        "diffusion moves oxygen and CO2 between alveoli and blood for respiration",
        "diffusion lets glucose and amino acids pass from the intestine into the blood",
        "diffusion carries metabolic wastes like urea from cells into blood for excretion",
        "diffusion lets neurotransmitters cross the synaptic cleft, continuing nerve signal transmission",
    ), Explanation=""))
rows.append(dict(Topic="Ecology (Animal Dependence on Plants)", Question="In four points, justify the fact that animals cannot survive without plants.",
    Answer_Summary=lettered(
        "plants are primary producers, converting solar energy into the food energy that flows through the whole food chain",
        "plants release oxygen via photosynthesis, which animals need for aerobic respiration",
        "plants absorb CO2, helping regulate atmospheric gas balance and prevent excess warming",
        "plants provide shelter and breeding grounds; losing plant habitats drives animal habitat loss and extinction",
    ), Explanation=""))
rows.append(dict(Topic="Plant Reproduction (Bryophyte Life Cycle)", Question="Describe the life cycle of a bryophyte (e.g. moss).",
    Answer_Summary=lettered(
        "the dominant phase is the haploid, photosynthetic gametophyte, which makes antheridia (male) and archegonia (female)",
        "in water, motile sperm swim from the antheridium to fertilize the egg in the archegonium, forming a diploid zygote",
        "the zygote develops into a sporophyte (foot, stalk, and capsule) still attached to the gametophyte",
        "meiosis inside the capsule produces haploid spores, which are released and germinate into new gametophytes",
        "because fertilization needs water for sperm to swim, bryophytes are limited to moist environments",
    ), Explanation=""))

for row in rows:
    row["Subject"] = "Biology"
    row["Form_Level"] = "Form 6"

fieldnames = ["Subject", "Form_Level", "Topic", "Question", "Answer_Summary", "Explanation"]
with open("necta-papers-acsee/biology_qa_final.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {len(rows)} rows to necta-papers-acsee/biology_qa_final.csv")

