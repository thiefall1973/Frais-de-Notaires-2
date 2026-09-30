"""
Agent de calcul des frais notariaux – Sénégal
Développé pour investissementimmoafrique.com
"""

import anthropic
from anthropic import beta_tool

FCFA_PER_EUR = 655.957

client = anthropic.Anthropic()


def _eur_to_fcfa(eur: float) -> float:
    return eur * FCFA_PER_EUR


def _fcfa_to_eur(fcfa: float) -> float:
    return fcfa / FCFA_PER_EUR


@beta_tool
def calculer_frais_notariaux(prix_eur: float) -> dict:
    """Calcule les frais notariaux pour une transaction immobilière au Sénégal.

    Args:
        prix_eur: Prix du bien immobilier en euros.
    """
    prix_fcfa = _eur_to_fcfa(prix_eur)

    if prix_fcfa <= 20_000_000:
        taux_notaire = 0.045
    elif prix_fcfa <= 80_000_000:
        taux_notaire = 0.03
    else:
        taux_notaire = 0.015

    base_notaire_fcfa = prix_fcfa * taux_notaire
    tva_notaire_fcfa = base_notaire_fcfa * 0.18
    total_notaire_fcfa = base_notaire_fcfa + tva_notaire_fcfa

    droits_enregistrement_fcfa = prix_fcfa * 0.05
    publicite_fonciere_fcfa = prix_fcfa * 0.01
    droits_timbre_fcfa = 6_000.0
    frais_dossier_fcfa = 200_000.0

    total_fcfa = (
        total_notaire_fcfa
        + droits_enregistrement_fcfa
        + publicite_fonciere_fcfa
        + droits_timbre_fcfa
        + frais_dossier_fcfa
    )

    def fmt(fcfa: float) -> dict:
        return {"eur": round(_fcfa_to_eur(fcfa), 2), "fcfa": round(fcfa)}

    return {
        "prix": {"eur": prix_eur, "fcfa": round(prix_fcfa)},
        "emoluments_notaire_tva": fmt(total_notaire_fcfa),
        "droits_enregistrement_5pct": fmt(droits_enregistrement_fcfa),
        "publicite_fonciere_1pct": fmt(publicite_fonciere_fcfa),
        "droits_timbre": fmt(droits_timbre_fcfa),
        "frais_dossier_certificats": fmt(frais_dossier_fcfa),
        "total_estime": fmt(total_fcfa),
    }


SYSTEM_PROMPT = """Tu es un conseiller expert en immobilier au Sénégal, spécialisé dans les frais notariaux.
Tu aides les investisseurs, notamment la diaspora, à comprendre et estimer les coûts liés à l'acquisition \
d'un bien immobilier au Sénégal.

Quand un utilisateur te donne un prix (en EUR ou en FCFA), utilise l'outil `calculer_frais_notariaux` \
pour calculer les frais précis et présente les résultats de façon claire et structurée.

Si le prix est fourni en FCFA, convertis-le en EUR (1 EUR = 655,957 FCFA) avant d'appeler l'outil.

Après le calcul, explique brièvement chaque ligne de frais et donne des conseils pratiques si pertinent.
"""


def run_agent(message_utilisateur: str) -> None:
    """Lance l'agent avec la question de l'utilisateur et affiche la réponse en streaming."""
    print(f"\nUtilisateur : {message_utilisateur}\n")
    print("Agent : ", end="", flush=True)

    messages = [{"role": "user", "content": message_utilisateur}]

    with client.beta.messages.stream(
        model="claude-opus-5-5",
        max_tokens=16000,
        thinking={"type": "adaptive"},
        system=SYSTEM_PROMPT,
        tools=[calculer_frais_notariaux],
        messages=messages,
    ) as stream:
        for event in stream:
            if hasattr(event, "type"):
                if event.type == "content_block_delta":
                    delta = event.delta
                    if hasattr(delta, "text"):
                        print(delta.text, end="", flush=True)

        final = stream.get_final_message()

    # Si des appels d'outils ont eu lieu, relancer avec les résultats
    if final.stop_reason == "tool_use":
        messages.append({"role": "assistant", "content": final.content})

        tool_results = []
        for block in final.content:
            if block.type == "tool_use":
                result = calculer_frais_notariaux(block.input["prix_eur"])
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(result),
                })

        messages.append({"role": "user", "content": tool_results})

        with client.beta.messages.stream(
            model="claude-opus-5-5",
            max_tokens=16000,
            thinking={"type": "adaptive"},
            system=SYSTEM_PROMPT,
            tools=[calculer_frais_notariaux],
            messages=messages,
        ) as stream2:
            for event in stream2:
                if hasattr(event, "type"):
                    if event.type == "content_block_delta":
                        delta = event.delta
                        if hasattr(delta, "text"):
                            print(delta.text, end="", flush=True)

    print("\n")


if __name__ == "__main__":
    exemples = [
        "Combien coûtent les frais notariaux pour un bien à 80 000 € au Sénégal ?",
        "J'achète un appartement à Dakar pour 50 000 000 FCFA, quels sont les frais ?",
        "Quels sont les différents postes de frais notariaux au Sénégal ?",
    ]

    for question in exemples:
        run_agent(question)
        print("-" * 60)
