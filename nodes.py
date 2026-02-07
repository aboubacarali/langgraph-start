from state import SupportState
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

# Charger les variables d’environnement (.env)
load_dotenv()

# Initialiser le modèle
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def classify_question(state: SupportState) -> SupportState:
    question = state["question"]

    prompt = f"""
    Tu es un classificateur de questions.

    Classe la question suivante dans UNE SEULE de ces catégories :
    - tech
    - commercial
    - faq

    Réponds uniquement par un mot parmi ces trois.

    Question : {question}
    """

    response = llm.invoke([HumanMessage(content=prompt)])

    category = response.content.strip().lower()

    state["category"] = category

    return state


def handle_tech(state: SupportState) -> SupportState:
    question = state["question"]

    prompt = f"""
    Tu es un support technique.

    Réponds clairement et de manière concise à la question technique suivante.
    Si des étapes sont nécessaires, donne-les sous forme de liste.

    Question : {question}
    """

    response = llm.invoke([HumanMessage(content=prompt)])
    state["answer"] = response.content.strip()

    return state


def handle_commercial(state: SupportState) -> SupportState:
    question = state["question"]

    prompt = f"""
    Tu es un support commercial.

    Réponds de manière professionnelle et concise à la question commerciale suivante.
    Mets l'accent sur les avantages et les options possibles.

    Question : {question}
    """

    response = llm.invoke([HumanMessage(content=prompt)])
    state["answer"] = response.content.strip()

    return state


def handle_faq(state: SupportState) -> SupportState:
    question = state["question"]

    prompt = f"""
    Tu es un assistant FAQ.

    Réponds clairement et de manière concise à la question suivante.

    Question : {question}
    """

    response = llm.invoke([HumanMessage(content=prompt)])
    state["answer"] = response.content.strip()

    return state
