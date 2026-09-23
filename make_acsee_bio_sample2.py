import csv

def lettered(*phrases):
    letters = "abcdefghij"
    return ", ".join(f"{letters[i]}) {p}" for i, p in enumerate(phrases))

rows = [
    dict(
        Subject="Biology", Form_Level="Form 6", Topic="Proteins",
        Question=("A Form Five student was provided with a sample containing globular protein to "
                   "identify its features. Which five features did the student identify?"),
        Answer_Summary=lettered(
            "soluble in water, forming colloidal solutions",
            "compact and spherical shape",
            "complex tertiary structure stabilized by hydrogen and ionic bonds",
            "specific biological function (enzymes, hormones, antibodies)",
            "sensitive to pH, temperature and ionic strength",
        ),
        Explanation="",
    ),
    dict(
        Subject="Biology", Form_Level="Form 6", Topic="Proteins",
        Question=("Denatured protein molecules lose both their three-dimensional structure and "
                   "functions. Explain five ways which you would use to prevent denaturation."),
        Answer_Summary=lettered(
            "maintain optimal temperature",
            "control pH levels within the protein's optimal range",
            "avoid exposure to harmful chemicals (detergents, heavy metals, solvents)",
            "use stabilizing agents like glycerol or specific salts",
            "prevent mechanical agitation (excessive shaking or stirring)",
        ),
        Explanation="",
    ),
    dict(
        Subject="Biology", Form_Level="Form 6", Topic="Role of Water in the Body",
        Question=("Explain how water is used in each of the following processes in the human body: "
                   "(i) Transportation (ii) Removal of wastes (iii) Secretion (iv) Hearing and balance"),
        Answer_Summary=lettered(
            "transportation: carries nutrients, hormones and gases in plasma",
            "waste removal: dissolves urea and creatinine for excretion",
            "secretion: forms saliva, mucus and digestive juices",
            "hearing/balance: endolymph transmits vibrations and detects movement",
        ),
        Explanation="",
    ),
    dict(
        Subject="Biology", Form_Level="Form 6", Topic="Cell Organelles",
        Question=("Use one point in each case to justify the need for animal cells to possess each of "
                   "the following organelles/structures: (i) Peroxisomes (ii) Lysosomes "
                   "(iii) Rough endoplasmic reticulum (iv) Glycocalyx"),
        Answer_Summary=lettered(
            "peroxisomes: break down hydrogen peroxide to detoxify the cell",
            "lysosomes: digest macromolecules, damaged organelles and pathogens",
            "rough endoplasmic reticulum: ribosomes synthesize proteins for secretion or the membrane",
            "glycocalyx: enables cell recognition, adhesion and protection",
        ),
        Explanation="",
    ),
    dict(
        Subject="Biology", Form_Level="Form 6", Topic="Nervous System",
        Question="Use four points to show how the structure of a synapse is adapted for transmission of impulses.",
        Answer_Summary=lettered(
            "synaptic vesicles in the presynaptic terminal store and quickly release neurotransmitters",
            "narrow synaptic cleft lets neurotransmitters diffuse across rapidly",
            "receptors on the postsynaptic membrane bind specifically to neurotransmitters for an accurate response",
            "voltage-gated calcium channels open on an action potential, triggering vesicle fusion for precise timing",
        ),
        Explanation=("The synapse structure is specialized for rapid, precise transmission of nerve "
                     "impulses between neurons or to an effector cell."),
    ),
]

fieldnames = ["Subject", "Form_Level", "Topic", "Question", "Answer_Summary", "Explanation"]
out_path = r"C:\Users\marti\OneDrive\Desktop\JIBU\necta-papers-acsee\biology_qa_sample2.csv"
with open(out_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {len(rows)} rows to {out_path}")
