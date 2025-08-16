#!/usr/bin/env python3
"""
Workout Planner (offline)
Usage:
  python main.py --input "Goal: gain muscle; Days: 4"
"""
import argparse, requests, os, sys, re

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL = "llama3.2:4b"
TIMEOUT = 180

def run_llama(prompt):
    r = requests.post(OLLAMA_URL, json={"model": MODEL, "prompt": prompt, "stream": False}, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json().get("response","").strip()

def build_prompt(spec):
    return (
        "Create a weekly strength/fitness plan based on the user's goal and days per week.\n"
        "Include: day split, exercises with sets/reps, progression tips, warmup and cautions.\n\n"
        f"User spec: {spec}"
    )

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", "-i", required=True)
    args = p.parse_args()
    print(run_llama(build_prompt(args.input)))

if __name__ == "__main__":
    main()
