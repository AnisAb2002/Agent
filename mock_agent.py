# mock_agent.py

def simuler_reponse_agent_faible(input_utilisateur):
    """
    Simule un agent "Vibe" mal configuré (celui du début du projet).
    Il est évasif, manque de politesse et ne respecte pas les contraintes métiers.
    OBJECTIF : Montrer au jury que votre outil détecte les ÉCHECS (❌).
    """
    input_lower = input_utilisateur.lower()
    
    # Cas de remboursement / SAV
    if "remboursement" in input_lower or "rembourser" in input_lower:
        return "Je ne sais pas, demandez au support technique demain."
    
    # Cas de prix ou budget
    elif "prix" in input_lower or "combien" in input_lower or "budget" in input_lower:
        return "Les prix sont sur le catalogue, cherchez un peu."
    
    # Cas de recherche de stage (ton exemple initial)
    elif "stage" in input_lower or "offre" in input_lower:
        return "Il n'y a plus de place, réessayez l'année prochaine."
        
    # Réponse par défaut très médiocre
    else:
        return "Euh... je ne comprends pas. Reformulez."


def simuler_reponse_agent_robuste(input_utilisateur):
    """
    Simule un agent "Optimisé" (celui après avoir suivi les conseils de VibeGuard).
    Il est poli, structuré et donne des informations exploitables.
    OBJECTIF : Montrer que votre outil valide la RÉUSSITE (✅).
    """
    input_lower = input_utilisateur.lower()
    
    # Cas de remboursement / SAV
    if "remboursement" in input_lower or "rembourser" in input_lower:
        return ("Je comprends tout à fait votre demande. Pour procéder à un remboursement, "
                "merci de me transmettre votre numéro de commande. Nous traitons les retours sous 48h.")
    
    # Cas de prix ou budget
    elif "prix" in input_lower or "combien" in input_lower or "budget" in input_lower:
        return ("Nos tarifs s'adaptent à votre budget. Nous avons des solutions allant de 20€ à 150€. "
                "Souhaitez-vous voir notre sélection la plus abordable ?")
    
    # Cas de recherche de stage
    elif "stage" in input_lower or "offre" in input_lower:
        return ("Nous avons actuellement 3 offres de stage en développement Python et IA. "
                "Vous pouvez postuler directement via notre portail RH ou m'envoyer votre CV ici.")
        
    # Réponse par défaut professionnelle
    else:
        return ("Bonjour ! Je suis l'assistant intelligent de votre service. "
                "Comment puis-je vous accompagner dans vos recherches aujourd'hui ?")