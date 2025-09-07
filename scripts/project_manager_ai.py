import os
from pathlib import Path

# Define the root directory of the project
# The script is in iqsf/scripts, so root is two levels up.
ROOT_DIR = Path(__file__).parent.parent

def generate_legal_docs():
    """Generates the content for the legal documents."""
    print("Generating legal documents...")
    legal_dir = ROOT_DIR / "legal"

    # Content from user's prompt
    foundation_cert_content = """
## Certificate of Incorporation
### International Queer Safety Foundation

1. **Name:**  
   International Queer Safety Foundation

2. **Registered Agent & Address:**  
   [Registered Agent Name/Company], [Address in Delaware, e.g., 1209 Orange St, Wilmington, DE 19801]

3. **Nonprofit Purpose:**  
   This corporation is organized and operated exclusively for charitable and educational purposes within the meaning of Section 501(c)(3) of the Internal Revenue Code, including (but not limited to):  
   - Promoting international queer safety, research, advocacy, and education.
   - Developing, distributing, and maintaining safety data, AI tools, and public resources for LGBTQ+ communities globally.
   - Advancing public understanding of intersectional safety risks and rights for queer individuals everywhere and in emerging contexts.

4. **No Private Inurement:**  
   No part of the net earnings of the corporation shall inure to the benefit of any director, officer, or member.

5. **Dissolution Clause:**  
   Upon dissolution, assets shall be distributed for exempt purposes within the meaning of Section 501(c)(3), preferably to organizations with aligned mission and geographic reach.

6. **Incorporator:**  
   Name: [Your Name]  
   Date: [Today’s Date]
"""

    foundation_bylaws_content = """
## Bylaws of the International Queer Safety Foundation

**Article I: Offices**  
Principal office in Delaware.

**Article II: Purpose**  
See certificate; mission is to foster, promote, and develop queer safety globally.

**Article III: Board of Directors**  
- Minimum of 3 directors, majority independent.
- Board governs Foundation, appoints CEOs, forms committees, and may appoint subsidiary boards (for PBC or EU subsidiaries).

**Article IV: No Compensation**  
- Directors serve without compensation, may cover direct expenses.

**Article V: Powers**  
- May form, own, or control for-profit and international entities in pursuit of mission-aligned revenue (PBC, digital subsidiaries, etc.).

**Article VI: Amendment**  
- The Board may amend these bylaws by majority vote.

**Article VII: Indemnification**  
- Standard Delaware nonprofit protections for directors and officers.

*Full bylaws to be AI-generated and reviewed by counsel for signature.*
"""

    pbc_cert_content = """
## Certificate of Incorporation
### IQSF Tech PBC

1. **Name:**  
   IQSF Tech PBC

2. **Registered Agent & Address:**  
   [Registered Agent Name/Company], [Delaware Address]

3. **Public Benefit Statement:**  
   This corporation is a public benefit corporation, formed for the specific benefit of supporting, funding, and advancing charitable, intersectional, and technological solutions for queer safety worldwide in alignment with (and wholly owned by) the International Queer Safety Foundation.

4. **Stock Ownership:**  
   All shares are held, and Board is controlled, by the IQSF Foundation (or as designated by its Bylaws).

5. **Revenue/Asset Flows:**  
   Net proceeds return to Foundation or are reinvested into mission-driven activities, as determined by Foundation board.

6. **Incorporator:**  
   Name: [Your Name]  
   Date: [Today’s Date]
"""
    
    estonia_ou_content = "## Estonia OÜ formation docs (AI outline/template)\n\n*This document will contain the AI-generated outline and templates for forming the Estonian Private Limited Company (OÜ).*"
    berlin_branch_content = "## Berlin HQ registration (intent, ownership doc)\n\n*This document will contain the AI-generated declaration of intent and ownership structure for the Berlin branch.*"

    (legal_dir / "foundation_cert.md").write_text(foundation_cert_content)
    (legal_dir / "foundation_bylaws.md").write_text(foundation_bylaws_content)
    (legal_dir / "pbc_cert.md").write_text(pbc_cert_content)
    (legal_dir / "estonia_ou.md").write_text(estonia_ou_content)
    (legal_dir / "berlin_branch.md").write_text(berlin_branch_content)
    print("Legal documents generated.")

def generate_docs_content():
    """Generates content for the /docs folder."""
    print("Generating content for /docs...")
    docs_dir = ROOT_DIR / "docs"

    entity_structure_content = """
# Org Chart / Governance

### Markdown Table
| Entity                        | Type     | Location       | Ownership / Control           |
|-------------------------------|----------|---------------|-------------------------------|
| International Queer Safety Foundation | Nonprofit (501c3) | Delaware, USA   | Primary entity (board governed)|
| IQSF Tech PBC                 | PBC      | Delaware, USA  | Wholly owned by Foundation    |
| IQSF Digital OÜ               | Private Limited | Estonia, EU   | Wholly owned by Foundation    |
| Berlin Operations GmbH (or branch)    | GmbH/Branch | Berlin, Germany | Wholly owned by Foundation    |

### Simple Visual Flow
```plaintext
[International Queer Safety Foundation (501c3, DE)]
                |
        ---------------------------
        |            |            |
[IQSF Tech PBC] [Estonia OÜ] [Berlin GmbH/Branch]
   (DE, PBC)      (EE, Digital)    (DE/EU hub)
```
"""
    (docs_dir / "ENTITY_STRUCTURE.md").write_text(entity_structure_content)
    
    ai_team_content = """
# AI Team Roles and Responsibilities

This document describes the roles and duties of the AI agents managing this project.
*(This is a placeholder. The full document will be generated by the Project Manager AI.)*
"""
    (docs_dir / "AI_TEAM.md").write_text(ai_team_content)

    onboarding_content = """
# Onboarding Guide

This guide provides the necessary steps for a new contributor (AI or human) to get started.
*(This is a placeholder. The full document will be generated by the Project Manager AI.)*
"""
    (docs_dir / "ONBOARDING.md").write_text(onboarding_content)

    print("Docs content generated.")


def main():
    """Main function to run the scaffolding tasks."""
    print("Starting project content generation...")
    generate_legal_docs()
    generate_docs_content()
    print("Project content generation complete!")

if __name__ == "__main__":
    main()
