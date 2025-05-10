from transformers import pipeline
from jinja2 import Template
from datetime import datetime
import os
import re
import argparse
import json

AGENT_LABELS = [
    "marketing", "support", "operations", "development", "multimedia", "sales", "data", "security"
]

INTEGRATION_MAP = {
    "hubspot": ["crm", "leads", "contacts"],
    "canva_api": ["design", "graphics", "social media"],
    "facebook_graph": ["facebook", "social media", "posts"],
    "twilio": ["sms", "phone", "ivr"],
    "openai": ["language", "text", "gpt"],
    "azure": ["cloud", "deployment"],
}

def load_template(file_path):
    with open(file_path, 'r') as f:
        return Template(f.read())

def extract_integrations(description):
    found = []
    for key, keywords in INTEGRATION_MAP.items():
        if any(word in description.lower() for word in keywords):
            found.append(key)
    return found or ["openai"]

def clean_name(text):
    return re.sub(r'\W+', '_', text.lower()).strip('_')

def generate_agent(nl_input):
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    classification = classifier(nl_input, AGENT_LABELS)
    agent_type = classification["labels"][0]
    agent_name = " ".join(nl_input.split(" ")[0:4]).capitalize()
    integrations = extract_integrations(nl_input)
    timestamp = datetime.now().isoformat()

    folder_name = clean_name(agent_name)
    os.makedirs(folder_name, exist_ok=True)

    tmpl = load_template("templates/agent_config_template.j2")
    config = tmpl.render(
        agent_name=agent_name,
        description=nl_input,
        agent_type=agent_type,
        integrations=integrations,
        timestamp=timestamp
    )

    with open(f"{folder_name}/agent_config.yaml", 'w') as f:
        f.write(config)

    print(f"✅ Created: {folder_name}/agent_config.yaml")
    print(f"🧠 Agent Type: {agent_type}")
    print(f"🔌 Integrations: {integrations}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--desc", help="Describe your agent in natural language", required=True)
    args = parser.parse_args()
    generate_agent(args.desc)
