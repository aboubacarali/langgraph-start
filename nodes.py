from state import SupportState


def classify_question(state: SupportState) -> SupportState:
    question = state["question"].lower()

    if "prix" in question:
        state["category"] = "commercial"
    elif "bug" in question:
        state["category"] = "tech"
    else:
        state["category"] = "faq"

    return state


def handle_tech(state: SupportState) -> SupportState:
    state["answer"] = "Un ticket technique a été créé."
    return state


def handle_commercial(state: SupportState) -> SupportState:
    state["answer"] = "Notre équipe commerciale vous contactera."
    return state


def handle_faq(state: SupportState) -> SupportState:
    state["answer"] = "Voici la réponse à votre question fréquente."
    return state
