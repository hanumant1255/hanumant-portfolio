from flask import Flask, render_template


app = Flask(__name__)


PROFILE = {
    "name": "Hanumant Shinde",
    "title": "Senior AI/ML Engineer",
    "location": "Pune, India",
    "phone": "+91-9763015647",
    "email": "the.real.hshinde@gmail.com",
    "linkedin": "https://linkedin.com/in/meethshinde",
    "github": "https://github.com/hanumant1255",
    "resume_file": "Hanumant_Shinde_Resume_2026.html",
}


METRICS = [
    {"value": "97%", "label": "SLM bug-triage accuracy"},
    {"value": "2B+", "label": "daily security transactions"},
    {"value": "70%", "label": "manual triage reduction"},
]


FEATURED_WORK = [
    {
        "title": "Binary SLM for Windows Bug Triage",
        "summary": (
            "Fine-tuned Phi-3 Mini 3.8B with QLoRA and PEFT to classify structured bug reports "
            "as auto-close or investigation-needed, outperforming GPT-4o on the target workflow."
        ),
        "impact": "97% accuracy, 0.96 F1, 300+ engineer-hours saved monthly",
        "stack": "Python, PyTorch, HuggingFace TRL, QLoRA, PEFT, Azure ML, ONNX",
    },
    {
        "title": "Multi-Domain SLM Data Pipeline",
        "summary": (
            "Architected a configurable dataset generator with LLM auto-labelling, human verification, "
            "heuristics, and incremental retraining support for security, performance, UI, and compliance models."
        ),
        "impact": "95% faster retraining cycles and reusable domain adaptation workflow",
        "stack": "Azure ML, dataset versioning, model registry, managed endpoints, evaluation pipelines",
    },
    {
        "title": "ZI-Agent for Network Policy Management",
        "summary": (
            "Led a multi-stage agentic AI system using LLM reasoning, GraphRAG, and MCP to automate "
            "network policy configuration for enterprise security teams."
        ),
        "impact": "60% less manual configuration time for 1,000+ network engineers",
        "stack": "Python, Java, GraphRAG, MCP, Kafka, Redis, Spring Boot, AWS",
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
        experience=EXPERIENCE,
        skills=SKILLS,
    )


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
