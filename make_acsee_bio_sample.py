import csv

rows = [
    dict(
        Subject="Biology", Form_Level="Form 6", Topic="Proteins",
        Question=("A Form Five student was provided with a sample containing globular protein to "
                   "identify its features. Which five features did the student identify?"),
        Answer_Summary="\n".join([
            "• Soluble in water — forms colloidal solutions",
            "• Compact, spherical shape",
            "• Complex tertiary structure, stabilized by hydrogen and ionic bonds",
            "• Perform specific biological roles (enzymes, hormones, antibodies)",
            "• Sensitive to pH, temperature and ionic strength — can denature",
        ]),
        Explanation="",
    ),
    dict(
        Subject="Biology", Form_Level="Form 6", Topic="Proteins",
        Question=("Denatured protein molecules lose both their three-dimensional structure and "
                   "functions. Explain five ways which you would use to prevent denaturation."),
        Answer_Summary="\n".join([
            "• Maintain optimal temperature",
            "• Control pH within the protein's normal range",
            "• Avoid harmful chemicals (detergents, heavy metals, solvents)",
            "• Use stabilizing agents such as glycerol or specific salts",
            "• Prevent mechanical agitation — avoid excessive shaking or stirring",
        ]),
        Explanation="",
    ),
    dict(
        Subject="Biology", Form_Level="Form 6", Topic="Role of Water in the Body",
        Question=("Explain how water is used in each of the following processes in the human body: "
                   "(i) Transportation (ii) Removal of wastes (iii) Secretion (iv) Hearing and balance"),
        Answer_Summary="\n".join([
            "• Transportation — carries nutrients, hormones and gases in blood plasma",
            "• Waste removal — dissolves and excretes urea and creatinine via the kidneys and sweat",
            "• Secretion — forms saliva, mucus and digestive juices",
            "• Hearing and balance — forms the endolymph fluid in the cochlea and semicircular canals",
        ]),
        Explanation="",
    ),
    dict(
        Subject="Biology", Form_Level="Form 6", Topic="Cell Organelles",
        Question=("Use one point in each case to justify the need for animal cells to possess each of "
                   "the following organelles/structures: (i) Peroxisomes (ii) Lysosomes "
                   "(iii) Rough endoplasmic reticulum (iv) Glycocalyx"),
        Answer_Summary="\n".join([
            "• Peroxisomes — detoxify harmful substances by breaking down hydrogen peroxide",
            "• Lysosomes — digest macromolecules, damaged organelles and pathogens",
            "• Rough endoplasmic reticulum — site of protein synthesis for secretion or membrane use",
            "• Glycocalyx — enables cell recognition, adhesion and protection",
        ]),
        Explanation="",
    ),
    dict(
        Subject="Biology", Form_Level="Form 6", Topic="Nervous System",
        Question="Use four points to show how the structure of a synapse is adapted for transmission of impulses.",
        Answer_Summary="\n".join([
            "• Synaptic vesicles store neurotransmitters for quick release",
            "• Narrow synaptic cleft allows neurotransmitters to diffuse across rapidly",
            "• Receptors on the postsynaptic membrane bind specifically for an accurate response",
            "• Voltage-gated calcium channels trigger vesicle fusion for precise timing",
        ]),
        Explanation=("The synapse structure is built to make nerve-impulse transmission both fast and "
                     "precise, from one neuron to the next or to an effector cell."),
    ),
]

fieldnames = ["Subject", "Form_Level", "Topic", "Question", "Answer_Summary", "Explanation"]
out_path = r"C:\Users\marti\OneDrive\Desktop\JIBU\necta-papers-acsee\biology_qa_sample.csv"
with open(out_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {len(rows)} rows to {out_path}")
