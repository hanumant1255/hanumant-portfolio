from flask import Flask, render_template


app = Flask(__name__)


PROFILE = {
    "name": "Hanumant Shinde",
    "title": "Senior AI/ML Engineer",
    "headline": "I turn ambiguous AI ideas into reliable systems that ship.",
    "summary": (
        "Senior AI/ML engineer building small language models, agentic workflows, "
        "MLOps pipelines, and high-scale backend systems for security and platform teams."
    ),
    "location": "Pune, India",
    "phone": "+91-9763015647",
    "email": "the.real.hshinde@gmail.com",
    "linkedin": "https://linkedin.com/in/meethshinde",
    "github": "https://github.com/hanumant1255",
    "resume_file": "Hanumant_Shinde_Resume_2026.html",
    "availability": "Open to AI/ML engineering, applied AI platform, and staff backend roles.",
    "quote": "Curiosity finds the edge case. Ownership gets it into production.",
    "site_url": "https://hanumant1255.github.io/hanumant-portfolio/",
    "thumbnail_url": "https://hanumant1255.github.io/hanumant-portfolio/static/portfolio-thumbnail.png",
}


METRICS = [
    {"value": "97%", "label": "SLM bug-triage accuracy", "detail": "Phi-3 Mini fine-tuned for structured bug fields"},
    {"value": "2B+", "label": "daily security transactions", "detail": "Risk pipelines designed for sub-100ms latency"},
    {"value": "70%", "label": "manual triage reduction", "detail": "300+ engineer-hours saved per month"},
]


FEATURED_WORK = [
    {
        "title": "Binary SLM for Windows Bug Triage",
        "tag": "SLM lifecycle",
        "problem": "Manual bug triage was slow, repetitive, and expensive at Windows platform scale.",
        "built": "Fine-tuned Phi-3 Mini 3.8B with QLoRA and PEFT, then deployed the model through Azure ML and ONNX optimization.",
        "impact": "97% accuracy, 0.96 F1, 300+ engineer-hours saved monthly",
        "stack": "Python, PyTorch, HuggingFace TRL, QLoRA, PEFT, Azure ML, ONNX",
    },
    {
        "title": "Multi-Domain SLM Data Pipeline",
        "tag": "Data and MLOps",
        "problem": "Every new model domain needed trustworthy labels without rebuilding the training workflow.",
        "built": "Created a configurable generator with LLM auto-labelling, human verification, heuristics, and incremental retraining.",
        "impact": "95% faster retraining cycles and reusable domain adaptation workflow",
        "stack": "Azure ML, dataset versioning, model registry, managed endpoints, evaluation pipelines",
    },
    {
        "title": "ZI-Agent for Network Policy Management",
        "tag": "Agentic AI",
        "problem": "Network engineers needed faster, safer ways to configure complex enterprise policy rules.",
        "built": "Led a multi-stage AI agent using LLM reasoning, GraphRAG, and MCP as a standalone service.",
        "impact": "60% less manual configuration time for 1,000+ network engineers",
        "stack": "Python, Java, GraphRAG, MCP, Kafka, Redis, Spring Boot, AWS",
    },
]


OPERATING_PRINCIPLES = [
    {
        "title": "Get the job done, then harden it",
        "text": "Start with the job to be done, scope the smallest reliable system, then measure whether it helped.",
    },
    {
        "title": "Stay curious near the data",
        "text": "The interesting bugs usually live between labels, telemetry, user behavior, and production constraints.",
    },
    {
        "title": "Make AI boring in production",
        "text": "Good models are only valuable when evaluation, monitoring, rollback, and ownership are just as solid.",
    },
    {
        "title": "Explain the tradeoff",
        "text": "I like decisions that a teammate can understand six months later: why this model, why this data, why now.",
    },
]


EXPERIENCE = [
    {
        "company": "Microsoft",
        "period": "Oct 2025 - Present",
        "role": "Senior AI Engineer, Small Language Models, Windows AI Platform",
        "highlights": [
            "Built and deployed a 97% accurate binary SLM for structured bug triage.",
            "Own Azure ML training jobs, model registry, managed endpoints, monitoring, and retraining loops.",
            "Optimized models to INT4 with ONNX for low-latency on-device inference.",
            "Built RAG and GraphRAG systems over Windows telemetry and bug corpora.",
        ],
    },
    {
        "company": "Zscaler",
        "period": "Feb 2022 - Sep 2025",
        "role": "Staff Backend Engineer, Security Platform",
        "highlights": [
            "Led ZI-Agent, a standalone agentic AI service for automated network policy management.",
            "Architected risk aggregation pipelines processing 2B+ security transactions per day under 100ms latency.",
            "Designed high-throughput Kafka and Avro message exchange with 99.99% fault tolerance.",
            "Mentored four engineers, all promoted to senior.",
        ],
    },
    {
        "company": "Xactly Corporation",
        "period": "Sep 2021 - Feb 2022",
        "role": "Senior Software Engineer",
        "highlights": [
            "Enhanced ORM framework used by 20+ teams and improved query performance by 35%.",
            "Delivered high-performance REST APIs with 95%+ test coverage.",
        ],
    },
    {
        "company": "Randstad RiseSmart",
        "period": "Jul 2020 - Aug 2021",
        "role": "Senior Development Engineer",
        "highlights": [
            "Re-architected a 500K+ user job portal from monolith to AWS ECS microservices.",
            "Cut infrastructure cost by 40% and improved response consistency by 60%.",
        ],
    },
    {
        "company": "TIAA and GS Lab",
        "period": "Jul 2016 - Jul 2020",
        "role": "Software Engineer",
        "highlights": [
            "Reduced API latency from 800ms to 300ms for a retirement platform serving 5M+ users.",
            "Contributed to an open-source networking library adopted by Intel's 5G division.",
        ],
    },
]


SKILLS = {
    "AI / ML": [
        "SLM/LLM fine-tuning",
        "QLoRA",
        "LoRA",
        "PEFT",
        "SFTTrainer",
        "Transformers",
        "PyTorch",
        "RAG",
        "GraphRAG",
        "AI agents",
        "MCP",
        "ONNX",
        "INT4/INT8 quantization",
    ],
    "MLOps": [
        "Azure ML",
        "training jobs",
        "model registry",
        "managed endpoints",
        "monitoring",
        "dataset versioning",
        "experiment tracking",
    ],
    "Backend": [
        "Python",
        "Java 8-21",
        "Spring Boot",
        "REST APIs",
        "distributed systems",
        "microservices",
        "low-latency systems",
    ],
    "Cloud and Data": [
        "Azure",
        "AWS",
        "Docker",
        "Kubernetes",
        "OpenShift",
        "Kafka",
        "Redis",
        "PostgreSQL",
        "MongoDB",
        "Elasticsearch",
    ],
}


@app.route("/")
def home():
    return render_template(
        "index.html",
        profile=PROFILE,
        metrics=METRICS,
        featured_work=FEATURED_WORK,
        operating_principles=OPERATING_PRINCIPLES,
        experience=EXPERIENCE,
        skills=SKILLS,
    )


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
