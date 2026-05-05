from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "Dave-Oluwafemi-SaaS-Support-Resume.pdf"


def p(text, style):
    return Paragraph(text, style)


def bullets(items, style):
    return ListFlowable(
        [ListItem(Paragraph(item, style), leftIndent=0) for item in items],
        bulletType="bullet",
        leftIndent=14,
        bulletFontSize=7,
        bulletOffsetY=1,
    )


def section(title, styles):
    return [
        Spacer(1, 0.12 * inch),
        Paragraph(title, styles["section"]),
        HRFlowable(width="100%", thickness=0.7, color=colors.HexColor("#2c3e50"), spaceAfter=6),
    ]


def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="name",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=20,
            leading=23,
            alignment=1,
            textColor=colors.HexColor("#2c3e50"),
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="role",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=14,
            alignment=1,
            textColor=colors.HexColor("#2c3e50"),
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="contact",
            parent=styles["Normal"],
            fontSize=8.8,
            leading=12,
            alignment=1,
            textColor=colors.HexColor("#3d4852"),
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="section",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=13,
            textColor=colors.HexColor("#2c3e50"),
            spaceBefore=2,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="job",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9.5,
            leading=12,
            textColor=colors.HexColor("#2c3e50"),
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="body",
            parent=styles["Normal"],
            fontSize=8.8,
            leading=12,
            textColor=colors.HexColor("#2f3a43"),
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="bullet",
            parent=styles["Normal"],
            fontSize=8.6,
            leading=11.2,
            textColor=colors.HexColor("#2f3a43"),
        )
    )

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=letter,
        rightMargin=0.62 * inch,
        leftMargin=0.62 * inch,
        topMargin=0.5 * inch,
        bottomMargin=0.5 * inch,
        title="Dave Oluwafemi SaaS Support Resume",
        author="Dave Oluwafemi",
    )

    story = [
        p("DAVE OLUWAFEMI", styles["name"]),
        p("SaaS Customer Support Specialist | Technical Operations | CRM & Integration Support", styles["role"]),
        p("Remote | Global | Lagos, Nigeria | +234 913 079 4050 | daveoluwafemi6@gmail.com", styles["contact"]),
        p(
            'LinkedIn: linkedin.com/in/dave-oluwafemi-53b716132 | GitHub: github.com/barba4real | Portfolio: <a href="https://barba4real.github.io/saas-support-portfolio/">barba4real.github.io/saas-support-portfolio</a>',
            styles["contact"],
        ),
    ]

    story += section("PROFESSIONAL SUMMARY", styles)
    story += [
        p(
            "SaaS Customer Support and Technical Operations Specialist with experience supporting high-volume digital platforms, resolving user and system issues, and maintaining structured CRM-based workflows in remote environments.",
            styles["body"],
        ),
        p(
            "Experienced in real-time customer support across email, chat, and voice channels, with strong ability to troubleshoot platform issues, investigate system behavior, and ensure fast and accurate resolution of customer requests.",
            styles["body"],
        ),
        p(
            "Skilled in SaaS-style support operations including ticketing systems, escalation handling, workflow management, CRM support, integration support, and cross-functional collaboration to maintain service reliability and customer satisfaction.",
            styles["body"],
        ),
    ]

    story += section("CORE SKILLS", styles)
    story.append(
        bullets(
            [
                "SaaS Customer Support across email, chat, and voice channels",
                "CRM Systems and Ticketing Workflows: Zendesk, Intercom, HubSpot, Salesforce",
                "Ticket Lifecycle Management, SLA Awareness, Escalation Handling, and Case Resolution",
                "Technical Troubleshooting, Root Cause Analysis, and Customer Issue Documentation",
                "CRM and Integration Support with foundational API, authentication, and request/response troubleshooting",
                "Postman for basic API testing and Chrome DevTools for web issue debugging",
                "Customer Onboarding, Workflow Support, Data Accuracy, Reporting, and Process Improvement",
                "Google Analytics 4, Google Tag Manager, Google Sheets, WordPress, Shopify, and Remote Support Operations",
            ],
            styles["bullet"],
        )
    )

    story += section("PROFESSIONAL EXPERIENCE", styles)
    story += [
        p("Remote Customer Support Specialist | ASAP Tickets | Remote | Jan 2026 - Present", styles["job"]),
        bullets(
            [
                "Delivered high-volume SaaS-style customer support across booking, account, and platform workflows.",
                "Investigated and resolved user and system issues using internal tools, structured data, and operational logs.",
                "Applied structured troubleshooting methods to identify root causes and ensure accurate resolution.",
                "Managed multiple support requests across chat, email, and voice channels in a fast-paced environment.",
                "Maintained accurate case documentation and CRM updates throughout the customer issue lifecycle.",
                "Coordinated with internal teams to resolve escalated platform and customer-impacting issues.",
            ],
            styles["bullet"],
        ),
        Spacer(1, 0.08 * inch),
        p("Digital Operations & SaaS Systems Specialist | Endless Pro Solutions | Remote | 2020 - Present", styles["job"]),
        bullets(
            [
                "Designed and managed structured digital workflows supporting SaaS-style customer data and operational systems.",
                "Implemented analytics tracking using Google Analytics 4 and Google Tag Manager.",
                "Developed automation processes to improve data accuracy and operational efficiency.",
                "Supported API integrations and third-party system connectivity for workflow optimization.",
                "Developed reporting structures to improve visibility across customer journeys and platform performance.",
                "Improved system efficiency through automation, workflow optimization, and structured process design.",
            ],
            styles["bullet"],
        ),
        Spacer(1, 0.08 * inch),
        p("Digital Support & Technical Consultant | Freelance | 2017 - 2020", styles["job"]),
        bullets(
            [
                "Provided technical support for users of web platforms, CRM systems, and digital tools.",
                "Resolved system errors, website issues, and configuration problems across multiple platforms.",
                "Supported user onboarding and guided clients through SaaS-style workflows.",
                "Delivered troubleshooting support and structured guidance for digital system usage.",
            ],
            styles["bullet"],
        ),
    ]

    story += section("TOOLS & TECHNOLOGIES", styles)
    story.append(
        bullets(
            [
                "Support & CRM: Zendesk, Intercom, HubSpot, Salesforce",
                "Technical & Debugging: Postman, Chrome DevTools, API integrations, MySQL basic queries",
                "Analytics & Tracking: Google Analytics 4, Google Tag Manager",
                "Data & Reporting: Google Sheets, customer data analysis, issue pattern identification",
                "Platforms & CMS: WordPress, Shopify",
                "Productivity & Collaboration: Google Workspace, Slack, Notion",
            ],
            styles["bullet"],
        )
    )

    story += section("EDUCATION", styles)
    story.append(
        bullets(
            [
                "Web Development Foundations | Independent Learning | 2014 - 2017",
                "Graphic Design & Creative Development | Professional Tutoring & Practice | 2005 - 2015",
                "CPISM & DISM - Information Systems Management | Aptech Worldwide | 2001 - 2003",
                "OND - Electrical & Electronics Engineering | Osun State College of Technology, Esa-Oke | 2003 - 2005",
                "Radio, Television & Electronics | Federal Technical College, Ilesha | 1997 - 2000",
            ],
            styles["bullet"],
        )
    )

    story += section("ADDITIONAL INFORMATION", styles)
    story.append(
        bullets(
            [
                "Strong experience in SaaS-style customer support environments.",
                "Skilled in troubleshooting system and user-related issues under pressure.",
                "Comfortable working with structured CRM and ticketing workflows.",
                "Quick learner of new SaaS tools and operational platforms.",
                "Experienced in remote-first, cross-functional environments.",
                "Available for global remote roles.",
            ],
            styles["bullet"],
        )
    )

    doc.build(story)
    print(OUT)


if __name__ == "__main__":
    build()
